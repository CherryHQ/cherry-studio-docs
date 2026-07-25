---
description: View, change, and troubleshoot Cherry Studio app, conversation, and global shortcuts.
icon: keyboard
---

# Shortcut Settings

Shortcut Settings provides one place to manage keyboard actions in Cherry Studio. You can review current bindings, change editable key combinations, temporarily disable an action, or restore the default configuration.

{% hint style="info" %}
In this guide, `Cmd/Ctrl` means `Command (⌘)` on macOS and `Ctrl` on Windows and Linux. The app displays the appropriate key for your current operating system.
{% endhint %}

## Open Shortcut Settings

Go to **Settings > Shortcuts**.

The left side of the page organizes shortcuts into four groups:

| Group | Included actions |
| --- | --- |
| Global and Window | Show or hide the app, open Settings, toggle the sidebar, zoom the interface, and search globally |
| Message Interaction | Clear messages, clear context, search messages, copy or edit messages, and select a model |
| Sessions and Topics | Create and rename topics, and show or hide the topic list |
| AI Assistant Tools | Global shortcuts for Quick Assistant and Selection Assistant |

A shortcut appears only when its feature is enabled. For example, Quick Assistant appears under **AI Assistant Tools** only after you enable it. The two Selection Assistant shortcuts are also available only on macOS and Windows.

The search box at the top searches only the current group. You can filter by an action name or by the displayed key combination.

## Change a Shortcut

### Set or replace a binding

1. Find the action you want to change.
2. Click the key area on the right. If the action is unbound, click **Press shortcut**.
3. Press the new key combination.
4. The shortcut is saved and enabled immediately after it passes validation.

Press `Esc` while editing to cancel. A valid combination usually includes both a modifier and a regular key, such as `Cmd/Ctrl + Shift + M`. You can also use `Esc` and `F1` through `F12` by themselves.

Some system-level shortcuts cannot be edited, including Open Settings, Exit Full Screen, and interface zoom. They remain visible in the list, but their key areas cannot be clicked.

### Enable or disable

Each shortcut has its own switch on the right:

- Turning the switch off preserves the key binding but stops the action from responding.
- Turning it back on continues using the existing binding.
- An unbound action cannot be enabled until you assign a key combination.

**Enable All** and **Disable All** affect only bound shortcuts in the current group and current filtered results. They do not change unbound actions.

### Resolve conflicts

Cherry Studio checks two types of conflict:

- **Duplicate within the app:** If the new combination is already assigned to another enabled Cherry Studio action, the app identifies the conflicting action and refuses to save the new binding.
- **Reserved by the system or another app:** If the operating system cannot register the combination, the app shows a red warning that the shortcut is already in use by the system or another application.

If a conflict occurs, assign a different combination to one of the actions. Reserved system keys, input method shortcuts, window manager shortcuts, and global shortcuts from other background apps can all prevent registration.

## Current Default Shortcuts

The following tables describe the current default configuration in Cherry Studio V2. After an upgrade, your actual bindings may retain previous customizations, so use the values displayed in the app as the source of truth.

### Global and Window

| Action | Default binding | Default state | Description |
| --- | --- | --- | --- |
| Show / Hide App | Unbound | Disabled | Show or hide Cherry Studio while another app is in the foreground |
| Open Settings | `Cmd/Ctrl + ,` | Enabled | Open the Settings window |
| Toggle Sidebar | `Cmd/Ctrl + [` | Enabled | Toggle or focus the assistant sidebar |
| Exit Full Screen | `Esc` | Enabled | Exit full-screen mode |
| Zoom In | `Cmd/Ctrl + =` | Enabled | Increase interface zoom; numpad `+` also works |
| Zoom Out | `Cmd/Ctrl + -` | Enabled | Decrease interface zoom; numpad `-` also works |
| Reset Zoom | `Cmd/Ctrl + 0` | Enabled | Restore the default zoom level |
| Search Messages | `Cmd/Ctrl + Shift + F` | Enabled | Open global message search |

