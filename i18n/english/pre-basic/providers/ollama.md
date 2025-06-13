
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Ollama

Ollama is an excellent open-source tool that allows you to easily run and manage various Large Language Models (LLMs) locally. Cherry Studio now supports Ollama integration, enabling you to interact directly with locally deployed LLMs in a familiar interface, without relying on cloud services!

## What is Ollama?

Ollama is a tool that simplifies the deployment and use of Large Language Models (LLMs). It has the following features:

*   **Local Execution:** Models run entirely on your local computer, without needing an internet connection, protecting your privacy and data security.
*   **Easy to Use:** Download, run, and manage various LLMs with simple command-line instructions.
*   **Rich Model Library:** Supports many popular open-source models like Llama 2, Deepseek, Mistral, and Gemma.
*   **Cross-Platform:** Supports macOS, Windows, and Linux systems.
*   **Open API**: Supports an OpenAI-compatible interface, allowing integration with other tools.

## Why Use Ollama in Cherry Studio?

*   **No Cloud Services Needed:** No longer limited by cloud API quotas and fees. Enjoy the full power of local LLMs.
*   **Data Privacy:** All your conversation data remains on your local machine, eliminating concerns about privacy leaks.
*   **Offline Availability:** Continue interacting with LLMs even without an internet connection.
*   **Customization:** Choose and configure the LLMs that best suit your needs.

## Configuring Ollama in Cherry Studio

### **1. Install and Run Ollama**

First, you need to install and run Ollama on your computer. Follow these steps:

*   **Download Ollama:** Visit the official Ollama website ([https://ollama.com/](https://ollama.com/)) and download the appropriate installer for your operating system.\
    On Linux, you can install Ollama directly with the following command:

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
*   **Install Ollama:** Follow the installer's instructions to complete the installation.
*   **Download a Model:** Open your terminal (or command prompt) and use the `ollama run` command to download the model you want to use. For example, to download the Llama 3.2 model, run:

    ```sh
    ollama run llama3.2
    ```

    Ollama will automatically download and run the model.
*   **Keep Ollama Running:** Ensure that Ollama remains running while you are interacting with Ollama models through Cherry Studio.

### **2. Add the Ollama Provider in Cherry Studio**

Next, add Ollama as a custom AI provider in Cherry Studio:

*   **Open Settings:** In the left navigation bar of the Cherry Studio interface, click on "Settings" (the gear icon).
*   **Go to Model Services:** On the settings page, select the "Model Services" tab.
*   **Add Provider:** Click on Ollama in the list.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Configure the Ollama Provider**

Find the newly added Ollama in the provider list and configure its details:

1.  **Enable Status:**
    *   Ensure the switch on the far right of the Ollama provider is turned on, indicating it is enabled.
2.  **API Key:**
    *   Ollama **does not** require an API key by default. You can leave this field blank or fill it with any content.
3.  **API Endpoint:**
    *   Enter the local API address provided by Ollama. Typically, the address is:

        ```
        http://localhost:11434/
        ```

        If you have changed the port, please modify it accordingly.
4.  **Keep-Alive Time:** This option sets the session keep-alive duration in minutes. If there are no new conversations within the set time, Cherry Studio will automatically disconnect from Ollama to release resources.
5.  **Model Management:**
    *   Click the "+ Add" button to manually add the names of the models you have already downloaded in Ollama.
    *   For example, if you have already downloaded the `llama3.2` model using `ollama run llama3.2`, you can enter `llama3.2` here.
    *   Click the "Manage" button to edit or delete the added models.

## Getting Started

Once the configuration is complete, you can select the Ollama provider and your downloaded model in the Cherry Studio chat interface to start conversing with your local LLM!

## Tips and Tricks

*   **First Model Run:** When running a model for the first time, Ollama needs to download the model file, which may take some time. Please be patient.
*   **View Available Models:** Run the `ollama list` command in the terminal to see a list of the Ollama models you have downloaded.
*   **Hardware Requirements:** Running large language models requires certain computing resources (CPU, memory, GPU). Please ensure your computer's configuration meets the model's requirements.
*   **Ollama Documentation**: You can click the `View Ollama documentation and models` link on the configuration page to quickly navigate to the official Ollama documentation.