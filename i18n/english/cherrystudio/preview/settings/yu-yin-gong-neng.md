---
hidden: True
icon: phone-arrow-up-right
---
# Voice Features


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




{% hint style="warning" %}
This feature has been shelved due to the relevant developer no longer maintaining the PR.
{% endhint %}

Cherry Studio Voice Feature Usage Guide

## I. Overview of Voice Features

Cherry Studio offers three main voice feature modules: TTS (Text-to-Speech), ASR (Automatic Speech Recognition), and Voice Call. These features allow you to interact naturally with AI through voice, enhancing your user experience.

-   **TTS (Text-to-Speech)**: Converts AI's textual replies into spoken output.
-   **ASR (Automatic Speech Recognition)**: Converts your spoken input into text.
-   **Voice Call**: Combines TTS and ASR to provide a ChatGPT-like voice conversation experience.

## II. TTS (Text-to-Speech) Function

### 1. Supported Service Types

Cherry Studio supports four types of TTS services:

-   **OpenAI**: Uses OpenAI's TTS API, requires an API key.
-   **Browser TTS**: Uses the browser's built-in speech synthesis function, free and requires no configuration.
-   **Siliconflow**: Uses Siliconflow's TTS service, requires an API key.
-   **Free Online TTS**: Uses a free online TTS service, no API key required.

### 2. Setup Method

1.  Go to the settings page and select the "Voice Features" tab.
2.  In the "TTS" sub-tab:
    -   Enable TTS function (turn on the switch).
    -   Select the TTS service type.
    -   Configure parameters according to the selected service type:
        -   **OpenAI**: Fill in API key, API address, select voice and model.
        -   **Browser TTS**: Select voice.
        -   **Siliconflow**: Fill in API key, API address, select voice, model, response format, and speech rate.
        -   **Free Online TTS**: Select voice and output format.
    -   Configure TTS filtering options (optional):
        -   Filter thinking process.
        -   Filter Markdown tags.
        -   Filter code blocks.
    -   Set whether to display the TTS progress bar.
    -   Click the "Test TTS" button to verify if the configuration is correct.

### 3. Usage

-   Once TTS is enabled, AI's replies will automatically be converted into spoken output.
-   In the chat interface, a TTS play button will be displayed below each AI reply.
-   Click the play button to play/pause the audio.
-   If the TTS progress bar is enabled, the playback progress will be displayed below the text.
-   Long texts will be automatically segmented and synthesized for continuous playback.

## III. ASR (Automatic Speech Recognition) Function

### 1. Supported Service Types

Cherry Studio supports three types of ASR services:

-   **OpenAI**: Uses OpenAI's Whisper model, requires an API key.
-   **Browser**: Uses the browser's built-in speech recognition function, free and requires no configuration.
-   **Local Server**: Connects to a local WebSocket server for speech recognition.

### 2. Setup Method

1.  Go to the settings page and select the "Voice Features" tab.
2.  In the "ASR" sub-tab:
    -   Enable ASR function (turn on the switch).
    -   Select the ASR service type.
    -   Configure parameters according to the selected service type:
        -   **OpenAI**: Fill in API key, API address, select model.
        -   **Browser**: No additional configuration required.
        -   **Local Server**: You can set whether to automatically start the ASR server when the application launches.
    -   Select the speech recognition language (default is Chinese).
3.  Click the "Test ASR" button to verify if the configuration is correct.

### 3. Usage

-   Once ASR is enabled, a speech recognition button will appear next to the input box.
-   Click the speech recognition button to start recording.
-   After speaking, your voice will be converted to text and filled into the input box.
-   Click the button again to end recording.
-   Speech recognition supports continuous recognition of multiple sentences in an additive mode.

## IV. Voice Call Function

### 1. Features

-   Combines TTS and ASR to provide a ChatGPT-like voice conversation experience.
-   Uses a draggable floating window interface.
-   Supports "push-to-talk" mode.
-   Supports custom hotkeys.
-   Supports window collapse.
-   Allows selection of a dedicated voice call model.
-   Supports custom prompts.

### 2. Setup Method

1.  Go to the settings page and select the "Voice Features" tab.
2.  In the "Call Function" sub-tab:
    -   Enable the voice call function (turn on the switch).
    -   Click the "Select Model" button to choose an AI model for voice calls.
    -   Customize the voice call prompt in the prompt text box (optional).
    -   Click "Save" to save the prompt, or "Reset" to restore the default prompt.

