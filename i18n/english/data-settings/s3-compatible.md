---
description: Back up and restore Cherry Studio V2 data with S3 or S3-compatible object storage.
icon: cloud-binary
---

# S3-Compatible Storage Backup

Cherry Studio V2 can save backups to AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS, Volcengine TOS, MinIO, and other object storage services that provide an S3-compatible API.

Here, S3 is a remote backup location, not a real-time synchronization service. Restoring overwrites current data with the selected backup and does not merge content created separately on different devices.

{% hint style="warning" %}
Backups may contain conversations, provider configurations, and other sensitive information. Keep the bucket private and use dedicated credentials limited to the target bucket or directory.
{% endhint %}

## Prepare the Bucket and Credentials

In the object storage console:

1. Create or select a private bucket.
2. Confirm the Region where the bucket is located.
3. Find the S3 API Endpoint supplied by the provider.
4. Create access credentials dedicated to Cherry Studio.
5. If supported, restrict the credentials to the Cherry Studio directory in that bucket.

Cherry Studio needs at least permission to list, upload, and read objects. To clean up old backups automatically or delete files in the manager, it also needs permission to delete objects.

Permission names vary by service. Common corresponding AWS IAM actions include `s3:ListBucket`, `s3:PutObject`, `s3:GetObject`, and `s3:DeleteObject`. Use the equivalent permissions for other compatible services.

## Configuration Fields

Open **Settings > Data Settings > S3** and enter:

| Field | Description |
| --- | --- |
| API URL | The S3 API Endpoint provided by the service, including `http://` or `https://` |
| Region | The bucket's Region; use the exact value required by the provider |
| Bucket | The Bucket name, not its console display name or a directory name |
| Access Key ID | The identifier for the dedicated access credential |
| Secret Access Key | The secret paired with the Access Key ID |
| Backup Directory | An optional object key prefix that isolates Cherry Studio backups |

All fields except **Backup Directory** are required to create a manual backup and open the backup manager.

### Do not repeat the Bucket in the Endpoint

The provider determines the Endpoint format. It may be regional, account-specific, or a self-hosted service address. Cherry Studio passes the **Bucket** as a separate parameter to the S3 client, so do not append the Bucket to the URL unless the provider's S3 SDK documentation explicitly requires it.

For example, the web console address, public object URL, and S3 API Endpoint may all be different. Copy the “S3-compatible Endpoint,” not the URL shown when opening an object in a browser.

Cherry Studio chooses virtual-host or path-style requests from the Endpoint domain:

- Recognized official domains for Alibaba Cloud, Tencent Cloud, and Volcengine use virtual-host style.
- `localhost`, IP addresses, and most other compatible services use path-style.
- An unparseable address falls back to path-style.

If the service supports several address formats, prefer the Endpoint documented for its AWS SDK / S3 SDK.

### Set the Backup Directory

**Backup Directory** becomes the object key prefix. You can enter `cherry-studio` or `/cherry-studio/`; extra leading and trailing `/` characters are removed when saved.

Use a separate prefix for each Cherry Studio data set, for example:

```text
cherry-studio/personal
```

The backup manager lists only objects under that prefix whose names end in `.zip`. Changing the directory does not move backups from the old directory, and they do not appear in the new directory's list.

## Verify the Configuration

The current page has no separate connection test button. The most complete verification is:

1. Fill in every required field and temporarily turn off automatic backup.
2. Click **Back Up Now**.
3. Keep the default filename and create a small test backup.
4. Click **Manage Backups**.
5. Confirm that the new ZIP, modification time, and size appear in the list.

This verifies the Endpoint, Region, Bucket, credentials, backup directory, and list and write permissions at the same time. If the bucket can be listed but upload fails, object write permission is usually missing. If upload succeeds but the object does not appear, check the prefix or list permission.

## Manual Backup

After clicking **Back Up Now**, confirm or change the filename. The default name contains the time, host name, and device type. Cherry Studio adds the `.zip` extension if it is missing.

With **Compact Backup** enabled, Cherry Studio skips images, knowledge base files, and other file data in the app's `Data` directory, backing up only chat history, settings, and similar content. A compact backup is not incremental and cannot recover skipped files after restoration.

