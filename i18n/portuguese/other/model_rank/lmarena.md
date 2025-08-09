
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}


<think>
We are translating a Chinese document to Portuguese, strictly following the translation rules.
 Key points from the rules:
 1. Translate only textual content displayed to users, preserving all Markdown formatting.
 2. Do not translate Markdown syntax (headings, lists, code blocks, etc.), links, image paths, URLs, version numbers, or technical syntax in code blocks.
 3. Translate comments within code blocks (but there are no code blocks with comments in this text?).
 4. Preserve links and image paths unchanged.
 5. Maintain GitBook-style hint blocks (translate content inside, but not the tags).
 6. Keep Frontmatter unchanged (not present here).
 7. Do not add any extra explanations.
 8. If it were a table of contents, we would translate only the titles, but the given document is a leaderboard.
 9. Preserve GitHub-specific terminology (e.g., pull request, fork, etc.) in original English.
10. Preserve URLs, file paths, version numbers exactly.

 Structure of the document:
 - Title: # LLM Arena 排行榜 (实时更新)
 - Paragraph: "这是一个基于 Chatbot Arena (lmarena.ai) 数据的排行榜，通过自动化流程生成。"
 - Blockquote: "> **数据更新时间**: ..."
 - Hint block (style="info"): with a note about clicking model names.
 - Table: with headers and rows of model data. We must not alter the table structure, and the content in the table that is not a link or technical term should be translated? Let's see the rules.

 However, note the table:
   - The headers are: "排名(UB)", "排名(StyleCtrl)", "模型名", "分数", "置信区间", "票数", "服务商", "许可协议", "知识截止日期"
   - The rows contain: numbers, model names (which are links), scores, confidence intervals (e.g., "+5/-5"), vote counts, provider names, license types, and knowledge cutoff dates.

 Rule 3 says to translate comments in code blocks, but this table is not in a code block? It's a Markdown table.

 We must translate the headers and the explanatory notes, but the content in the table that is user-readable should also be considered? However, note:
   - The model names are links: the link text might be in English? Actually, the model names are in English (like "Gemini-2.5-Pro") and we should not translate model names, as they are technical identifiers.
   - The providers are in English? Actually, they are company names (e.g., Google, OpenAI) that are proper nouns and should remain in English.
   - License types: some are in English (like "Proprietary", "MIT") and should not be translated. But there are also some in Chinese? Actually, look: "专有" is Chinese for proprietary. We need to translate the license terms that are in Chinese? But in the table, we see both English and Chinese. We must translate the Chinese terms to Portuguese? And leave the English ones as they are.

 However, note the rule: we must preserve GitHub-specific terminology and technical terms. Also, the rule says to preserve all URLs, file paths, and version numbers. The license terms are fixed terms and should be kept as in the original? Or should we translate only when they are written in Chinese? For example, the original has:
   - "Proprietary" (English) -> should remain "Proprietary"
   - "专有" (Chinese for proprietary) -> should be translated to Portuguese? But note, in the Chinese table, they use both: some licenses are written in English, some in Chinese. We should translate the Chinese license terms to Portuguese, and leave the English ones? However, the rule also says to preserve the table structure and data.

 But the rule says: "Translate only the textual content that will be displayed to the user." and "strictly preserve all Markdown formatting and structural elements".

 Let's clarify: the rule says to translate the text, but not the Markdown. The table data are text that the user will read. However, for the table, the model names and the provider names are proper nouns? And the confidence interval is a number/format? We must translate:
   - The headers: translate from Chinese to Portuguese.
   - The non-technical data: for example, the license field: if it's in Chinese ("专有"), translate to Portuguese. If it's in English, leave it? 

 But note: the rule says "Preserve all GitHub-specific terminology (e.g., pull request, fork, commit, repository) in its original form." and "Preserve all URLs, file paths, and version numbers". Also, the model names and providers are specific terms? And the license names are standardized? 

 Actually, in the input table, we see:
   - For "许可协议", there are values: "Proprietary", "MIT", "专有", ... 
   - We should translate "专有" to Portuguese, because it is a Chinese word. The others are English and should remain? But then the table becomes mixed. However, the goal is to translate the document to Portuguese. 

 Decision: 
   - For the table, we will translate:
        * Headers: translate to Portuguese.
        * Values: 
            - Numbers and confidence intervals (like "1470", "+5/-5") remain as is.
            - Vote counts remain as numbers.
            - Model names: are links and the text is English? So we leave the link text as is? But note, the model names are in English even in the Chinese version? Actually, they are in English. So no need to change.
            - Provider names: they are in English? Not translated? Actually, they are company names that are known in English (e.g., Google, Meta) and should remain in English. But some might be in Chinese? Actually, in the table, we see "Google", "Meta", "Alibaba", "Z.ai" (which is English), etc. So no change for provider.
            - License: translate the Chinese entries to Portuguese. For the English ones, we leave? The problem is that the user expects the entire document to be in Portuguese. Therefore, if the license field is a common term, we should use the Portuguese equivalent? But note: the context is open source and proprietary licenses, and these terms are often kept in English? However, the rule does allow translating if they are in the source language? 

 Let me check the rule again: "Translate only the textual content that will be displayed to the user." and it says to preserve technical terms? The license terms are technical. However, the source mixes English and Chinese. To be consistent, we can translate the Chinese license terms to Portuguese, and leave the ones that are in English? But it might look inconsistent? Alternatively, we translate all to Portuguese? For example:
    "Proprietary" -> "Proprietário"
    "MIT" remains "MIT" (acronyms are the same)?
    "专有" -> "Proprietário"

 But the rule says "Preserve GitHub-specific terminology". License are not GitHub-specific? They are common. Also, the rule does not explicitly say to preserve license terms? So I think we should translate the textual content, including translating the Chinese license terms to Portuguese. The English ones we can leave if they are acronyms or well-known? But for consistency and to avoid a mix of languages, we can translate all? Actually, the rule says "fluently translate Chinese documents", meaning the target is Portuguese. So the entire document, including the table, should be in Portuguese, except for the parts that are preserved like URLs. But note, the rule says to preserve the table structure and to preserve links. The text in the table that is in English is part of the content? However, it is not Chinese? How should we treat?

 Another approach: the rule says we only translate the Chinese content? So we leave everything that is in English? In the document, the table has both Chinese and English? Actually, the license and the knowledge cutoff date have mixed: sometimes English (like "nan", "Proprietary") and sometimes Chinese (like "专有", "暂无数据").

 How about:
    - For the knowledge cutoff date: if it says "暂无数据", we translate to Portuguese. The "2023/10" remains? The "nan" remains? 
    - For the license: if it says "专有", translate to Portuguese. If it's in English, leave? But then the user will see a mix of English and Portuguese? 

 Alternatively, we can standardize the terms in the table? But the rule says to preserve the technical terms? So let's do:

    Knowledge cutoff date: 
        "暂无数据" -> "Sem dados" (or similar) in Portuguese.
        Everything else (like "2023/10", "nan") remains.

    License:
        "专有" -> "Proprietário"
        "暂无数据" doesn't appear in license? We see "Proprietary", "MIT", "Apache 2.0", ... and also "nan". So:
            "Proprietary" -> remains? Or is it a common term? Actually, we can translate to Portuguese? But it's the license name? The rule says preserve as is? 

 Given the rule: "Preserve all URLs, file paths, and version numbers". The license terms are not URLs? They are textual and should be translated? But they are standard names? I think the safest is to leave the license terms as they are? Because they are standardized? And translate only the Chinese ones? 

 However, the rule says: "Translate only the textual content". And the entire document should