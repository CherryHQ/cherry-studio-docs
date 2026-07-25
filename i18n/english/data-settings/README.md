---
description: Back up, restore, migrate, import, and export data in Cherry Studio V2.
icon: floppy-disk
---

# Data Settings

Cherry Studio V2 data options are under **Settings > Data Settings**. From here, you can create and restore manual backups, configure automatic local or cloud backups, migrate data to another directory, and manage import and export options.

{% hint style="warning" %}
Restoring a backup, migrating the data directory, or resetting data can overwrite existing content. First create a working backup and confirm that the backup file is stored outside the app data directory.
{% endhint %}

## Page Structure

Data Settings includes these pages on the left:

| Page | Purpose |
| --- | --- |
| Data | Manual backup and restore, export to phone, migrate app data, view logs, clear cache, and reset data |
| Local Backup | Write backups to the computer, an external drive, or a mounted network directory, and configure automatic backups |
| WebDAV | Save and restore backups with remote storage that supports WebDAV |
| Nutstore | Sign in to Nutstore, choose a remote directory, and manage backups |
| S3 | Save backups to S3 or S3-compatible object storage |
| Import Settings | Import data from supported external apps |
| Export Menu | Choose the formats and destinations shown in the conversation export menu |
| Markdown Export | Set the default directory, formulas, model information, and citation format |

## Choose a Backup Method

| Use case | Recommended method |
| --- | --- |
| Save a portable backup immediately | Click **Backup** on the **Data** page |
| Back up regularly to the computer, an external drive, or a mounted NAS | Use **Local Backup** |
| Use an existing cloud drive or server that supports WebDAV | Use [WebDAV Backup](WebDAV.md) |
| Connect through Nutstore account authorization | Use **Nutstore** |
| Use existing object storage such as AWS S3, Cloudflare R2, or MinIO | Use [S3-Compatible Storage Backup](s3-compatible.md) |

“Automatic backup” on cloud and local pages means creating new backup files on a schedule. It is not real-time, bidirectional synchronization between two devices. If several computers use the same backup location, finish a backup on one device, then manually select that version to restore on another. Restoring in both directions after simultaneous changes can overwrite newer data.

## What a Backup Contains

A regular backup contains the Cherry Studio database, settings, and app-managed file data, including chat history, assistant configurations, images, and knowledge base files.

With **Compact Backup** enabled, the backup still retains chat history and settings but skips images, knowledge base files, and other file data in the app's `Data` directory. This reduces file size and speeds up backup, but the skipped files cannot be recovered from that backup after restoration.

{% hint style="info" %}
“Compact Backup” is not an incremental backup. Each run still creates an independent backup file; it simply excludes file data.
{% endhint %}

Backups can contain conversation content, provider configurations, and other sensitive information. Do not share them publicly or restore files from unknown sources. Use a private directory, a strong password, and least-privilege credentials for remote storage.

## Manual Backup and Restore

Go to **Settings > Data Settings > Data**:

1. To reduce backup size, enable **Compact Backup** first. Keep it disabled when you need to preserve images and knowledge base files.
2. Click **Backup** and choose a location outside the app data directory.
3. Wait for the backup to finish. Do not quit the app or remove the drive while it is writing.

To restore, click **Restore** and select a Cherry Studio backup file. The restore replaces current data with data from the backup, and the app may restart automatically when it finishes.

Periodically test a restore. After confirming that the current data has another backup, verify that the backup file is recognized and that its version and time are correct. Do not wait until the original data is lost to perform the first test.

## Automatic Backup and Retention

Local Backup, WebDAV, Nutstore, and S3 each save their own automatic backup configuration. The current schedule options are:

- Off;
- 1, 5, 15, or 30 minutes;
- 1, 2, 6, 12, or 24 hours.

The maximum number of retained backups can be Unlimited, 1, 3, 5, 10, 20, or 50. After reaching the limit, Cherry Studio removes older automatic backups. “Unlimited” does not actively control storage usage.

Each backup method also has an independent **Compact Backup** switch. Changing the switch on the **Data** page does not replace settings on the Local Backup, WebDAV, Nutstore, or S3 pages.

### Configure Automatic Local Backup

1. Open **Local Backup**.
2. Choose a writable directory. It cannot be inside the Cherry Studio app data directory or installation directory.
3. Choose the automatic backup schedule and maximum backup count.
4. Decide whether to enable **Compact Backup** based on your restore requirements.
5. Check **Backup Status** for the latest time or an error message.

