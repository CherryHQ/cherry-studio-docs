---
description: 暂时不支持Claude模型
---
# Vertex AI


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




## Επισκόπηση του Μαθήματος

### 1. Λήψη κλειδιού API

* Πριν αποκτήσετε το κλειδί API του Gemini, πρέπει να έχετε ένα έργο Google Cloud (αν έχετε ήδη, αυτό το βήμα μπορεί να παραλειφθεί)
* Μεταβείτε στο [Google Cloud](https://console.cloud.google.com/projectcreate) για να δημιουργήσετε έργο, συμπληρώστε το όνομα του έργου και κάντε κλικ στο "Δημιουργία έργου"

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Μεταβείτε στον [Πίνακα ελέγχου Vertex AI](https://console.cloud.google.com/vertex-ai)
* Ενεργοποιήστε το [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) στο έργο που δημιουργήσατε

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Ρύθμιση δικαιωμάτων πρόσβασης API

* Ανοίξτε τη σελίδα δικαιωμάτων [Λογαριασμοί υπηρεσίας](https://console.cloud.google.com/iam-admin/serviceaccounts) και δημιουργήστε έναν λογαριασμό υπηρεσίας

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Στη σελίδα διαχείρισης λογαριασμών υπηρεσίας, βρείτε τον λογαριασμό που μόλις δημιουργήσατε, κάντε κλικ στο `Κλειδιά` και δημιουργήστε ένα νέο κλειδί σε μορφή JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Μετά την επιτυχή δημιουργία, το αρχείο κλειδιού θα αποθηκευτεί αυτόματα στον υπολογιστή σας σε μορφή JSON αρχείου. Παρακαλώ **αποθηκεύστε το με ασφάλεια**

## 3. Ρύθμιση του Vertex AI στο Cherry Studio

* Επιλέξτε τον πάροχο υπηρεσιών Vertex AI
* Συμπληρώστε τα αντίστοιχα πεδία του αρχείου JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Κάντε κλικ στην προσθήκη [μοντέλου](https://console.cloud.google.com/vertex-ai/model-garden) και είστε έτοιμοι να ξεκινήσετε!