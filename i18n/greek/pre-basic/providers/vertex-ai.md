---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# Vertex AI

## Επισκόπηση του μαθήματος

### 1. Λήψη κλειδιού API

* Για να λάβετε ένα κλειδί API για το Gemini, θα χρειαστείτε ένα έργο Google Cloud (εάν έχετε ήδη, αυτό το βήμα παραλείπεται)
* Μεταβείτε στο [Google Cloud](https://console.cloud.google.com/projectcreate) για να δημιουργήσετε ένα έργο, συμπληρώστε το όνομα του έργου και πατήστε "Δημιουργία έργου"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Μεταβείτε στον [πίνακα ελέγχου Vertex AI](https://console.cloud.google.com/vertex-ai)
* Στο δημιουργημένο έργο, ενεργοποιήστε το [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Ρύθμιση δικαιωμάτων πρόσβασης API

* Ανοίξτε τη σελίδα δικαιωμάτων [λογαριασμών υπηρεσιών](https://console.cloud.google.com/iam-admin/serviceaccounts) και δημιουργήστε έναν λογαριασμό υπηρεσίας

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Στη σελίδα διαχείρισης λογαριασμών υπηρεσιών, βρείτε τον λογαριασμό που μόλις δημιουργήσατε, πατήστε `Κλειδιά` και δημιουργήστε ένα νέο κλειδί μορφής JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Μετά την επιτυχή δημιουργία, το αρχείο κλειδιού θα αποθηκευτεί αυτόματα στον υπολογιστή σας σε μορφή JSON - **φυλάξτε το με ασφάλεια**

## 3. Ρύθμιση του Vertex AI στο Cherry Studio

* Επιλέξτε τον πάροχο υπηρεσιών Vertex AI
* Συμπληρώστε τα αντίστοιχα πεδία του αρχείου JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Πατήστε "Προσθήκη [μοντέλου](https://console.cloud.google.com/vertex-ai/model-garden)" και είστε έτοιμοι να ξεκινήσετε!