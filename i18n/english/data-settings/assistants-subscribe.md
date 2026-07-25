---
icon: rss
---

# Assistant Subscription Configuration

An assistant subscription sets a public JSON URL as the **data source for the assistant template library**. A team maintains one template list, and members see the latest content after reloading the Assistant Library.

{% hint style="info" %}
A subscription provides selectable **templates**. It does not modify custom templates under My and does not automatically update assistants that have already been created. After you add a subscribed template as an assistant, it becomes an independent local copy.
{% endhint %}

## Before You Subscribe

Prepare a public URL that returns JSON directly, such as a Raw file in object storage, a static website, or a code repository.

The subscription URL should meet these requirements:

- Prefer `https://`.
- It can be accessed without a sign-in, Cookie, or request header.
- Opening the URL returns JSON directly, not a download page, preview page, or HTML page.
- The JSON root is an array.
- Each template contains at least `id`, `name`, `prompt`, and `group`.
- Each `id` is unique within the subscription, and `group` is an array of strings.

{% hint style="warning" %}
Cherry Studio reads content directly from this URL. There is currently no input for a username, password, or custom request header. Do not put an access token, API key, or other credential in the subscription URL or JSON file.
{% endhint %}

## Configure a Subscription

1. Open the Cherry Studio **Launchpad**.
2. Enter the **Assistant Library**.
3. Click **Import from External Source** in the upper-right corner.
4. Find **Assistant Subscription** at the bottom of the dialog.
5. Paste the subscription URL, then click **Subscribe**.
6. After the app reloads, return to the Assistant Library to review the remote templates and groups.

A successful subscription means only that the URL is currently reachable. If the response is not a valid template array, the Assistant Library may still fail to display it correctly. Validate the JSON as described below.

## JSON Format

The following minimal example is a suitable starting point:

```json
[
  {
    "id": "product-manager",
    "name": "Product Manager",
    "emoji": "🧭",
    "description": "Clarifies requirements, scope, and product plans.",
    "group": ["Product", "Work"],
    "prompt": "You are an experienced product manager. Clarify the goal and constraints first, then provide structured, actionable recommendations.",
    "regularPhrases": []
  },
  {
    "id": "writing-editor",
    "name": "Writing Editor",
    "emoji": "✍️",
    "description": "Reviews article structure, expression, and readability.",
    "group": ["Writing"],
    "prompt": "You are a professional editor. Preserve the author's intent, identify specific issues, and provide a revision that can be used directly.",
    "regularPhrases": []
  }
]
```

### Field Reference

| Field | Recommended as required | Description |
| --- | --- | --- |
| `id` | Yes | A stable, unique template identifier. Do not assign the same value to two templates. |
| `name` | Yes | The template name displayed in the Assistant Library. |
| `prompt` | Yes | The system prompt used after creating the assistant. |
| `group` | Yes | The groups for the template. This must be an array, such as `["Writing", "Work"]`. A template can appear in several groups. |
| `emoji` | No | The template icon. Without it, the interface may not display the expected icon. |
| `description` | No | The template summary used for preview and search. |
| `regularPhrases` | No | An array of common phrases. Use `[]` or omit the field when none are needed. |

{% hint style="warning" %}
`group` must be an array even when it contains only one value. Writing `"group": "Writing"` prevents the template from loading correctly by group.
{% endhint %}

## Validate the Subscription File

Before publishing, check at least the following:

1. Open the subscription URL directly in a browser and confirm that the JSON body appears.
2. Use a JSON validator to check for trailing commas, missing quotation marks, and mismatched brackets.
3. Confirm that the root is `[]`, not `{}`.
4. Confirm that every template has nonempty `name` and `prompt` values.
5. Confirm that every `group` is an array and every `id` is unique.
6. Test with one or two templates before expanding the list.

If you are comfortable with a command line, you can also check whether the URL is reachable and the JSON is parseable:

```bash
curl -fsSL "https://example.com/assistants.json" | jq .
```

Replace the example URL with your own public subscription URL.

## How a Subscription Updates

An assistant subscription is not a push service and has no fixed background synchronization interval.

- Cherry Studio requests the subscription URL again when it loads assistant templates.
- After modifying the remote JSON, reload the app or reenter the Assistant Library to see new content.
- The remote list replaces the built-in template data source, but custom templates under My are not deleted.
- If the remote URL is temporarily unavailable, the app tries to fall back to built-in templates.
- An assistant already created from a template is an independent copy and does not continue changing with the remote JSON.

To modify an assistant that has already been created, edit that assistant directly instead of changing only the subscription file.

## Unsubscribe or Change the URL

1. Open **Assistant Library > Import from External Source**.
2. In **Assistant Subscription**, click **Unsubscribe**.
3. Wait for the app to reload and return to built-in templates.
4. To change the data source, reopen the same dialog, enter the new URL, and subscribe.

When a subscription is active, the button unsubscribes. To change the URL, unsubscribe first, then subscribe to the new URL.

## Difference from Import

Cherry Studio has several similar entries with different purposes:

| Feature | Result | Suitable use |
| --- | --- | --- |
| Assistant Subscription | Remote JSON becomes the assistant template data source and is reread when the Assistant Library loads | A team centrally maintains and continuously updates a set of templates |
| URL / File Import in the Assistant Library | Immediately copy templates to My; afterward they are independent of the original file | Import once, then edit locally |
| [V2 Library Import](../cherrystudio/preview/library.md) | Create Library assistants from a file, clipboard, or supported Raw URL | Centrally manage assistants in the V2 Library |

{% hint style="info" %}
To share only one assistant, prefer export and import. Configure a subscription only when you need to maintain a complete public template set over time.
{% endhint %}

## Security Recommendations

- Subscribe only to a URL maintained by you or a trusted team.
- Use HTTPS and restrict who can edit the subscription file.
- After a subscription update, spot-check new or changed prompts.
- Do not store passwords, tokens, or personal information in `prompt`, `description`, or the URL.
- Use version control for an important subscription file so you can roll back quickly after a problem.

Prompts in a template affect how the assistant responds. Before adding a template as an assistant, read the complete prompt and confirm that it contains no unexpected instructions.

## FAQ

### Built-in templates still appear after subscribing

Confirm that the URL begins with `http://` or `https://` and is accessible without signing in. Then reload the app and return to the Assistant Library.

### The URL opens, but no groups appear

Check that the root is an array and that each template's `group` is an array of strings. A template without a valid group does not appear correctly in the category list.

### The response is a web page instead of JSON

You may have copied a repository file's preview page. Use its Raw file URL or deploy the JSON to a static URL that returns the file content directly.

### Assistants did not change after updating the JSON

Reload the app or reenter the Assistant Library. An assistant that has already been created does not synchronize automatically; edit it manually or create it again from the updated template.

### The remote service is temporarily unavailable

Cherry Studio tries to use built-in templates. Reload the app after the service recovers, and check that DNS, certificates, redirects, and cross-origin access work correctly.

***

### Get Help and Submit Feedback

If you encounter a problem during configuration or use, contact us through the official channels under [Feedback and Suggestions](../question-contact/suggestions.md).
