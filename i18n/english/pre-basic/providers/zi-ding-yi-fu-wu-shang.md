
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Custom Providers

Cherry Studio not only integrates mainstream AI model services but also empowers you with powerful customization capabilities. Through the **Custom AI Providers** feature, you can easily integrate any AI model you require.

## Why Do You Need Custom AI Providers?

* **Flexibility:** Break free from predefined provider lists and freely choose the AI models that best suit your needs.
* **Diversity:** Experiment with various AI models from different platforms to discover their unique advantages.
* **Controllability:** Directly manage your API keys and access addresses to ensure security and privacy.
* **Customization:** Integrate privately deployed models to meet the demands of specific business scenarios.

## How to Add a Custom AI Provider?

Add your custom AI provider to Cherry Studio in just a few simple steps:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Open Settings:** Click the "Settings" (gear icon) in the left navigation bar of the Cherry Studio interface.
2. **Enter Model Services:** Select the "Model Services" tab in the settings page.
3. **Add Provider:** On the "Model Services" page, you'll see existing providers. Click the "+ Add" button below the list to open the "Add Provider" pop-up.
4. **Fill in Information:** In the pop-up, provide the following details:
   * **Provider Name:** Give your custom provider a recognizable name (e.g., MyCustomOpenAI).
   * **Provider Type:** Select your provider type from the dropdown menu. Currently supports:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Save Configuration:** After filling in the details, click the "Add" button to save your configuration.

## Configuring Custom AI Providers

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

After adding, locate your newly added provider in the list and configure it:

1. **Activation Status:** Toggle the activation switch on the far right of the list to enable this custom service.
2. **API Key:**
   * Enter the API key provided by your AI provider.
   * Click the "Test" button to verify the key's validity.
3. **API Address:**
   * Enter the base URL to access the AI service.
   * Always refer to your AI provider's official documentation for the correct API address.
4. **Model Management:**
   * Click the "+ Add" button to manually add model IDs you want to use under this provider (e.g., `gpt-3.5-turbo`, `gemini-pro`).

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    * If unsure about specific model names, consult your AI provider's official documentation.
    * Click the "Manage" button to edit or delete added models.

## Getting Started

After completing the above configurations, you can select your custom AI provider and model in Cherry Studio's chat interface and start conversing with AI!

## Using vLLM as a Custom AI Provider

vLLM is a fast and easy-to-use LLM inference library similar to Ollama. Here's how to integrate vLLM into Cherry Studio:

1. **Install vLLM:** Follow vLLM's official documentation ([https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)) to install vLLM.

    ```sh
    pip install vllm # if using pip
    uv pip install vllm # if using uv
    ```
2. **Launch vLLM Service:** Start the service using vLLM's OpenAI-compatible interface via two main methods:

    * Using `vllm.entrypoints.openai.api_server`
    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Using `uvicorn`
    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Ensure the service launches successfully, listening on the default port `8000`. You can also specify a different port using the `--port` parameter.

3. **Add vLLM Provider in Cherry Studio:**
   * Follow the steps above to add a new custom AI provider.
   * **Provider Name:** `vLLM`
   * **Provider Type:** Select `OpenAI`.
4. **Configure vLLM Provider:**
   * **API Key:** Leave this field blank or enter any value since vLLM doesn't require an API key.
   * **API Address:** Enter vLLM's API address (default: `http://localhost:8000/`, adjust if using a different port).
   * **Model Management:** Add the model name loaded in vLLM (e.g., `gpt2` for the command `python -m vllm.entrypoints.openai.api_server --model gpt2`).
5. **Start Chatting:** Now select the vLLM provider and the `gpt2` model in Cherry Studio to chat with the vLLM-powered LLM!

## Tips and Tricks

* **Read Documentation Carefully:** Before adding custom providers, thoroughly review your AI provider's official documentation for API keys, addresses, model names, etc.
* **Test API Keys:** Use the "Test" button to quickly verify API key validity.
* **Verify API Addresses:** Different providers and models may have varying API addresses—ensure correctness.
* **Add Models Judiciously:** Only add models you'll actually use to avoid cluttering.