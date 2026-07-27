---
icon: radio
---

# Channels

Channels connect an [Agent](agent.md) in Cherry Studio to instant messaging platforms. When a member sends a message in a group or direct conversation, the bound Agent processes the request in Cherry Studio and replies in the original conversation.

Currently supported:

* Feishu / Lark
* Telegram
* QQ
* WeChat
* Discord
* Slack

For example, a knowledge assistant can answer internal questions in a Feishu group, a personal assistant can receive instructions through Telegram, or a [scheduled task](scheduled-tasks.md) can send a daily report to a specified channel.

{% hint style="info" %}
Channels run locally in Cherry Studio. Channel connections and message processing stop when you exit the app. When you reopen it, enabled channels that are bound to an Agent reconnect automatically. Channels do not depend on the API Server.
{% endhint %}

## Before you begin

Before adding a channel:

1. Create and configure an [Agent](agent.md) that can hold a conversation normally.
2. Select an available model for the Agent and verify that its provider is configured correctly.
3. Prepare the bot credentials required by the target platform, or use the QR code setup provided by Feishu and WeChat.

A channel can be bound to a regular Agent or an Agent with Autonomous Mode enabled. Manually creating a channel does not require Autonomous Mode. If you want an Agent to create channels, troubleshoot connections, or coordinate tasks on its own, use an Agent with Autonomous Mode enabled and review its tool permissions carefully.

## Add a channel

Open `Settings → Channels`, select the target platform, then click **Add**.

The common settings are:

| Setting | Description |
|---|---|
| Name | Distinguishes multiple channel instances on the same platform |
| Bind Agent | The Agent that handles channel messages; the channel does not connect until an Agent is bound |
| Platform credentials | The App ID, token, or secret required by the platform |
| Allowed Chat IDs | Restricts which conversations can use the bot |
| Channel Permission Mode | Inherits the Agent settings or applies a permission mode only to this channel |
| Enabled | Attempts to connect immediately when enabled; disabling preserves the configuration but disconnects the channel |

You can add multiple instances of the same platform, and one Agent can be bound to multiple channels. For example, the same Agent can connect to both a Feishu group and a Telegram direct conversation, while each channel instance uses different credentials, allowlists, and permission modes.

After saving, check the connection status in the channel details. Cherry Studio reconnects an instance when you change its enabled state, credentials, or bound Agent.

## Configure each platform

{% tabs %}
{% tab title="Feishu / Lark" %}
Feishu and Lark support two setup methods:

* **QR code setup**: Leave App ID and App Secret empty, enable the channel, and scan the QR code shown on the page. After registration, Cherry Studio saves the obtained credentials and reconnects.
* **Manual setup**: Enter the App ID and App Secret for your custom app, then choose the `Feishu` or `Lark` domain. Encrypt Key and Verification Token are optional, depending on your app configuration.

When creating an app manually, enable bot capabilities, message permissions, and long-connection event subscriptions in the relevant open platform. Feishu and Lark apps and domains cannot be mixed.
{% endtab %}

{% tab title="Telegram" %}
Use the Telegram Bot Token. You can create a bot and obtain the token through BotFather.

The allowlist uses Telegram Chat IDs. After the bot connects, send `/whoami` in the target direct conversation or group to get the current Chat ID.
{% endtab %}

{% tab title="QQ" %}
Enter the App ID and Client Secret for the QQ bot application.

The allowlist supports typed conversation IDs, for example:

* `c2c:openid`: Direct conversation
* `group:groupid`: Group conversation
* `channel:channelid`: Channel
* `dm:guildid`: Channel direct message

Send `/whoami` to view the current conversation type and ID.
{% endtab %}

{% tab title="WeChat" %}
WeChat uses QR code login, so you do not need to enter a token manually. Add and enable the instance, then scan the QR code with WeChat to sign in. The login credentials are stored in Cherry Studio's local data directory.

Enter WeChat User IDs in the allowlist. You can send `/whoami` in a conversation to get the current ID.
{% endtab %}

{% tab title="Discord" %}
Enter the Discord Bot Token and invite the bot to the target server.

Enter Discord Channel IDs in the allowlist. You can also send `/whoami` in the target channel or direct message and copy the conversation ID returned by Cherry Studio.
{% endtab %}

