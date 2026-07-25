---
icon: trash-xmark
---

# Clear CSS Settings

Syntax or selector errors in Custom CSS can cover buttons, hide text, prevent scrolling, or even make Settings inaccessible. Choose a recovery method below based on whether the interface is still usable.

## Method 1: Clear It in Settings

If you can still open Settings:

1. Go to **Settings > General Settings > Custom CSS**.
2. Copy any CSS you need to troubleshoot into a text file.
3. Select and delete everything in the editor.
4. Wait for the interface to recover.
5. Quit Cherry Studio completely, reopen it, and confirm that the issue does not return.

This is the preferred method. Clearing the editor also removes the saved Custom CSS setting.

## Method 2: Restore the Interface Temporarily with Developer Tools

If the faulty styles make the Settings page unusable, first remove the injected style node from the current window.

{% hint style="warning" %}
The command below only **restores the current window temporarily**. Before reloading or restarting the app, you must return to Settings and clear the CSS, or the faulty styles will reappear.
{% endhint %}

### 1. Open Developer Tools

Use any of these methods:

- Windows / Linux: press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd>;
- macOS: press <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>;
- App menu: select **View > Toggle Developer Tools**;
- Right-click an empty area of the page and select **Inspect**.

### 2. Open Console

Select **Console** at the top of Developer Tools. If docking Developer Tools leaves too little space, move it into a separate window.

### 3. Remove the Current Styles

Manually enter the following line in Console, then press Enter:

```javascript
document.getElementById('user-defined-custom-css')?.remove()
```

After the command runs, Custom CSS should be removed from the current main window immediately.

Some Chromium versions block direct pasting into Console. Follow the security prompt in Developer Tools, or type this short command manually. Do not paste any other scripts from unknown sources.

### 4. Delete the Saved CSS

Do not reload or close the current window. Immediately:

1. Return to Cherry Studio;
2. Open **Settings > General Settings > Custom CSS**;
3. Clear the editor;
4. Close Developer Tools;
5. Quit the app completely and reopen it.

If the interface works normally after restarting, the saved CSS has been cleared.

## Delete Only the Problematic Rules

If you want to keep the rest of the theme:

1. Use Method 2 to restore the interface temporarily;
2. Copy all CSS from the editor into an external text file;
3. Clear the editor and confirm that the app recovers;
4. Restore only a small section at a time;
5. Check light mode, dark mode, chats, Settings, and dialogs separately.

When the issue returns, the last rule you restored is usually the best place to begin troubleshooting.

Common causes include:

- Missing `}`, `;`, or quotation marks;
- Global overrides that use `display: none`, `position: fixed`, or an extremely high `z-index`;
- Rules that hide every button, input, or scroll container;
- Old class names or legacy theme selectors such as `body[theme-mode="dark"]`;
- Widespread use of `!important`;
- A third-party theme that is incompatible with the current DOM structure.

## Frequently Asked Questions

### Nothing Changes After Running the Command

Make sure Console is connected to the Cherry Studio main page, not a mini-app webpage or Developer Tools itself. Run this command again:

```javascript
document.getElementById('user-defined-custom-css')
```

If it returns `null`, the current window does not contain this style node. The issue might not be caused by Custom CSS, or the command might be running in the wrong page context.

### The Issue Returns After Restarting

This happens because you removed only the style node from the current page without clearing the saved setting. Repeat Method 2, then open the CSS editor and clear its contents without reloading the page.

### The Keyboard Shortcut Does Not Open Developer Tools

Try **View > Toggle Developer Tools** from the app menu, or right-click and select **Inspect**. A system keyboard shortcut utility might intercept the default key combination.

### The Settings Page Still Does Not Open

Do not delete the entire app data directory or edit the database directly. Keep the current version number, system information, and log directory, then seek help through an official feedback channel.

### Custom Styling Remains After Clearing the CSS

Check whether an operating system theme, Cherry Studio's built-in theme color, font settings, or a third-party window tool is still enabled. These are separate from Custom CSS and are not reset by the steps on this page.

## Prevent the Issue from Happening Again

- Add only a small section of rules at a time;
- Save a working version before making changes;
- Prefer overriding semantic variables over relying on internal class names and DOM hierarchy;
- After upgrading Cherry Studio, disable complex themes before validating them section by section;
- Use only third-party CSS that you can read and understand.

For more writing guidance, see [Custom CSS](css.md).

***

### Get Help and Submit Feedback

If you still cannot recover the interface, contact us through an official channel listed in [Feedback and Suggestions](../question-contact/suggestions.md).
