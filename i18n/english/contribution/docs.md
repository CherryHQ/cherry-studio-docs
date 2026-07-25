---
icon: file-lines
---

# Contribute Documentation

The Cherry Studio community documentation is maintained in a Markdown repository and presented through GitBook. You can contribute through a GitHub Pull Request or, after receiving edit access, make changes through a GitBook Change Request.

* Documentation repository: [CherryHQ/cherry-studio-docs](https://github.com/CherryHQ/cherry-studio-docs)
* Product code: [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)
* Published documentation: [docs.cherryai.com.cn](https://docs.cherryai.com.cn/)

Use GitHub for bulk updates, multilingual changes, and pages that require checking facts against the code. GitBook is suitable for small copy edits or visual comments.

## Confirm the Scope First

Answer four questions before submitting:

1. Are you modifying an existing page or adding a new one?
2. Which Cherry Studio version or behavior on `main` does the content describe?
3. Which languages can the contributor verify reliably?
4. Are product screenshots required, and do they add information that text cannot explain?

If the content concerns current features, setting names, model capabilities, or data paths, verify it against the product's `main` code and actual interface first. Do not merely copy old documentation, third-party articles, or model-generated output.

## Documentation Structure

Simplified Chinese is stored at the repository root. Other published languages are stored under:

| Language | Directory | Table of contents file |
| :--- | :--- | :--- |
| Simplified Chinese | Repository root | `SUMMARY.md` |
| Traditional Chinese | `i18n/traditional-chinese/` | `i18n/traditional-chinese/SUMMARY.md` |
| English | `i18n/english/` | `i18n/english/SUMMARY.md` |
| Japanese | `i18n/japanese/` | `i18n/japanese/SUMMARY.md` |
| Russian | `i18n/russian/` | `i18n/russian/SUMMARY.md` |

By default, GitBook uses `README.md` at the root as the homepage and `SUMMARY.md` as the sidebar table of contents. Each language has its own directory and `SUMMARY.md`; page hierarchy and names should remain consistent within the corresponding language.

## Path 1: Contribute Through GitHub

### 1. Fork and Clone

Fork the documentation repository on GitHub, then run:

```bash
git clone https://github.com/YOUR_GITHUB_NAME/cherry-studio-docs.git
cd cherry-studio-docs
git remote add upstream https://github.com/CherryHQ/cherry-studio-docs.git
git fetch upstream
git switch -c docs/short-description upstream/main
```

### 2. Modify an Existing Page

Keep the existing file path and edit the corresponding Markdown directly. Moving or renaming a file changes its page URL. If a path must change, list the old and new addresses in the PR so maintainers can confirm the redirect.

When changing multiple languages, edit the file in each language directory separately. Do not overwrite another language with Simplified Chinese, and do not leave English or Japanese pages referencing Chinese interface screenshots.

### 3. Add a New Page

A new page should include at least:

1. A Simplified Chinese Markdown file.
2. An entry in the correct section of `SUMMARY.md`.
3. Pages in other languages that can be verified, with entries in their corresponding `SUMMARY.md`.
4. Local images used by the page.
5. Links to the new page from a relevant parent page or adjacent tutorial.

Use a stable, readable English filename or follow the existing directory style. Do not put dates, version numbers, or marketing titles in a path unless the page applies only to that version.

If you cannot translate a language reliably yet, do not submit unchecked machine translation. List the missing languages in the PR description so maintainers can arrange follow-up work.

## What Makes a Good Product Documentation Page

The structure depends on the task, but a page should usually include:

* **Purpose**: What the reader will accomplish.
* **Prerequisites**: Required versions, models, accounts, files, or permissions.
* **Steps**: Current interface names in the real operating order.
* **Result**: What appears, is generated, or is saved when the task succeeds.
* **Boundaries**: Platform differences, costs, privacy, data transmission, and irreversible actions.
* **Troubleshooting**: The most common failures that readers can actually diagnose.
* **Next step**: A link to the feature the reader will use next.

Explanations of “why” should be brief and support a decision. Do not include the writing process, internal discussions, unverified background, or repetitive product promotion.

### Writing Requirements

* Use current UI text for headings and button names.
* Describe one action per step and place the result immediately after the action.
* Include dynamic prices, model lists, and promotions only when necessary, and state that the provider's current page is authoritative.
* Do not equate a compatible API with complete feature support.
* Do not promise that a third-party service will remain free, available forever, or return identical results.
* For high-risk actions, explain backups, permissions, and rollback.
* API Keys, tokens, cookies, personal paths, and real conversations must not appear in prose or code examples.

## Screenshot Standards

Use screenshots only to locate an entry point, explain a complex state, or show a result. When the text is already clear, do not add screenshots merely to make the page “look complete.”

### Dimensions and Composition

Use these settings consistently for Cherry Studio desktop screenshots:

* Physical dimensions: `1920 × 1200`
* Aspect ratio: `16:10`
* DPR: `2`
* Keep the same window size, crop area, and visual scale for screenshots on the same page

Do not make one screenshot extremely wide and another nearly square in the same set. Preserve enough operating context while keeping the target control clearly visible.

### Multiple Languages

Simplified Chinese, Traditional Chinese, English, Japanese, and Russian pages should use the product UI in the corresponding language. Conversation content, assistant names, sample filenames, and result text should also match the page language.

If an interface is genuinely untranslated in the target language, describe the product's current state in the PR instead of using a screenshot from another language to imply that localization is complete.

### Privacy and Files

* Use fictional accounts, assistants, directories, and conversations.
* Hide API Keys, tokens, email addresses, usernames, personal directories, and notifications.
* Do not use a database or knowledge base containing real user data.
* Store images in `.gitbook/assets/` with unique, meaningful filenames.
* Use relative paths in Markdown and add alt text that describes each image's purpose.
* Do not reference expiring temporary download URLs, private Lark links, or local absolute paths.

PNG and WebP are recommended. Keep screenshots clear, but avoid saving large areas of meaningless blank space or unnecessarily oversized files.

## Markdown and GitBook

The repository uses common Markdown plus GitBook hint and image blocks. Follow the style of nearby pages when making changes.

### Internal Links

Use relative paths:

```markdown
[Agents](../advanced-basic/agent.md)
```

A directory homepage can link to the directory or its `README.md`, but confirm that the target exists first. Do not replace repository-internal links with complete production URLs; branch Previews and multilingual pages can otherwise jump back to the production site.

### Hint Blocks

Use a hint only when the information truly needs emphasis:

```markdown
{% hint style="warning" %}
Back up your data before proceeding.
{% endhint %}
```

Do not stack many hints on one page. Use ordinary paragraphs or lists for regular steps and supplementary information.

### Table of Contents Files

`SUMMARY.md` determines the GitBook sidebar hierarchy. When adding, moving, or renaming a page, also check the corresponding language's `SUMMARY.md`:

```markdown
* [Agent Case Studies](advanced-basic/agent-an-li/README.md)
  * [Gold Market Review Agent](advanced-basic/agent-an-li/gold-price-case.md)
```

Do not reference the same Markdown file more than once in one `SUMMARY.md`.

## Local Checks

Before submitting, run at least:

```bash
git status --short
git diff --check
git diff -- SUMMARY.md
```

Then confirm manually that:

* Git tracks every new Markdown file and image.
* Paths in `SUMMARY.md` exist and their indentation hierarchy is correct.
* Relative links and image paths on each page exist.
* The five languages do not leak into one another's prose or screenshots.
* Code blocks, hint blocks, and frontmatter are all closed.
* There are no temporary URLs, real keys, personal directories, or duplicate files generated by an editor.

You can inspect Markdown formatting on GitHub, but GitHub and GitBook do not render identically. Recheck complex hints, image dimensions, sidebar hierarchy, and page navigation in GitBook Preview.

## Create a Pull Request

Commit and push the branch:

```bash
git add path/to/page.md SUMMARY.md .gitbook/assets/
git commit -m "docs(section): update page title"
git push -u origin docs/short-description
```

The PR description should include at least:

* Which pages were changed or added.
* The corresponding product version, code location, or official source.
* Languages completed and still missing.
* Screenshots added or replaced.
* Link, structure, and visual checks performed.
* Whether any page path or sidebar entry changed.

Create a Draft if the PR is not ready. Merge only after maintainers have confirmed the prose, facts, images, and languages.

## Preview and Production Publishing

After the documentation repository is connected to GitBook, GitHub and GitBook can synchronize in both directions, but **the synchronized repository and branch are configured by a GitBook administrator**. Opening a PR does not immediately change the production documentation.

When the GitBook configuration supports it, the PR receives a status check containing a Preview URL. Note that:

* Preview usually requires the visitor to sign in to GitBook.
* For security reasons, a PR from a fork might not generate a Preview by default; an administrator can change this setting.
* Preview might also be unavailable when the site is unpublished or uses specific access restrictions.

Do not promise in the PR description that everyone can open the GitBook Preview. If no automatic Preview is available, maintainers should provide a review environment or use an internal preview before merging.

Only after the PR is merged into the branch currently connected to GitBook do the changes enter the GitBook synchronization and publishing flow. Maintainers control merge access and production publishing.

Official GitBook references:

* [Git Sync](https://gitbook.com/docs/integrations/git-sync)
* [GitHub Pull Request Preview](https://gitbook.com/docs/getting-started/git-sync/github-pull-request-preview)
* [README and SUMMARY Configuration](https://gitbook.com/docs/getting-started/git-sync/content-configuration)

## Path 2: Edit Through GitBook

To request GitBook edit access, email `support@cherry-ai.com` with the subject “Request Cherry Studio Docs Editor Access” and include:

* Your GitBook account email.
* The sections and languages you want to maintain.
* Relevant documentation or product experience.
* The changes you plan to make.

After receiving access, create a Change Request in GitBook instead of editing published content directly. Invite maintainers to Review after completing your checks. When the Change Request is merged, GitBook synchronizes the changes to the corresponding Git branch according to the administrator's configuration.

For bulk edits, cross-language restructuring, or large image replacements, a GitHub branch is still recommended because it supports file-by-file review and automated checks.

## After Review

Maintainers might ask you to correct facts, reduce screenshots, add sources, or unify terminology. When updating:

1. Modify only the scope addressed by the feedback.
2. Keep the structure consistent across all five languages.
3. Recheck language, dimensions, and privacy after screenshot changes.
4. Reply with the changes made and validation results.

If an issue is found after the documentation is merged, fix it with a new PR. Do not hide errors by deleting history or directly overwriting the production branch.

For code contributions, read [Contribute Code](code.md). If you are unsure where to report a problem, start with [Feedback and Suggestions](../question-contact/suggestions.md).
