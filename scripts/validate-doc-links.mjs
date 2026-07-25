import fs from 'node:fs'
import path from 'node:path'

const root = process.cwd()
const ignoredDirectories = new Set(['.git', 'i18n', 'node_modules'])

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    if (entry.isDirectory()) {
      return ignoredDirectories.has(entry.name) ? [] : walk(path.join(directory, entry.name))
    }
    return entry.name.endsWith('.md') ? [path.join(directory, entry.name)] : []
  })
}

function markdownTargets(content) {
  const targets = []
  for (let start = content.indexOf(']('); start !== -1; start = content.indexOf('](', start + 2)) {
    let depth = 1
    let escaped = false
    let value = ''
    for (let index = start + 2; index < content.length; index += 1) {
      const character = content[index]
      if (escaped) {
        value += character
        escaped = false
      } else if (character === '\\') {
        value += character
        escaped = true
      } else if (character === '(') {
        depth += 1
        value += character
      } else if (character === ')') {
        depth -= 1
        if (depth === 0) {
          targets.push(value.trim())
          break
        }
        value += character
      } else {
        value += character
      }
    }
  }
  return targets
}

function htmlTargets(content) {
  return [...content.matchAll(/<(?:img|source)\b[^>]*?\bsrc=["']([^"']+)["']/gi)].map(
    (match) => match[1].trim(),
  )
}

function normalizeTarget(rawTarget) {
  let target = rawTarget
  if (target.startsWith('<') && target.endsWith('>')) target = target.slice(1, -1)
  target = target.replace(/\s+(?:"[^"]*"|'[^']*')$/, '')
  target = target.split('#', 1)[0].split('?', 1)[0]
  try {
    return decodeURIComponent(target)
  } catch {
    return target
  }
}

const missing = []
const structuralErrors = []
const markdownFiles = walk(root)

for (const file of markdownFiles) {
  const content = fs.readFileSync(file, 'utf8')
  const relativeFile = path.relative(root, file).replaceAll('\\', '/')

  for (const [label, openPattern, closePattern] of [
    ['figure', /<figure\b/gi, /<\/figure>/gi],
    ['GitBook hint', /{%\s*hint\b/gi, /{%\s*endhint\s*%}/gi],
    ['GitBook tabs', /{%\s*tabs\s*%}/gi, /{%\s*endtabs\s*%}/gi],
    ['GitBook tab', /{%\s*tab\b/gi, /{%\s*endtab\s*%}/gi],
  ]) {
    const opens = [...content.matchAll(openPattern)].length
    const closes = [...content.matchAll(closePattern)].length
    if (opens !== closes) structuralErrors.push({ file: relativeFile, label, opens, closes })
  }

  if (/^(?:<{7}|={7}|>{7})/m.test(content)) {
    structuralErrors.push({ file: relativeFile, label: 'merge conflict marker' })
  }

  for (const rawTarget of [...markdownTargets(content), ...htmlTargets(content)]) {
    if (
      !rawTarget ||
      rawTarget.startsWith('#') ||
      /^(?:https?:|mailto:|tel:|data:|javascript:)/i.test(rawTarget) ||
      rawTarget.includes('{{')
    ) {
      continue
    }

    const target = normalizeTarget(rawTarget)
    if (!target) continue

    const resolved = target.startsWith('/')
      ? path.join(root, target.replace(/^[/\\]+/, ''))
      : path.resolve(path.dirname(file), target)

    if (!fs.existsSync(resolved)) {
      missing.push({
        file: relativeFile,
        target: rawTarget,
        resolved: path.relative(root, resolved).replaceAll('\\', '/'),
      })
    }
  }
}

const summary = fs.readFileSync(path.join(root, 'SUMMARY.md'), 'utf8')
const summaryMarkdownTargets = markdownTargets(summary)
  .map(normalizeTarget)
  .filter((target) => target.endsWith('.md'))
if (new Set(summaryMarkdownTargets).size !== summaryMarkdownTargets.length) {
  structuralErrors.push({ file: 'SUMMARY.md', label: 'duplicate Markdown target' })
}

if (missing.length > 0 || structuralErrors.length > 0) {
  console.error(JSON.stringify({ checkedFiles: markdownFiles.length, missing, structuralErrors }, null, 2))
  process.exitCode = 1
} else {
  console.log(
    `Validated ${markdownFiles.length} Markdown files and ${summaryMarkdownTargets.length} SUMMARY targets: links, media and structural blocks are valid.`,
  )
}
