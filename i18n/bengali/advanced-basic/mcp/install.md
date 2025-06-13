
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# MCP পরিবেশ ইনস্টলেশন

**MCP (Model Context Protocol)** হল একটি ওপেন-সোর্স প্রোটোকল যা বড় ভাষা মডেল (LLM) কে প্রমিত উপায়ে প্রসঙ্গ তথ্য প্রদান করার জন্য ডিজাইন করা হয়েছে। MCP সম্পর্কে আরও জানতে দেখুন [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Cherry Studio এ MCP ব্যবহার

`fetch` ফাংশনের উদাহরণের মাধ্যমে Cherry Studio তে MCP ব্যবহারের পদ্ধতি দেখানো হলো। বিস্তারিত [ডকুমেন্টেশন](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) এ পাওয়া যাবে।

### **প্রস্তুতি: UV এবং Bun ইনস্টল করুন**

{% hint style="warning" %}
Cherry Studio বর্তমানে শুধুমাত্র অন্তর্নির্মিত [UV](https://github.com/astral-sh/uv) এবং [Bun](https://github.com/oven-sh/bun) ব্যবহার করে। এটি সিস্টেমে পূর্বে ইনস্টল করা UV/Bun **পুনরায় ব্যবহার করবে না**।
{% endhint %}

`সেটিংস > MCP সার্ভার` তে `ইনস্টল` বাটনে ক্লিক করলে এটি স্বয়ংক্রিয়ভাবে ডাউনলোড ও ইনস্টল হবে। GitHub সরাসরি ডাউনলোডের কারণে গতি ধীর হতে পারে এবং ব্যর্থতার সম্ভাবনা বেশি। ইনস্টল সফল কিনা তা নিচে উল্লিখিত ফোল্ডারে ফাইল উপস্থিতি দ্বারা যাচাই করুন।

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**এক্সিকিউটেবল ফাইল ইনস্টল ডিরেক্টরি:**

Windows: `C:\Users\ব্যবহারকারীর নাম\.cherrystudio\bin`

macOS ও Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>bin ডিরেক্টরি</p></figcaption></figure>

**ইনস্টলেশনে সমস্যা হলে:**

আপনার সিস্টেমের কমান্ডগুলো সফট লিংকের মাধ্যমে এই পাথে সংযোগ করতে পারেন। ডিরেক্টরি না থাকলে নিজে তৈরি করুন। অথবা ম্যানুয়ালি নিচের লিংক থেকে ডাউনলোড করে এই ডিরেক্টরিতে রাখুন:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)