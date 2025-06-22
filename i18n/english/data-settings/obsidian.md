---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Obsidian Configuration Tutorial

Cherry Studio supports integration with Obsidian, allowing you to export complete conversations or individual messages to your Obsidian vault.

{% hint style="warning" %}
This process does not require installing additional Obsidian plugins. However, since the mechanism used by Cherry Studio to import to Obsidian is similar to the Obsidian Web Clipper, it is recommended to upgrade Obsidian to the latest version (the current version should be at least greater than **1.7.2**) to prevent [import failure when conversations are too long](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Latest Tutorial

{% hint style="info" %}
Compared to the old export to Obsidian feature, the new version can automatically select the vault path, eliminating the need to manually enter the vault name and folder name.
{% endhint %}

### Step 1: Configure Cherry Studio

Open Cherry Studio's _Settings_ → _Data Settings_ → _Obsidian Configuration_ menu. The drop-down box will automatically display the names of Obsidian vaults that have been opened on this machine. Select your target Obsidian vault:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Step 2: Export Conversations

#### Exporting a Complete Conversation

Return to Cherry Studio's conversation interface, right-click on the conversation, select _Export_, and click _Export to Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

A window will pop up allowing you to configure the **Properties** of the note exported to Obsidian, its **folder location**, and the **processing method**:

* **Vault**: Click the drop-down menu to select another Obsidian vault
* **Path**: Click the drop-down menu to select the folder for storing the exported conversation note
* As Obsidian note properties:
  * Tags
  * Created time
  * Source
* Three available processing methods:
  * **New (overwrite if exists)**: Create a new conversation note in the `folder` specified at **Path**. If a note with the same name exists, it will overwrite the old note
  * **Prepend**: When a note with the same name already exists, export the selected conversation content and add it to the beginning of that note
  * **Append**: When a note with the same name already exists, export the selected conversation content and add it to the end of that note

{% hint style="info" %}
Only the first method includes Properties. The latter two methods do not include Properties.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Configuring note properties</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Selecting path</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Choosing processing method</p></figcaption></figure>

After selecting all options, click OK to export the complete conversation to the specified folder in the corresponding Obsidian vault.

#### Exporting a Single Message

To export a single message, click the _three-dash menu_ below the message, select _Export_, and click _Export to Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Exporting a single message</p></figcaption></figure>

The same window as when exporting a complete conversation will appear, requiring you to configure the **note properties** and **processing method**. Complete the configuration following the same steps as in [Exporting a Complete Conversation](#exporting-a-complete-conversation).

### Successful Export

🎉 Congratulations! You've completed all configurations for Cherry Studio's integration with Obsidian and finished the entire export process. Enjoy yourselves!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Export to Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Viewing export results</p></figcaption></figure>

***

## Old Tutorial (for Cherry Studio < v1.1.13)

### Step 1: Prepare Obsidian

Open your Obsidian vault and create a `folder` to store exported conversations (shown as "Cherry Studio" folder in the example):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Note the text highlighted in the bottom-left corner - this is your `vault` name.

### Step 2: Configure Cherry Studio

In Cherry Studio's _Settings_ → _Data Settings_ → _Obsidian Configuration_ menu, enter the `vault` name and `folder` name obtained in [Step 1](#di-yi-bu):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

`Global Tags` is optional and can be used to set tags for all exported conversations in Obsidian. Fill in as needed.

### Step 3: Export Conversations

#### Exporting a Complete Conversation

Return to Cherry Studio's conversation interface, right-click on the conversation, select _Export_, and click _Export to Obsidian_:

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Exporting a complete conversation</p></figcaption></figure>

A window will pop up allowing you to adjust the **Properties** of the note exported to Obsidian and select a **processing method**. Three processing methods are available:

* **New (overwrite if exists)**: Create a new conversation note in the `folder` specified in [Step 2](#di-er-bu). If a note with the same name exists, it will overwrite the old note
* **Prepend**: When a note with the same name already exists, export the selected conversation content and add it to the beginning of that note
* **Append**: When a note with the same name already exists, export the selected conversation content and add it to the end of that note

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Configuring note properties</p></figcaption></figure>

{% hint style="info" %}
Only the first method includes Properties. The latter two methods do not include Properties.
{% endhint %}

#### Exporting a Single Message

To export a single message, click the _three-dash menu_ below the message, select _Export_, and click _Export to Obsidian_:

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Exporting a single message</p></figcaption></figure>

The same window as when exporting a complete conversation will appear. Complete the configuration by following the same steps in [Exporting a Complete Conversation](#exporting-a-complete-conversation).

### Successful Export

🎉 Congratulations! You've completed all configurations for Cherry Studio's integration with Obsidian and finished the entire export process. Enjoy yourselves!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Export to Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Viewing export results</p></figcaption></figure>