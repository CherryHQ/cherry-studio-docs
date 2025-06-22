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

I. Overview of Voice Features

Cherry Studio provides three major voice feature modules: TTS (Text to Speech), ASR (Automatic Speech Recognition), and voice call. These features allow you to communicate with AI via voice naturally, enhancing the user experience.

- TTS (Text to Speech): Converts AI's text responses into speech output
- ASR (Automatic Speech Recognition): Transforms your voice into text input
- Voice Call: Combines TTS and ASR to enable ChatGPT-like voice conversation experience

II. TTS (Text to Speech) Feature

1. Supported Service Types

Cherry Studio supports four TTS service types:

- OpenAI: Uses OpenAI's TTS API, requires API key
- Browser TTS: Utilizes browser's built-in speech synthesis, free and requires no configuration
- SiliconFlow: Uses SiliconFlow's TTS service, requires API key
- Free Online TTS: Uses free online TTS services, no API key needed

2. Configuration Methods

1) Go to settings page, select "Voice Features" tab
2) In the "TTS" sub-tab:
   - Enable TTS feature (toggle switch)
   - Select TTS service type
   - Configure parameters according to selected service type:
     - OpenAI: Enter API key, API URL, choose voice and model
     - Browser TTS: Select voice
     - SiliconFlow: Enter API key, API URL, choose voice, model, response format and speech rate
     - Free Online TTS: Select voice and output format
3) Configure TTS filter options (optional):
   - Filter thinking process
   - Filter Markdown tags
   - Filter code blocks
4) Set whether to display TTS progress bar
5) Click "Test TTS" button to verify configuration

3. Usage Guide

- After enabling TTS, AI responses will automatically convert to voice output
- Each AI response shows a TTS play button in chat interface
- Click play button to start/pause speech
- If TTS progress bar is enabled, playback progress shows below text
- Long texts will be segmented and played continuously

III. ASR (Automatic Speech Recognition) Feature

1. Supported Service Types

Cherry Studio supports three ASR service types:

- OpenAI: Uses OpenAI's Whisper model, requires API key
- Browser: Uses browser's built-in speech recognition, free and requires no configuration
- Local Server: Connects to local WebSocket server for speech recognition

2. Configuration Methods

1) Go to settings page, select "Voice Features" tab
2) In the "ASR" sub-tab:
   - Enable ASR feature (toggle switch)
   - Select ASR service type
   - Configure parameters according to selected service type:
     - OpenAI: Enter API key, API URL, select model
     - Browser: No additional configuration required
     - Local Server: Option to auto-start ASR server on application launch
   - Select speech recognition language (default: Chinese)
3) Click "Test ASR" button to verify configuration

3. Usage Guide

- After enabling ASR, a voice recognition button appears next to input box
- Click voice button to start recording
- Speech converts to text and populates input field
- Click again to stop recording
- Supports continuous recognition through cumulative mode

IV. Voice Call Feature

1. Feature Highlights

- Integrates TTS and ASR for ChatGPT-like voice conversation
- Uses draggable floating window interface
- Supports push-to-talk mode
- Supports custom hotkeys
- Supports window collapsing
- Dedicated voice call model selection
- Customizable prompts

2. Configuration Methods

1) Go to settings page, select "Voice Features" tab
2) In the "Call Feature" sub-tab:
   - Enable voice call feature (toggle switch)
   - Click "Select Model" to choose AI model for voice calls
   - Customize voice call prompts in prompt field (optional)
   - Click "Save" to save prompts or "Reset" to restore defaults

3. Usage Guide

1) Click voice call button (phone icon) beside input field in chat interface
2) Voice call window opens with welcome prompt
3) Press and hold "Push-to-Talk" button to start recording (or use hotkey)
4) Release button to end recording and submit to AI
5) AI generates response which plays via TTS
6) Use control buttons:
   - Mute/Unmute: Controls TTS output
   - Pause/Resume: Controls conversation flow
   - Settings: Hotkey configuration
   - Collapse: Minimizes window to show only push-to-talk button
7) Click close button to end call

4. Hotkey Setup

1) Click settings button in voice call window
2) Click hotkey button in settings panel
3) Press desired key (e.g. Space, Shift)
4) Click "Save"
5) Press configured hotkey to start recording, release to send

V. Common Issues & Solutions

1. TTS Related Issues

- Issue: No sound from TTS
  Solution: Verify TTS is enabled, check service configuration and required parameters

- Issue: Poor TTS quality
  Solution: Try different service types or voices

- Issue: Error messages during TTS playback
  Solution: Validate API key and network connection

2. ASR Related Issues

- Issue: ASR not recognizing speech
  Solution: Verify ASR is enabled, check service configuration and required parameters

- Issue: Low ASR accuracy
  Solution: Try different service types or adjust microphone position/volume

- Issue: ASR server connection failure
  Solution: Check local server status or restart application

3. Voice Call Issues

- Issue: Voice call window won't open
  Solution: Verify voice call is enabled, confirm TTS/ASR configuration

- Issue: Push-to-talk unresponsive
  Solution: Check microphone permissions or restart voice call

- Issue: No voice output from AI responses
  Solution: Confirm TTS is enabled and not muted

VI. Advanced Settings & Customization

1. TTS Advanced Settings

- Filter options: Hide thinking process, Markdown, or code blocks for smoother playback
- Progress bar display: Toggle visibility
- Custom voices/models: Add custom options

2. ASR Advanced Settings

- Auto-start server: Set whether ASR server auto-launches with application
- Language selection: Choose recognition languages

3. Voice Call Advanced Settings

- Custom prompts: Personalize AI responses for voice conversations
- Dedicated model selection: Separate model for voice calls
- Custom hotkeys: Personalize recording controls

VII. Usage Recommendations

1. Selecting TTS services:
   - For high quality: Recommend OpenAI or SiliconFlow
   - For no configuration: Use Browser TTS or Free Online TTS

2. Selecting ASR services:
   - For high accuracy: Recommend OpenAI
   - For no configuration: Use browser's speech recognition

3. Optimizing voice calls:
   - Use headphones to prevent ASR from capturing TTS output
   - Use in quiet environments for better recognition
   - Custom prompts make AI responses more voice-friendly

4. Tailoring settings:
   - For text-based conversations: Enable only TTS
   - For voice input: Enable only ASR
   - For full voice interaction: Enable voice call feature

We hope this guide helps you maximize Cherry Studio's voice capabilities for more natural and convenient AI interactions!
```