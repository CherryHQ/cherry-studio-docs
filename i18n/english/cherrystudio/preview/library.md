---
icon: library
---

# Resource Management Entry Points

Cherry Studio V2 no longer provides a standalone Library page. Assistants, agents, skills, and prompts can still be managed, but their entry points now live in the contexts where they are used.

{% hint style="warning" %}
The legacy `/app/library` route is no longer served, and Launchpad has no Library tile. After an upgrade, pinned tabs for the old route are removed automatically. Do not continue looking for the page shown in older screenshots.
{% endhint %}

## Current Entry Points

| Resource | Where to manage it | Main actions |
| :--- | :--- | :--- |
| Assistant | Open **Chat**, then enter assistant management from the resource menu on the left | Create, import, edit, duplicate, export, group, and delete assistants |
| Agent | Open **Work**, then enter agent management from the resource menu on the left | Create, edit, configure working directories and tools, and delete agents |
| Skill | Open **Settings → Skills** | Search, install, inspect, and uninstall global skills |
| Prompt | Open **Quick Phrases** from the conversation composer, then choose **Manage** or **Add** | Create, edit, search, insert, and delete reusable prompts |

These entry points appear directly in the current working context. For example, after editing an assistant, you can return to the conversation without first leaving for a separate resource page.

## Assistant Library and Resource Management

[Assistant Library](agents.md) is still used to browse and import community assistants. An imported assistant appears in your assistant list and is maintained from the assistant management entry in **Chat**.

Assistant Library is not a replacement route for the former standalone Library:

- Assistant Library provides community content.
- Assistant management maintains assistants you already own.
- Agents, skills, and prompts use the separate entry points in the table above.

## An Old Link Does Not Open

If a bookmark, history entry, or older guide contains `/app/library`:

1. Do not keep refreshing that address.
2. Open the new entry point for the corresponding resource type.
3. The app removes old pinned tabs during restore; it does not delete the underlying assistant, agent, skill, or prompt data.

Global Search also filters legacy Library route records so that the removed page is not opened again.

## Next Steps

- Learn how to use [Assistant Library](agents.md).
- Learn how to create and run [agents](../../advanced-basic/agent.md).
- Learn how to install and manage [skills](../../pre-basic/settings/skills.md).
- Learn how to manage [Quick Phrases](../../pre-basic/settings/quick-phrase.md).
