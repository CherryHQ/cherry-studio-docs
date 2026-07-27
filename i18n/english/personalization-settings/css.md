---
icon: file-code
---

# Custom CSS

Custom CSS can override Cherry Studio interface styles. Use it to adjust colors, spacing, rounded corners, and component appearances that built-in settings do not provide.

{% hint style="warning" %}
Custom CSS is an advanced feature. Component structure, class names, and variables may change after an app upgrade; a style that works now is not guaranteed to keep working in later versions.
{% endhint %}

## When to Use It

Before writing CSS, check **Settings > General Settings > Display & Language**. V2 provides built-in options for:

- Light, Dark, and System themes;
- The theme accent color;
- Interface zoom;
- Global and code fonts;
- Topic position and display.

These built-in options are more stable and can be reset directly. Use Custom CSS only when built-in settings cannot produce the result you need.

## Open the CSS Editor

1. Click **Settings** in the lower-left corner of Cherry Studio.
2. Enter **General Settings**.
3. Select **Custom CSS** in the second-level menu.
4. Enter or paste CSS into the editor.

The content is saved to local settings and applied to the interface after it changes; there is no separate Save button.

Keep a copy of the current CSS before changing it, then work in small sections. After each addition, check chats, Settings, dialogs, and auxiliary windows so an issue is easier to locate.

## Start with a Minimal Style

The following example changes only the user message background and a common corner radius:

```css
:root {
  --chat-background-user: rgba(0, 185, 107, 0.08);
  --list-item-border-radius: 12px;
}
```

To configure Light and Dark themes separately, use the theme classes on the root element:

```css
:root:not(.dark) {
  --chat-background-user: rgba(0, 120, 80, 0.08);
}

:root.dark {
  --chat-background-user: rgba(90, 220, 160, 0.12);
}
```

{% hint style="info" %}
Cherry Studio V2 uses `.light` / `.dark` classes for the current theme. The `body[theme-mode="dark"]` pattern common in old themes should no longer be the foundation for new styles.
{% endhint %}

## Common Semantic Variables

Prefer overriding semantic variables. They are less likely to break than selectors that target internal class names directly.

| Variable | Purpose |
| --- | --- |
| `--color-primary` | Primary accent color |
| `--color-background` | Main background color |
| `--color-background-subtle` | Secondary background color |
| `--color-foreground` | Primary text color |
| `--color-foreground-secondary` | Secondary text color |
| `--color-border` | Common border color |
| `--color-card` | Card background color |
| `--color-popover` | Popover background color |
| `--chat-background-user` | User message background color |
| `--chat-background-assistant` | Assistant message background color |
| `--font-family` | Global font stack |
| `--code-font-family` | Code font stack |

For example, the following style sets separate backgrounds and borders for both themes:

```css
:root:not(.dark) {
  --color-background: #f7f8f6;
  --color-background-subtle: #f0f2ef;
  --color-border: rgba(20, 35, 28, 0.12);
}

:root.dark {
  --color-background: #171a18;
  --color-background-subtle: #1e221f;
  --color-border: rgba(235, 255, 244, 0.12);
}
```

{% hint style="warning" %}
The accent color and fonts already have built-in settings. If CSS overrides the same variables, the final result depends on selector specificity and load order and may differ from the value shown in Settings.
{% endhint %}

## Modify a Specific Component

When variables cannot achieve the result, inspect the element with browser developer tools, then write a selector.

```css
/* 示例：让设置页中的卡片边框更明显 */
[class*="border-border"] {
  border-color: color-mix(in srgb, var(--color-border) 75%, var(--color-foreground) 25%);
}
```

These selectors are more vulnerable to version changes than semantic variables. Follow these principles:

- Limit the scope whenever possible; avoid overriding every `div`, `button`, or `input`.
- Avoid selectors that depend on hierarchy and position, such as `:nth-child()`.
- Do not assume that generated class names remain stable.
- Avoid broad use of `!important`.
- Add a short comment to each group of rules to explain its purpose.
- Check both Light and Dark themes after a change.

The component selector above only demonstrates the technique; it is not a stable public interface.

## Find Current Variables

Cherry Studio is migrating to the new V2 design system, so variables fall into two categories:

- [V2 theme variables](https://github.com/CherryHQ/cherry-studio/blob/main/packages/ui/src/styles/theme.css);
- [Variables for legacy interface compatibility](https://github.com/CherryHQ/cherry-studio/blob/main/src/renderer/assets/styles/legacy-vars.css).

Compatibility variables are still in use but may be removed later. New themes should prefer V2 semantic variables and recheck their results after each major version upgrade.

The **cherrycss.com** link at the top of the editor opens the community theme site. Before using a community theme, read its complete CSS and confirm that the source is trustworthy.

## Security Recommendations

CSS is not JavaScript, but it can still request network resources through `url()`, `@import`, or external fonts. When using a third-party theme:

- Check whether it references an unfamiliar domain.
- Do not put a token, Cookie, username, or local path in CSS.
- Prefer storing required images and fonts in a trusted location.
- Preserve the original theme source and version number.
- Do not run an extra console script from the theme author if its purpose is unclear.

## Restore Default Styles

Under normal circumstances:

1. Open **Settings > General Settings > Custom CSS**.
2. Copy and back up any content you still need.
3. Remove all CSS from the editor.
4. Confirm that the interface recovers; restart the app if necessary.

If an incorrect style covers the Settings button or makes the page unusable, see [Clear CSS Settings](clear-css.md).

## FAQ

### CSS has no effect

First confirm that the syntax is complete and no closing brace is missing. Then check whether the selector still matches elements in the current version and whether the variable exists.

### The Light theme works, but the Dark theme does not

Separate the rules for both themes, use `:root:not(.dark)` and `:root.dark`, and check the contrast between text and background.

### Changing the accent color has no effect

Built-in settings write the accent color to a runtime variable. Prefer **Display & Language > Accent Color**. If CSS must override it, check `--cs-theme-primary` and selector specificity, but avoid maintaining two sets of values at once.

### The layout breaks after an upgrade

Temporarily remove all Custom CSS and confirm whether the issue disappears. Restore it section by section, removing rules that depend on old class names, old DOM hierarchy, or compatibility variables.

### An auxiliary window looks wrong

Custom CSS may also apply to Quick Assistant, Selection Assistant, and other windows. Avoid overly broad global selectors and check each window you use.

***

### Get Help and Submit Feedback

If you encounter a problem during configuration or use, contact us through the official channels under [Feedback and Suggestions](../question-contact/suggestions.md).
