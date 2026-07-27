---
description: Understand the current status of voice features in Cherry Studio V2 Community Edition and the available alternatives.
hidden: true
icon: phone-arrow-up-right
---

# Voice Features

{% hint style="warning" %}
Cherry Studio V2 Community Edition currently has no built-in voice input, text-to-speech, or real-time voice calling. The TTS, ASR, and voice call settings shown in older documentation are not part of the current `main` version. Do not follow those old instructions.
{% endhint %}

## Current Status

The current Settings pages have no **Voice Features** entry, and the chat input area has no built-in recording or voice call button.

The following capabilities are not currently available in Cherry Studio V2 Community Edition:

- Read AI responses aloud automatically (TTS)
- Convert speech from a microphone into input text (ASR / STT)
- Hold a real-time voice conversation in a floating window
- Configure a voice provider, voice, speaking rate, or speech recognition model
- Assign a dedicated push-to-talk shortcut

You therefore do not need to enter an API key from OpenAI, SiliconFlow, or another voice service for these features, and you will not find corresponding options under **Settings**.

## Audio Attachments Are Not Voice Input

Cherry Studio can recognize common audio file types and lets you attach files in supported contexts. Whether a model can understand the audio depends on the selected model, the provider's protocol, and the model's capabilities.

Uploading an audio file is fundamentally different from using an in-app voice feature:

| Scenario | Current status |
| --- | --- |
| Upload an existing audio file to a model that supports audio input | Depends on the model and provider |
| Record from a microphone and transcribe directly into the input box | Not supported |
| Read model responses aloud automatically | Not supported |
| Hold a continuous voice call with a model | Not supported |

If the model selector or provider does not explicitly indicate audio input support, do not assume that the model can process audio attachments.

## Available Alternatives

For voice input, use the operating system's built-in dictation feature or another transcription tool, then paste the resulting text into Cherry Studio. Availability, shortcuts, and privacy policies depend on the operating system or tool you use.

To have responses read aloud, use an operating system accessibility feature or an external text-to-speech tool. Cherry Studio does not manage these tools' voices, speaking rates, audio storage, or network requests.

{% hint style="info" %}
Before using a third-party dictation, transcription, or text-to-speech service, review its data handling and privacy policy. Do not send sensitive conversations to an untrusted service.
{% endhint %}

## How to Confirm Future Support

If voice features return to the Community Edition, there should be both an accessible interface entry and an official release note. Rely on the **Settings** pages in your current version and [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases), not only on old screenshots or historical pull requests.

If your installed version includes a voice entry not covered here, first verify the version number and installation source, then submit an interface screenshot and reproduction details through [Feedback and Suggestions](../../../question-contact/suggestions.md).
