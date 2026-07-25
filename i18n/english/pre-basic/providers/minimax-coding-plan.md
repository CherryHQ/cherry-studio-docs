# MiniMax Token Plan (formerly Coding Plan)

MiniMax has upgraded Coding Plan to **Token Plan**. It is designed for individual developers, AI coding, and frequent everyday use, allowing MiniMax model calls through subscription allowances or Credits.

Cherry Studio V2 does not have a separate "Coding Plan" provider. Enter a dedicated Token Plan Key in the built-in **MiniMax** or **MiniMax Global** provider.

{% hint style="info" %}
This page path is retained for compatibility with the old documentation. Use the current **Token Plan** page as the source of truth for the actual product name, plans, and allowances on the MiniMax platform. Do not continue to apply outdated information from older tutorials, such as M2.1, fixed monthly prices, or "40 requests every five hours."
{% endhint %}

## Token Plan vs. the Standard API

| Item | Token Plan | Standard pay-as-you-go API |
| --- | --- | --- |
| Key source | Token Plan / subscription management | API Keys |
| Common Key | `sk-cp...` | Standard API Key |
| Metering | Plan allowances, Credits, and rolling windows | Billed by actual API usage |
| Validity | Depends on the subscription, seat, or Credits | Depends on the account balance and Key status |
| Intended use | Personal interaction, coding tools, and everyday use | Production integrations and reliable pay-as-you-go calls |

The two types of Key are **not interchangeable**. Using a standard API Key as a Token Plan Key, or using a Token Plan Key as a standard pay-as-you-go Key, may return a 401 or allowance error or charge the wrong billing source.

MiniMax recommends the pay-as-you-go API for production. Token Plan may enforce RPM, TPM, rolling-window, weekly allowance, and peak-time dynamic rate limits. It is not an unlimited batch service.

## Choose the Mainland China or International Platform

| Account and subscription | Cherry Studio provider | OpenAI Base URL | Anthropic Base URL |
| --- | --- | --- | --- |
| Mainland China MiniMax platform | MiniMax | `https://api.minimaxi.com/v1` | `https://api.minimaxi.com/anthropic` |
| MiniMax international platform | MiniMax Global | `https://api.minimax.io/v1` | `https://api.minimax.io/anthropic` |

Do not mix accounts, Keys, or Base URLs between the Mainland China and international platforms. Choose based on the platform where you purchased Token Plan and created the Key, not your current physical location.

## Get a Token Plan Key

### Mainland China Platform