Before an S3 upload, Cherry Studio creates a ZIP locally and reads the file into memory before uploading it. A large complete backup can noticeably increase disk and memory usage. Do not quit the app, disconnect the network, or let the system sleep while it runs.

## Automatic Backup and Retention

**Automatic Sync** actually runs periodic backups and supports:

- Off;
- Every 1, 5, 15, or 30 minutes;
- Every 1, 2, 6, 12, or 24 hours.

Complete one successful manual backup before enabling automatic backup. Higher frequency increases request count, traffic, and object storage operation costs.

**Maximum Backups** can be Unlimited, 1, 3, 5, 10, 20, or 50. After reaching the limit, Cherry Studio uses the host name and device type in default filenames to remove older backups from the current device.

The following objects are generally not cleaned up automatically:

- Backups from another device;
- Backups with custom filenames that omit the current device identifier;
- Objects outside the current backup directory;
- Objects that do not end in `.zip`.

When using Unlimited, configure a storage usage alert or lifecycle rule with the object storage service to prevent indefinite accumulation.

## Manage and Restore Backups

Click **Manage Backups** to view, refresh, restore, and delete ZIP backups in the current directory.

Before restoring:

1. Create another backup of the current data.
2. Verify the target version by filename, modification time, and size.
3. Confirm that no other device is writing to the same directory.
4. Click **Restore** for the target file and confirm the overwrite.

The app may restart automatically after restoration. Deleting an object cannot be undone. If the credentials lack delete permission, viewing and restoring may work while deletion and automatic cleanup fail.

{% hint style="warning" %}
Several computers can share one Bucket and prefix, but restore does not merge data. When migrating between devices, back up the target device first, then restore the intended version from the source device.
{% endhint %}

## Security and Cost Recommendations

- Use a private Bucket; do not enable public read access for the backup directory.
- Use a separate, least-privilege Access Key instead of cloud account root credentials.
- Do not show the complete Secret Access Key in screenshots, logs, or feedback.
- Use HTTPS for a public Endpoint. A self-hosted MinIO should also use a trusted certificate or be accessible only from a trusted network.
- Monitor storage capacity, PUT / GET / LIST request charges, and outbound traffic costs.
- If a key leaks, revoke and recreate it immediately in the provider console; changing only the value in Cherry Studio is not enough.

## FAQ

### The Back Up Now button is disabled

Confirm that API URL, Region, Bucket, Access Key ID, and Secret Access Key are all filled in. Backup Directory can be blank.

### The service returns 301, PermanentRedirect, or a Region mismatch

The Endpoint or Region does not match the Bucket's location. Return to the object storage console and copy the correct S3 Endpoint and exact Region for that Bucket.

### The service returns 403, AccessDenied, or SignatureDoesNotMatch

Confirm that the Access Key and Secret are paired, the credentials are valid, and the system time is accurate. Also check the Endpoint format, Region, and least-privilege policy. Signature errors are often caused by an address or Region mismatch.

### A self-hosted MinIO cannot connect

Confirm that the Endpoint includes its port, such as `https://minio.example.com:9000`, and that the device running Cherry Studio can reach the address. An IP address or `localhost` uses path-style. If MinIO is behind a reverse proxy, also check the certificate, request body, and timeout limits.

### Upload succeeds, but the manager cannot see the file

Check that the current **Backup Directory** matches the value used during upload and that the credentials can list the Bucket. The manager displays only objects under the current prefix whose names end in `.zip`.

### Old files remain after reaching the maximum backup count

Automatic cleanup recognizes only backups from the current device that follow the default naming convention. Custom names and objects from other devices or prefixes must be deleted manually or handled with storage service lifecycle rules.

### A large backup increases memory usage

The current S3 upload reads the generated ZIP into memory. Enable **Compact Backup** to reduce its size by excluding knowledge base and image files, or run it when the data set is smaller.

If the issue persists, submit your Cherry Studio version, storage service name, redacted Endpoint / Region / Bucket, HTTP status code, and complete error message through [Feedback and Suggestions](../question-contact/suggestions.md).
