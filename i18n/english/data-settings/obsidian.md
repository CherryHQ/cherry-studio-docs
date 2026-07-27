---
description: Export Cherry Studio V2 topics, messages, or notes to a local Obsidian vault.
icon: gem
---

# Obsidian Configuration and Export

Cherry Studio V2 can export a complete topic, an individual message, or a Cherry Studio note as a Markdown file in Obsidian. Export uses Obsidian's built-in `obsidian://` URI and the system clipboard; no third-party Obsidian plugin is required.

Configuration is under **Settings > Integrations > Obsidian**. **Data Settings > Export Menu** only controls whether “Export to Obsidian” appears in menus.

{% hint style="warning" %}
“New (overwrite if it exists)” replaces an existing Markdown file at the same path. For your first test, create a test folder and back up any important vault first.
{% endhint %}

## Before You Begin

1. Install Obsidian on the current computer and launch it at least once.
2. Open the target local vault in Obsidian.
3. Confirm that the vault folder still exists and that the current user can read and write it.
4. Reopen Obsidian settings in Cherry Studio.

Cherry Studio reads Obsidian's local configuration and lists vaults registered on this computer:

- Windows: Reads the Obsidian configuration under the user's app data.
- macOS: Reads `~/Library/Application Support/obsidian/obsidian.json`.
- Linux: Supports common XDG, Snap, and Flatpak configuration locations.

A vault synchronized to another computer but never opened in the current Obsidian client does not automatically appear in the list.

## Choose the Default Vault

1. Open **Settings > Integrations > Obsidian**.
2. Under **Default Obsidian Vault**, select the target vault.
3. Return to the conversation page.

If no default has been selected, Cherry Studio uses the first vault in the discovered list. You can still temporarily choose another vault in the export dialog.

{% hint style="info" %}
“Repository” and “Vault” in the Cherry Studio interface both refer to an Obsidian vault. This setting selects a local vault name, not a remote Obsidian Sync vault or account.
{% endhint %}

## Enable the Export Menu

If “Export to Obsidian” is missing from a menu:

1. Open **Settings > Data Settings > Export Menu**.
2. Enable **Export to Obsidian**.
3. Return to the conversation or note and reopen its export menu.

This switch controls only entry visibility; it does not affect vault discovery or the `obsidian://` protocol.

## Open the Export Dialog

### Export a Complete Topic

Open the target topic's menu in the topic list on the left and select **Export to Obsidian**.

The complete topic is converted to Markdown in message order. The default handling method is **New (overwrite if it exists)**.

### Export an Individual Message

Open the message menu and select **Export to Obsidian**.

An individual message export includes only the current message. The dialog still lets you change the title, target path, and handling method.

### Export a Cherry Studio Note

Select **Export to Obsidian** from the note menu. A note uses its current Markdown content and does not display the Export Chain of Thought switch.

## Configure the Export Dialog

| Field | Purpose |
| --- | --- |
| Title | The filename source for a new file and the YAML `title` in New mode |
| Vault | The target Obsidian vault for this export |
| Path | The vault root, an existing folder, or an existing `.md` file |
| Tags | Written to YAML `tags` in New mode; separate multiple tags with ASCII commas |
| Created Time | Written to YAML `created` in New mode |
| Source | Written to YAML `source` in New mode; defaults to `Cherry Studio` |
| Handling Method | New/overwrite, prepend, or append |
| Export Chain of Thought | Determines whether available reasoning content is included for a conversation or message |

Title cannot be empty. When creating a new file, Cherry Studio removes filename characters that are invalid on the current platform and truncates an excessively long name.

### Choose a Path

The path selector reads folders and Markdown files in the target vault and ignores hidden entries whose names begin with `.`.

- Selecting **Root Directory** or a folder generates a new `.md` filename from the title.
- Selecting an existing `.md` file uses that file path directly, changes the title to its filename, and switches the default method to **Append**.
- After switching vaults, select the path again.

If the directory tree is empty, confirm that the vault path still exists and that Cherry Studio has permission to read the directory.

## Three Handling Methods

| Handling method | Existing file with the same name | Write position | YAML Properties |
| --- | --- | --- | --- |
| New (overwrite if it exists) | Overwrite existing content | Replace the entire file | Write `title`, `created`, `source`, and `tags` |
| Prepend | Preserve existing content | Add new content at the beginning | Do not write new Properties |
| Append | Preserve existing content | Add new content at the end | Do not write new Properties |

Prepend and Append insert a Markdown separator between the old and new content. They do not try to merge headings or regenerate existing YAML.

{% hint style="warning" %}
When you select a folder and use “New (overwrite if it exists),” the title determines the target filename. An existing file with the same name in that directory is replaced.
{% endhint %}

## Export Reasoning Content

The conversation and message export dialogs provide an **Export Chain of Thought** switch:

- Off: Export only normal answer content.
- On: Include reasoning content when the message contains it.

Exported content becomes regular Markdown. Before sharing the file with someone else or publishing it, check whether it contains drafts, intermediate work, or sensitive information.

The switch does not generate reasoning that did not already exist and does not appear when exporting a Cherry Studio note.

## How Export Works

After you confirm, Cherry Studio:

1. Writes the Markdown content to the system clipboard.
2. Constructs an `obsidian://new` URI containing the vault, file path, and handling method.
3. Asks the operating system to open Obsidian.
4. Lets Obsidian create, overwrite, prepend, or append the file from the clipboard.

A success message in Cherry Studio therefore means the export request was sent; it does not guarantee that the file was written. Switch to Obsidian and confirm that the target file exists with the correct content.

This flow uses parameters such as `clipboard`, `append`, and `overwrite` from the [official Obsidian URI](https://help.obsidian.md/Extending%2BObsidian/Obsidian%2BURI).

## FAQ

### Settings displays “No Obsidian Vault Found”

Launch Obsidian under the same operating system user, open the target local vault, then reenter Cherry Studio settings. Only vaults registered in Obsidian's local configuration can be discovered.

### The vault is visible, but the path list is empty

The vault folder may have moved, be offline, or lack read permission. Return to Obsidian, confirm that the vault opens normally, and check whether its external drive or network directory is online.

### Obsidian does not open after clicking Export

The operating system may not have registered the `obsidian://` protocol. Windows and macOS usually register it after Obsidian runs. On Linux, ensure that the desktop file's `Exec` entry supports the `%u` parameter. See the registration instructions in the official Obsidian URI documentation.

### Cherry Studio reports success, but no note is created

The success message only means the URI was sent. Check whether Obsidian opened, whether the target vault is correct, and whether the operating system lets Cherry Studio open an external protocol. Also confirm that security software did not block or immediately replace the clipboard.

### Export overwrote an old note

“New (overwrite if it exists)” replaces a file at the same path. Recover it from a vault backup, version control, or Obsidian Sync version history. Next time, use a different title, another folder, Prepend, or Append.

### Prepend or Append did not create Properties

This is the current design. Only New/overwrite mode generates YAML Properties; Prepend and Append write only a separator and Markdown body.

### Obsidian is missing from the conversation menu

Go to **Settings > Data Settings > Export Menu** and enable **Export to Obsidian**. If it is already enabled, reenter the current conversation and open the menu again.

### The vault is still missing on Linux

Confirm the Obsidian installation method and configuration path. Cherry Studio checks common XDG, Snap, and Flatpak locations, but a custom portable build or nonstandard path may not be discovered automatically.

If the issue persists, submit your Cherry Studio and Obsidian versions, operating system, installation method, whether an `obsidian://` link opens, and the redacted vault name and path through [Feedback and Suggestions](../question-contact/suggestions.md).
