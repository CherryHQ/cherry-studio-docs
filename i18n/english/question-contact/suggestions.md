---
icon: file-signature
---

# Feedback and Suggestions

Choosing the right channel and providing reproducible information can significantly reduce the time needed to confirm and address an issue.

## Choose a feedback channel

| Need | Recommended channel | Appropriate content |
| :--- | :--- | :--- |
| Software failure | [GitHub Bug Report](https://github.com/CherryHQ/cherry-studio/issues/new/choose) | Crashes, broken features, regressions, interface errors |
| Feature suggestion | [GitHub Feature Request](https://github.com/CherryHQ/cherry-studio/issues/new/choose) | New features, interaction improvements, enhancements |
| Usage discussion | [GitHub Discussions](https://github.com/CherryHQ/cherry-studio/discussions) | How-to questions, shared experience, solution discussions |
| Security vulnerability | [GitHub Security Advisory](https://github.com/CherryHQ/cherry-studio/security/advisories/new) | Vulnerabilities that may expose data, bypass permissions, or perform unauthorized actions |
| GitHub is unavailable | [support@cherry-ai.com](mailto:support@cherry-ai.com) | You cannot sign in to GitHub, or ordinary support information should not be public |

{% hint style="warning" %}
Do not submit a security vulnerability in a public Issue or disclose reproduction details in a group chat. Use a private Security Advisory.
{% endhint %}

## Complete four steps before submitting

1. Update to the latest stable release and confirm that the issue still reproduces.
2. Review [Frequently Asked Questions](questions.md) to rule out configuration, quota, network, and model-provider problems.
3. Search existing [Open Issues](https://github.com/CherryHQ/cherry-studio/issues), [Closed Issues](https://github.com/CherryHQ/cherry-studio/issues?q=is%3Aissue%20state%3Aclosed), and [Discussions](https://github.com/CherryHQ/cherry-studio/discussions).
4. Remove API Keys, Tokens, Cookies, personal file paths, and private chat content from screenshots, logs, and configuration.

If the same issue already exists, add new reproduction information there instead of creating a duplicate Issue.

## Report a Bug

### Title

Include the **feature, platform, and symptom** so a maintainer can understand the issue before opening the description.

```text
[Bug] macOS: Knowledge Base remains in Processing after reindexing
```

Do not use only “Does not work,” “Something is wrong,” or “Please fix.”

### Required information

An actionable Bug report includes at least:

* The Cherry Studio version.
* Windows, macOS, or Linux and the operating-system version.
* The affected feature, model provider, and model name; never include an API Key.
* Steps that reproduce the issue reliably.
* The actual and expected results.
* The version or action after which the issue first appeared.
* Troubleshooting already attempted.
* Necessary screenshots, recordings, and redacted logs.

Find the version under **Settings → About**. Open application logs under **Settings → Data Settings → Data → Application logs**.

### Recommended template

```markdown
## Environment

- Cherry Studio:
- System:
- Installation source:
- Model provider / model:

## Reproduction steps

1.
2.
3.

## Actual result


## Expected result


## Additional information

- Does it reproduce reliably?
- First affected version:
- Already attempted:
- Redacted log / screenshot:
```

### Minimal reproduction

If the issue is related to a specific assistant, Knowledge Base, MCP Server, or custom CSS, reduce the variables first:

* Create a blank assistant or topic.
* Temporarily disable unrelated MCP Servers, skills, and web search.
* Use a small piece of non-sensitive test content.
* Record which setting causes the issue when enabled.

A minimal reproduction is more useful for finding the root cause than a screenshot of the entire environment.

## Submit a feature suggestion

A feature suggestion should explain not only what you want, but also the current problem.

Include:

1. **Use case**: who encounters the problem and in which workflow.
2. **Current obstacle**: why the existing features do not meet the need.
3. **Expected result**: the ideal interaction and output.
4. **Workaround**: how you handle it today and the disadvantages.
5. **Scope and boundaries**: which cases must be supported and which may wait.
6. **Supporting material**: a redacted screenshot, flowchart, or interaction sketch when needed.

Keep one Issue focused on one independent requirement. Several unrelated requests in the same Issue make scope confirmation and scheduling more difficult.

See the [Cherry Studio Roadmap](https://github.com/orgs/CherryHQ/projects/7) for the project direction. The Roadmap is not a delivery commitment; current maintainer guidance determines the final scope and schedule.

## Questions and discussions

Use [GitHub Discussions](https://github.com/CherryHQ/cherry-studio/discussions) for ordinary usage questions. Include:

* Your goal.
* Your current configuration and navigation path.
* What you have already tried.
* The step where you are blocked.
* The type of help you need.

If the question contains a reproducible software defect, use a Bug Report instead. If a new requirement needs implementation tracking, use a Feature Request.

## Report a security issue

Use a private [GitHub Security Advisory](https://github.com/CherryHQ/cherry-studio/security/advisories/new) if:

* An API Key, Token, or local data may be read unexpectedly.
* A permission confirmation can be bypassed.
* Untrusted content may trigger an unauthorized command or file operation.
* An update package, dependency, or network communication has an exploitable risk.

Include the affected scope, reproduction steps, necessary verification material, and possible mitigations. Do not submit real user data or credentials that are still active.

For non-vulnerability security questions, contact [security@cherry-ai.com](mailto:security@cherry-ai.com).

## Community channels

Community groups are suitable for sharing experience and helping one another, but they are not formal issue trackers. Submit issues that need maintainer confirmation, release association, or ongoing tracking to GitHub.

* [Telegram: CherryStudioAI](https://t.me/CherryStudioAI)
* [Discord: Cherry Studio](https://discord.gg/wez8HtpxqQ)
* [QQ group: 575014769](https://qm.qq.com/q/lo0D4qVZKi)

Group invitations may change because of platform rules or membership limits. If a link no longer works, use the latest entry in the [official Cherry Studio repository](https://github.com/CherryHQ/cherry-studio) README.

## Protect your privacy

Before submitting, check that:

* API Keys, access Tokens, Cookies, and passwords are completely obscured.
* Names, company names, and project names in file paths are redacted.
* Chats, Knowledge Bases, and documents contain no unnecessary personal or business data.
* Logs contain only the period relevant to the issue.
* Screenshots do not expose sensitive information in other apps, browser tabs, or notifications.

If a credential has already been published, deleting the post is not enough. Revoke it in the provider console and generate a new one immediately.
