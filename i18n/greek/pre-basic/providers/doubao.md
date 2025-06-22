
{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# ByteDance (Doubao)

* Συνδεθείτε στο [Volcano Engine](https://console.volcengine.com/)
* Κάντε απευθείας κλικ [εδώ για άμεση πρόσβαση](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Λήψη κλειδιού API

* Κάντε κλικ στη [Διαχείριση κλειδιού API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) στην πλευρική γραμμή
* Δημιουργήστε ένα κλειδί API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* Μετά την επιτυχή δημιουργία, κάντε κλικ στο μικρό εικονίδιο ματιού δίπλα στο κλειδί API για να το εμφανίσετε και να το αντιγράψετε

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* Επικολλήστε το κλειδί API στο CherryStudio και ενεργοποιήστε τον διακόπτη του παρόχου

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Ενεργοποίηση και προσθήκη μοντέλων

* Στην πλευρική γραμμή της κονσόλας Ark, ενεργοποιήστε τα απαραίτητα μοντέλα μέσω της [Διαχείρισης ενεργοποίησης](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false). Μπορείτε να ενεργοποιήσετε τη σειρά Doubao και μοντέλα όπως το DeepSeek ανάλογα με τις ανάγκες σας.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* Στο [έγγραφο λίστας μοντέλων](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), βρείτε το αναγνωριστικό μοντέλου (Model ID) που αντιστοιχεί στο επιθυμητό μοντέλο.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Παράδειγμα λίστας αναγνωριστικών μοντέλων του Volcano Engine"><figcaption></figcaption></figure>

* Στο Cherry Studio, μεταβείτε στις ρυθμίσεις [Υπηρεσιών μοντέλων](../../cherrystudio/preview/settings/providers.md) και επιλέξτε Volcano Engine
* Κάντε κλικ στην "Προσθήκη" και επικολλήστε το αναγνωριστικό μοντέλου στο πεδίο κειμένου

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* Προσθέστε τα μοντέλα ένα προς ένα ακολουθώντας αυτή τη διαδικασία

### Διεύθυνση API

Οι διευθύνσεις API μπορούν να γραφτούν με δύο τρόπους:

* Ο πρώτος (προεπιλεγμένος στον πελάτη): `https://ark.cn-beijing.volces.com/api/v3/`
* Ο δεύτερος: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Δεν υπάρχει σημαντική διαφορά μεταξύ των δύο μορφών. Μπορείτε να διατηρήσετε την προεπιλεγμένη χωρίς αλλαγές.

Για διαφορές στο τέλος μεταξύ `/` και `#`, ανατρέξτε στην ενότητα ρυθμίσεων API του παρόχου: [Επισκεφθείτε την ενότητα](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Παράδειγμα cURL από το επίσημο έγγραφο</p></figcaption></figure>