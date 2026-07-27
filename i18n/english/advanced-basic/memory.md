---
icon: brain
---

# Agent workspace memory

Cherry Studio V2 lets an agent retain important information across multiple sessions that use the same workspace. Memory is stored in the `memory` folder under the agent's first accessible directory. You do not need to configure a global memory switch or an embedding model.

This feature is intended for agent tasks and does not automatically merge regular chats into memory. Memory is stored by workspace path rather than in a separate directory for each agent ID. If two agents use the same directory as their first accessible directory, they read and write the same memory files.

## Requirements

The agent must have at least one accessible directory configured. Its first accessible directory becomes the workspace, and the memory files are stored at:

```text
<workspace>/memory/
├── FACT.md
└── JOURNAL.jsonl
```

If the agent has no accessible directory, workspace memory cannot be read or written.

## Two types of memory

| File | What it stores | How it is used |
| :--- | :--- | :--- |
| `FACT.md` | Durable facts, conventions, and technical decisions | Soul Mode and standard custom agents load it in later sessions and update it when the facts change |
| `JOURNAL.jsonl` | Completed tasks, one-time events, and session notes | Entries are appended over time; the agent searches them when needed instead of loading the entire journal into context |

To decide whether something belongs in `FACT.md`, ask: “Will this still matter in six months?” If it only describes the process or result of a particular task, it is better suited to the Journal.

## Ask an agent to remember information

In an agent session, directly state what should be retained. For example:

> Remember: this project uses pnpm consistently. Run lint and unit tests before committing.

For durable rules, ask the agent to update its persistent facts. For one-time progress, ask it to add an entry to the Journal. The agent writes the information through its built-in workspace memory tool.

{% hint style="warning" %}
Memory files are stored in the local workspace. Do not ask an agent to record passwords, API keys, access tokens, or other sensitive information.
{% endhint %}

## Use memory in later sessions

When you use an agent that supports workspace memory and start a new session in the same workspace, Cherry Studio provides the durable facts from `FACT.md` to the agent. To find an earlier event, ask the agent to search the Journal. For example:

> Find the records about last week's release failure.

Searches can filter by text and tag and return the most recent matching entries.

Currently, automatic loading of `FACT.md` applies to Soul Mode and standard custom agents. The built-in Cherry Assistant does not automatically load these workspace facts.

## View or maintain memory

You can inspect `memory/FACT.md` in the workspace to see which durable facts are currently stored. When a fact needs correction, tell the agent to update its memory so that it can write the change safely through the memory tool.

`JOURNAL.jsonl` contains one JSON record per line. Search it through the agent rather than rewriting it manually in bulk.

## If the agent did not remember

Check the following in order:

1. Confirm that the current agent has an accessible directory configured.
2. Confirm that the current agent's first accessible directory still points to the original workspace.
3. Check whether the information was written to `memory/FACT.md`.
4. Determine whether you need a durable fact or a one-time entry from the Journal.

Legacy global memory and V2 agent workspace memory are separate systems. When troubleshooting V2 memory, use `memory/FACT.md` and `memory/JOURNAL.jsonl` in the current workspace as the source of truth.
