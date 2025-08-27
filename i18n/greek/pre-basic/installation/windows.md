---
description: Windows 版本安装教程
icon: windows
---

{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}


<think>
We are translating from Chinese to Greek (Ελληνικά). The rules must be strictly followed: translate only the text meant for the user, preserve all Markdown, code blocks, links, image paths, and special tags like {% hint %} and {% embed %}. Keep URLs, file paths, and technical terms unchanged.

Steps:
1. Translate the main headings: "Windows" becomes "Windows" (since it's an OS name, often kept in English, but the rule says to translate textual content. However, in Greek, it's common to use "Windows" as is. But to follow rules, we should translate if it's not a proper noun. However, "Windows" is a product name and should remain. The rules say to preserve GitHub terminology and product names. So we'll keep "Windows".)

   But note: the rule says "Preserve all GitHub-specific terminology (e.g., pull request, fork, commit, repository)" and also URLs, file paths. "Windows" is an OS name, so we can leave it as is. Similarly, "Edge" is a browser name.

   However, the user instruction is to translate to Greek, so we need to translate the textual content. But for product names, they are often left in the original. Since the rule says to preserve GitHub terminology and we are to translate only textual content that will be displayed, and because "Windows" is a brand, we leave it. But the heading is just the word "Windows", which in the context is the OS, so we can write it as "Windows" in Greek? Actually, in Greek, they use "Windows". To be safe, we'll keep it as "Windows".

   Similarly, "Edge" we keep.

2. Translate the hint: 
   "注意：Windows 7系统不支持安装 Cherry Studio。" 
   to Greek: "Σημείωση: Το σύστημα Windows 7 δεν υποστηρίζει την εγκατάσταση του Cherry Studio."

3. The sentence "点击下载选择合适的版本" becomes "Κάντε κλικ για λήψη και επιλέξτε την κατάλληλη έκδοση".

4. The embed URL must remain: {% embed url="https://cherry-ai.com/download" %}

5. The image paths and alt texts: 
   - For alt text: "打开官方网站" becomes "Άνοιγμα επίσημης ιστοσελίδας"
   - The caption: "<p>打开官方网站</p>" becomes "<p>Άνοιγμα επίσημης ιστοσελίδας</p>"
   - Similarly, other alt texts and captions.

6. The note in blockquote: 
   "如果出现浏览器提示文件不被信任等情况选择保留即可" -> "Εάν εμφανιστεί προειδοποίηση του προγράμματος περιήγησης ότι το αρχείο δεν είναι αξιόπιστο, κλικ στην επιλογή 'Διατήρηση'."
   Then "`选择保留` → `信任 Cherry-Studio`" should remain in code, so we don't translate the code inside the backticks? Actually, the rule says: within code blocks, translate comments. But this is in a blockquote and not a code block. The rule says to preserve Markdown formatting. The text inside backticks is inline code, so we should preserve the exact content? The rule says: "the Markdown syntax itself should NOT be translated", and the code within code blocks should have comments translated. But this is inline code and part of the instruction.

   However, the rule says: "code, commands, file names, URLs, version numbers, and other technical syntax ... should remain untranslated". So we leave the inline code as is: "`选择保留` → `信任 Cherry-Studio`". But note: the text inside is in Chinese. The user sees the text. Since the rule says to translate only the textual content that will be displayed, and this inline code is meant to be displayed, we must translate it? But the rule also says to preserve Markdown formatting and that the Markdown syntax should not be translated. The content of the inline code is a command or option that the user should see? In the original, it's showing what the user should click. 

   After re-reading the rules: Rule 3 says "Translate comments within code blocks", but this is not a code block. For other parts, we must translate the textual content. Therefore, we should translate the content inside the inline code? But then it would change the actual text that the user sees in the software? The user might be using a Chinese version of the browser? So if we translate to Greek, we have to change the button labels to Greek? That would be more helpful.

   Alternatively, the rule says: "the code, commands, ... within ... the document should remain untranslated". This part is showing what the user should see on the screen (the button labels). So it's not code or command, it's the text of the button. Therefore, we should translate it? But note that the rule says to preserve technical syntax. The rule is a bit ambiguous.

   Since the overall instruction is to translate the document for Greek users, we should translate the text that the user will read, including the labels that they are supposed to see on the screen? But in reality, if the user's browser is in Greek, the button might say something else. So perhaps we should translate to the expected Greek button labels? 

   However, the rule says: "Translate only the textual content that will be displayed to the user" meaning the document's text. The text inside backticks is displayed as an example of what the button says. So if we are translating the document, we should translate that text as well? But the rule also says to preserve code and commands. Since it's inside backticks, it's treated as code? 

   Let me decide: I think we should translate it because the rule says to translate text that will be displayed to the user. The user is reading the Greek document, so we need to tell them what to click in Greek. We'll translate the content of the inline code? But wait, the rule says: "the Markdown syntax itself should NOT be translated" and the content inside the backticks is part of the code? But the rule doesn't explicitly say. To be safe, let's keep the original for code and only translate when it's clearly a comment? 

   However, the rule 3 specifically applies to code blocks. For inline code, it's not defined. Since the rules say to preserve technical syntax, and the button labels are part of the instruction, we have to translate the entire sentence including the quoted button names? 

   But note the rule 1: "Translate only the textual content that will be displayed to the user". The whole document is to be read by a Greek user, so we translate all the text that is not code or URL. The inline code is just a way to format the button label. So we'll translate the content inside the backticks? 

   However, that might break the formatting because we are changing the text inside the code. Alternatively, we can treat the inline code as a piece of text that must be translated, so we replace the Chinese with Greek and keep it in the same Markdown.

   Given that the rule says to preserve Markdown formatting, and the content of inline code might be considered as a command that should remain (like a button name that is fixed in the software, which might be in English or Chinese)? But in this context, the document is being translated to Greek, so we should change the button labels to the expected Greek terms? 

   I think the safe way is to translate the entire sentence including the button labels. So:

   Original: 
   "如果出现浏览器提示文件不被信任等情况选择保留即可
   >
   > `选择保留` → `信任 Cherry-Studio`"

   Translation:
   "Εάν εμφανιστεί προειδοποίηση του προγράμματος περιήγησης ότι το αρχείο δεν είναι αξιόπιστο, επιλέξτε 'Διατήρηση'.
   >
   > `Επιλογή διατήρησης` → `Εμπιστοσύνη στο Cherry-Studio`"

   But note: the rule 2 says "strictly preserve all Markdown formatting". The Markdown formatting is the backticks and the blockquote. We are only changing the content inside? The rule says the Markdown syntax should not be translated, meaning the symbols, but the content inside can be translated? 

   Since the rule 3 says to translate comments in code blocks, we can infer that other text in the document should be translated, including inline code if it's meant as instruction? 

   Alternatively, we can look at the example: in the previous translation we did for English, we translated the entire document. And in that case, we left links and URLs but translated the text. So we will do the same for Greek.

   Conclusion: we translate the content of the inline code to Greek, but keep the Markdown formatting.

7. The headings and other text: 
   - "打开文件" -> "Άνοιγμα αρχείου"
   - "安装" -> "Εγκατάσταση"
   - Captions: "Edge 浏览器正在下载" -> "Το πρόγραμμα περιήγησης Edge κάνει λήψη"
   - "Edge 下载列表" -> "Λίστα λήψεων του Edge"
   - "软件安装界面" -> "Διεπαφή εγκατά