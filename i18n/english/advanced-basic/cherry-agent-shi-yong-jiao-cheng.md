---
icon: robot
---
# Cherry Agent Usage Tutorial


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




Cherry Studio v1.7.0.alpha introduces Agent, allowing the use of Claude Code within Cherry Studio. This tutorial will guide you through the complete setup and launch process.

### 1. Create an Anthropic Type Provider

Any service provider that supports Anthropic endpoints can be used. Taking CherryIn as an example, create a new Agent service provider, fill in the key and address, and add any model. (⚠️Agent mode consumes a large number of tokens, please pay attention to token usage)

> Users who have subscribed to Claude Code can also fill in their key and URL to obtain the model.

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.26.35@2x.png" alt=""><figcaption></figcaption></figure>

### 2. Enable API Server

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 19.56.22@2x.png" alt=""><figcaption></figcaption></figure>

### 3. Create an Agent

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.24.43@2x.png" alt=""><figcaption></figcaption></figure>

Right-clicking on an Agent allows you to enter the editing interface, where you can edit the Agent's permissions and the tools/mcp services it can use.

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.25.10@2x (1).png" alt=""><figcaption></figcaption></figure>

### Results Display

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.30.26@2x (1).png" alt=""><figcaption></figcaption></figure>