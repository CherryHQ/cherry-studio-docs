---
icon: seal-question
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Frequently Asked Questions

## Common Error Codes

* **4xx (Client Error Status Codes)**: Generally indicate requests that cannot be completed due to syntax errors, authentication/authorization failures, etc.
* **5xx (Server Error Status Codes)**: Generally indicate server-side errors like server downtime, request timeouts, etc.

| Error Code         | Possible Scenarios                                                                 | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4>      | Request body format error, etc.                                                  | <p>Check error message in chat response or use the <a href="questions.md#console-error-viewing-method">console</a> to view error details, then follow prompts.</p><p><mark style="color:purple;">【Common Case 1】</mark> For Gemini models, card binding may be required;<br><mark style="color:purple;">【Common Case 2】</mark> Data size exceeds limit, common with vision models where image size exceeds provider's request limit;<br><mark style="color:purple;">【Common Case 3】</mark> Added unsupported parameters or incorrect parameter values. Try testing with a clean assistant;<br><mark style="color:purple;">【Common Case 4】</mark> Context exceeds limit - clear context, start new conversation, or reduce context messages.</p> |
| <h4>401</h4>      | Authentication failure: Unsupported model or provider account suspension          | Contact service provider or check account status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>403</h4>      | No permission for requested operation                                             | Follow instructions based on error message in chat response or [console](questions.md#console-error-viewing-method)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <h4>404</h4>      | Requested resource not found                                                      | Check request paths, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <h4>422</h4>      | Semantically invalid request despite correct format                               | Common with JSON semantic errors (e.g., null values; numbers/booleans passed where strings required)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>429</h4>      | Request rate limit reached                                                        | Request rate (TPM/RPM) capped, try again later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <h4>500</h4>      | Internal server error                                                             | Contact service provider if persistent                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>501</h4>      | Server doesn't support requested functionality                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <h4>502</h4>      | Bad Gateway: Invalid response from upstream server                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <h4>503</h4>      | Service Unavailable: Server overloaded/maintenance                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <h4>504</h4>      | Gateway Timeout: Proxy server didn't receive timely response from upstream        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

***

## Console Error Viewing Method

* Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> when focused on Cherry Studio client window (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- Cherry Studio client window must be active to open console
- Console must be opened before making requests (test/dialogue) to collect request info
{% endhint %}

* In console window, click <mark style="color:blue;">`Network`</mark> → locate last entry marked with red <mark style="color:red;">`×`</mark> labeled <mark style="color:red;">`completions`</mark>_(for dialogue/translation/model check errors)_ or <mark style="color:red;">`generations`</mark>_(for image generation errors)_ → click <mark style="color:blue;">`Response`</mark> to view full error message (area ④ in image).

> If unable to diagnose error, screenshot this interface and share in [official community](https://t.me/CherryStudioAI)

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

This method works for dialogue, model testing, knowledge base creation, image generation, etc. Always open console before making requests.

{% hint style="info" %}
Name (area ② in image) varies by scenario:

Dialogue/Translation/Model Check: <mark style="color:red;">`completions`</mark>  
Image Generation: <mark style="color:red;">`generations`</mark>  
Knowledge Base Creation: <mark style="color:red;">`embeddings`</mark>  
{% endhint %}

***

## Formula Not Rendering/Formula Rendering Error

* If formula code displays instead of rendering, check delimiters:

> **Delimiter Usage**  
> _Inline Formulas_  
> * Single dollar sign: `$formula$`
> * Or `\(formula\)`  
> 
> _Formula Blocks_  
> * Double dollar sign: `$$formula$$`
> * Or `\[formula\]`  
> * Example: `$$\sum_{i=1}^n x_i$$`  
>   $$\sum_{i=1}^n x_i$$

* For rendering errors/garbled text (common with Chinese in formulas), try switching rendering engine to KateX.

***

## Unable to Create Knowledge Base/"Failed to Get Embedding Dimensions"

1. Model unavailable  
> Verify provider supports the model and check service status.

2. Used non-embedding model

***

## Model Cannot Recognize Images/Unable to Upload/Select Images

First confirm if the model supports image recognition. Hot models in Cherry Studio are categorized - models with an eye icon after the name support image recognition.

Image-capable models support file uploads. If model features aren't matched correctly:  
- Go to provider's model list  
- Click settings icon next to model name  
- Enable image option  

Check model details on provider's page. Vision-incompatible models won't benefit from enabling image options.