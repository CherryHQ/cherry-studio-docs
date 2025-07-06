---
icon: cloud-arrow-up
---
# WebDAV Αντιγράφων Ασφαλείας


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




{% hint style="success" %}
Το WebDAV έχει σχετικά χαμηλό όριο για υπηρεσίες, με τις πιο συνηθισμένες να είναι οι χωροφύλακες:

- [Jianguoyun](https://www.jianguoyun.com/)
- [123 Pan](https://www.123pan.com/) (απαιτεί συνδρομή)
- [Alibaba Cloud Drive](https://www.alipan.com/) (απαιτεί αγορά)
- [Box](https://www.box.com/) (δωρεάν χώρος 10GB, μέγιστο μέγεθος αρχείου 250MB)
- [Dropbox](https://www.dropbox.com/) (δωρεάν χώρος 2GB, επεκτάσιμο έως 16GB με προσκλήσεις)
- [TeraCloud](https://teracloud.jp/en/) (δωρεάν χώρος 10GB + 5GB με πρόσκληση)
- [Yandex Disk](https://disk.yandex.com/) (δωρεάν χώρος 10GB)

Εναλλακτικά, μερικές υπηρεσίες απαιτούν την εγκατάστασή τους:

- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [sharelist](https://github.com/reruin/sharelist)
{% endhint %}

Η δημιουργία αντιγράφων ασφαλείας στο Cherry Studio υποστηρίζεται μέσω του πρωτοκόλλου WebDAV. Μπορείτε να επιλέξετε μια κατάλληλη υπηρεσία WebDAV για την υποστήριξη στα σύννεφα.

Μέσω WebDAV μπορείτε να επιτύχετε συγχρονισμό δεδομένων πολλαπλών συσκευών:  
`Υπολογιστής Α` $$\xrightarrow{\text{αντιγράφων ασφαλείας}}$$ `WebDAV` $$\xrightarrow{\text{αποκατάσταση}}$$ `Υπολογιστής Β`

#### Παράδειγμα με τον Jianguoyun

1. Συνδεθείτε στο jianguoyun.com, επιλέξτε το όνομα χρήστη και πατήστε "Πληροφορίες λογαριασμού":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Επιλέξτε "Καταστατικά ασφαλείας" και πατήστε "Προσθήκη εφαρμογής":

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Εισάγετε όνομα εφαρμογής και δημιουργήστε τυχαίο κωδικό:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Αντιγράψτε και αποθηκεύστε τον κωδικό:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Λάβετε τη διεύθυνση διακομιστή, το όνομα χρήστη και τον κωδικό:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Στο Cherry Studio > Ρυθμίσεις > Ρυθμίσεις δεδομένων, συμπληρώστε τις πληροφορίες WebDAV:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Επιλέξτε δημιουργία αντιγράφου ασφαλείας ή αποκατάσταση δεδομένων και ορίστε τη συχνότητα αυτόματης δημιουργίας αντιγράφων:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>