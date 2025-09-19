---
icon: seal-question
---
# Frequently Asked Questions


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Common Error Codes

*   **4xx (Client Error Status Codes)**: Generally, these indicate issues like incorrect request syntax, failed authentication, or authorization failures, preventing the request from being completed.
*   **5xx (Server Error Status Codes)**: Generally, these indicate server-side errors, such as server downtime or request processing timeouts.

| Error Code | Possible Scenarios | Solution |
| :--------- | :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **400**    | Request body format error, etc. | <p>Check the error content returned by the conversation or view the error content in the <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a>, and follow the prompts.</p><p><a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa"><mark style="color:purple;">【Common Scenario 1】</mark>: If it's a Gemini model, you might need to bind a card;<br><mark style="color:purple;">【Common Scenario 2】</mark>: Data volume exceeded, common in visual models where the image volume exceeds the upstream single request traffic limit, leading to this error code;<br><mark style="color:purple;">【Common Scenario 3】</mark>: Unsupported parameters added or incorrect parameter entry. Try creating a clean assistant to test if it works normally;<br><mark style="color:purple;">【Common Scenario 4】:</mark> Context limit exceeded, clear context or start a new conversation or reduce the number of context entries.</a></p> |
| **401**    | Authentication failed: Model not supported or server account banned, etc. | Contact or check the account status with the corresponding service provider. |
| **403**    | Request operation unauthorized | Perform corresponding actions based on the error message returned by the conversation or the [console](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa) error message. |
| **404**    | Requested resource not found | Check the request path, etc. |
| **422**    | Request format is correct, but semantic error | The server can parse such errors but cannot process them. This is common in JSON semantic errors (e.g., null values; expecting a string but receiving a number or boolean, etc.). |
| **429**    | Request rate limit reached | Request rate (TPM or RPM) limit reached, please try again after a while. |
| **500**    | Internal server error, unable to complete the request | If it persists, contact the upstream service provider. |
| **501**    | The server does not support the requested functionality, unable to complete the request | |
| **502**    | As a gateway or proxy server, it received an invalid response from an upstream server while attempting to fulfill the request. | |
| **503**    | The server is temporarily unable to handle the client's request due to overload or system maintenance. The length of the delay may be indicated in the server's Retry-After header. | |
| **504**    | As a gateway or proxy server, it did not receive a timely response from the upstream server. | |

***

## How to View Console Errors

*   Click on the Cherry Studio client window and press the shortcut <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>).

{% hint style="info" %}
*   The active window must be the Cherry Studio client window to open the console;
*   You need to open the console first, then click on test or initiate a conversation and other requests to collect request information.
{% endhint %}

*   In the popped-up console window, click <mark style="color:blue;">`Network`</mark> → click to view the last <mark style="color:red;">`completions`</mark> marked with a red <mark style="color:red;">`×`</mark> at ② _(when encountering errors in conversation, translation, model connectivity checks, etc.)_ or <mark style="color:red;">`generations`</mark> _(when encountering errors in drawing)_ → click <mark style="color:blue;">`Response`</mark> to view the complete returned content (area ④ in the figure).

> If you cannot determine the cause of the error, please send a screenshot of this interface to the [Official Communication Group](https://t.me/CherryStudioAI) for help.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

This inspection method can be used not only to obtain error information during conversations but also during model testing, adding knowledge bases, drawing, etc. In any case, you need to open the debug window first and then perform the request operation to get the request information.·

{% hint style="info" %}
The name in the Name column (at ② in the figure above) will vary in different scenarios.

Conversation, Translation, Model Check: <mark style="color:red;">`completions`</mark>

Drawing: <mark style="color:red;">`generations`</mark>

Knowledge Base Creation: <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Formulas Not Rendered / Formula Rendering Errors

*   If the formula is not rendered but the formula code is displayed directly, check if the formula has delimiters.

> **Delimiter Usage**
>
> _Inline Formulas_
>
> *   Use a single dollar sign: `$formula$`
> *   Or use `\(` and `\)`, e.g.: `\(formula\)`
>
> _Standalone Formula Blocks_
>
> *   Use double dollar signs: `$$formula$$`
> *   Or use `\[formula\]`
> *   Example: `$$\sum_{i=1}^n x_i$$`\
>     $$\sum_{i=1}^n x_i$$

*   Formula rendering errors/garbled text are common when formulas contain Chinese content; try switching the formula engine to KateX.

***

## Failed to Create Knowledge Base / Failed to Get Embedding Dimensions Prompt

1.  Model status unavailable

> Confirm whether the service provider supports this model or if the model service status is normal with the service provider.

2.  Used a non-embedding model

***

## Model Cannot Recognize Images / Unable to Upload or Select Images

First, confirm whether the model supports image recognition. Cherry Studio categorizes popular models, and those with an eye icon after their name support image recognition.

Image recognition models support uploading image files. If the model's functionality is not correctly matched, you can find the model in the corresponding service provider's model list, click the settings button after its name, and check the image option.

Specific model information can be found and reviewed with the corresponding service provider. Similar to embedding models, models that do not support vision do not need to have the image function forcibly enabled, and checking the image option will have no effect.