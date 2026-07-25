---
description: Adjust the theme, colors, zoom, fonts, and topic list layout in Cherry Studio V2.
icon: table-columns
---

# Display Settings

Cherry Studio V2 display options are under **Settings > General Settings > Display & Language**. This page covers appearance and conversation layout settings. For language, system startup, proxy, and privacy settings, see [General Settings](general.md).

## Theme and Accent Color

### Choose a theme

**Theme** provides three modes:

| Mode | Effect |
| --- | --- |
| Light | Always use the light interface |
| Dark | Always use the dark interface |
| System | Follow the operating system's current light or dark appearance |

The interface updates immediately after you choose a mode. With **System**, Cherry Studio changes when the operating system switches appearance.

### Set the accent color

**Accent Color** affects primary buttons, selected states, and emphasized elements. You can:

- Choose a green, red, amber, blue, or purple preset.
- Click the color picker to choose another color.
- Enter a hexadecimal color in the input box, such as `#3B82F6`.

Color input supports `#RGB` and `#RRGGBB`. When saved, the value is converted to the full six-character uppercase format. Invalid colors are not applied.

The default accent color is `#00B96B`.

{% hint style="info" %}
The accent color is not a complete custom theme. To change more interface styles, use [Custom CSS](../../../personalization-settings/css.md), and save your existing styles before making changes.
{% endhint %}

## Platform-Specific Window Options

Some display options appear only on the relevant operating system:

- **macOS: Transparent Window** — Switch between transparent and opaque window styles.
- **Linux: Use System Title Bar** — Use the window title bar provided by the system. The app restarts after you confirm.

Windows does not display either option. Desktop environment, system theme, and graphics configuration can affect transparency and title bar appearance.

## Interface Zoom

The **Zoom** section displays the current percentage:

- Click `-` to zoom out.
- Click `+` to zoom in.
- Click the reset icon to restore the default percentage.

Each adjustment changes zoom by 10%. Zoom affects text, icons, and interface controls together; it is different from changing only the font size of chat messages.

You can also use these default shortcuts:

| Action | macOS | Windows / Linux |
| --- | --- | --- |
| Zoom in | `⌘ + =` | `Ctrl + =` |
| Zoom out | `⌘ + -` | `Ctrl + -` |
| Reset | `⌘ + 0` | `Ctrl + 0` |

Use **Settings > Shortcuts** as the source of truth for the current shortcut states. For details, see [Shortcut Settings](key-shortcut.md).

## Font Settings

### Global font

**Global Font** affects regular text throughout the app interface. The selector reads fonts available on the current system and previews them in the list.

If a font name does not appear:

1. Confirm that the font is installed in the operating system.
2. Close and reopen Cherry Studio so the app reads the font list again.
3. Return to the font selector and search again.

Click the reset icon on the right to restore the default font.

### Code font

**Code Font** is used for code and other areas that need monospaced text. Choose a monospaced font that contains the target language characters, numbers, and common symbols to avoid misaligned code or missing glyphs.

Global Font and Code Font are independent. Resetting one does not affect the other.

{% hint style="info" %}
The chat message font size belongs to message display settings and is not adjusted separately here. Use Zoom when the entire interface is too large or small. Use Global Font or Code Font when you only want to change the typeface.
{% endhint %}

## Topic Settings

### Topic position

**Topic Position** determines which side of the conversation area shows the topic list:

- **Left:** Assistants and topics share the left area, with tabs to switch between them.
- **Right:** The assistant list stays on the left, and the topic list appears on the right side of the conversation area.

Changing this option does not move or delete existing topics or messages; it only changes the interface layout.

### Automatically switch to topics

This option appears only when Topic Position is **Left**.

When enabled, clicking an assistant or Agent automatically switches to its topic / session list. When disabled, it changes only the current assistant or Agent and does not switch the left tab.

### Show topic time

When enabled, each topic displays its creation time in `YYYY/MM/DD HH:mm` format. Disabling the option hides the time without changing the topic's creation timestamp.

### Keep pinned topics first

When enabled, pinned topics appear before regular topics, while regular topics retain their existing order.

Disabling the option does not remove pinned markers; it only stops reordering by pinned status. You can still pin or unpin a topic from its menu.

## FAQ

### The interface did not change immediately after selecting “System”

First confirm that the operating system has switched to another appearance and that Cherry Studio still has **System** selected. If the desktop environment does not deliver the system theme event correctly, reopen the app and check again.

### A newly installed font is missing from the list

Cherry Studio reads system fonts when you enter Settings. After installing a font, reopen the app, then return to **Display & Language**.

### The topic list is not in the expected position

Check whether **Topic Position** is set to Left or Right, and confirm that the topic list is not currently hidden on the conversation page. You can also restore it with the topic display shortcut, which defaults to `Cmd/Ctrl + ]`.

### Custom CSS causes display problems

Go to **Settings > General Settings > Custom CSS**, temporarily remove the relevant styles, and see whether the interface recovers. Custom CSS selectors may change between versions, so avoid relying on deeply nested internal DOM structures.

If the problem persists, submit your operating system, Cherry Studio version, display setting values, and a full interface screenshot through [Feedback and Suggestions](../../../question-contact/suggestions.md).
