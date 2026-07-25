---
description: Configure language and display, system startup, proxy, notifications, privacy, and custom CSS in Cherry Studio V2.
icon: sliders
---

# General Settings

General Settings in Cherry Studio V2 is divided into four pages:

1. **Display and Language**
2. **System and Startup**
3. **Privacy and Advanced**
4. **Custom CSS**

Open:

> **Settings → General Settings**

This page explains what each setting does, its dependencies, and when a restart is required.

## Display and Language

### Interface Language

The application currently offers:

- Simplified Chinese
- Traditional Chinese
- English
- German
- Japanese
- Russian
- Greek
- Spanish
- French
- Portuguese
- Romanian
- Vietnamese

The interface updates immediately after switching. Third-party model names, errors returned by providers, assistant content, and user-defined text are not translated automatically.

{% hint style="info" %}
The number of languages supported by the application interface is not the same as the languages in which the community documentation is published. The community documentation is currently maintained in Simplified Chinese, Traditional Chinese, English, Japanese, and Russian.
{% endhint %}

### Theme and Accent Color

Theme options are:

- Light
- Dark
- Follow System

The accent color is used for buttons, selected states, and some emphasized elements. If custom CSS also changes theme variables, its final effect may override the accent color setting.

### Transparent Window

macOS displays a Transparent Window switch. It controls system material and window background effects; other platforms do not show this option.

If transparency causes low text contrast, window flickering, or unclear screenshots, switch back to an opaque window.

### Use System Title Bar

Linux displays a Use System Title Bar switch. After a change, the application asks for confirmation and restarts.

The system title bar can improve compatibility with some desktop environments and window managers, but looks different from Cherry Studio's built-in title bar.

### Interface Zoom

You can zoom in or out in `10%` increments or restore the default zoom.

Zoom affects the visual size of the entire Settings window and main interface. When taking screenshots or investigating layout problems, record the zoom level. A value other than `100%` may show different content at the same window size.

### Global and Code Fonts

You can select system fonts separately for:

- The global interface font;
- Code blocks and editors.

The list comes from the current operating system. If another device does not have the same font, the interface falls back to the default.

For more appearance details, see [Display Settings](display.md) and [Font Settings](../../../personalization-settings/font.md).

### Topic List

The topic list can:

- Appear on the left or right;
- Show topic times;
- Place pinned topics at the top.

When the topic list is on the left, you can also enable **Automatically Switch to Topic List After Clicking an Assistant**. This switch is not shown when the list is on the right.

## System and Startup

### Launch at Startup

When enabled, Cherry Studio attempts to start when you sign in to the system.

If it does not work, check:

- Whether the system allows login items or startup applications;
- Whether security software blocks it;
- Whether the application was moved or reinstalled;
- Whether the current user can change login items.

### Minimize to Tray at Startup

When enabled, the application does not show the main window immediately at startup.

This setting depends on the tray feature. Enabling it automatically enables **Show Tray Icon**.

### Show Tray Icon

The tray menu can show the main window, open Quick Assistant, or quit the application. When the tray icon is disabled:

- **Minimize to Tray at Startup** is also disabled;
- **Minimize to Tray When Closing the Window** is also disabled.

This prevents a window from becoming hidden with no way to reopen it.

### Minimize to Tray When Closing the Window

When enabled, clicking the window's close button only hides the main window; the Cherry Studio process continues running in the background.

To quit completely, use Quit in the tray menu. When this switch is off, closing behavior follows the operating system and application exit logic.

{% hint style="warning" %}
Background operation may keep active tasks, channels, or scheduled tasks running. To stop all activity, do not merely close the window; confirm that the application has quit.
{% endhint %}

## Proxy Settings

Proxy modes are:

| Mode | Behavior |
| --- | --- |
| System Proxy | Uses the operating system's current proxy configuration |
| Custom Proxy | Uses the proxy address and bypass rules entered in Cherry Studio |
| No Proxy | Does not actively use a proxy |

### Custom Proxy Address

Enter a valid HTTP, HTTPS, or SOCKS proxy URL, for example:

```text
socks5://127.0.0.1:6153
```

The protocol and port must match the local proxy application. If authentication is required, configure it in a URL form supported by that application and avoid exposing usernames or passwords in screenshots or feedback.

Cherry Studio rejects an invalid address.

### Proxy Bypass Rules

Bypass rules connect specified addresses directly instead of using the custom proxy. They are useful for:

- `localhost` and `127.0.0.1`;
- LAN model services;
- Local SearXNG, Ollama, or LM Studio;
- Internal enterprise domains that should not use the proxy.

Follow the setting's instructions for rule format. An incorrect bypass rule may route a local service through the proxy or make an external service fail after bypassing it.

### Proxy Troubleshooting

When a model service times out, do not only switch proxy modes repeatedly. Check in order:

1. Whether a browser or terminal can access the provider;
2. Whether the proxy application is listening on the configured port;
3. Whether Cherry Studio's proxy mode and address are correct;
4. Whether a bypass rule matches the target domain incorrectly;
5. Whether a local service should use a direct connection;
6. Whether the window or application needs to be reopened or restarted after changing the proxy.

## Disable Hardware Acceleration