1. Sign in to the [MiniMax Open Platform](https://platform.minimaxi.com/);
2. Open [Token Plan](https://platform.minimaxi.com/subscribe/token-plan);
3. Purchase a plan, redeem an entitlement, or confirm that a Team seat has been assigned;
4. Go to the API Keys page;
5. Select **Create Token Plan Key**;
6. Copy the new Key and store it securely.

### International Platform

1. Sign in to the [MiniMax API Platform](https://platform.minimax.io/);
2. Open [Token Plan](https://platform.minimax.io/subscribe/token-plan);
3. Purchase a plan or Credits, or confirm your Team seat;
4. Go to API Keys;
5. Create a **Token Plan Key**;
6. Copy the new Key and store it securely.

{% hint style="danger" %}
Do not put a Token Plan Key in chats, documents, code repositories, or troubleshooting screenshots. An exposed Key may consume subscription allowances or Credits. Delete and replace it immediately on the MiniMax platform.
{% endhint %}

The `sk-cp` prefix alone does not prove that a Key is usable. Also confirm that the subscription is active, the seat is assigned, Credits are available, and the Key comes from the correct platform.

## Configure Cherry Studio

1. Open `Settings → Model Providers`;
2. Switch the filter on the left to **All Providers**;
3. Select **MiniMax** for a Mainland China account or **MiniMax Global** for an international account;
4. Paste the Token Plan Key into API Key;
5. Check that the Base URL matches the account platform;
6. Turn on the provider switch at the top of the page;
7. Click **Add** or synchronize models;
8. Review the synchronization preview and apply the changes;
9. Enable only the models currently included in the plan;
10. Run a model health check.

Cherry Studio's MiniMax presets retain both OpenAI- and Anthropic-compatible addresses. Standard chats use the OpenAI-compatible path by default, while some Code Tools can use the Anthropic-compatible path.

For more protocol, vision, reasoning, MCP, and PDF boundaries, see [MiniMax](minimax.md).

## Choose a Model

The current MiniMax presets in Cherry Studio V2 include:

- `MiniMax-M3`
- `MiniMax-M2.7`
- `MiniMax-M2.7-highspeed`

Models available through MiniMax Token Plan may change as plans and products are upgraded. Use the subscription page, account usage page, and actual model synchronization results as the source of truth.

Recommendations:

1. Test the plan's current featured model, `MiniMax-M3`, first;
2. Test `MiniMax-M2.7` when you need compatibility with an older workflow;
3. Use `MiniMax-M2.7-highspeed` only when the plan explicitly includes the high-speed model;
4. Do not manually add the older `MiniMax-M2.1` and assume that the plan still includes it;
5. A model with the same name may have different allowance rules under Token Plan and the pay-as-you-go API.

{% hint style="warning" %}
A model appearing in a Cherry Studio preset or synchronization list does not guarantee that your Token Plan includes it. MiniMax makes the final server-side authorization decision.
{% endhint %}

## Reasoning, Vision, and MCP

### Reasoning

MiniMax M-series models return reasoning content. Cherry Studio must preserve reasoning blocks and tool-call information across multi-turn chats to maintain context continuity in later requests.

If changing a reasoning option causes a parameter error, restore it to **Default** and retry. A Token Plan Key does not change the parameters accepted by the model itself.

### Vision

Token Plan has expanded to multimodal models, but whether Cherry Studio can currently send an image directly still depends on the specific model ID and V2 capability detection.

After synchronization, confirm that the model shows image support and test it with a small image. If the current V2 does not correctly detect vision support for `MiniMax-M3`, do not bypass the restriction by changing only the display name.

### MCP

Cherry Studio MCP uses the model's Tool Calling capability. MiniMax Token Plan also provides official Web Search and Understand Image MCP services, but these are not the same as MCP servers configured in Cherry Studio.

When using Cherry Studio MCP:

1. Complete a standard chat first;
2. Enable only one simple tool;
3. Check whether the model produces an actual structured call;
4. Add more tools afterward.

If you need an official MiniMax Token Plan MCP service, configure it separately according to the official guide and remember that it consumes resources from the corresponding plan.

## Check Usage

The most reliable method is to open the Token Plan or subscription management page on the MiniMax platform and check:

- The current plan or Team seat;
- Remaining allowances and Credits;
- Usage by model;
- Rolling-window recovery time;
- Periodic allowances;
- High-speed model eligibility;
- Subscription expiration.

Do not estimate remaining usage only from the number of successful Cherry Studio requests. Long contexts, vision, generative models, and different models may use separate allowance pools.

## Limits and 429 Errors

Token Plan may simultaneously enforce:

- Short-term RPM / TPM rate limits;
- A five-hour rolling window;
- Weekly allowances;
- Separate allowances for multimodal models;
- Dynamic rate limiting during peak periods;
- Plan concurrency limits.

Therefore, `429 Too Many Requests` does not necessarily mean that the entire subscription allowance is exhausted.

Troubleshoot in this order:

1. Pause for one minute and retry;
2. Check the Token Plan usage page;
3. Check the rolling window and weekly allowance;
4. Reduce concurrency, long contexts, and automatic retries;
5. Confirm that multiple people are not sharing one personal Key;
6. Upgrade the plan or switch to a pay-as-you-go API Key if necessary.

Replacing the Key directly with a standard API Key in the same provider changes the allowance and billing source. Check the account balance and budget before doing so.

## Troubleshooting

### A 401 Error Is Returned

The Key may be incorrect or deleted, the subscription may have expired, the seat may be invalid, or Mainland China and international Base URLs may be mixed. Copy the Token Plan Key again from the corresponding platform.

### A 403 Error Is Returned

The current plan, Team policy, or model permission does not allow the request. Check Token Plan entitlements and model availability.

### A 404 Error Is Returned

The Base URL, protocol path, or model ID is incorrect. Restore the MiniMax / MiniMax Global preset addresses and synchronize models again.

### A 429 Error Is Returned

This may be a per-minute rate limit, rolling window, weekly allowance, or peak-time dynamic limit. Use the Token Plan usage page as the source of truth instead of repeatedly sending the request.

### Standard Models Work, but the High-Speed Model Does Not

The current plan may not include the high-speed entitlement, or high-speed capacity may be temporarily unavailable. Use a standard model and check the plan description.

### The Model List Still Shows Older Models

Synchronize again and check that the provider connects to the correct platform. A manually retained older model does not mean the current plan supports it.

### The Key Check Succeeds, but the Chat Uses the Account Balance

You may have entered a standard pay-as-you-go API Key instead of a Token Plan Key. Check the MiniMax bill and Key type immediately.

### Production Use Is Frequently Rate-Limited

Token Plan is designed for personal interaction and development workflows. Production, batch, or high-concurrency services should use the pay-as-you-go API with budgets, monitoring, and retry policies.

For current MiniMax Token Plan plans, models, and usage rules, see the [Mainland China documentation](https://platform.minimaxi.com/docs/token-plan/quickstart) or [international documentation](https://platform.minimax.io/docs/token-plan/quickstart). For general provider configuration, see [MiniMax](minimax.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