### Message Interaction

| Action | Default binding | Default state | Description |
| --- | --- | --- | --- |
| Clear Messages | `Cmd/Ctrl + L` | Enabled | Delete all messages in the current topic after confirmation |
| Search Messages in Current Conversation | `Cmd/Ctrl + F` | Enabled | Find messages within the current topic |
| Clear Context | `Cmd/Ctrl + K` | Enabled | Toggle the context separator in the current topic without deleting message history |
| Copy Previous Message | `Cmd/Ctrl + Shift + C` | Disabled | Copy the body of the last message in the current topic |
| Edit Last User Message | `Cmd/Ctrl + Shift + E` | Disabled | Open the last user message for editing |
| Select Model | `Cmd/Ctrl + Shift + M` | Enabled | Open the conversation model selector for the current assistant |

{% hint style="warning" %}
**Clear Messages** and **Clear Context** are different actions. Clear Messages deletes every message in the current topic after confirmation. Clear Context only starts subsequent conversation from a new context segment; existing messages remain on the page. Triggering Clear Context again removes an unused separator at the end.
{% endhint %}

### Sessions and Topics

| Action | Default binding | Default state | Description |
| --- | --- | --- | --- |
| New Topic | `Cmd/Ctrl + N` | Enabled | Create an independent topic under the current assistant |
| Rename Topic | `Cmd/Ctrl + T` | Disabled | Change the current topic name |
| Toggle Topic Display | `Cmd/Ctrl + ]` | Enabled | Toggle or focus the topic list |

### AI Assistant Tools

| Action | Default binding | Default state | Requirement |
| --- | --- | --- | --- |
| Quick Assistant | `Cmd/Ctrl + E` | Disabled | Enable the feature in Quick Assistant settings first |
| Toggle Selection Assistant | Unbound | Disabled | Enable Selection Assistant first; macOS and Windows only |
| Selection Assistant: Pick Text | Unbound | Disabled | Enable Selection Assistant first; macOS and Windows only |

Quick Assistant, Selection Assistant, and Show / Hide App use global shortcuts. After they are bound and enabled, they respond even when the Cherry Studio window is not focused. Most other conversation and window shortcuts work only while the Cherry Studio window is in the foreground.

For configuration details, see [Quick Assistant](../kuai-jie-zhu-shou.md) and [Selection Assistant](../selection-assistant.md).

## Restore Default Settings

An edited shortcut displays a restore icon. Clicking it restores only that action's default binding and default enabled state.

Click **Reset** at the top of the page and confirm to restore the default configuration for all shortcuts. This action overwrites your custom shortcut bindings.

## FAQ

### A shortcut does not respond

Check the following in order:

1. Confirm that the action has a key binding and is enabled.
2. Confirm that the relevant feature, such as Quick Assistant or Selection Assistant, is enabled.
3. For conversation shortcuts, confirm that the Cherry Studio window is in the foreground.
4. Check whether the interface shows a red warning that the system or another app is using the shortcut.
5. Check whether the operating system, input method, or another background app uses the same combination.

If the shortcut still does not work after you change it, test with an uncommon combination, then try restarting Cherry Studio.

### Why can't I see the Selection Assistant shortcuts?

Selection Assistant shortcuts appear only when the feature is enabled, and they are currently supported only on macOS and Windows. Linux does not display these two shortcuts.

### Why didn't “Enable All” enable some actions?

The bulk action processes only shortcuts that are already bound within the current group and current search results. For any unbound item that displays “Press shortcut,” assign a key combination first.

### How do I quickly return to the default configuration?

If you changed only one shortcut by mistake, use the restore icon next to that action. If several settings are now incorrect, use **Reset** at the top of the page.

If the issue persists, submit your operating system version, Cherry Studio version, conflicting key combination, and reproduction steps through [Feedback and Suggestions](../../../question-contact/suggestions.md).
