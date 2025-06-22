---
icon: database
---

{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# Ρυθμίσεις Δεδομένων

Αυτή η διεπαφή επιτρέπει τη δημιουργία αντιγράφων ασφαλείας δεδομένων πελάτη στο cloud και τοπικά, την αναζήτηση τοπικών καταλόγων δεδομένων και την εκκαθάριση της κρυφής μνήμης, μεταξύ άλλων λειτουργιών.

### Αντίγραφα ασφαλείας δεδομένων

Αυτή τη στιγμή, η δημιουργία αντιγράφων ασφαλείας δεδομένων υποστηρίζει μόνο τη μέθοδο WebDAV. Μπορείτε να επιλέξετε μια υπηρεσία που υποστηρίζει WebDAV για τη δημιουργία αντιγράφων ασφαλείας στο cloud.

Μπορείτε επίσης να συγχρονίσετε δεδομένα σε πολλαπλές συσκευές χρησιμοποιώντας τη διαδικασία: `A电脑` $$\xrightarrow{\text{αντίγραφο ασφαλείας}}$$ `WebDAV` $$\xrightarrow{\text{αποκατάσταση}}$$ `B电脑`.

#### Παράδειγμα με το Jianguoyun

1. Συνδεθείτε στο Jianguoyun, κάντε κλικ στο όνομα χρήστη στην επάνω δεξιά γωνία και επιλέξτε «Πληροφορίες λογαριασμού»:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Επιλέξτε «Επιλογές ασφαλείας», κάντε κλικ στην επιλογή «Προσθήκη εφαρμογής»

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Εισαγάγετε το όνομα εφαρμογής και δημιουργήστε έναν τυχαίο κωδικό πρόσβασης:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Αντιγράψτε και αποθηκεύστε τον κωδικό πρόσβασης:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Λάβετε τη διεύθυνση διακομιστή, το όνομα χρήστη και τον κωδικό πρόσβασης:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Στις Ρυθμίσεις του Cherry Studio > Ρυθμίσεις δεδομένων, συμπληρώστε τις πληροφορίες WebDAV:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Επιλέξτε να δημιουργήσετε αντίγραφο ασφαλείας ή να ανακτήσετε δεδομένα και μπορείτε να ρυθμίσετε το χρονικό διάστημα για τα αυτόματα αντίγραφα ασφαλείας:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Υπηρεσίες WebDAV με χαμηλές απαιτήσεις συνήθως είναι διαδικτυακά στιφάδια:

* [Jianguoyun](https://www.jianguoyun.com/)
* [123pan](https://www.123pan.com/) (απαιτεί συνδρομένο μέλος)
* [Alipan](https://www.alipan.com/) (απαιτεί αγορά)
* [Box](https://www.box.com/) (δωρεάν χώρος 10GB, όριο μεγέθους αρχείου 250MB)
* [Dropbox](https://www.dropbox.com/) (δωρεάν 2GB, επέκταση έως 16GB με πρόσκληση φίλων)
* [TeraCloud](https://teracloud.jp/en/) (δωρεάν χώρος 10GB, +5GB επιπλέον με πρόσκληση)
* [Yandex Disk](https://disk.yandex.com/) (10GB για δωρεάν λογαριασμούς)

Επιπλέον, ορισμένες υπηρεσίες απαιτούν δική σας ανάπτυξη:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}