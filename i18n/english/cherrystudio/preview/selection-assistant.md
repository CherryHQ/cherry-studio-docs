---
icon: highlighter
---

# Selection Assistant

Selection Assistant displays a floating toolbar when you select text in another application. You can translate, explain, summarize, search, or copy the selected content immediately, and you can add your own AI actions.

{% hint style="info" %}
Selection Assistant and [Quick Assistant](kuai-jie-zhu-shou.md) are separate features. Selection Assistant acts on text you have just selected, while Quick Assistant opens a window for entering a new request from a shortcut or the system tray.
{% endhint %}

## Platform support

| Platform | Current support |
| --- | --- |
| macOS | Supported; Accessibility permission is required the first time you enable it |
| Windows | Supports immediate selection, Ctrl Key, and Shortcut trigger modes |
| Linux X11 | Supports the main features; keyboard monitoring may require permission for the `input` group |
| Linux Wayland | Limited by the desktop environment; the toolbar may only appear in the center and Application Filter may not work |

In a Wayland session, the settings page checks XWayland, permission for the `input` group, and desktop compositor compatibility. If the current environment is incompatible, switch to X11.

## Enable Selection Assistant

1. Open **Settings → Selection Assistant**.
2. Turn on **Enable**.
3. Choose a Trigger Mode.

Before the feature is enabled, the settings page displays a demonstration toolbar so you can check Compact Mode and the action layout.

### macOS Accessibility permission

When you enable the feature for the first time on macOS:

1. Select Go to Settings in the permission notice.
2. Open **Privacy & Security → Accessibility**.
3. Grant permission to Cherry Studio.
4. Return to Cherry Studio and enable Selection Assistant again.

If this permission is revoked, Cherry Studio automatically disables Selection Assistant.

### Linux permission notice

If the settings page reports that permission for the `input` group has not been granted, run:

```bash
sudo usermod -aG input $USER
```

Then sign out of your current system session and sign in again. On Wayland, you may also need to launch in XWayland mode; follow the environment check shown on the settings page.

## Choose a Trigger Mode

| Mode | Platform | Behavior |
| --- | --- | --- |
| Selection | macOS, Windows, Linux | Shows the toolbar immediately after you select text |
| Ctrl Key | Windows | Shows the toolbar only when you hold Ctrl after selecting text |
| Shortcut | macOS, Windows | Shows the toolbar when you press the configured selection shortcut |

To use Shortcut mode, open **Settings → Shortcuts**, then configure and enable a key combination for “Selection Assistant: Select Text.” No shortcut is assigned by default.

If immediate selection triggers the toolbar unintentionally, use Ctrl Key or Shortcut mode instead.

## Use the toolbar

1. Select text in a supported application.
2. Wait for the toolbar to appear, or press the trigger you selected.
3. Select the action you need.

The Cherry Studio icon on the left side of the toolbar is a drag area that moves the entire toolbar. With **Compact Mode** enabled, the toolbar displays only icons; hover over an icon to see its name.

## Built-in actions

Selection Assistant includes seven built-in actions.

| Action | Default state | Behavior |
| --- | --- | --- |
| Translate | Enabled | Detects the source language and chooses between the target and alternative languages |
| Explain | Enabled | Uses a model to explain the selected content |
| Summarize | Enabled | Uses a model to summarize the selected content |
| Search | Enabled | Opens a query with the configured search engine |
| Copy | Enabled | Writes the selected content to the clipboard |
| Refine | Disabled | Uses a model to optimize or polish the selected content |
| Quote | Disabled | Quotes the selected content in the input box of the main Cherry Studio window |

Translate uses the configured translation model. Explain, Summarize, Refine, and custom AI actions without a selected assistant use the default model.

{% hint style="warning" %}
Web search, MCP, and Knowledge Base are disabled in Selection Assistant AI result windows. If you need these tools, quote the content to the main window and continue there.
{% endhint %}

## Arrange and enable actions

Under **Settings → Selection Assistant → Actions**, enabled actions appear in the upper list and disabled actions appear in the lower list.

You can:

* Drag actions to change their order on the toolbar
* Drag an action to the upper list to enable it
* Drag an action to the lower list to disable it
* Reset built-in actions to their default order and state

The toolbar can have up to 8 enabled actions and must retain at least 1. Resetting does not delete custom actions, but it moves them to the disabled area.

You cannot edit the prompts for built-in actions here. You can configure a different search engine for Search.

## Add a custom action

You can create up to 10 custom actions.

1. Select Add Custom Action in the Actions settings.
2. Enter an action name.
3. Select or randomly generate a Lucide icon.
4. Choose the default model or select an assistant.
5. Enter a prompt.
6. Save the action, then drag it to the enabled area.

Use `{{text}}` in the prompt to represent the selected text. If you do not include the placeholder, the selected text is automatically appended to the end of the prompt.

When you choose “Use Assistant,” the action also uses that assistant's system prompt, model, and model parameters.

## Configure a search engine

1. Find **Search** in the Actions list.
2. Select its settings button.
3. Choose Google, Baidu, or Bing, or add a custom search engine.

A custom URL must:

* Start with `http://` or `https://`
* Include the `{{queryString}}` placeholder

When you run Search, Cherry Studio URL-encodes the selected text before replacing the placeholder. If the selected content is already a URL or an absolute local path, Cherry Studio attempts to open it directly.

## Use the result window

Translate, Explain, Summarize, Refine, and custom AI actions open a separate result window.

In the window, you can:

* Show or hide the original text
* Copy the original text or model result
* Stop generation
* Regenerate
* Minimize or close the window
* Pin the window
* Temporarily adjust its opacity

In a Translate window, you can also change the target language directly and set the target and alternative languages.

## Adjust window behavior

Under **Action Window**, you can configure:

| Setting | Effect |
| --- | --- |
| Follow Toolbar | Opens the result window near the toolbar; when disabled, opens it in the center |
| Remember Size | Reuses the last adjusted window size during the current app session |
| Auto Close | Closes an unpinned result window when it loses focus |
| Auto Pin | Pins each result window by default when it opens |
| Opacity | Sets the default result window opacity from 20% to 100% |

Adjusting opacity in a result window affects only that window. The setting on the settings page applies to result windows opened afterward.

## Configure Application Filter

Application Filter can limit Selection Assistant to specified applications or exclude specified applications.

1. Open **Settings → Selection Assistant → Advanced**.
2. Select Whitelist or Blacklist.
3. Select Edit and enter one application identifier per line.

| Platform | Value | Example |
| --- | --- | --- |
| macOS | Bundle ID, supports partial matching | `com.google.Chrome` |
| Windows | Executable file name, supports partial matching | `chrome.exe` |

Entries are converted to lowercase and duplicates are removed. Application Filter may not work in Wayland mode.

## Troubleshooting

### The toolbar does not appear after selecting text

Make sure the feature is enabled and the correct Trigger Mode is selected, then check whether the current application is excluded by Application Filter. On macOS, also check the Accessibility permission.

### Ctrl Key mode does not work on Windows

Some applications or keyboard mapping tools intercept Ctrl. Use Selection or Shortcut mode instead, and check whether a tool such as AHK has remapped the key.

### The toolbar appears in the wrong position on Linux

This is usually caused by coordinate differences between Wayland and XWayland. Review the environment check on the settings page. If the requirements cannot be met, switch to X11.

### An AI action returns no result

Check whether the default model or selected assistant is available. Translate also requires a separately configured translation model.

### Quoted text does not appear

Quote sends the selected content to the input box in the main Cherry Studio window. Make sure the main window is open, then switch to the Chats page to view it.

## Privacy

Copy writes only to the system clipboard. Search sends the query to the selected search engine. Quote sends the text to the main Cherry Studio window.

The selected text is sent to the corresponding model service only when you run Translate, Explain, Summarize, Refine, or a custom AI action. Before processing sensitive text, review the action type and the provider's data policy.

***

### Get help and submit feedback

If you encounter a problem, use the information under [Feedback and Suggestions](../../question-contact/suggestions.md) to contact the community.