{% tab title="Slack" %}
Slack uses Socket Mode and requires both:

* A Bot Token, usually beginning with `xoxb-`
* An App-Level Token, usually beginning with `xapp-`

After installing the app and granting message permissions, add the bot to the target channel. Enter Slack Channel IDs in the allowlist; send `/whoami` to obtain one.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Bot credentials grant access to the account. Do not send tokens or secrets in public conversations, screenshots, or documents. If you suspect a credential has leaked, revoke and regenerate it immediately on the corresponding platform.
{% endhint %}

## Restrict accessible conversations

**Allowed Chat IDs** control access to the channel:

* **Empty**: Any conversation that can message the bot can trigger the Agent.
* **IDs entered**: Only conversations on the list can trigger the Agent; other messages are ignored.

When the allowlist is empty, Cherry Studio automatically records the IDs of conversations that have successfully interacted with the bot. These records can also be used as proactive delivery targets for [scheduled tasks](scheduled-tasks.md).

Send `/whoami` in the target conversation first, copy the returned ID, and then add it to the allowlist. Do not leave the allowlist empty long-term for groups or other multi-user environments.

## Set channel permissions

Channel permissions determine how requests coming from the channel can call Agent tools. The default is **Inherit from agent**. You can override the current channel with:

* **Default**: Applies the default confirmation rules before sensitive operations.
* **Accept Edits**: Automatically accepts file edits; other high-risk operations remain restricted.
* **Bypass Permissions**: Stops asking for confirmation and has the highest risk.
* **Plan Mode**: Prioritizes analysis and planning instead of modifying anything directly.

Channel permissions are applied whenever a message arrives, so changes also take effect in existing conversations.

{% hint style="danger" %}
Messages from instant messaging platforms are external input. Consider **Bypass Permissions** only when the Agent's workspace, tools, and allowlist are all strictly restricted. Do not give a bot in a public group access to sensitive directories or credentials.
{% endhint %}

## Use commands in a channel

After the channel connects, you can send the bot:

| Command | Action |
|---|---|
| `/new` | Switch the current channel to a new conversation |
| `/compact` | Compact the context of the current conversation |
| `/help` | View Agent information and available commands |
| `/whoami` | View the current conversation ID for configuring the allowlist |

If one channel needs to serve different teams or work at different permission levels, create separate channel instances with their own Agents, allowlists, and permissions instead of sharing one high-permission configuration.

## Use with scheduled tasks

A channel can receive messages and serve as a delivery target for [scheduled tasks](scheduled-tasks.md):

1. Create and connect the channel.
2. Interact with the bot at least once in the target conversation, or enter an allowed Chat ID directly.
3. Create a scheduled task and select the channel to receive it.

If the allowlist is empty and the target conversation has never interacted with the bot, Cherry Studio may not have an available proactive delivery target.

## Troubleshoot connection problems

### Still disconnected after saving

Check the following in order:

1. Is the channel enabled and bound to an Agent?
2. Are the Agent's model and provider working?
3. Do the token, secret, App ID, and platform domain match?
4. Is the bot installed in the target workspace, server, or group with message permissions?
5. Open **Logs** in the channel details and review the real-time connection errors.

After you correct and save the configuration, Cherry Studio reconnects the channel. You can also disable and then re-enable the instance.

### The bot is online but does not reply

* Check whether the current conversation ID is on the allowlist.
* In a group, confirm that the bot can read messages. Some platforms require you to mention the bot or grant additional group-message permissions.
* Confirm that Cherry Studio is still running.
* Check whether the Agent's model is available and whether channel permissions block a required tool.

### The connection does not complete after scanning

* Confirm that the QR code has not expired. Start the scanning process again if it has.
* For Feishu / Lark, use a client account that matches the selected domain.
* If the WeChat login expires, scan again to update the local login credentials.

{% hint style="warning" %}
Each platform has its own terms of service and organization policies for bots, message retention, and automation. Obtain the required authorization before adding a bot to a company group or offering it as an external service.
{% endhint %}

***

### 💡 Get help and submit feedback

If you have questions, encounter a bug, or have an improvement suggestion while configuring or using channels, see the official options in [Feedback and Suggestions](../question-contact/suggestions.md).
