
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# MCP কনফিগারেশন এবং ব্যবহার

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1.  Cherry Studio সেটিংস খুলুন।
2.  `MCP সার্ভার` অপশনটি খুঁজুন।
3.  `সার্ভার যোগ করুন` ক্লিক করুন।
4.  MCP সার্ভারের সংশ্লিষ্ট প্যারামিটার পূরণ করুন ([রেফারেন্স লিংক](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch))। প্রয়োজনীয় বিষয়বস্তু অন্তর্ভুক্ত হতে পারে:
    *   নাম: একটি কাস্টম নাম, যেমন `fetch-server`
    *   টাইপ: `STDIO` নির্বাচন করুন
    *   কমান্ড: `uvx` লিখুন
    *   প্যারামিটার: `mcp-server-fetch` লিখুন
    *   (অন্যান্য প্যারামিটার থাকতে পারে, নির্দিষ্ট সার্ভার অনুযায়ী)
5.  `সংরক্ষণ করুন` ক্লিক করুন।

{% hint style="success" %}
উপরোক্ত কনফিগারেশন সম্পন্ন করার পর, Cherry Studio স্বয়ংক্রিয়ভাবে প্রয়োজনীয় MCP সার্ভার - `fetch server` ডাউনলোড করবে। ডাউনলোড সম্পূর্ণ হলে, আমরা এটি ব্যবহার শুরু করতে পারব! লক্ষ্য রাখুন: যদি mcp-server-fetch কনফিগারেশন সফল না হয়, তাহলে কম্পিউটারটি পুনরায় চালু করার চেষ্টা করুন।
{% endhint %}

### চ্যাট বক্সে MCP সার্ভার সক্ষম করুন

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

*   `MCP সার্ভার` সেটিংসে সফলভাবে MCP সার্ভার যোগ করা হয়েছে

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **ব্যবহারের প্রভাব প্রদর্শন**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

উপরের ছবি থেকে দেখা যায়, MCP-এর `fetch` ফিচার সংযুক্ত করার পরে, Cherry Studio ব্যবহারকারীর প্রশ্নের উদ্দেশ্য আরও ভালভাবে বুঝতে পারে এবং ওয়েব থেকে প্রাসঙ্গিক তথ্য আহরণ করে আরও সঠিক এবং বিস্তৃত উত্তর দিতে পারে।