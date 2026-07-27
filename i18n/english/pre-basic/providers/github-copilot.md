# GitHub Copilot

Cherry Studio can connect to your Copilot account through GitHub device authorization and read the models currently available to that account. You do not need to create an API Key manually, but the GitHub account must have valid access to Copilot.

{% hint style="info" %}
GitHub Copilot, GitHub Models, and GitHub Copilot CLI are three separate entry points. This page covers `Settings → Model Providers → GitHub Copilot`, which lets you use Copilot models in Cherry Studio chats.
{% endhint %}

## Before You Begin

Before starting, confirm that:

1. You have a GitHub account that you can sign in to;
2. The account has Copilot Free, Student, Pro, Pro+, or Max, or a Business / Enterprise entitlement assigned by an organization;
3. No organization or enterprise policy blocks the relevant models or Copilot features;
4. Your current network can access GitHub sign-in and Copilot services;
5. You understand the model availability and [GitHub AI Credits](https://docs.github.com/en/copilot/concepts/billing) rules for your current plan.

Models, allowances, and billing rules vary by plan and may change. Cherry Studio synchronizes models that the Copilot API currently exposes to your account and that are not disabled by policy. Do not rely on a fixed model list from an older tutorial.

GitHub Copilot Free and Student currently provide limited model access primarily through automatic model selection. Paid and organization plans offer more selectable models, but availability still depends on the account, region, organization policies, and GitHub's current release status.

## Authorize in Cherry Studio

1. Open `Settings → Model Providers`;
2. Switch the filter on the left to **All Providers**;
3. Select **GitHub Copilot**;
4. Click **Start Authorization**;
5. Wait for Cherry Studio to generate a Device Code;
6. Copy the authorization code. The app usually copies it automatically, but you can also copy it manually;
7. Click **Open Authorization Page**;
8. In the browser, sign in to the GitHub account you want to use;
9. Enter the Device Code and confirm authorization;
10. Return to Cherry Studio;
11. Click **Connect to Github** to complete the connection.

After a successful connection, the page displays the GitHub username and avatar and automatically enables the provider.

{% hint style="warning" %}
The account already signed in to the browser may not be the account you intend to connect. Check the username before authorizing, especially when switching among personal, work, and enterprise-managed accounts.
{% endhint %}

## What Happens During Authorization

Cherry Studio uses GitHub Device Flow:

1. It requests a temporary Device Code from GitHub;
2. You confirm authorization on the GitHub page;
3. Cherry Studio exchanges the authorization result for a GitHub access token;
4. It then obtains a temporary token for Copilot requests;
5. It encrypts the GitHub access token through the operating system's secure storage and saves it locally;
6. It refreshes the Copilot token for later model synchronization or chats.

For this reason, successful authorization on the GitHub page is only the first step. Cherry Studio must also obtain a Copilot token before it can show a successful connection.

{% hint style="danger" %}
Do not send a Device Code, access token, or Copilot token to anyone, and do not include one in documentation, chats, code repositories, or screenshots. An authorization code is temporary but can still be misused while it remains valid.
{% endhint %}

## Synchronize Models

After authorization succeeds:

1. Confirm that the GitHub Copilot provider is enabled;
2. Click **Add** or synchronize models;
3. Review the synchronization preview;
4. Apply the changes;
5. Enable only the models you plan to use;
6. Run a health check for each model.

Cherry Studio accesses Copilot's `/models` endpoint and filters out:

- Models that GitHub policies mark as unavailable;
- Non-model entries such as account-routing items;
- Voice, transcription, and other models that are not currently suitable for the chat list.

If models suddenly appear, disappear, or change names, the cause is usually a change in the GitHub plan, organization policy, or server-side release. Synchronize again to retrieve the current list.

## Plans, Models, and Costs

GitHub measures GitHub Copilot usage against your GitHub account. Starting a request from Cherry Studio does not make it free.

- Different plans include different amounts of GitHub AI Credits;
- Model usage depends on input, output, cached tokens, and the model price;
- Organizations and enterprises can configure shared allowances, user budgets, and additional usage restrictions;
- When the allowance is exhausted, calls may be blocked or incur additional charges;
- Some older annual plans may continue to use legacy premium request accounting until renewal.

A model appearing in Cherry Studio does not mean it has the same cost under your plan. Check GitHub's billing and Copilot usage pages before using it.

## Rate Limiting

The GitHub Copilot provider page includes a **Rate limiting** slider from 1 to 60, with a default value of 10. It controls the minimum wait between consecutive Cherry Studio requests to this provider, in seconds.

- Keep the default value for ordinary chats;
- Increase it if you encounter rate limits;
- You can lower it for rapid sequential testing, but it cannot bypass GitHub's server-side limits;
- Multiple windows, automated tasks, or concurrent requests can still accumulate against account limits.

GitHub also applies server-side throttling based on capacity, fair use, and abuse prevention. If you encounter throttling, wait before retrying and check your usage and plan instead of repeatedly resending requests.

## Choose Models and Capabilities

### Standard Chat

Select a model currently available in the model list and send a short message. After basic chat succeeds, test long contexts, images, or tools.

### Vision

Cherry Studio adds a vision-support request header to Copilot requests, but the ability to process images still depends on the specific model and account permissions.

1. Select a model explicitly listed as supporting images;
2. Upload one small image;
3. Confirm that the model actually understands the image;
4. Then test multiple or high-resolution images.

The same model may show different capabilities before and after a GitHub update. Use the current health check and actual results as the source of truth.

### MCP and Tool Calling

Cherry Studio MCP requires a model that supports structured Tool Calling.

1. Complete a standard chat first;
2. Enable only one simple MCP tool;
3. Explicitly ask the model to call the tool;
4. Check whether it produces an actual structured call;
5. Confirm that the model continues its answer after receiving the tool result;
6. Add more tools gradually.

Having access to Copilot does not mean that every visible model supports tools. If a model only says that it will call a tool without making an actual call, choose a model with stronger tool capabilities.

### Reasoning and Parameters

Different Copilot models use different reasoning parameters. Cherry Studio applies the corresponding configuration based on model detection, but a server-side model update may arrive before the client recognition rules.

If you encounter a parameter error:

1. Restore the reasoning option to **Default**;
2. Clear custom parameters;
3. Synchronize models again;
4. Retry the health check;
5. Enable the required parameters one at a time.

## PDFs and Attachments

V2 currently extracts PDF text locally before sending it to the model through Copilot's OpenAI-compatible API:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes context and GitHub AI Credits;
- Images in a PDF must be sent separately to a vision model.

Before uploading a file, confirm that its content complies with your organization's data-use and confidentiality requirements. Copilot is a cloud service; do not treat it as a local offline model.

## Organization and Enterprise Accounts

Organizations and enterprises can control Copilot features, models, and network access. Even when an account shows an assigned Copilot entitlement, policies may still prevent access to some models.

For an organization account issue, ask an administrator to check:

- Whether the user has been assigned a Copilot seat;
- Whether Copilot Chat and the relevant models are enabled;
- Whether any model-level policy restrictions apply;
- Whether the budget or GitHub AI Credits are exhausted;
- Whether the enterprise network permits only specific Copilot subscription endpoints;
- Whether a firewall, proxy, or TLS inspection blocks GitHub Copilot.

Organization policies apply to multiple entry points authenticated with that identity, not only Cherry Studio.

## Proxies and Networks

Authorization and model calls must at least reach GitHub sign-in, the GitHub API, and Copilot services. A company proxy, firewall, VPN, or security application may allow only some addresses and cause:

- Device Code generation to fail;
- Browser authorization to succeed while the Cherry Studio connection fails;
- User information to load while the Copilot token cannot be obtained;
- An empty model list;
- Chat requests to time out or be rejected.

Prefer a system proxy or HTTP proxy currently supported by Cherry Studio, and ask your network administrator to permit the required addresses according to the [GitHub Copilot allowlist](https://docs.github.com/en/copilot/reference/copilot-allowlist-reference).

Do not add custom request headers from an unknown source. The request-header editor on the GitHub Copilot page is primarily for special proxy or compatibility scenarios. Incorrect `Authorization`, `Host`, client-identification, or routing headers may cause authentication to fail.

## Sign Out or Change Accounts

To switch accounts:

1. Click **Exit GitHub** on the GitHub Copilot provider page;
2. Confirm that the username and avatar are cleared;
3. Switch to the target GitHub account in the browser;
4. Complete device authorization again;
5. Synchronize models again.

Signing out in Cherry Studio deletes the locally stored Copilot credentials and provider key, but it does not revoke OAuth authorization in the GitHub account. If a device is lost or you suspect credential exposure, also revoke access in GitHub's authorized application settings and review the account's security log.

## Troubleshooting

### Failed to Obtain a Device Code

Check the network, proxy, firewall, and GitHub service status. Confirm that the system time is correct, disable any security application that may intercept GitHub sign-in requests, and retry.

### GitHub Is Authorized, but the Connection Fails

Cherry Studio has not yet obtained the GitHub or Copilot token. Return to the app and click **Connect to Github**. If the request times out, generate a new Device Code instead of reusing the old one.

### The Username Appears, but Models Do Not Synchronize

A valid GitHub sign-in does not guarantee that the account has Copilot access. Check the Copilot plan, organization seat, model policies, and usage allowance, then sign out and authorize again.

### The Model List Is Empty

The account may have access only to automatic model selection, the organization may have disabled models, or the network may be blocking the Copilot `/models` request. Confirm that the account works on GitHub's official Copilot page before synchronizing again.

### A Model Suddenly Disappeared

GitHub may have changed its release status, plan availability, or organization policy. Synchronize again and check GitHub's current model list.

### A 401 or 403 Error Is Returned

The credentials may have expired, authorization may have been revoked, the account may lack Copilot access, or an organization policy may deny access. Sign out and authorize again. If the problem continues, check the account plan and administrator policies.

### A 429 or Rate-Limit Error Is Returned

Wait before retrying, increase Cherry Studio's rate-limiting value, and check GitHub AI Credits, budgets, and server-side throttling.

### Images or MCP Do Not Work

Confirm that the selected model supports the relevant capability. A successful basic chat does not mean that the model supports vision or tool calling.

### Copilot Does Not Work on a Company Network

Ask a network administrator to check the Copilot allowlist, subscription-specific domains, proxy authentication, and TLS inspection. Do not solve the problem by disabling every security policy.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For Copilot plans, usage, and policies, see the [official GitHub Copilot documentation](https://docs.github.com/en/copilot). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
