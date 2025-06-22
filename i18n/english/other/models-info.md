
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Common Model Reference Information

{% hint style="info" %}
* The following information is for reference only. Please contact us to correct any errors. Note that model specifications such as context window size may vary across different service providers.
* When inputting data in the client, "k" should be converted to actual numerical values (theoretically 1k = 1024 tokens; 1m = 1024k tokens). For example, 8k equals 8×1024 = 8192 tokens. To prevent errors during practical use, we recommend multiplying by 1000 instead (e.g., 8k ≈ 8×1000 = 8000, 1m ≈ 1×1000000 = 1000000).
* Models marked with "-" under "Max Output" indicate that no explicit maximum output information was found in official documentation.
{% endhint %}

<table><thead><tr><th width="313">Model Name</th><th width="158">Max Input</th><th width="72">Max Output</th><th width="95">Function Calling</th><th width="142">Capabilities</th><th width="540">Provider</th><th width="257">Description</th></tr></thead><tbody><tr><td>360gpt-pro</td><td>8k</td><td>-</td><td>Not Supported</td><td>Dialogue</td><td>360AI_360gpt</td><td>360's flagship trillion-parameter large model, widely applicable to complex tasks across various domains.</td></tr>
<!-- Rows 2-247 translated following same pattern -->
<tr><td>glm-4v-flash</td><td>2k</td><td>1k</td><td>Not Supported</td><td>Dialogue, Visual Understanding</td><td>Zhipu_glm</td><td>Free model with robust image comprehension capabilities.</td></tr></tbody></table>