### 3. Usage

1.  In the chat interface, click the voice call button (phone icon) to the right of the input box.
2.  The voice call window will open and play a welcome message.
3.  Long-press the "Push to Talk" button to start recording (or use the configured hotkey).
4.  Release the button to end recording and send to AI for processing.
5.  AI generates a reply and plays it via TTS.
6.  Use the control buttons in the window:
    -   **Mute/Unmute button**: Controls TTS output.
    -   **Pause/Resume button**: Pauses or resumes the conversation.
    -   **Settings button**: Configures hotkeys.
    -   **Collapse button**: Collapses the window, leaving only the "Push to Talk" row.
7.  Click the close button to end the call.

### 4. Hotkey Settings

1.  In the voice call window, click the settings button.
2.  In the pop-up settings panel, click the hotkey button.
3.  Press the key you want to set (e.g., Spacebar, Shift key, etc.).
4.  Click the "Save" button to save the setting.
5.  To use, press and hold the configured hotkey to start recording, release to end recording and send.

## V. Common Issues and Solutions

### 1. TTS Related Issues

-   **Issue**: TTS cannot play sound.
    **Solution**: Check if TTS is enabled, ensure the correct service type is selected, and all necessary parameters are configured.

-   **Issue**: TTS playback quality is poor.
    **Solution**: Try switching to a different TTS service type or voice.

-   **Issue**: TTS shows an error message during playback.
    **Solution**: Check if the API key is correct and if the network connection is normal.

### 2. ASR Related Issues

-   **Issue**: ASR cannot recognize speech.
    **Solution**: Check if ASR is enabled, ensure the correct service type is selected, and all necessary parameters are configured.

-   **Issue**: ASR recognition accuracy is low.
    **Solution**: Try switching to a different ASR service type, or adjust microphone position and volume.

-   **Issue**: ASR server connection failed.
    **Solution**: Check if the local server is running correctly, or try restarting the application.

### 3. Voice Call Related Issues

-   **Issue**: The voice call window cannot open.
    **Solution**: Check if the voice call function is enabled and ensure that both TTS and ASR functions are correctly configured.

-   **Issue**: Push to talk does not respond.
    **Solution**: Check if microphone permissions have been granted, or try restarting the voice call.

-   **Issue**: AI reply has no voice output.
    **Solution**: Check if TTS is enabled and ensure it is not muted.

## VI. Advanced Settings and Customization Options

### 1. TTS Advanced Settings

-   **Filtering Options**: You can choose to filter the thinking process, Markdown tags, and code blocks for smoother TTS playback.
-   **Progress Bar Display**: You can choose whether to display the TTS progress bar.
-   **Custom Voice and Model**: You can add custom voice and model options.

### 2. ASR Advanced Settings

-   **Auto-start Server**: You can set whether to automatically start the ASR server when the application launches.
-   **Language Selection**: You can choose different speech recognition languages.

### 3. Voice Call Advanced Settings

-   **Custom Prompt**: You can customize the voice call prompt to guide how the AI replies in voice call mode.
-   **Dedicated Model Selection**: You can select a dedicated AI model for voice calls, separate from the model used in the current chat.
-   **Hotkey Customization**: You can set custom hotkeys to control recording.

## VII. Usage Recommendations

### 1. Choose the Right TTS Service:

-   For high-quality speech, OpenAI or Siliconflow are recommended.
-   If you prefer not to configure an API, you can use Browser TTS or Free Online TTS.

### 2. Choose the Right ASR Service:

-   For high accuracy, OpenAI is recommended.
-   If you prefer not to configure an API, you can use the browser's built-in speech recognition.

### 3. Optimize Voice Call Experience:

-   Using headphones can prevent TTS output from being re-captured by ASR.
-   Using it in a quiet environment can improve recognition accuracy.
-   Using custom prompts can make AI replies more suitable for voice playback.

### 4. Adjust Settings According to Your Needs:

-   If you primarily use text communication, you can enable only the TTS function.
-   If you primarily use voice input, you can enable only the ASR function.
-   If you need a complete voice conversation experience, enable the voice call function.

We hope this guide helps you make the most of Cherry Studio's voice features and enjoy a more natural and convenient AI interaction experience!