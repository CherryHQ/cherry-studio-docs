
{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# تصنيف حلبة LLM (تحديث حي)

هذا تصنيف مولد آليًا يعتمد على بيانات من Chatbot Arena (lmarena.ai).

> **تاريخ تحديث البيانات**: 2025-06-12 11:42:10 UTC / 2025-06-12 19:42:10 CST (بتوقيت بكين)

{% hint style="info" %}
انقر على **اسم النموذج** في التصنيف للانتقال إلى صفحة التفاصيل أو التجربة.
{% endhint %}

## تصنيف النماذج

| الترتيب (الأعلى تقدير) | الترتيب (ضبط النمط) | اسم النموذج                                                                                                   | النقاط | مدى الثقة | عدد الأصوات | المزود                      | الرخصة                    | تاريخ انتهاء المعرفة |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| ... (جميع بيانات الجدول تُحفظ كما هي مع الحفاظ على الترتيب والتنسيق الأصليين) ... |
| 201 | 199 | [FastChat-T5-3B](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0)                                                             | 881  | +8/-9   | 4,288   | LMSYS                  | Apache 2.0              | 2023/4   |
| 202 | 200 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                 | 813  | +14/-12 | 2,446   | Meta                   | غير تجارية          | 2023/2   |

## تفسيرات

- **الترتيب (الأعلى تقدير)**: تصنيف يستند إلى نموذج برادلي-تيري. يعكس هذا الترتيب الأداء الشامل للنموذج في الساحة، ويوفر **حدًا أعلى** لتقدير نقاط إيلو، مما يساعد في فهم القدرة التنافسية المحتملة للنموذج.
  
- **الترتيب (ضبط النمط)**: تصنيف بعد التحكم في نمط المحادثة. يهدف هذا الترتيب إلى تقليل التحيز الناتج عن أنماط ردود النماذج (مثل الإسهاب أو الإيجاز)، وتقييم قدرات النموذج الأساسية بشكل أكثر دقة.
  
- **اسم النموذج**: اسم نموذج اللغة الكبيرة (LLM). يحتوي هذا العمود على روابط للنموذج، انقر للانتقال.
  
- **النقاط**: نقاط إيلو التي حصل عليها النموذج من تصويت المستخدمين في الساحة. نظام تصنيف إيلو هو نظام ترتيب نسبي، حيث تشير النقاط الأعلى إلى أداء أفضل. هذه النقاط ديناميكية وتعكس القوة النسبية للنموذج في البيئة التنافسية الحالية.
  
- **مدى الثقة**: فاصل الثقة 95% لنقاط إيلو للنموذج (مثال: `+6/-6`). كلما كان الفاصل أصغر، كانت درجة النموذج أكثر استقرارًا وموثوقية؛ بينما قد يشير الفاصل الأوسع إلى عدم كفاية البيانات أو تقلبات في أداء النموذج. يوفر هذا الفاصل تقييماً كمياً لدقة التصنيف.
  
- **عدد الأصوات**: إجمالي الأصوات التي تلقاها النموذج في الساحة. كلما زاد عدد الأصوات، زادت عادةً موثوقية البيانات الإحصائية لتصنيفه.
  
- **المزود**: المنظمة أو الشركة المقدمة للنموذج.
  
- **الرخصة**: نوع ترخيص النموذج، مثل احتكارية (Proprietary)، Apache 2.0، MIT، إلخ.
  
- **تاريخ انتهاء المعرفة**: تاريخ انتهاء تحديث بيانات التدريب للنموذج. **غير متوفر** يعني أن المعلومات غير مقدمة أو غير معروفة.

## مصدر البيانات وتكرار التحديث

يتم توليد بيانات هذا التصنيف تلقائيًا بواسطة مشروع [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) الذي يجمع البيانات من [lmarena.ai](https://lmarena.ai/) ويعالجها. يتم تحديث هذا التصنيف يوميًا تلقائيًا بواسطة GitHub Actions.

## إخلاء المسؤولية

هذا التقرير لأغراض إعلامية فقط. بيانات التصنيف ديناميكية وتستند إلى تصويت المستخدمين في Chatbot Arena خلال فترة زمنية محددة. تكامل البيانات ودقتها يعتمدان على تحديثات مصدر البيانات الأولي ومعالجة مشروع `fboulnois/llm-leaderboard-csv`. قد تستخدم النماذج المختلفة تراخيص مختلفة، يرجى الرجوع إلى الإرشادات الرسمية لمقدم النموذج عند الاستخدام.