Choosing a valid directory enables automatic local backup. If the backup directory is on an external drive or network mount, keep it online with enough free space while the backup runs.

## Export to Phone

**Data > Export to Phone** offers two methods:

- **Local Network Transfer:** Scan for the Cherry Studio mobile app on the same local network, connect, and send a temporary backup.
- **Export as File:** Create a ZIP backup that the mobile app can import from a file.

Both methods transfer part of the data, such as chat history and settings, and skip file data in the `Data` directory. They do not replace a complete backup.

If no device appears on the local network, confirm that the computer and phone use the same network, the mobile app has opened its local network transfer page, and the system firewall is not blocking device discovery or file transfer.

## Change the App Data Directory

**Data > App Data** displays the current directory. Click the edit icon to place Cherry Studio data on another drive.

The new directory must meet these conditions:

- It is not the root of a drive.
- It is not inside the current app data directory.
- It is not inside the Cherry Studio installation directory.
- The current user has write permission.

When confirming, you can choose to copy data from the original directory. If the target directory is not empty, the app warns again because continuing may overwrite files there. During migration, do not force-quit, disconnect the drive, or let the device sleep. The app restarts afterward and may restart more than once in some cases.

Changing only the path without copying data starts from the content already present at the new location; this is not the same as migrating current data. For a complete move, keep **Copy Data** enabled and create a backup before starting.

## Logs, Cache, and Reset

- **App Logs:** Open the log directory to troubleshoot a problem or submit logs when requested in feedback. Review and remove sensitive information before sharing.
- **Clear Cache:** Delete app cache and Mini App local data. This does not delete chat history, and the action cannot be undone.
- **Reset Data:** Erase Cherry Studio data and restart the app. The page asks for confirmation twice. Use it only when you have a working backup and genuinely want to start over.

{% hint style="danger" %}
Do not confuse “Clear Cache” with “Reset Data.” The first affects cache; the second erases the local database and app-managed data.
{% endhint %}

## Import External App Data

The current **Import Settings** page provides **Import ChatGPT Data**. Click **Import File**, then select exported ChatGPT data in the dialog.

Keep a backup of current Cherry Studio data before importing. If the page lists no other app, the current version does not provide an importer for it here. Do not restore another app's database or backup file as a Cherry Studio backup.

## Configure the Export Menu

**Export Menu** controls the export options shown on the conversation page. Current options include:

- Image;
- Markdown;
- Markdown (with reasoning);
- Notion, Yuque, Joplin, Obsidian, and SiYuan Note;
- Word (DOCX);
- Copy as plain text.

Enabling a switch only makes that option appear in the export menu; it does not configure the third-party service automatically. Destinations such as Notion and Yuque still require the corresponding connection under **Settings > Integrations**.

## Configure Markdown Export

**Markdown Export** can configure:

- A default export path; when blank, a save dialog appears each time;
- Force `$$` delimiters for LaTeX formulas;
- Use the topic name as the message heading;
- Show the model name and model provider;
- Exclude citation content;
- Normalize citation markers to Markdown footnote format.

Some options also affect Markdown-based third-party exports, such as Notion and Yuque. Before enabling “Exclude citation content” or “Normalize citation format,” test with a conversation that contains citations and verify that the result meets your expectations.

## FAQ

### Automatic backup never creates a file

Confirm that the schedule is not Off, the target directory or remote service is accessible, and the bottom of the page shows a recent backup time or error. If the local directory is on a removable device or network mount, also confirm that it is currently online.

### Images or knowledge base files are missing after restoring a compact backup

This is expected. A compact backup retains only chat history and settings; it does not include file data from the `Data` directory. Use a full backup created with Compact Backup disabled.

### The app looks like a fresh installation after changing the data directory

**Copy Data** may have been disabled during migration, or the app may have started from an empty directory. Before writing a large amount of new data, check whether the original directory still exists, then move back through Settings or restore from a backup.

### Data did not merge automatically after restoring on several computers

Restore is an overwrite operation and does not merge new content from both sides. Compare backup times before restoring, and save another backup of the current device first.

If the issue persists, submit your operating system, Cherry Studio version, backup method, error message, and a screenshot of the redacted settings through [Feedback and Suggestions](../question-contact/suggestions.md).
