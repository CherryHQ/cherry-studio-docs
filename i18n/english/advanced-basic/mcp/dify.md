# Connect a Dify Knowledge Base

If your team already uses [Dify](https://dify.ai/) to manage information, you can retrieve content from those knowledge bases directly through Cherry Studio's built-in `@cherry/dify-knowledge` MCP server, without importing the documents again.

After connecting it, an assistant or Agent can first read the knowledge bases accessible to the current key, retrieve relevant chunks for a question, and use the results as the basis for its answer. This feature only reads knowledge bases; it does not create, modify, or delete data in Dify.

## Before you begin

Complete the following steps in Dify first:

1. Create at least one knowledge base, import documents, and wait for indexing to finish.
2. Generate a **Knowledge API Key** from the knowledge base's API access page. Do not use an application (App) API key.
3. Confirm the API base URL:
   - Dify Cloud: `https://api.dify.ai/v1`
   - Self-hosted deployment: Use the deployment's knowledge-base API URL, which usually ends in `/v1`

{% hint style="warning" %}
An API key can read knowledge-base content within its permission scope. Do not put a real key in documentation, screenshots, or public chats. If a key is exposed, revoke it in Dify and generate a new one immediately.
{% endhint %}

## Install the built-in MCP server

1. In Cherry Studio, open **Settings → MCP Servers**.
2. Search for `@cherry/dify-knowledge` in the list of built-in MCP servers.
3. Click **Install**.
4. Click `@cherry/dify-knowledge` in the installed server list to open its details page.

Cherry Studio runs this built-in server directly. You do not need to install Node.js, Python, or a third-party MCP program separately.

## Enter the connection details

On the **Settings** page in the server details, enter:

| Field | Value | Example |
| --- | --- | --- |
| Arguments | The Dify knowledge-base API base URL, entered on one line | `https://api.dify.ai/v1` |
| Environment Variables | `DIFY_KEY=Knowledge API Key` | `DIFY_KEY=dataset-xxxxxxxx` |

Save the configuration, then enable the server. If the connection succeeds, the **Tools** page displays these two tools:

- `list_knowledges`: Lists the knowledge bases accessible to the current API key and their IDs.
- `search_knowledge`: Retrieves content using a knowledge base ID and query text. If `topK` is omitted, it returns up to six results by default.

{% hint style="info" %}
Do not append `/datasets` to the Arguments value or enter a specific knowledge base ID. Cherry Studio constructs the knowledge-base list and retrieval endpoints automatically for each tool call.
{% endhint %}

## Use it in a conversation

After installing and enabling the server, grant access to the assistant or Agent that will use it:

1. Open the tool settings for the target assistant or Agent.
2. Add and enable `@cherry/dify-knowledge`.
3. Select a model that supports tool calls and start a conversation.

For your first test, ask the model to confirm which knowledge bases it can access:

```text
List the Dify knowledge bases you can currently access, including the name and ID of each knowledge base.
```

After confirming the target knowledge base, ask a question that specifies the scope and output requirements:

```text
Find the steps for migrating an account in the “Product Help Center” knowledge base.
Answer only from the retrieved information and list the key precautions.
```

The model calls `list_knowledges` or `search_knowledge` as needed. Tool results include the document name, chunk content, relevance score, and keywords. The model's capabilities and prompt still determine how it organizes the final answer.

## Troubleshooting

### A missing argument error appears when enabling the server

Make sure **Arguments** contains the API base URL. This built-in server needs at least one argument line to start.

### A request returns 401, 403, or an access error

Check the following in order:

- The variable name is exactly `DIFY_KEY`;
- You are using a knowledge-base API key, not an application API key;
- The key is still valid and can access the target knowledge base;
- The private deployment's API URL is accessible from the current computer.

### The connection works, but the knowledge base list is empty

Make sure Dify contains at least one knowledge base, then check the permission scope of the current Knowledge API Key. Cherry Studio can list only the knowledge bases accessible to that key.

### Dify is not called during a conversation

Make sure the server is enabled and added to the current assistant or Agent. You must also use a model that supports tool calls. If needed, explicitly ask the model to “search the Dify knowledge base first, then answer.”

### Retrieval results are not useful

First, make sure document indexing has finished in Dify, then ask again with more specific keywords. The current built-in tool uses Dify's semantic retrieval API; it does not replace Dify's chunking, indexing, or retrieval configuration.

## Related documentation

- [MCP Server Troubleshooting](./chang-jian-wen-ti.md)
- [Built-in MCP Servers](in-memory.md)
- [Feedback and Suggestions](../../question-contact/suggestions.md)