By default, Electron uses hardware acceleration to render the interface. Enable **Disable Hardware Acceleration** only for problems such as:

- A black or white screen;
- Window flickering;
- Incorrect font or image rendering;
- Crashes caused by a specific graphics driver.

After a change, the application asks for confirmation and restarts.

Disabling hardware acceleration may make scrolling, animation, and complex interfaces less smooth. It is not a universal solution to every performance problem.

## Spell Check

When enabled, inputs use Electron's spell checking to mark potentially misspelled words.

On Windows and Linux, you can also select checking languages, including English, Spanish, French, German, Italian, Portuguese, Russian, Dutch, Polish, Slovak, and Greek.

macOS uses system-provided spell checking, so the interface does not show the same multi-language selector.

Spell check affects only local input suggestions. It does not call a model to correct text or change messages that have already been sent.

## Notifications

You can control:

| Notification | Trigger |
| --- | --- |
| Assistant Messages | Message events such as completion of an assistant response |
| Backup | The backup flow completes or produces a result |
| Knowledge Base | Knowledge base embedding or indexing completes |

Even when an in-app switch is enabled, the operating system may block notifications. Allow Cherry Studio in system notification settings and check Focus or Do Not Disturb mode.

A notification only means that a task produced a result; it does not guarantee success. Check the final status and error information for backup and knowledge base tasks.

## Anonymous Error Reports and Usage Statistics

**Send Anonymous Error Reports and Usage Statistics** controls the application's data collection switch.

Whether to enable it is the user's choice. To understand collection scope, retention, and third-party processing, review the privacy notice shown by the current version and the project's official privacy policy. Do not infer every data category from the switch label alone.

Disabling the switch does not prevent users from voluntarily sending feedback, nor does it stop configured model services, Web Search, MCP, or external integrations from transmitting data required by their features.

## Developer Mode

Developer Mode enables features intended for debugging or development.

Regular users can leave it off. When troubleshooting, enable it temporarily according to developer or maintainer instructions, then disable it afterward.

Developer Mode does not automatically fix connection problems or give models extra capabilities. Debug interfaces and logs may contain conversations, paths, request parameters, or service information and must be sanitized before sharing.

## Custom CSS

General Settings includes a CSS editor that can override application styles directly.

It can adjust:

- Font sizes and spacing;
- Colors and corner radii;
- How specific components are displayed;
- Community themes.

For instructions on writing, restoring, and clearing CSS, see [Custom CSS](../../../personalization-settings/css.md) and [Clear CSS](../../../personalization-settings/clear-css.md).

{% hint style="danger" %}
Incorrect CSS may hide buttons, make text invisible, or break the layout. Read third-party theme code and back up existing CSS before pasting it. If Settings becomes unusable, follow the Clear CSS documentation to recover.
{% endhint %}

Internal class names and structures may change after a Cherry Studio update, so old CSS is not guaranteed to remain compatible.

## Recommended Check Order

### New Users

1. Select the interface language;
2. Choose Light, Dark, or Follow System;
3. Keep zoom at `100%`;
4. Enable startup and tray behavior only as needed;
5. Start with System Proxy and switch to Custom Proxy only when necessary;
6. Keep hardware acceleration enabled;
7. Enable notifications as needed.

### Network Problems

1. Check the provider key and address;
2. Check the system or custom proxy;
3. Check bypass rules;
4. Test the provider's official address on the same network;
5. Restart the application and test again.

### Display Problems

1. Restore `100%` zoom;
2. Switch to the default theme and fonts;
3. Temporarily clear custom CSS;
4. Disable Transparent Window;
5. As a final step, disable hardware acceleration and restart.

## Troubleshooting

### Why Does the Application Have More Languages Than the Documentation?

The application and community documentation have different language coverage. The application currently provides twelve interface languages; this community documentation is currently maintained in five languages.

### Custom Proxy Still Cannot Connect After Saving

Confirm that the URL includes a protocol such as `http://` or `socks5://`, the port is correct, the proxy application is running, and the target domain is not bypassed.

### The Application Still Runs After the Window Is Closed

Check **Minimize to Tray When Closing the Window**. When enabled, the close button does not quit the application; quit from the tray menu.

### Tray-Related Switches Change Automatically

This is a dependency:

- Enabling “Minimize to Tray at Startup” or “Minimize to Tray When Closing the Window” automatically enables the tray;
- Disabling the tray also disables both dependent settings.

### The Application Restarts After Changing the System Title Bar or Hardware Acceleration

This is expected. Both settings must take effect during application startup, so Cherry Studio restarts after the change is confirmed.

### A Font Is Missing from the List

The list comes from fonts installed on the current system. Install the font in the operating system, then reopen Cherry Studio. Synchronizing settings from another device does not synchronize font files.

### Notifications Are Enabled but Do Not Appear

Check system notification permission, Do Not Disturb mode, and whether the task actually finished. A Linux desktop environment may also require an available notification service.

***

### Get Help and Submit Feedback

If General Settings has a problem, submit feedback through the official channels listed in [Feedback and Suggestions](../../../question-contact/suggestions.md). Include the Cherry Studio version, operating system, relevant switch, proxy mode, or display setting, and sanitize credentials, domains, and personal paths in logs and screenshots.
