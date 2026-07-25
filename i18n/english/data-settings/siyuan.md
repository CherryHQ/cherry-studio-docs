---
description: Connect to the SiYuan Note API and export Cherry Studio V2 conversations or notes as SiYuan documents.
icon: map
---

# SiYuan Note Configuration and Export

Cherry Studio V2 can export a complete topic, an individual message, or a Cherry Studio note to a specified SiYuan notebook. Exported content is created as a Markdown document through the SiYuan Kernel API.

Configuration is under **Settings > Integrations > SiYuan Note**. **Data Settings > Export Menu** only controls whether “Export to SiYuan Note” is displayed.

{% hint style="warning" %}
An API Token can access your SiYuan data. Do not show the complete Token in screenshots, feedback, or shared configurations. For a self-hosted instance, do not expose an unprotected API directly to the internet.
{% endhint %}

## Prepare SiYuan Note

1. Start SiYuan Note and confirm that its Kernel is running.
2. Create or select the notebook that will receive exported content.
3. Obtain the API Token.
4. Copy the target notebook ID.
5. Confirm that the device running Cherry Studio can reach the SiYuan API URL.

The default local Endpoint for the official SiYuan API is:

```text
http://127.0.0.1:6806
```

Find the API Token under **SiYuan Note > Settings > About**. For the complete interface contract, see the [official SiYuan API documentation](https://github.com/siyuan-note/siyuan/blob/master/API.md).

## Obtain the Notebook ID

Open the target notebook's settings in SiYuan Note and use **Copy Notebook ID**. An ID usually looks like:

```text
20210817205410-2kvfpfn
```

Do not enter the notebook name, workspace path, or a document ID. Cherry Studio passes this value as the `notebook` parameter to SiYuan's document creation interface.

## Configure Cherry Studio

Go to **Settings > Integrations > SiYuan Note** and enter:

| Field | Description |
| --- | --- |
| API URL | The SiYuan Kernel URL, such as `http://127.0.0.1:6806` |
| API Token | The API Token displayed in SiYuan settings |
| Notebook ID | The target Notebook ID that receives exported documents |
| Document Root Path | Optional; the parent path for all exported documents in the notebook |

Do not add `/` to the end of the API URL. This avoids a double slash when it is joined with an `/api/...` path.

### Local and Self-Hosted URLs

- **SiYuan and Cherry Studio are on the same computer:** Usually use `http://127.0.0.1:6806`.
- **SiYuan is on another local network device or NAS:** Use an IP address and port that the Cherry Studio device can reach; do not enter the other device's own `127.0.0.1`.
- **Publicly accessible self-hosted instance:** Use an HTTPS domain and restrict source access with a firewall or reverse proxy.

When connecting to SiYuan behind Docker, a NAS, or a reverse proxy, also confirm that the `/api/` path is not rewritten or blocked.

## Check the Connection

After entering **API URL** and **API Token**, click **Check**.

Cherry Studio calls:

```text
POST /api/notebook/lsNotebooks
```

A successful check means that the URL is reachable, the Token works, and the interface returns `code: 0`. The check does not verify:

- Whether the entered Notebook ID exists;
- Whether the target notebook is open;
- Whether the Document Root Path is valid;
- Whether the current configuration can create a document successfully.

Run one real export even after the check succeeds.

## Set the Document Root Path

When left blank, Cherry Studio uses:

```text
/CherryStudio
```

You can also enter another path, for example:

```text
/AI Conversations
```

If the path does not begin with `/`, Cherry Studio adds it automatically.

### Use a Date Template

The root path is first rendered through SiYuan's `renderSprig` interface, so you can use a supported Sprig template to organize documents by date. For example:

```text
/CherryStudio/{{now | date "2006/01"}}
```

This may render as:

```text
/CherryStudio/2026/07
```

Invalid template syntax causes export to fail. For the first configuration, use a fixed path, confirm that export succeeds, then add a template.

## Enable the Export Menu

If “Export to SiYuan Note” is missing from a menu:

1. Open **Settings > Data Settings > Export Menu**.
2. Enable **Export to SiYuan Note**.
3. Return to the topic, message, or note and reopen the export menu.

This switch controls only menu visibility; it does not fill in integration settings automatically.

## Perform the First Export

First test with a short message that contains no sensitive information:

1. Open the menu for a topic, message, or Cherry Studio note.
2. Select **Export to SiYuan Note**.
3. Wait for a success or error message.
4. Return to the target SiYuan notebook.
5. Check whether the root path contains a document named from the topic or message title.
6. Open the document and review its heading, paragraphs, lists, code blocks, and formulas.

Before each export, Cherry Studio calls `lsNotebooks` again to check the connection, then:

1. Renders the Document Root Path.
2. Removes certain special characters from the title.
3. Joins the root path and document title.
4. Calls `POST /api/filetree/createDocWithMd` to create the document.

The official SiYuan interface does not overwrite an existing document when the same path is requested again. To update old content, handle the old document in SiYuan, or change the title or root path and export again.

## Exported Content Scope

- **Complete Topic:** Convert messages in the current topic to Markdown in order.
- **Individual Message:** Export only the selected message.
- **Cherry Studio Note:** Export the current note's Markdown content.

The current SiYuan export has no separate “Include Reasoning Content” switch. To preserve specific content, confirm the actual text to be exported in Cherry Studio first.

## Security Recommendations

- For local use, keep the API listening only on the local device or a trusted network.
- For remote use, enable HTTPS and restrict access through the reverse proxy and firewall.
- If a Token leaks, replace it immediately in SiYuan, then update Cherry Studio.
- Do not put a real Token in documentation, screenshots, chats, or a version control repository.
- Configure reliable backups for important notebooks; export does not replace a SiYuan data backup.

## FAQ

### Check reports “Enter the API URL and Token”

The check requires only API URL and Token. Confirm that both inputs are nonempty and that the URL includes `http://` or `https://`.

### The local URL cannot connect

Confirm that SiYuan is running, a browser on the same computer can reach `127.0.0.1:6806`, and the port has not changed. You cannot use `127.0.0.1` when Cherry Studio and SiYuan are on different devices.

### The check succeeds, but export reports incomplete configuration

An actual export also requires **Notebook ID**. Enter the Notebook ID, not the notebook name or a document ID.

### The check succeeds, but document creation fails

Confirm that the target notebook exists and is available, then simplify the root path to `/CherryStudio`. If export then works, the original Sprig template or path may be invalid.

### A self-hosted instance returns 401 or 403

Confirm that the Token is complete, the reverse proxy preserves the `Authorization: Token ...` request header, and its access policy allows the device running Cherry Studio.

### The service returns 404 or an HTML page

The API URL may point to a web subpath, or the reverse proxy may not forward `/api/` to the SiYuan Kernel. Use the instance root URL and do not include `/api/notebook/lsNotebooks`.

### A repeated export did not overwrite the old document

This is the behavior of the `createDocWithMd` interface: the same path does not overwrite an existing document. Change the document title or root path, or handle the old document in SiYuan first.

### SiYuan Note is missing from the conversation menu

Go to **Settings > Data Settings > Export Menu** and enable **Export to SiYuan Note**. If it is already enabled, reenter the current conversation and open the menu again.

If the issue persists, submit your Cherry Studio and SiYuan versions, deployment method, redacted API URL, Notebook ID, root path, and interface error details through [Feedback and Suggestions](../question-contact/suggestions.md).
