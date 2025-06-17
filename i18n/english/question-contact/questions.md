---
icon: seal-question
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Frequently Asked Questions

## Common Error Codes

*   **4xx (Client Error Status Codes)**: Generally indicate that the request cannot be completed due to a syntax error, authorization failure, or authentication failure.
*   **5xx (Server Error Status Codes)**: Generally indicate a server-side error, such as the server being down, or the request processing timing out.

| Error Code | Possible Causes | Solution |
| :--- | :--- | :--- |
| <h4>400</h4> | Incorrect request body format, etc. | <p>Check the error message returned in the conversation or view the error content in the <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a>, and follow the prompts.</p><p><mark style="color:purple;">[Common Case 1]</mark>: If it's a Gemini model, you may need to link a credit card;<br><mark style="color:purple;">[Common Case 2]</mark>: Data size exceeds the limit, common with vision models. This error code is returned if the image size exceeds the upstream's single request traffic limit;<br><mark style="color:purple;">[Common Case 3]</mark>: Added unsupported parameters or filled in parameters incorrectly. Try creating a new, clean assistant to test if it works normally;<br><mark style="color:purple;">[Common Case 4]:</mark> Context exceeds the limit. Clear the context, start a new conversation, or reduce the number of context messages.</p> |
| <h4>401</h4> | Authentication failed: The model is not supported or the server-side account is banned, etc. | Contact or check the status of the corresponding service provider's account. |
| <h4>403</h4> | No permission for the requested operation. | Perform the corresponding action based on the error message returned in the conversation or the error message in the [console](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa). |
| <h4>404</h4> | Cannot find the requested resource. | Check the request path, etc. |
| <h4>422</h4> | The request format is correct, but there is a semantic error. | The server can parse this type of error but cannot process it. Commonly occurs with JSON semantic errors (e.g., null values; a value required to be a string is written as a number or boolean, etc.). |
| <h4>429</h4> | Request rate has reached the limit. | The request rate (TPM or RPM) has reached the limit. Take a break and try again later. |
| <h4>500</h4> | Internal server error, unable to complete the request. | If it persists, contact the upstream service provider. |
| <h4>501</h4> | The server does not support the functionality required to fulfill the request. | |
| <h4>502</h4> | The server, while acting as a gateway or proxy, received an invalid response from an inbound server it accessed in attempting to fulfill the request. | |
| <h4>503</h4> | The server is temporarily unable to handle the client's request due to overload or system maintenance. The length of the delay may be included in the server's Retry-After header. | |
| <h4>504</h4> | The server, acting as a gateway or proxy, did not receive a timely response from the upstream server. | |

***

## How to Check Console Errors

*   After clicking the Cherry Studio client window, press the shortcut key <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (for Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- The currently active window must be the Cherry Studio client window to open the console;
- You need to open the console first, and then click test or initiate a conversation or other requests to collect request information.
{% endhint %}

*   In the pop-up console window, click <mark style="color:blue;">`Network`</mark> → click to view the last item in section ② marked with a red <mark style="color:red;">`×`</mark>, which will be <mark style="color:red;">`completions`</mark> *(for errors in conversations, translations, model connectivity checks, etc.)* or <mark style="color:red;">`generations`</mark> *(for errors in painting)* → click <mark style="color:blue;">`Response`</mark> to view the full returned content (area ④ in the figure).

> If you cannot determine the cause of the error, please send a screenshot of this interface to the [Official Communication Group](https://t.me/CherryStudioAI) for help.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

This inspection method can be used not only to obtain error information during conversations, but also during model testing, adding knowledge bases, painting, etc. In any case, you need to open the debugging window first, and then perform the request operation to obtain the request information.

{% hint style="info" %}
The name in the Name column (② in the image above) will vary depending on the scenario

Conversation, Translation, Model Check: <mark style="color:red;">`completions`</mark>

Painting: <mark style="color:red;">`generations`</mark>

Knowledge Base Creation: <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Formulas Not Rendered / Formula Rendering Errors

*   If the formula code is displayed directly instead of being rendered, check if the formula has delimiters.

> **Delimiter Usage**
>
> _Inline formulas_
>
> *   Use single dollar signs: `$formula$`
> *   Or use `\(` and `\)`, like: `\(formula\)`
>
>
>
> _Block formulas_
>
> *   Use double dollar signs: `$$formula$$`
> *   Or use `\[formula\]`
> *   Example: `$$\sum_{i=1}^n x_i$$`\
>     $$\sum_{i=1}^n x_i$$

*   Formula rendering errors/garbled text are common when the formula contains Chinese content. Try switching the formula engine to KateX.

***

## Unable to Create Knowledge Base / "Failed to get embedding dimensions" prompt

1.  Model status is unavailable

> Confirm whether the service provider supports the model or if the model's service status is normal.

2.  A non-embedding model was used.

***

## Model Cannot Recognize Images / Unable to Upload or Select Images

First, you need to confirm if the model supports image recognition. Cherry Studio categorizes popular models; those with a small eye icon next to their name support image recognition.

Image recognition models support uploading image files. If the model's functionality is not correctly matched, you can find the model in the corresponding service provider's model list, click the settings button after its name, and check the image option.

For specific model information, you can check the details from the corresponding service provider. Similar to embedding models, models that do not support vision do not need to have the image function forced on; checking the image option will have no effect.