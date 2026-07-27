---
icon: cherries
---

# CherryIN

CherryIN is a model provider template built into Cherry Studio that lets you access multiple models through one account. V2 presets OpenAI Chat Completions and Anthropic Messages endpoints and provides account login, balance display, a top-up entry point, and route switching.

{% hint style="info" %}
CherryIN is different from the [CherryAI Free Trial](cherryin/). CherryIN uses your own account, credentials, and balance. CherryAI is an in-app trial source and does not appear in the regular Model Services list.
{% endhint %}

## Choose a login method

Open `Settings → Model Services → CherryIN`. You can use either of the following methods.

### Method 1: Log in to a CherryIN account

1. Select **Login with OAuth**;
2. Complete login and authorization in your browser;
3. Return to Cherry Studio;
4. Confirm that the page displays your account information and balance;
5. Make sure the switch at the top of the CherryIN page is on.

After successful authorization, Cherry Studio retrieves an API Key available to the account and adds the OAuth Key to the CherryIN configuration. To add funds, use **Top Up** on the account card to open the CherryIN console.

### Method 2: Enter an API Key manually

1. Open [CherryIN Key Management](https://open.cherryin.ai/console/token);
2. Create or copy an available Key;
3. Return to the CherryIN page in Cherry Studio;
4. Add the Key in the API Key area;
5. Turn on the provider switch.

{% hint style="danger" %}
Do not paste an API Key into chat messages, documentation, or issue screenshots. When troubleshooting, show only a few masked characters at the beginning and end.
{% endhint %}

## Choose a connection route

CherryIN provides three domains in V2:

| Page option | Domain | Recommendation |
|---|---|---|
| Accelerated Route | `open.cherryin.cc` | Try first on networks in mainland China |
| International Route | `open.cherryin.net` | Try first on overseas or international networks |
| Backup Route | `open.cherryin.ai` | Try when the primary route is temporarily inaccessible |

If the page displays a route menu, changing the route replaces the domain for each provider endpoint while preserving its path. If the menu is unavailable, check the current Base URL in the API address area.

{% hint style="warning" %}
Route names identify preset entry points and do not guarantee the same speed on every network. Run a connection check after selecting one and rely on the actual result.
{% endhint %}

## Sync and enable models

1. Under **Models**, select **Add**;
2. Review added, updated, and removed entries in the sync preview;
3. Apply the changes;
4. Search for the models you plan to use;
5. Turn on the target models;
6. Run Model Health Check.

CherryIN's model list, pricing, and available quota can change, so this page does not specify fixed models. See [CherryIN Models and Pricing](https://open.cherryin.ai/pricing) and refer to the results synced by the client.

## APIs and models

The CherryIN template presets OpenAI- and Anthropic-compatible endpoints. Cherry Studio sends requests based on model information and endpoint type.

- General chat models usually use an OpenAI-compatible API;
- Models such as Claude can use an Anthropic-compatible API;
- Some Gemini or image models use dedicated routes;
- Capabilities and parameters can differ when endpoints provide models with the same name.

Do not judge Agent, Vision, Reasoning, or Tool capabilities by the model name alone. Review model tags and complete an actual test.

## Verify the configuration

Complete these checks in order:

1. Run a connection check in the authentication area;
2. Run Health Check in the model list;
3. Return to the Chats page and select the target model;
4. Send a simple text message;
5. If you need images or tool calling, run a minimal test for each.

A model appears in the model selector only when both the provider and model switches are enabled.

## Account and logout

After you log in with an account, Cherry Studio can display the CherryIN account information and balance. Selecting **Logout** clears the CherryIN OAuth login state stored locally and removes Keys that OAuth added.

Manually added Keys and OAuth Keys come from different sources. If you still need a manual Key, confirm that it remains enabled after logout.

## Troubleshooting

### Cherry Studio does not reopen after login

Keep Cherry Studio running and complete authorization in the browser again. If the system blocks the app-link callback, allow the browser to open Cherry Studio.

### Login succeeds but the model list is empty

Select **Add** first. If the list remains empty, check whether the account has an available Key, the current route is accessible, and the CherryIN console has made models available to the account.

### The provider returns 401 or 403

The Key may have expired, been disabled, or lack model permission. Log in again, or create a new Key on the Key Management page and replace the old one.

### Requests time out or cannot connect

Switch between the accelerated, international, and backup routes, then run the connection check again. Also check the system proxy, firewall, and local network.

### Claude or Agent requests fail

Confirm that the selected model has Tool capability and that the request uses an Anthropic-compatible endpoint. A provider supporting an Anthropic endpoint does not mean every model from that provider supports Agent.

For general configuration and multi-Key information, see [Model Services](README.md) and [Model Services settings](../../cherrystudio/preview/settings/providers.md). If the problem persists, submit the Cherry Studio version, operating system, model ID, and sanitized error details. See [Feedback and Suggestions](../../question-contact/suggestions.md) for contact options.
