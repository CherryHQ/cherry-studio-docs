---
icon: floppy-disk
---

# Change the Storage Location

The Cherry Studio app data directory stores its database, internal files, knowledge bases, notes, and some runtime state. If the system drive lacks space or you need to put data on another local drive that stays online, migrate the directory from within the app.

{% hint style="danger" %}
Changing the data directory is a high-risk operation. Create a restorable backup first and confirm that it contains the files you need. Do not quit the app, shut down, or disconnect the target drive during migration.
{% endhint %}

## View the Current Directory

Open **Settings > Data Settings > Data Directory** and review the current path in the **App Data** row. Click the path or **Open Directory** to open it in the system file manager.

The path shown in Settings is accurate for the current instance and takes precedence over a default path found online.

Common default locations include:

| System | Common location |
| --- | --- |
| macOS | `~/Library/Application Support/CherryStudio` |
| Windows | `%APPDATA%\CherryStudio` |
| Linux | `~/.config/CherryStudio` |
| Windows portable version | The `data` folder beside the program |

Different installation methods, older versions, and portable builds may use different paths. Use the path displayed in the app.

## What Is Affected

The app data directory usually contains:

- The local Cherry Studio database.
- Files managed internally by the app.
- Knowledge base and note data.
- Some installed resources and workspaces.
- Chromium / Electron session and network state.
- Some logs and cache.

The following may not move with the directory:

- Files located outside the directory and only referenced by Cherry Studio.
- Fonts installed in the operating system and system-level configuration.
- Independent Cherry Studio infrastructure directories under the user's home directory.
- Data in third-party apps, cloud services, or model services.

Do not treat changing the app data directory as a complete backup method.

## Prepare for Migration

1. Create a local backup under **Settings > Data Settings**, or use [WebDAV](../data-settings/WebDAV.md) / [S3-Compatible Storage](../data-settings/s3-compatible.md).
2. If uploaded files must be retained, confirm that “Skip File Data During Backup” is not enabled.
3. Stop active generation, knowledge base processing, file import, and synchronization tasks.
4. Confirm that the target drive has enough space, a stable connection, and write permission for the current user.
5. Create an **empty folder** as the target.
6. Record the current path and keep the original directory until migration has been verified.

{% hint style="warning" %}
Avoid a network share, on-demand cloud synchronization directory, or removable drive that is frequently disconnected. The database and runtime state require continuous, stable local file access.
{% endhint %}

## Choose the Target Directory

1. Open **Settings > Data Settings > Data Directory**.
2. Click the change directory icon on the right side of **App Data**.
3. Select or create the target folder.
4. Verify the **Original Path** and **New Path** in the confirmation dialog.
5. Decide whether to enable **Copy Data**.
6. Confirm, then wait for the app to finish migrating and restarting.

Cherry Studio rejects these targets:

- The root of a drive or file system.
- The current app data directory itself or a directory inside it.
- The Cherry Studio installation directory.
- A directory where the current user lacks write permission.

## The “Copy Data” Switch

### Enabled

After the app restarts, it copies data from the original directory to the new one. Use this to move while preserving current conversations, assistants, files, and knowledge bases.

- Prefer an empty directory.
- Copy time depends on file count, knowledge base size, and drive speed.
- The app may restart more than once.
- Do not force-quit during the copy.

### Disabled

Only the directory is switched; old data is not copied. The new directory may first appear as an empty Cherry Studio environment, while old data remains in the original directory.

Disable this only when you explicitly want a fresh data directory or have prepared the target directory by another method.

{% hint style="danger" %}
If the target directory is not empty and you continue, existing files may be overwritten, risking data loss or a failed copy. Unless its content can be replaced, cancel and choose an empty directory.
{% endhint %}

## Verify After Migration

Do not delete the original directory immediately after migration. Check in order:

1. Open **Settings > Data Settings > Data Directory** and confirm that the new path appears.
2. Open several historical topics and assistants at random.
3. Check that knowledge bases, notes, and internal files are available.
4. Create a test conversation, then quit normally.
5. Start Cherry Studio again and confirm that the new data remains.
6. Create another backup.

Complete at least two full launches and use the app for a while before deciding whether to archive or delete the original directory.

## Use a Different Removable Drive

If the data directory is on an external drive:

- Connect the drive before starting Cherry Studio.
- Keep the same mount point or drive letter.
- Do not eject the drive while the app is running.
- Confirm that the drive remains online before system sleep, updates, or backup.

If one launch looks like a fresh installation, quit the app first and do not reset or create a large amount of new data. Reconnect the original drive, confirm its path and drive letter, then launch and check again.

## Return to the Original Directory

If the new directory does not work correctly:

1. Do not delete either the new or old directory.
2. Back up any data that is still accessible.
3. Select the original directory again under **Data Directory**.
4. If the original directory already contains complete data, disable **Copy Data** to avoid overwriting in either direction.
5. Restart, then repeat the checks under “Verify After Migration.”

Do not manually merge two data directories while the app is running. Database, configuration, and runtime state files with the same names cannot be merged safely by ordinary file overwrites.

## FAQ

### The root of a drive cannot be selected

This is a protection. Create a dedicated subdirectory on the drive, such as `CherryStudioData`, then select it.

### The app reports no write permission

Check the directory owner and permissions, or choose a location writable by the current account. Do not bypass the problem by running the app as an administrator permanently.

### Migration takes a long time

Large files and knowledge bases increase copy time. First check whether the drive is still active instead of force-quitting immediately. If it eventually fails, keep the original directory and review the app logs.

### The original path still appears after restart

Confirm that migration reported no error, the target drive is still online, and the directory permissions are correct. Do not delete the original directory yet. If several restarts still fail to switch it, report the version, system, and log details through an official channel.

### External files are missing from the new directory

The app migrates only its managed data directory. External files located elsewhere are not copied automatically. Keep their original paths accessible, or migrate them separately and relink them.

***

### Get Help and Submit Feedback

If you encounter a problem during migration, preserve both directories and the logs, then contact us through the official channels under [Feedback and Suggestions](../question-contact/suggestions.md).
