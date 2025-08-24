---
hidden: True
icon: phone-arrow-up-right
---
# Voice Function


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




{% hint style="warning" %}
This feature has been put on hold because the relevant developers have not continued to maintain the PR.
{% endhint %}

Cherry Studio Voice Function User Guide

I. Overview of Voice Function

Cherry Studio provides three major voice function modules: TTS (Text-to-Speech), ASR (Automatic Speech Recognition), and Voice Call. These features allow you to interact naturally with AI through voice, enhancing your user experience.

- TTS (Text-to-Speech): Converts AI's text replies into speech output.
- ASR (Automatic Speech Recognition): Converts your voice into text input.
- Voice Call: Combines TTS and ASR to achieve a ChatGPT-like voice conversation experience.

II. TTS (Text-to-Speech) Function

1. Supported Service Types

Cherry Studio supports four types of TTS services:

- OpenAI: Uses OpenAI's TTS API, requires an API key.
- Browser TTS: Uses the browser's built-in speech synthesis function, free and requires no configuration.
- Siliconflow: Uses Siliconflow's TTS service, requires an API key.
- Free Online TTS: Uses a free online TTS service, requires no API key.

2. Setup Method

1) Go to the settings page, select the "Voice Function" tab.
2) In the "TTS" sub-tab:
   - Enable TTS function (toggle on).
   - Select TTS service type.
   - Configure corresponding parameters based on the selected service type:
     - OpenAI: Fill in API key, API address, select voice and model.
     - Browser TTS: Select voice.
     - Siliconflow: Fill in API key, API address, select voice, model, response format, and speech rate.
     - Free Online TTS: Select voice and output format.
3) Configure TTS filtering options (optional):
   - Filter thinking process.
   - Filter Markdown tags.
   - Filter code blocks.
4) Set whether to display the TTS progress bar.
5) Click the "Test TTS" button to test if the configuration is correct.

3. Usage Method

- After enabling the TTS function, AI's replies will be automatically converted to speech output.
- In the chat interface, a TTS play button will be displayed below each AI reply.
- Click the play button to play/pause the voice.
- If the TTS progress bar is enabled, the playback progress will be displayed below the text.
- Long texts will be automatically segmented, synthesized, and played continuously.

III. ASR (Automatic Speech Recognition) Function

1. Supported Service Types

Cherry Studio supports three types of ASR services:

- OpenAI: Uses OpenAI's Whisper model, requires an API key.
- Browser: Uses the browser's built-in speech recognition function, free and requires no configuration.
- Local Server: Connects to a local WebSocket server for speech recognition.

2. Setup Method

1) Go to the settings page, select the "Voice Function" tab.
2) In the "ASR" sub-tab:
   - Enable ASR function (toggle on).
   - Select ASR service type.
   - Configure corresponding parameters based on the selected service type:
     - OpenAI: Fill in API key, API address, select model.
     - Browser: No additional configuration required.
     - Local Server: Can set whether to automatically start the ASR server when the application launches.
   - Select speech recognition language (defaults to Chinese).
3) Click the "Test ASR" button to test if the configuration is correct.

3. Usage Method

- After enabling the ASR function, a speech recognition button will be displayed next to the input box.
- Click the speech recognition button to start recording.
- After speaking, your voice will be converted to text and filled into the input box.
- Click the button again to end recording.
- Speech recognition supports continuous recognition of multiple sentences, using an additive mode.

IV. Voice Call Function

1. Features

- Combines TTS and ASR to achieve a ChatGPT-like voice conversation experience.
- Uses a draggable floating window interface.
- Supports push-to-talk (long-press to speak) mode.
- Supports custom hotkeys.
- Supports window collapsing.
- Can select a dedicated voice call model.
- Supports custom prompts.

2. Setup Method

1) Go to the settings page, select the "Voice Function" tab.
2) In the "Call Function" sub-tab:
   - Enable voice call function (toggle on).
   - Click the "Select Model" button to choose the AI model for voice calls.
   - Customize the voice call prompt in the prompt text box (optional).
   - Click the "Save" button to save the prompt, or click the "Reset" button to restore the default prompt.

