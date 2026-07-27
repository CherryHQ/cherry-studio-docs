---
icon: cloud
---

# Vertex AI

Cherry Studio V2's built-in Vertex AI template connects to Vertex AI through a Google Cloud **Service Account**. It requires a project ID, location, Service Account client email, and private key; it does not use a Gemini API Key.

V2 can call Gemini models on Vertex AI and select the Vertex Anthropic route for available Claude models. Actual availability depends on the project, location, permissions, and access granted through Model Garden.

{% hint style="info" %}
A Gemini API Key from Google AI Studio cannot be used directly for this configuration. If you only have a Gemini API Key, use the [Google Gemini](google-gemini.md) provider.
{% endhint %}

## Before you begin

Complete the following preparation in Google Cloud:

- Select or create a Google Cloud project;
- Enable billing for the project;
- Enable the Vertex AI API;
- Create a Service Account dedicated to Cherry Studio;
- Grant the account the minimum permissions required to call the target models;
- Create and securely download a Service Account JSON key;
- Confirm a Location where the target model is available.

Google's official quickstart generally requires the caller to have the **Vertex AI User** (`roles/aiplatform.user`) role. Enterprise projects may use custom IAM roles; ask an administrator to grant access according to your organization's policy.

Relevant resources:

- [Vertex AI quickstart](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart)
- [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
- [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)

## Read fields from the JSON key

Cherry Studio currently requires you to enter the following values manually:

| Cherry Studio field | Value in the Service Account JSON or Google Cloud |
| --- | --- |
| Client Email | `client_email` |
| Private Key | `private_key`, including the complete BEGIN/END lines |
| Project ID | `project_id` |
| Location | A Location where the target model is available, such as `us-central1` |

When copying the private key, preserve the original line breaks and the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines.

{% hint style="danger" %}
A Service Account private key is a highly sensitive credential. Do not include the complete JSON, `private_key`, or client configuration page in chat messages, documents, code repositories, or issue screenshots. If exposed, delete the key immediately in Google Cloud and create a new one.
{% endhint %}

## Configure Vertex AI

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**, then select **VertexAI**;
3. Enter the JSON `client_email` value in **Client Email**;
4. Enter the complete `private_key` value in **Private Key**;
5. Enter `project_id` in **Project ID**;
6. Enter a Location where the target model is available in **Location**;
7. Leave the API Host empty;
8. Turn on the provider switch at the top of the page;
9. Add and enable the models you plan to use.

{% hint style="warning" %}
The Vertex AI API Host is generally generated from the project and location, so entering it manually is not recommended. Change it only when you intentionally use a reverse proxy and understand its complete path.
{% endhint %}

## Add and select models

Click **Add** in the model list, review the sync preview, and apply the changes. If the remote endpoint does not return the target model, click **Custom** and enter the model ID from Model Garden or Google's official documentation.

- Gemini models use Google Generate Content capabilities;
- Claude models use the Vertex Anthropic route;
- The model must be available in the current project and Location;
- Third-party models may require additional enablement, authorization, or acceptance of terms;
- The model name, location, and version must all match; do not simply copy a model ID from another project.

The statement in older documentation that Claude was temporarily unsupported no longer applies to V2. However, support for the route in code does not mean your Google Cloud project has access to the model.

## Check the connection

1. Confirm that all four required fields come from the same Service Account and project;
2. Confirm that the Vertex AI API is enabled;
3. Confirm that the Service Account has the required IAM permissions;
4. Select a model that has been added and enabled;
5. Run the connection check;
6. Run the model health check;
7. Return to the chat interface and send a simple message.

If Gemini works but Claude does not, first check whether Claude is available in the current project, location, and Model Garden instead of changing the Gemini configuration.

## Manage multiple projects or locations

If different projects or locations use different credentials, duplicate the VertexAI provider and configure each copy separately:

- Include the project or location in its name;
- Keep only the models available in that environment;
- Do not mix the Service Account from project A with the project ID from project B;
- Validate each copy when rotating keys;
- Use different Service Accounts for production and testing environments.

This reduces the scope of permissions and makes quota, location, and model availability issues easier to distinguish.

## Troubleshooting

### VertexAI is not configured

At least one of the Project ID, Location, Client Email, or Private Key fields is empty. Check that the private key is complete, then allow the setting to save after the field loses focus.

### Response code 401 or authentication failure

The Service Account key is invalid or deleted, the private key format is damaged, or the client email and private key do not match. Verify the fields against the same JSON file.

### Response code 403

The Vertex AI API is not enabled, the Service Account lacks the required IAM permissions, or the target model has not been made available to the project. Check the project, API, and roles in Google Cloud.

### Response code 404 or model not found

The model ID, project, or Location does not match. Check the regions supported by the target model in Model Garden, then update Cherry Studio.

### Response code 429

The current project, location, or model has reached a quota limit. Check quota and usage in the Google Cloud Console.

### Gemini works, but Claude does not

Confirm that the Claude model is available in the current project and location, and use the complete, correct model ID. Vertex AI access for Gemini does not automatically grant access to third-party models.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
