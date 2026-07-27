---
icon: square-code
---

# Contribute Code

Cherry Studio welcomes code contributions for features, bug fixes, tests, performance, accessibility, developer tooling, and more. Day-to-day V2 development currently takes place on the `main` branch. Before starting, confirm the problem, scope of the change, and validation method.

Project repository: [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)

## Before You Begin

Read:

* [Contributing Guide](https://github.com/CherryHQ/cherry-studio/blob/main/CONTRIBUTING.md)
* [Code of Conduct](https://github.com/CherryHQ/cherry-studio/blob/main/CODE_OF_CONDUCT.md)
* [Development Guide](https://github.com/CherryHQ/cherry-studio/blob/main/docs/guides/development.md)
* [Project Development Conventions](https://github.com/CherryHQ/cherry-studio/blob/main/CLAUDE.md)
* [Open Source License](https://github.com/CherryHQ/cherry-studio/blob/main/LICENSE)

Before implementing a large feature, changing a user flow, or refactoring a public interface, search [Issues](https://github.com/CherryHQ/cherry-studio/issues) and existing Pull Requests. If there is no relevant discussion, open an Issue describing the problem, goal, and proposed approach first. This reduces duplicated work and mismatched direction.

For a first contribution, start with these labels:

* [good first issue](https://github.com/CherryHQ/cherry-studio/labels/good%20first%20issue)
* [help wanted](https://github.com/CherryHQ/cherry-studio/labels/help%20wanted)
* [kind/bug](https://github.com/CherryHQ/cherry-studio/labels/kind%2Fbug)

## Choose the Correct Branch

| Change | Base branch | PR target branch |
| :--- | :--- | :--- |
| Current features, V2 development, refactoring, optimization, and bug fixes | `main` | `main` |
| Minimal maintenance fixes for the released V1 | `v1` | `v1` |

V1 fixes do not automatically enter `main`. If the same issue exists on the current development branch, open a separate forward-port PR targeting `main`.

Do not commit directly to upstream branches. Fork the repository first, then create a short-lived feature branch from the correct base.

## Prepare the Development Environment

The current `main` pins Node.js in `.node-version` at `24.11.1` and pnpm in `package.json` at `10.27.0`. These versions change as the repository evolves. Always use the files in your local branch as the source of truth when starting work.

### Windows: Enable Symbolic Links First

The repository uses symbolic links to synchronize some files. Before cloning, Windows users should:

1. Enable **Developer Mode** in system settings or obtain permission to create symbolic links.
2. Run:

```powershell
git config --global core.symlinks true
```

3. Then clone the repository. If you cloned before enabling symbolic links, enable them and clone again.

### Fork and Clone

Fork `CherryHQ/cherry-studio` on GitHub, then run:

```bash
git clone https://github.com/YOUR_GITHUB_NAME/cherry-studio.git
cd cherry-studio
git remote add upstream https://github.com/CherryHQ/cherry-studio.git
git fetch upstream
git switch -c fix/short-description upstream/main
```

Replace `YOUR_GITHUB_NAME` and the branch name with your own values. Use `feat/` for features, `fix/` for bug fixes, and `docs/` for documentation changes.

### Install Node.js and Dependencies

Use a version manager that supports `.node-version` or `.nvmrc` to install the Node.js version required by the repository. For example:

```bash
nvm install
nvm use
corepack enable
corepack pnpm install
```

Use the repository-pinned pnpm through Corepack. Do not use another global pnpm to rewrite `pnpm-lock.yaml`. Unless you intentionally change dependencies, a PR should not contain unrelated lockfile changes.

### Create the Local Environment File

```bash
cp .env.example .env
```

Git ignores `.env`. Enter only values required for local development. Do not commit real API Keys, tokens, cookies, or other credentials to code, tests, logs, or screenshots.

### Start the App

```bash
corepack pnpm dev
```

The first launch generates OpenAPI files before opening the Electron development instance. To debug the main or renderer process, use:

```bash
corepack pnpm debug
```

If dependency installation or startup fails, first check the Node.js and pnpm versions, confirm that another package manager has not modified the lockfile, then inspect the first error in the terminal.

## Start Making Changes

### Understand Local Conventions First

Cherry Studio is a monorepo containing an Electron main process, preload layer, React renderer, and multiple shared packages. Before editing a directory:

1. Read `README.md` in that directory and its parent directories.
2. Review nearby implementations and tests of the same kind.
3. Search for `@deprecated` markers to avoid extending an interface being phased out.
4. Modify only the files required to solve the current problem.

The renderer must not access Node.js APIs directly. When cross-process capabilities are required, follow the existing preload and IPC boundaries. Use the project's `loggerService` for logging; do not add `console.log`.

### Keep Changes Testable

For a bug fix, prefer adding a test that reproduces the problem. For new behavior, add tests for success, failure, and boundary cases. The project uses Vitest and provides test commands by area:

```bash
corepack pnpm test:main
corepack pnpm test:renderer
corepack pnpm test:aicore
corepack pnpm test:shared
```

You do not need to run every area each time. During development, run the tests closest to the change first, then run the full checks before submission.

### User-Visible Text

When adding or changing interface text, use the existing internationalization mechanism. Do not write strings directly in a component if they apply to only one language. Run at least:

```bash
corepack pnpm i18n:check
corepack pnpm i18n:hardcoded:strict
```

When synchronizing new keys, read the repository's [Internationalization Guide](https://github.com/CherryHQ/cherry-studio/blob/main/docs/guides/i18n.md) before running the corresponding scripts.

### Database Schema

When modifying a Drizzle Schema, generate and commit the corresponding migration:

```bash
corepack pnpm db:migrations:generate
corepack pnpm db:migrations:check
```

If migration numbering conflicts after a rebase, do not rename only the SQL file or edit the snapshot manually. Regenerate it according to the repository's data migration documentation, then confirm that the migration chain and Schema agree.

## Checks Before Submission

Review the actual changes first:

```bash
git status --short
git diff --check
git diff
```

Confirm that there are no temporary files, credentials, personal paths, unrelated formatting changes, or accidental lockfile modifications.

Run the tests most relevant to the change, then run the full check provided by the repository:

```bash
corepack pnpm build:check
```

`build:check` runs checks for code style, types, OpenAPI, documentation links, tests, and more. CI might run database, strict internationalization, skill, or package-specific checks separately. If the change affects those areas, run the corresponding command in advance.

{% hint style="info" %}
Check scripts and the Node.js version change with `main`. If a command on this page conflicts with the repository, follow `package.json`, `.node-version`, `CONTRIBUTING.md`, and the CI configuration on the current branch.
{% endhint %}

## Create a Commit

The project requires small, focused Conventional Commits with a DCO sign-off:

```bash
git add path/to/changed-file
git commit --signoff -m "fix(module-name): describe the change"
```

Common types include `feat`, `fix`, `refactor`, `docs`, `test`, and `chore`. The scope should identify a specific module and use a short kebab-case name. Do not use a generic scope such as `main`.

`--signoff` adds this line to the commit message:

```text
Signed-off-by: Your Name <your.email@example.com>
```

It states that you have the right to submit the contribution under the project's license. It is not the same as a GPG or SSH cryptographic signature.

## Synchronize with Upstream

Before creating a PR, update your branch to the latest `main`:

```bash
git fetch upstream
git rebase upstream/main
```

Resolve conflicts and rerun the relevant checks, then push your branch:

```bash
git push -u origin fix/short-description
```

If you already pushed and need to update the remote after rebasing, first confirm that only you use the branch, then use the safer `--force-with-lease`. Do not force-push a shared branch directly.

## Submit a Pull Request

When creating a PR:

1. Select `CherryHQ/cherry-studio` as the base repository.
2. For V2 and current development changes, select `main` as the base.
3. Complete the PR template with before-and-after behavior, implementation rationale, tradeoffs, related Issues, Breaking Changes, and Release Notes.
4. For user-visible changes, include screenshots or a screen recording and describe the test system and validation steps.
5. Request Review only after all required content is ready.

If the direction is not yet settled or development is still underway, create a **Draft PR** first. Draft PRs skip project CI and are not automatically assigned for Review. Mark the PR Ready for review when it is complete.

A non-Draft PR from a new contributor might first receive the `needs-ok-to-test` label, and CI will not run immediately. A maintainer starts the test workflow by adding `/ok-to-test` to the PR. This is a normal security process; do not repeatedly close and reopen the PR.

## Address Review Feedback

After receiving feedback:

1. Confirm each issue and the expected behavior.
2. Commit small, clear follow-up changes on the original branch.
3. Rerun affected tests.
4. Reply with the change location and validation results.
5. Leave resolved discussions for the Reviewer to confirm.

Do not delete valid tests, loosen types, or bypass security checks merely to “make CI green.” If a failure is unrelated to the current PR, provide logs and reproduction evidence in the PR and ask a maintainer to assess it.

## Frequently Asked Questions

### The Lockfile Changes Extensively After Installing Dependencies

This usually means that the Node.js or pnpm version does not match. Revert unintentional lockfile changes, prepare the environment again according to `.node-version` and `packageManager`, then run `corepack pnpm install`.

### Skills or Synchronized Files Behave Incorrectly on Windows

Confirm that Developer Mode and `core.symlinks=true` were enabled before cloning. If symbolic links in the repository were checked out as regular files, enable the setting and clone again.

### CI Never Starts

First check whether the PR is still a Draft. New contributors should also check for the `needs-ok-to-test` label and wait for a maintainer to run `/ok-to-test`.

### Unsure Whether to Open an Issue

For a small, well-defined bug fix, you can open a PR directly and provide reproduction steps in its description. For a large feature, interface change, or change with multiple possible approaches, reach consensus through an Issue first.

For documentation contributions, read [Contribute Documentation](docs.md). For other questions, contact the community through [Feedback and Suggestions](../question-contact/suggestions.md).