3. Usage Method

1) In the chat interface, click the voice call button (phone icon) to the right of the input box.
2) The voice call window will open and play a welcome voice.
3) Long-press the "Long-press to speak" button to start recording (or use the configured hotkey).
4) Release the button to end recording and send it to the AI for processing.
5) AI generates a reply and plays it via TTS.
6) Use the control buttons in the window:
   - Mute/Unmute button: Controls TTS output.
   - Pause/Resume button: Pauses or resumes the conversation.
   - Settings button: Configures hotkeys.
   - Collapse button: Collapses the window, leaving only the "long-press to speak" row.
7) Click the close button to end the call.

4. Hotkey Settings

1) In the voice call window, click the settings button.
2) In the pop-up settings panel, click the hotkey button.
3) Press the key you want to set (e.g., Spacebar, Shift key, etc.).
4) Click the "Save" button to save the settings.
5) When using, hold down the set hotkey to start recording, and release to end recording and send.

V. Common Issues and Solutions

1. TTS Related Issues

- Issue: TTS cannot play sound.
  Solution: Check if the TTS function is enabled, and ensure the correct service type is selected and necessary parameters are configured.

- Issue: TTS playback quality is poor.
  Solution: Try changing to a different TTS service type or voice.

- Issue: Error message displayed during TTS playback.
  Solution: Check if the API key is correct and the network connection is normal.

2. ASR Related Issues

- Issue: ASR cannot recognize speech.
  Solution: Check if the ASR function is enabled, and ensure the correct service type is selected and necessary parameters are configured.

- Issue: ASR recognition accuracy is low.
  Solution: Try changing to a different ASR service type, or adjust microphone position and volume.

- Issue: ASR server connection failed.
  Solution: Check if the local server is running properly, or try restarting the application.

3. Voice Call Related Issues

- Issue: Voice call window cannot be opened.
  Solution: Check if the voice call function is enabled, and ensure TTS and ASR functions are correctly configured.

- Issue: Push-to-talk (long-press to speak) does not respond.
  Solution: Check if microphone permissions have been granted, or try restarting the voice call.

- Issue: AI reply has no voice output.
  Solution: Check if the TTS function is enabled and not muted.

VI. Advanced Settings and Customization Options

1. TTS Advanced Settings

- Filtering options: You can choose to filter thinking processes, Markdown tags, and code blocks to make TTS playback smoother.
- Progress bar display: You can choose whether to display the TTS progress bar.
- Custom voice and model: You can add custom voice and model options.

2. ASR Advanced Settings

- Auto-start server: You can set whether to automatically start the ASR server when the application launches.
- Language selection: You can select different speech recognition languages.

3. Voice Call Advanced Settings

- Custom prompt: You can customize the voice call prompt to guide AI's reply style in voice call mode.
- Dedicated model selection: You can select a dedicated AI model for voice calls, separate from the model used for the current conversation.
- Hotkey customization: You can set custom hotkeys to control recording.

VII. Usage Recommendations

1. Choose a suitable TTS service:
   - If pursuing high-quality speech, OpenAI or Siliconflow is recommended.
   - If you don't want to configure an API, you can use Browser TTS or Free Online TTS.

2. Choose a suitable ASR service:
   - If pursuing high accuracy, OpenAI is recommended.
   - If you don't want to configure an API, you can use the browser's built-in speech recognition.

3. Optimize Voice Call Experience:
   - Using headphones can prevent TTS output from being recaptured by ASR.
   - Using in a quiet environment can improve recognition accuracy.
   - Using custom prompts can make AI replies more suitable for voice playback.

4. Adjust settings according to your needs:
   - If primarily using text communication, you can enable only the TTS function.
   - If primarily using voice input, you can enable only the ASR function.
   - If a complete voice conversation experience is desired, enable the voice call function.

We hope this user guide helps you make full use of Cherry Studio's voice features and enjoy a more natural and convenient AI interaction experience!