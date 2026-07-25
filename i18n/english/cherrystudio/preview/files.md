---
icon: folder
---

# Files

The Files page lets you view and clean up content in the Cherry Studio file index, such as chat attachments, pasted images, and some files generated or saved by the app.

It is not a general file manager for your computer and does not show every file on your disk automatically.

{% hint style="info" %}
Knowledge base data sources are managed separately on the Knowledge Base page and may not appear here. To update, reindex, or delete knowledge base material, go to [Knowledge Base](knowledge-base.md).
{% endhint %}

## Open the Files page

1. Click **+** on the right side of the top tab bar to open a new Launchpad tab.
2. Click **Files** in the Launchpad.

Type filters appear on the left, and files in the current category appear on the right.

## View and filter files

The left side provides four categories:

| Category | Content shown |
| --- | --- |
| Documents | Files identified as documents |
| Images | Image files |
| Text | Plain text and text-based files |
| All Files | All content in the file index |

The page opens to the **Documents** category by default. Switching categories clears the current multi-selection.

### Sort files

You can sort by:

* Creation time
* Size
* File name

The first click on a field sorts in descending order. Click the same field again to switch to ascending order.

### File information

Documents, Text, and All Files use a list view. Each item includes the file name, extension, creation time, count, and file size.

The Images category uses a thumbnail grid for quick browsing.

## Open or preview a file

### Documents and text

Click a file name in the list. Cherry Studio asks the operating system to open the file with the default app configured for that format.

Opening may fail if the file was moved, disk permissions are insufficient, or the system has no available default app.

### Images

Click an image thumbnail to open the image viewer. You can move between other images in the current category from the viewer.

## Rename a file

In the Documents, Text, or All Files list:

1. Find the target file.
2. Click the edit button on the right side of its row.
3. Enter a new name and confirm.

If the new name does not include the original extension, Cherry Studio keeps the original extension automatically.

{% hint style="warning" %}
Renaming changes only the file name shown and managed by Cherry Studio. It does not modify the file content.
{% endhint %}

## Delete one file

### Documents and text

Click the delete button on the right side of the file row, then confirm in the dialog.

### Images

Move the pointer over an image thumbnail, click the delete button in the upper-right corner, then confirm.

Deleting a file also removes its attachment references from messages. This action cannot be undone in Cherry Studio.

If an image is still used by a Painting record, Cherry Studio prevents deletion and shows a message. Handle the related record in Painting first.

## Delete files in bulk

Bulk actions are available in the Documents, Text, and All Files categories. The Images category does not provide multi-selection.

1. Select the files to delete, or click **Select All** in the upper-right corner.
2. Open the bulk actions menu.
3. Select **Batch Delete** and confirm.

{% hint style="warning" %}
Batch deletion also removes attachment references to these files from messages. Before continuing, make sure important files have a separate backup.
{% endhint %}

## Which files appear here

You will usually see:

* Content uploaded or pasted in a chat and saved to the app's file directory
* Images or other results generated during a chat and added to the file index
* Local files registered by the legacy Cherry Studio file workflow

The following may not appear:

* Files on your computer that were never added to Cherry Studio
* Files stored only on an external provider's server
* Original material managed separately by the new knowledge base data source workflow
* Content already removed from the file index

To add a new attachment in Chat, go to [Chat](chat.md) and use the Attachment button in the input box, or drag in a file.

## Storage location

File content is stored in the Cherry Studio app data directory. Use **Settings → Data Settings → Data Directory** to view or migrate it. Do not move, rename, or delete internal files in the directory manually while the app is running.

For the exact location and migration method, see [Change Storage Location](../../personalization-settings/storage.md).

## Troubleshooting

### Attachments disappear from old messages after file deletion

This is part of the current deletion behavior: deleting a file also removes its attachment references from messages. Do not delete the original file from the Files page if you need to keep historical attachments.

### Imported knowledge base material is missing

Knowledge bases use their own data source and indexing workflow. View, reindex, or delete the material from the knowledge base details page.

### Nothing happens when clicking a file name

Confirm that the file still exists and that the system has a default app configured for its extension. Manually moving the app data directory can also invalidate the original path.

### An image cannot be deleted

The image may still be used by a Painting record. Open the Painting page and handle the related record, then return to the Files page and delete the image.

***

### Get help and submit feedback

If you encounter a problem, contact the community using the information under [Feedback and suggestions](../../question-contact/suggestions.md).
