---
description: 暂时不支持Claude模型
---
# Vertex AI


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




## Επισκόπηση Οδηγού

### 1. Λήψη Κλειδιού API

* Πριν λάβετε το κλειδί API για το Gemini, χρειάζεστε ένα έργο Google Cloud (αν έχετε ήδη, αυτό το βήμα παραλείπεται)
* Επισκεφθείτε το [Google Cloud](https://console.cloud.google.com/projectcreate) για να δημιουργήσετε έργο, συμπληρώστε το όνομα έργου και πατήστε "Δημιουργία έργου"

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Μετάβαση στην [Κονσόλα Vertex AI](https://console.cloud.google.com/vertex-ai)
* Ενεργοποιήστε το [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) στο δημιουργηθέν έργο

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Ρύθμιση Δικαιωμάτων Πρόσβασης API

* Ανοίξτε τη σελίδα δικαιωμάτων [Λογαριασμοί Υπηρεσιών](https://console.cloud.google.com/iam-admin/serviceaccounts) και δημιουργήστε λογαριασμό υπηρεσίας

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Στη σελίδα διαχείρισης λογαριασμών υπηρεσιών, βρείτε τον νέο λογαριασμό, κάντε κλικ στο `Κλειδιά` και δημιουργήστε νέο κλειδί σε μορφή JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Μετά την επιτυχή δημιουργία, το αρχείο κλειδιού θα αποθηκευτεί αυτόματα στον υπολογιστή σας σε μορφή JSON. **Παρακαλώ φυλάξτε το προσεκτικά**

## 3. Ρύθμιση του Vertex AI στο Cherry Studio

* Επιλέξτε τον πάροχο υπηρεσιών Vertex AI
* Συμπληρώστε τα αντίστοιχα πεδία από το αρχείο JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Κάντε κλικ στο Προσθήκη [μοντέλου](https://console.cloud.google.com/vertex-ai/model-garden) και μπορείτε να αρχίσετε να το χρησιμοποιείτε με ευχαρίστηση!