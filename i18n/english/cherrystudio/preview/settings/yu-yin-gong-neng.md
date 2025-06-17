---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Voice Features

```
Cherry Studio Voice Features User Guide

I. Voice Feature Overview

Cherry Studio provides three major voice feature modules: TTS (Text-to-Speech), ASR (Automatic Speech Recognition), and Voice Call. These features allow you to communicate naturally with the AI via voice, enhancing your user experience.

- TTS (Text-to-Speech): Converts AI-generated text responses into speech output.
- ASR (Automatic Speech Recognition): Converts your voice into text input.
- Voice Call: Combines TTS and ASR to provide a voice conversation experience similar to ChatGPT.

II. TTS (Text-to-Speech) Functionality

1. Supported Service Types

Cherry Studio supports four types of TTS services:

- OpenAI: Uses OpenAI's TTS API, requires an API key.
- Browser TTS: Uses the browser's built-in speech synthesis feature, free and requires no configuration.
- Siliconflow: Uses the TTS service from Siliconflow, requires an API key.
- Free Online TTS: Uses a free online TTS service, no API key required.

2. Setup Instructions

1) Go to the Settings page and select the "Voice Features" tab.
2) In the "TTS" sub-tab:
   - Enable the TTS feature (toggle the switch on).
   - Select the TTS Service Type.
   - Configure the corresponding parameters based on the selected service type:
     - OpenAI: Fill in the API Key, API Address, and select the voice and model.
     - Browser TTS: Select the voice.
     - Siliconflow: Fill in the API Key, API Address, and select the voice, model, response format, and speed.
     - Free Online TTS: Select the voice and output format.
3) Configure TTS filtering options (optional):
   - Filter thought processes.
   - Filter Markdown tags.
   - Filter code blocks.
4) Set whether to display the TTS progress bar.
5) Click the "Test TTS" button to check if the configuration is correct.

3. How to Use

- After enabling the TTS feature, AI responses will automatically be converted to speech output.
- In the chat interface, a TTS play button will appear below each AI response.
- Click the play button to play/pause the speech.
- If the TTS progress bar is enabled, the playback progress will be displayed below the text.
- Long texts will be automatically synthesized in segments and played back continuously.

III. ASR (Automatic Speech Recognition) Functionality

1. Supported Service Types

Cherry Studio supports three types of ASR services:

- OpenAI: Uses OpenAI's Whisper model, requires an API key.
- Browser: Uses the browser's built-in speech recognition feature, free and requires no configuration.
- Local Server: Connects to a local WebSocket server for speech recognition.

2. Setup Instructions

1) Go to the Settings page and select the "Voice Features" tab.
2) In the "ASR" sub-tab:
   - Enable the ASR feature (toggle the switch on).
   - Select the ASR Service Type.
   - Configure the corresponding parameters based on the selected service type:
     - OpenAI: Fill in the API Key, API Address, and select the model.
     - Browser: No additional configuration needed.
     - Local Server: You can configure whether to automatically start the ASR server when the application launches.
   - Select the speech recognition language (defaults to Chinese).
3) Click the "Test ASR" button to check if the configuration is correct.

3. How to Use

- After enabling the ASR feature, a speech recognition button will appear next to the input box.
- Click the speech recognition button to start recording.
- After you speak, your voice will be converted to text and inserted into the input box.
- Click the button again to stop recording.
- Speech recognition supports continuous recognition of multiple sentences in an additive mode.

IV. Voice Call Functionality

1. Features

- Combines TTS and ASR to provide a voice conversation experience similar to ChatGPT.
- Uses a draggable floating window interface.
- Supports press-and-hold-to-talk mode.
- Supports customizable hotkeys.
- Supports window collapse/expand.
- Allows selection of a dedicated voice call model.
- Supports custom prompts.

2. Setup Instructions

1) Go to the Settings page and select the "Voice Features" tab.
2) In the "Call Feature" sub-tab:
   - Enable the voice call feature (toggle the switch on).
   - Click the "Select Model" button to choose the AI model for voice calls.
   - Customize the voice call prompt in the prompt text box (optional).
   - Click the "Save" button to save the prompt, or the "Reset" button to restore the default prompt.

3. How to Use

1) In the chat interface, click the voice call button (phone icon) to the right of the input box.
2) The voice call window will open and play a welcome message.
3) Press and hold the "Press and Hold to Talk" button to start recording (or use the configured hotkey).
4) Release the button to stop recording and send the audio to the AI for processing.
5) The AI generates a response and plays it back via TTS.
6) Use the control buttons in the window:
   - Mute/Unmute button: Controls TTS output.
   - Pause/Resume button: Pauses or resumes the conversation.
   - Settings button: Configures hotkeys.
   - Collapse button: Collapses the window, leaving only the "Press and Hold to Talk" bar visible.
7) Click the close button to end the call.

4. Hotkey Settings

1) In the voice call window, click the settings button.
2) In the settings panel that appears, click the hotkey button.
3) Press the key you want to set (e.g., Spacebar, Shift key).
4) Click the "Save" button to save the setting.
5) To use, press and hold the set hotkey to start recording, and release it to stop recording and send.

V. FAQ and Solutions

1. TTS-related Issues

- Issue: TTS playback has no sound.
  Solution: Check if the TTS feature is enabled, and ensure the correct service type and necessary parameters are configured.

- Issue: Poor TTS playback quality.
  Solution: Try switching to a different TTS service type or voice.

- Issue: Error message displayed during TTS playback.
  Solution: Check if the API key is correct and if the network connection is stable.

2. ASR-related Issues

- Issue: ASR cannot recognize speech.
  Solution: Check if the ASR feature is enabled, and ensure the correct service type and necessary parameters are configured.

- Issue: Low ASR recognition accuracy.
  Solution: Try switching to a different ASR service type, or adjust your microphone's position and volume.

- Issue: ASR server connection failed.
  Solution: Check if the local server is running correctly, or try restarting the application.

3. Voice Call-related Issues

- Issue: The voice call window won't open.
  Solution: Check if the voice call feature is enabled, and ensure that the TTS and ASR features are configured correctly.

- Issue: "Press and Hold to Talk" is unresponsive.
  Solution: Check if microphone permissions have been granted, or try restarting the voice call.

- Issue: The AI response has no voice output.
  Solution: Check if the TTS feature is enabled and ensure it is not muted.

VI. Advanced Settings and Customization Options

1. Advanced TTS Settings

- Filtering Options: You can choose to filter thought processes, Markdown tags, and code blocks to make TTS playback smoother.
- Progress Bar Display: You can choose whether to display the TTS progress bar.
- Custom Voices and Models: You can add custom voice and model options.

2. Advanced ASR Settings

- Auto-start Server: You can set whether the ASR server should start automatically when the application launches.
- Language Selection: You can choose different speech recognition languages.

3. Advanced Voice Call Settings

- Custom Prompts: You can customize the voice call prompt to guide how the AI responds in voice call mode.
- Dedicated Model Selection: You can select a specific AI model for voice calls, separate from the model used in the current conversation.
- Hotkey Customization: You can set custom hotkeys to control recording.

VII. Usage Suggestions

1. Choose the right TTS service:
   - If you are looking for high-quality speech, we recommend using OpenAI or Siliconflow.
   - If you prefer not to configure an API, you can use Browser TTS or Free Online TTS.

2. Choose the right ASR service:
   - For high accuracy, we recommend using OpenAI.
   - If you prefer not to configure an API, you can use the browser's built-in speech recognition.

3. Optimize the voice call experience:
   - Using headphones can prevent the TTS output from being captured again by the ASR.
   - Using the feature in a quiet environment can improve recognition accuracy.
   - Using custom prompts can make AI responses more suitable for voice playback.

4. Adjust settings according to your needs:
   - If you primarily use text-based communication, you can enable only the TTS feature.
   - If you primarily use voice input, you can enable only the ASR feature.
   - For a complete voice conversation experience, enable the voice call feature.

We hope this guide helps you make full use of Cherry Studio's voice features and enjoy a more natural and convenient AI interaction experience!
```