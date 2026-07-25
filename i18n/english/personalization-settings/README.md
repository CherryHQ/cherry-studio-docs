---
icon: pen-swirl
---

# Personalization Settings

Cherry Studio V2 places common appearance options under **Settings > General Settings > Display & Language**. You can adjust the theme, color, zoom, fonts, and topic layout without writing code. Use Custom CSS only when the built-in options cannot meet your needs.

{% hint style="info" %}
“Personalization Settings” is a topic name in this documentation, not a separate in-app settings menu. Open **Settings** in the lower-left corner, then enter **General Settings**.
{% endhint %}

## Choose the Right Method First

| What you want to do | Recommended entry | Risk |
| --- | --- | --- |
| Switch between Light, Dark, and System | Settings > General Settings > Display & Language | Low |
| Change the theme accent color | Settings > General Settings > Display & Language | Low |
| Zoom the entire interface in or out | Settings > General Settings > Display & Language | Low |
| Change the global font or code font | Settings > General Settings > Display & Language | Low |
| Adjust topic position, time, and pinned ordering | Settings > General Settings > Display & Language | Low |
| Deeply customize component styles | Settings > General Settings > Custom CSS | Medium |
| Migrate app data to another drive | Settings > Data Settings > Data Directory | High; create a backup first |

Start with the built-in options. Built-in settings are maintained across versions and are usually more stable than Custom CSS.

## Display & Language

Open **Settings > General Settings > Display & Language** to adjust the following.

### Language and Theme

- **Language**: Change the Cherry Studio interface language.
- **Theme**: Choose Light, Dark, or System.
- **Accent Color**: Choose a preset color or enter a custom color.
- **Window Transparency**: Appears only on macOS.
- **Use System Title Bar**: Appears only on Linux and requires an app restart after changes.

### Interface Zoom

Use the minus and plus buttons to adjust the zoom level step by step. Click the reset button to restore the default zoom.

If only message text looks small, adjust the message font size first. If buttons, sidebars, and dialogs are all small, adjust the entire interface zoom.

### Fonts

V2 reads fonts installed in the operating system and provides separate options for:

- **Global Font**: Used for most interface text and body content.
- **Code Font**: Used for code blocks, code editors, and other monospaced content.

A selected font takes effect immediately. Click its reset button to restore the default. For suggestions when installing new fonts, see [Font Recommendations](font.md).

{% hint style="info" %}
The font list comes from the current operating system. If the list does not update after installing a font, quit Cherry Studio completely and reopen it.
{% endhint %}

### Topic Layout

You can place the topic list on the left or right and control:

- Whether clicking an assistant automatically switches to topics.
- Whether topic time is displayed.
- Whether selected topics are pinned to the top.

“Automatically switch to topics when clicking an assistant” appears only when topics are positioned on the left.

## Custom CSS

When the built-in theme and layout options cannot meet your needs, go to **Settings > General Settings > Custom CSS** and edit the styles directly.

Custom CSS can change spacing, colors, rounded corners, and the appearance of specific components. Component structure may change after an app upgrade, however, and old rules may stop working. Read [Custom CSS](css.md) before starting and keep a copy of a working stylesheet.

If an incorrect style makes Settings unusable, follow [Clear CSS Settings](clear-css.md) to recover.

{% hint style="warning" %}
Do not reach for CSS first when changing a font or accent color. V2 provides built-in options for both; built-in settings are easier to restore and less likely to break after an upgrade.
{% endhint %}

## Data Directory

Changing the storage location is a data migration operation, not an appearance setting. The entry is under **Settings > Data Settings > Data Directory**.

Migration can involve conversations, assistants, knowledge bases, and other local data. Create a backup first and confirm that the target directory:

- Is not the root of a drive.
- Is not inside the current data directory.
- Is not inside the app installation directory.
- Is writable.
- Has enough free space.

For detailed steps and precautions, see [Change the Storage Location](storage.md).

## Recommended Order

To adjust the interface quickly, use this order:

1. Choose the theme and accent color.
2. Adjust interface zoom.
3. Choose the global font and code font.
4. Adjust the topic layout.
5. Add Custom CSS only after confirming that built-in options still cannot meet your needs.

This reduces style conflicts and makes restoring the default appearance easier later.

***

### Get Help and Submit Feedback

If you encounter a problem during configuration or use, contact us through the official channels under [Feedback and Suggestions](../question-contact/suggestions.md).
