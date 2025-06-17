
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Custom Providers

Cherry Studio not only integrates mainstream AI model services but also gives you powerful customization capabilities. With the **Custom AI Provider** feature, you can easily connect to any AI model you need.

## Why Do You Need Custom AI Providers?

*   **Flexibility:** No longer limited to the preset list of providers, you are free to choose the AI model that best suits your needs.
*   **Diversity:** Experiment with AI models from various platforms to discover their unique advantages.
*   **Controllability:** Directly manage your API keys and access addresses to ensure security and privacy.
*   **Customization:** Integrate privately deployed models to meet the needs of specific business scenarios.

## How to Add a Custom AI Provider?

You can add your custom AI provider in Cherry Studio in just a few simple steps:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1.  **Open Settings:** In the left navigation bar of the Cherry Studio interface, click "Settings" (the gear icon).
2.  **Go to Model Services:** On the settings page, select the "Model Services" tab.
3.  **Add Provider:** On the "Model Services" page, you will see a list of existing providers. Click the "+ Add" button below the list to open the "Add Provider" pop-up window.
4.  **Fill in Information:** In the pop-up window, you need to fill in the following information:
    *   **Provider Name:** Give your custom provider an easily recognizable name (e.g., MyCustomOpenAI).
    *   **Provider Type:** Select your provider type from the drop-down list. Currently supported types are:
        *   OpenAI
        *   Gemini
        *   Anthropic
        *   Azure OpenAI
5.  **Save Configuration:** After filling in the information, click the "Add" button to save your configuration.

## Configuring a Custom AI Provider

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

After adding a provider, you need to find it in the list and configure its details:

1.  **Enable Status:** On the far right of the custom provider list, there is an enable switch. Turning it on enables this custom service.
2.  **API Key:**
    *   Fill in the API Key provided by your AI service provider.
    *   Click the "Check" button on the right to verify the key's validity.
3.  **API Address:**
    *   Fill in the API access address (Base URL) for the AI service.
    *   Be sure to refer to the official documentation provided by your AI service provider to get the correct API address.
4.  **Model Management:**

    *   Click the "+ Add" button to manually add the model IDs you want to use under this provider, such as `gpt-3.5-turbo`, `gemini-pro`, etc.

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    *   If you are unsure of the specific model names, please refer to the official documentation provided by your AI service provider.
    *   Click the "Manage" button to edit or delete the models that have been added.

## Start Using

After completing the above configuration, you can select your custom AI provider and model in the Cherry Studio chat interface and start conversing with the AI!

## Using vLLM as a Custom AI Provider

vLLM is a fast and easy-to-use LLM inference library, similar to Ollama. Here are the steps to integrate vLLM into Cherry Studio:

1.  **Install vLLM:** Install vLLM by following the official vLLM documentation ([https://docs.vllm.ai/en/latest/getting\_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm # If you use pip
    uv pip install vllm # If you use uv
    ```
2.  **Start the vLLM Service:** Start the service using the OpenAI-compatible interface provided by vLLM. There are two main ways to do this:

    *   Start using `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    *   Start using `uvicorn`

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Ensure the service starts successfully and listens on the default port `8000`. Of course, you can also specify the port number for the vLLM service using the `--port` parameter.

3. **Add vLLM Provider in Cherry Studio:**
   *   Follow the steps described earlier to add a new custom AI provider in Cherry Studio.
   *   **Provider Name:** `vLLM`
   *   **Provider Type:** Select `OpenAI`.
4. **Configure vLLM Provider:**
   *   **API Key:** Since vLLM does not require an API key, you can leave this field blank or fill in any content.
   *   **API Address:** Fill in the API address of the vLLM service. By default, the address is: `http://localhost:8000/` (if you use a different port, please modify it accordingly).
   *   **Model Management:** Add the model name you loaded in vLLM. In the example `python -m vllm.entrypoints.openai.api_server --model gpt2` above, you should enter `gpt2` here.
5. **Start Chatting:** Now, you can select the vLLM provider and the `gpt2` model in Cherry Studio and start chatting with the vLLM-powered LLM!

## Tips and Tricks

*   **Read the Documentation Carefully:** Before adding a custom provider, be sure to carefully read the official documentation of the AI service provider you are using to understand key information such as API keys, access addresses, and model names.
*   **Check the API Key:** Use the "Check" button to quickly verify the validity of the API key to avoid issues caused by an incorrect key.
*   **Pay Attention to the API Address:** The API address may vary for different AI service providers and models. Be sure to fill in the correct address.
*   **Add Models On-Demand:** Please only add the models you will actually use to avoid adding too many unnecessary models.