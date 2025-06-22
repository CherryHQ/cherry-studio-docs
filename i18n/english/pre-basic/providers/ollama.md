
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Ollama

Ollama is an excellent open-source tool that allows you to easily run and manage various large language models (LLMs) locally. Cherry Studio now supports Ollama integration, enabling you to interact directly with locally deployed LLMs through the familiar interface without relying on cloud services!

## What is Ollama?

Ollama is a tool that simplifies the deployment and use of large language models (LLMs). It has the following features:

* **Local Operation:** Models run entirely on your local computer without requiring internet connectivity, protecting your privacy and data security.
* **Simple and User-Friendly:** Download, run, and manage various LLMs through simple command-line instructions.
* **Rich Model Selection:** Supports popular open-source models like Llama 2, Deepseek, Mistral, Gemma, and more.
* **Cross-Platform:** Compatible with macOS, Windows, and Linux systems.
* **OpenAPI:** Features OpenAI-compatible interfaces for integration with other tools.

## Why Use Ollama with Cherry Studio?

* **No Cloud Service Needed:** Break free from cloud API quotas and fees, and fully leverage the power of local LLMs.
* **Data Privacy:** All your conversation data remains locally stored with no privacy concerns.
* **Offline Availability:** Continue interacting with LLMs even without an internet connection.
* **Customization:** Choose and configure the most suitable LLMs according to your needs.

## Configuring Ollama in Cherry Studio

### **1. Install and Run Ollama**

First, you need to install and run Ollama on your computer. Follow these steps:

* **Download Ollama:** Visit the [Ollama official website](https://ollama.com/) and download the installation package for your operating system.  
  For Linux systems, you can directly install Ollama by running:
  
    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Install Ollama:** Complete the installation by following the installer instructions.
* **Download Models:** Open a terminal (or command prompt) and use the `ollama run` command to download your desired model. For example, to download the Llama 2 model, run:
  
    ```sh
    ollama run llama3.2
    ```
  
    Ollama will automatically download and run the model.
* **Keep Ollama Running:** Ensure Ollama remains running while using Cherry Studio to interact with its models.

### **2. Add Ollama as a Provider in Cherry Studio**

Next, add Ollama as a custom AI provider in Cherry Studio:

* **Open Settings:** Click on "Settings" (gear icon) in the left navigation bar of Cherry Studio.
* **Access Model Services:** Select the "Model Services" tab in the settings page.
* **Add Provider:** Click "Ollama" in the provider list.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Configure Ollama Provider**

Locate the newly added Ollama provider in the list and configure it in detail:

1. **Enable Status:**
   * Ensure the switch on the far right of the Ollama provider is turned on (indicating enabled status).
2. **API Key:**
   * Ollama typically requires **no API key**. Leave this field blank or enter any content.
3. **API Address:**
   * Enter Ollama's local API address. Normally, this is:
     ```
     http://localhost:11434/
     ```
     Adjust if you've modified the default port.
4. **Keep-Alive Time:** Sets the session retention time in minutes. Cherry Studio will automatically disconnect from Ollama if no new interactions occur within this period to free up resources.
5. **Model Management:**
   * Click "+ Add" to manually add the names of models you've downloaded in Ollama.
   * For example, if you downloaded `llama3.2` via `ollama run llama3.2`, enter `llama3.2` here.
   * Click "Manage" to edit or delete added models.

## Getting Started

After completing the above configurations, select Ollama as the provider and choose your downloaded model in Cherry Studio's chat interface to start conversations with local LLMs!

## Tips and Tricks

* **First-Time Model Execution:** Ollama needs to download model files during initial runs, which may take considerable time. Please be patient.
* **View Available Models:** Run `ollama list` in the terminal to see your downloaded Ollama models.
* **Hardware Requirements:** Running large language models requires substantial computing resources (CPU, RAM, GPU). Ensure your computer meets the model's requirements.
* **Ollama Documentation:** Click the `View Ollama Documentation and Models` link in the configuration page to quickly access Ollama's official documentation.