---
description: Learn which Cherry Studio V2 data directory, import, export, and cleanup settings are currently available.
icon: floppy-disk
---

# Data Settings

Open **Settings → Data Settings** to manage the app data directory, import and export options, cache, logs, and note-service connections.

{% hint style="warning" %}
In-app Backup & Restore V2 is not available yet. The Data, Local Backup, WebDAV, Nutstore, and S3 pages display a “Backup & Restore V2 is not available yet” notice, and their backup controls are disabled. Do not rely on these entries to preserve or restore important data.
{% endhint %}

## Page Overview

| Group | Page | Current purpose |
| --- | --- | --- |
| Data | Data | View or migrate the app data directory, open logs, clear cache, reset data, and configure privacy options |
| Cloud Backup | Local Backup, WebDAV, Nutstore, S3 | Pages are visible, but backup, restore, automatic sync, and credential input are unavailable |
| Import | Import App Data | Choose which sources appear in the import menu |
| Export | Export Menu | Choose which formats and destinations appear in the conversation export menu |
| Export | Markdown Export | Configure the default directory, file name, formulas, model information, and citation format |
| Note Export | Notion, Yuque, Joplin, Obsidian, SiYuan | Configure each note service or local note repository as an export destination |

## Data Page

### App Data Directory

The **App Data** row shows the directory actually used by the current instance. Click the path or **Open Directory** to view it in the system file manager, or click the change-directory icon to start a migration.

Migration restarts the app and may copy its database, internal files, knowledge bases, and notes. Read [Change the Storage Location](../personalization-settings/storage.md) first, prepare an offline copy, and use an empty target directory.

### App Logs

Click **Open Logs** to open the log directory. When reporting a problem, provide only logs relevant to the failure time and first check them for paths, prompts, or other sensitive information.

### Clear Cache

**Clear Cache** removes regenerable cache and local Trace data. It is not the same as deleting conversations or resetting the entire app. Do not treat cache clearing as a universal fix for sign-in, model configuration, or knowledge base problems.

### Data Reset

**Data Reset** is destructive: it clears data in the current instance and returns it to its initial state. In-app backup is currently unavailable, so do not use this action without an independent copy.

## Import Settings

**Import App Data** controls which sources appear in the import menu. It changes menu entries only and does not read data from other apps in the background.

Confirm that a file comes from a trusted source and keep the original before importing. Results depend on the source format and the formats supported by the current version.

## Export Settings

### Export Menu

Choose which formats or third-party destinations appear when exporting a conversation. Disabling an item only hides its entry; it does not delete files already exported.

### Markdown Export

Configure the default save directory, file-name rules, and whether to include model information, citations, formulas, and other content. Use a directory outside the app data directory so that exports can be archived independently.

### Note Export

Notion, Yuque, Joplin, Obsidian, and SiYuan have separate settings. After configuring a service URL, token, or local directory, export one non-sensitive test item to verify its destination and formatting before exporting in bulk.

{% hint style="info" %}
Export is a one-way write, not two-way synchronization, and it is not a complete backup. External attachments, knowledge base indexes, and internal app state may not be included.
{% endhint %}

## Protect Data for Now

Until Backup & Restore V2 becomes available:

1. Record the current directory shown under **App Data**.
2. Fully quit Cherry Studio.
3. Copy the entire directory to another drive and confirm that the copy is readable.
4. Keep original source files for important material and export essential conversations.

Do not copy or merge database files while the app is running. When the backup feature becomes available, follow the current app state and the latest version of this page.

***

### Get Help and Submit Feedback

If the data directory, import, or export fails, keep the version, operating system, and necessary logs, then contact the community through [Feedback and Suggestions](../question-contact/suggestions.md).
