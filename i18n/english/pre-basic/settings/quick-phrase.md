---
icon: bolt
---

# Prompts and quick insertion

Prompts let you save content that you enter repeatedly, such as writing requirements, analysis frameworks, or response formats. After saving a prompt, you can quickly search for it and insert it from the chat input without typing it again each time.

Cherry Studio V2 manages this content as **prompts**, replacing the **Quick Phrases** used in earlier versions.

## Create a prompt

### Create one from Library

1. Open [Library](../../cherrystudio/preview/library.md).
2. Select **Prompt** in the left sidebar.
3. Select the new prompt button, then enter a name and content.
4. Select **Save**.

The name is used to find and identify the prompt. The content is the text that will be inserted into the input box. After you save it, the prompt appears both in Library and in the prompt list available from the chat input.

### Create one from the input box

1. Select the lightning bolt icon below the chat input to open the prompt list.
2. Select **Add Prompt...** at the bottom of the list.
3. Enter a name and content, then save the prompt.

To edit or delete an existing prompt, open it from Library.

## Insert a prompt from the input box

You can open the prompt list in either of these ways:

* Select the lightning bolt icon below the chat input.
* Type `/` in the input box to open the Quick Menu, then select **Prompt Management**.

After you search for and select a prompt, Cherry Studio inserts its content at the current cursor position. If text is selected, inserting a prompt with the lightning bolt button replaces that selection. When you open the Quick Menu with `/`, the inserted prompt replaces the trigger and search text.

You can continue editing the inserted content before sending it to the model.

## Variables

The prompt editor can insert `${variable}` as placeholder text. The current version saves and inserts the placeholder unchanged; it does not fill in a value automatically. After inserting the prompt into the chat input, press Tab to select the next `${...}` placeholder. After the last placeholder, pressing Tab again returns to the first one.

{% hint style="warning" %}
Before sending the message, manually replace `${variable}` with the actual content. Do not store passwords, API keys, or other sensitive information in prompts.
{% endhint %}

## Tips

* Use a name that describes the task, such as “Review product documentation” or “Create a meeting summary.”
* Put stable requirements in the prompt, then add information that changes each time after insertion.
* Regularly remove prompts that you no longer use or that duplicate other content so that search results remain concise.
