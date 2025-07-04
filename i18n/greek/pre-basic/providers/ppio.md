
{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# PPIO Paio Cloud

## Cherry Studio Integration with PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Επισκόπηση Εκπαιδευτικού Προγράμματος <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Το Cherry Studio είναι ένας πολυμοντέλος πελάτης για επιφάνεια εργασίας, που υποστηρίζει τώρα εγκαταστάσεις για συστήματα Windows, Linux και macOS. Συνδυάζει κορυφαία LLM μοντέλα, προσφέροντας βοήθεια για πολλαπλά σενάρια. Οι χρήστες μπορούν να βελτιώσουν την παραγωγικότητά τους μέσω έξυπνης διαχείρισης συνομιλιών, προσαρμοσμένων ανοιχτού κώδικα και πολλαπλών θεματικών διεπαφών.

Το Cherry Studio είναι πλέον πλήρως συμβατό με το **PPIO High-Performance API Channel**—με εταιρικές εγγυήσεις υπολογιστικής ισχύος, επιτυγχάνει **ταχεία απόκριση για DeepSeek-R1/V3** και **99.9% διαθεσιμότητα υπηρεσιών**, παρέχοντάς σας μια ομαλή εμπειρία.

Το παρακάτω εκπαιδευτικό πρόγραμμα περιλαμβάνει μια ολοκληρωμένη λύση ολοκλήρωσης (με ρύθμιση κλειδιών), επιτρέποντάς σας να ξεκινήσετε την προηγμένη λειτουργία «Cherry Studio έξυπνης δρομολόγησης + PPIO High-Performance API» σε λιγότερο από 3 λεπτά.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. Πρόσβαση στο CherryStudio και προσθήκη του «PPIO» ως πάροχου μοντέλου <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Αρχικά, μεταβείτε στον επίσημο ιστότοπο για λήψη του Cherry Studio: [https://cherry-ai.com/download](https://cherry-ai.com/download) (Εάν η σύνδεση αποτύχει, ανοίξτε αυτόν τον σύνδεσμο στο Quark Cloud: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Κάντε κλικ στις Ρυθμίσεις (κάτω αριστερά), ορίστε τον προσαρμοσμένο πάροχο ως: `PPIO` και κάντε κλικ στο «ΟΚ»

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Μεταβείτε στη [Διαχείριση API Κλειδιών PPIO Paio Cloud](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), κάντε κλικ στο **Αβατάρ Χρήστη** → **Διαχείριση API Κλειδιών**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Κάντε κλικ στο κουμπί **+ Δημιουργία** για δημιουργία νέου API κλειδιού. Δώστε ένα προσαρμοσμένο όνομα κλειδιού. **Το κλειδί εμφανίζεται μόνο κατά τη δημιουργία - φροντίστε να το αντιγράψετε και να το αποθηκεύσετε σε ένα έγγραφο για μελλοντική χρήση.**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Εισαγάγετε το κλειδί στο CherryStudio: Κάντε κλικ στις Ρυθμίσεις, επιλέξτε **PPIO Paio Cloud**, εισάγετε το δημιουργημένο API κλειδί και κάντε κλικ στο **Έλεγχος**

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Επιλέξτε μοντέλο: π.χ. deepseek/deepseek-r1/community. Για αλλαγή μοντέλου, απλά επιλέξτε διαφορετικό.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

Οι εκδόσεις DeepSeek R1 και V3 community παρέχονται για δοκιμή και περιλαμβάνουν πλήρη παραμέτρους μοντέλων. Για μαζική χρήση, **χρεώστε τον λογαριασμό σας και αλλάξτε σε εκδόσεις πέραν της community**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Ρύθμιση Χρήσης Μοντέλου <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) Μετά την επιτυχή σύνδεση (εμφάνιση επιτυχίας στο Έλεγχος), το σύστημα είναι έτοιμο για χρήση

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Κάντε κλικ στο **@**, επιλέξτε το μοντέλο DeepSeek R1 κάτω από τον πάροχο PPIO και ξεκινήστε τη συνομιλία~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

[Μέρος υλικού από: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)]

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. Βίντεο Εκπαιδευτικού Προγράμματος PPIO × Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Για οπτική εκμάθηση, δείτε το εκπαιδευτικό βίντεό μας στο Bilibili. Ακολουθήστε βήμα-βήμα ρυθμίσεις για «PPIO API + Cherry Studio»: [《Είστε κουρασμένοι από τα συνεχή loadings του DeepSeek;》PPIO Paio Cloud + DeepSeek πλήρης έκδοση = Χωρίς συμφόρηση, άμεση λειτουργία](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

[Πηγή βίντεο: sola]