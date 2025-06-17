---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Obsidian Configuration Tutorial

Cherry Studio supports integration with Obsidian, allowing you to export entire conversations or single messages to your Obsidian vault.

{% hint style="warning" %}
This process does not require installing any additional Obsidian plugins. However, since Cherry Studio's import mechanism is similar to the Obsidian Web Clipper, it's recommended to upgrade Obsidian to the latest version (at least greater than **1.7.2**) to avoid [import failures with long conversations](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Latest Tutorial

{% hint style="info" %}
Compared to the old export feature, the new version can automatically select the vault path, so you no longer need to manually enter the vault name and folder name.
{% endhint %}

### Step 1: Configure Cherry Studio

Open Cherry Studio's _Settings_ → _Data Settings_ → _Obsidian Configuration_ menu. The dropdown will automatically list the Obsidian vaults that have been opened on your machine. Select your target Obsidian vault:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Step 2: Export Conversation

#### Exporting an Entire Conversation

Go back to the conversation interface in Cherry Studio, right-click on the conversation, select _Export_, and click _Export to Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

A window will pop up, allowing you to adjust the **Properties**, the **folder location** in Obsidian, and the **handling method** for the exported note:

*   **Vault**: Click the dropdown menu to select other Obsidian vaults
*   **Path**: Click the dropdown menu to select the folder where the exported note will be stored
*   As Obsidian note properties (Properties):
    *   Tags (tags)
    *   Creation time (created)
    *   Source (source)
*   There are three **handling methods** for exporting to Obsidian:
*   There are three **handling methods** for exporting to Obsidian:
    *   **Create new (overwrite if exists)**: Creates a new note in the `folder` specified in the **Path**. If a note with the same name already exists, it will be overwritten.
    *   **Prepend**: If a note with the same name exists, the selected conversation content will be prepended to the beginning of that note.
    *   **Append**: If a note with the same name exists, the selected conversation content will be appended to the end of that note.

{% hint style="info" %}
Only the first method will include Properties; the other two methods will not.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Configure note properties</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Select path</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Select handling method</p></figcaption></figure>

After selecting all options, click OK to export the entire conversation to the corresponding folder in the specified Obsidian vault.

#### Exporting a Single Message

To export a single message, click the _three-bar menu_ below the message, select _Export_, and click _Export to Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Export single message</p></figcaption></figure>

A window similar to the one for exporting an entire conversation will appear, asking you to configure the **note properties** and **handling method**. Follow the [tutorial above](obsidian.md#dao-chu-wan-zheng-dui-hua) to complete the process.

### Export Successful

🎉 Congratulations! You have now completed all the configurations for integrating Cherry Studio with Obsidian and have gone through the entire export process. Enjoy!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Export to Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>View the exported result</p></figcaption></figure>



***

## Old Tutorial (for Cherry Studio < v1.1.13)

### Step 1: Prepare Obsidian

Open your Obsidian vault and create a `folder` to save the exported conversations (the example in the image uses a folder named "Cherry Studio"):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Take note of the text in the bottom-left corner; this is your `vault` name.

### Step 2: Configure Cherry Studio

In Cherry Studio's _Settings_ → _Data Settings_ → _Obsidian Configuration_ menu, enter the `vault` name and `folder` name you noted in [Step 1](obsidian.md#di-yi-bu):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

The `Global Tags` field is optional. You can set tags that will be applied to all exported conversations in Obsidian. Fill it in as needed.

### Step 3: Export Conversation

#### Exporting an Entire Conversation

Go back to the conversation interface in Cherry Studio, right-click on the conversation, select _Export_, and click _Export to Obsidian_.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Export entire conversation</p></figcaption></figure>

A window will pop up, allowing you to adjust the **Properties** for the exported note and the **handling method**. There are three **handling methods** for exporting to Obsidian:

*   **Create new (overwrite if exists)**: Creates a new note in the `folder` you specified in [Step 2](obsidian.md#di-er-bu). If a note with the same name already exists, it will be overwritten.
*   **Prepend**: If a note with the same name exists, the selected conversation content will be prepended to the beginning of that note.
*   **Append**: If a note with the same name exists, the selected conversation content will be appended to the end of that note.

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Configure note properties</p></figcaption></figure>

{% hint style="info" %}
Only the first method will include Properties; the other two methods will not.
{% endhint %}

#### Exporting a Single Message

To export a single message, click the _three-bar menu_ below the message, select _Export_, and click _Export to Obsidian_.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Export single message</p></figcaption></figure>

A window similar to the one for exporting an entire conversation will appear, asking you to configure the **note properties** and **handling method**. Follow the [tutorial above](obsidian.md#dao-chu-wan-zheng-dui-hua) to complete the process.

### Export Successful

🎉 Congratulations! You have now completed all the configurations for integrating Cherry Studio with Obsidian and have gone through the entire export process. Enjoy!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Export to Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>View the exported result</p></figcaption></figure>