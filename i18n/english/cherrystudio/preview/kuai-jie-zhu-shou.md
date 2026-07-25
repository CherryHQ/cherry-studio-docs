---
icon: browsers
---

# Quick Assistant

Quick Assistant is a lightweight window that you can open above another application. Use it for a temporary question, translation, summary, or explanation without switching back to the main Cherry Studio window first.

{% hint style="info" %}
Quick Assistant and [Selection Assistant](selection-assistant.md) are separate features. A global shortcut or the system tray opens Quick Assistant; Selection Assistant shows an action toolbar after you select text.
{% endhint %}

## Before you begin

Quick Assistant calls models you have already configured. Before enabling it, make sure at least one chat model is available. To use Text Translation, also configure a translation model.

See [Default Models](settings/default-models.md) for the related settings.

## Enable Quick Assistant

1. Open **Settings → Quick Assistant**.
2. Turn on **Enable Quick Assistant**.
3. Choose whether to enable **Click the tray icon to start**.
4. Choose whether to enable **Read clipboard at startup**.
5. Under **Quick Assistant Model**, select Use Assistant or Default Model.

A Quick Assistant preview appears at the bottom of the Settings page. Use it to confirm that the model and interface work correctly.

### Choose a model mode

| Mode | Result |
| --- | --- |
| Use Assistant | Select an existing assistant and use its system prompt, model, and model parameters |
| Default Model | Use the current default model without applying a specific assistant |

Text Translation uses its separately configured translation model, not the assistant selected here.

{% hint style="warning" %}
Answers, summaries, and explanations in Quick Assistant disable web search, MCP, and knowledge bases. Use [Chat](chat.md) in the main window when you need these capabilities.
{% endhint %}

## Configure how it opens

### Global shortcut

1. Open **Settings → Keyboard Shortcuts**.
2. Find **Quick Assistant**.
3. Enable the shortcut.
4. Change the key combination if needed.

The prefilled combinations are:

* macOS: Command + E
* Windows / Linux: Ctrl + E

The shortcut is disabled initially. Enabling the main Quick Assistant switch does not enable the global shortcut automatically.

See [Keyboard Shortcut Settings](settings/key-shortcut.md) for more details.

### System tray

After enabling **Click the tray icon to start**, clicking the Cherry Studio tray icon opens Quick Assistant and also enables the system tray feature.

Even without click-to-start enabled, you can right-click the tray icon while Quick Assistant is enabled and select Quick Assistant from the menu.

## Open and run an action

1. Press the enabled global shortcut in any application, or use the tray entry.
2. Enter the content to process.
3. Select an action.

| Action | Purpose |
| --- | --- |
| Answer this question | Send the input to the model as a regular question |
| Text Translation | Select a target language and translate the input |
| Content Summary | Process the input with the built-in summary instruction |
| Explanation | Process the input with the built-in explanation instruction |

Use the Up and Down arrow keys to switch actions, then press Enter to run the selected action.

### Use clipboard content

When **Read clipboard at startup** is enabled, Quick Assistant attempts to read new plain-text clipboard content each time the window appears and shows it as reference text.

You can then:

* Select translation, summary, or explanation directly
* Enter an additional request and send it together with the clipboard text
* Press Backspace on the home page to clear the clipboard reference text

The window receives no usable reference text when the clipboard is empty, contains something other than plain text, or the operating system denies read permission.

## View results and continue asking

Answers, summaries, and explanations appear as a stream. After using Answer this question, you can continue entering messages on the results page to form a temporary chat.

On the Text Translation page, you can change the target language, and the result regenerates with the new setting.

Quick Assistant content is a temporary session. After returning to the home page or closing the window, do not treat it as a long-term chat record in the main window.

## Window controls

| Action | Result |
| --- | --- |
| Esc while generating | Pause the current generation |
| Esc on a results page | Return to the Quick Assistant home page |
| Esc on the home page | Hide the window |
| C on a results page | Copy the latest model output |
| Click the pin | Keep the window on top so it does not hide automatically when it loses focus |
| Click outside the window | Hide Quick Assistant when it is not pinned |

When the window opens again, it keeps the current model mode, clipboard setting, and translation target language.

## Usage tips

* Enable clipboard reading to reduce steps when processing a short passage you just copied.
* Select a dedicated assistant when you frequently use a fixed tone or format.
* Use Default Model to reduce configuration when you only need a quick answer.
* Use Chat in the main window for long documents, attachments, web search, or knowledge base material.

## Troubleshooting

### Command + E or Ctrl + E does nothing

Confirm that both the main Quick Assistant switch and the shortcut are enabled. If another application uses the key combination, change it under Keyboard Shortcut Settings.

### Clicking the tray icon does not open it

Confirm that **Click the tray icon to start** is enabled and check whether the Cherry Studio icon is hidden in the system tray. You can also right-click the icon and open Quick Assistant from the menu.

### The window disappears after clicking elsewhere

This is expected when the window is not pinned. Click the pin in the lower-right corner when you need to compare content in another application.

### Clipboard content is not read

Confirm that the setting is enabled, the clipboard contains plain text, and the app has clipboard permission. Copy new content and open the window again.

### Translation returns no result

Text Translation uses the translation model. Check the translation model under Default Models, the provider status, and the API configuration.

### An assistant's knowledge base or MCP does not work

Quick Assistant disables web search, MCP, and knowledge bases. Use the assistant in the main window instead.

## Privacy note

When clipboard reading is enabled, Quick Assistant reads the plain-text clipboard when the window appears. The text is sent to the selected model service only after you run an answer, translation, summary, or explanation action.

Before handling a password, key, or other sensitive content, clear the clipboard reference text or turn off **Read clipboard at startup**.

***

### Get help and submit feedback

If you encounter a problem, contact the community using the information under [Feedback and suggestions](../../question-contact/suggestions.md).
