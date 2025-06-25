---
description: 数据设置→Obsidian配置
icon: gem
---

# Οδηγός Obsidian

{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

## Φροντιστήριο Ρύθμισης Obsidian

Το Cherry Studio υποστηρίζει συνεργασία με το Obsidian, επιτρέποντας την εξαγωγή πλήρων συνομιλιών ή μεμονωμένων απαντήσεων στη βιβλιοθήκη του Obsidian.

{% hint style="warning" %}
**Απαιτείται η τελευταία έκδοση του Obsidian**\
Η διαδικασία δεν απαιτεί πρόσθετο plugin του Obsidian. Ωστόσο, καθώς η εισαγωγή στο Obsidian χρησιμοποιεί παρόμοιες αρχές με το Obsidian Web Clipper, συνιστάται η χρήση της **τελευταίας έκδοσης** (τουλάχιστον > **1.7.2**) για την αποφυγή αποτυχιών σε μεγάλες συνομιλίες [(παράδειγμα ζητήματος)](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

### Νέο φροντιστήριο

{% hint style="info" %}
Στην νέα έκδοση, η ρύθμιση **αυτόματα εντοπίζει τη διαδρομή βιβλιοθήκης**, χωρίς να απαιτείται χειροκίνητη εισαγωγή ονομάτων.
{% endhint %}

#### Βήμα 1: Ρύθμιση Cherry Studio

Πραγματοποιήστε τα εξής στο Cherry Studio:\
&#xNAN;_&#x3A1;υθμίσεις_ → _Διαχείριση δεδομένων_ → _Ρυθμίσεις Obsidian_\
Στην αναπτυσσόμενη λίστα θα εμφανιστούν οι βιβλιοθήκες που έχετε ανοίξει. Επιλέξτε την προορισμού σας:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

#### Βήμα 2: Εξαγωγή συνομιλιών

**Πλήρης συνομιλία**

1. Δεξί κλικ στη συνομιλία
2. Επιλέξτε _Εξαγωγή_ → _Εξαγωγή σε Obsidian_

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Παραμετροποίηση ρυθμίσεων παραθύρου εξαγωγής:

* **Βιβλιοθήκη**: Επιλογή άλλης βιβλιοθήκης (προαιρετικό)
* **Διαδρομή**: Φάκελος προορισμού
* **Ιδιότητες σε Properties**:
  * Ετικέτες (tags)
  * Ημερομηνία δημιουργίας (created)
  * Πηγή (source)
* **Τρόπος εξαγωγής**:
  * **Δημιουργία (αν υπάρχει, αντικατάσταση)**: Δημιουργεί νέα σημείωση. Αντικαθιστά υπάρχοντα.
  * **Προσθήκη στην αρχή**: Προσθέτει στο υπάρχον αρχείο (χωρίς Properties).
  * **Προσθήκη στο τέλος**: Προσθέτει στο τέλος υπάρχοντος αρχείου (χωρίς Properties).

{% hint style="info" %}
Μόνο η πρώτη μέθοδος συμπεριλαμβάνει ιδιότητες (Properties).
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Ρύθμιση ιδιοτήτων</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Επιλογή διαδρομής</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Επιλογή μεθόδου</p></figcaption></figure>

**Ατομική απάντηση**

1. Κάντε κλικ στο μενού ≡ δίπλα στην απάντηση
2. Επιλέξτε _Εξαγωγή_ → _Εξαγωγή σε Obsidian_

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Εξαγωγή μεμονωμένης απάντησης</p></figcaption></figure>

Επαναλάβετε τις [ρυθμίσεις εξαγωγής πλήρους συνομιλίας](obsidian.md#dao-chu-wan-zheng-dui-hua).

#### Επιτυχής εξαγωγή

🎉 Όλα έτοιμα! Η διαδικασία εξαγωγής στο Obsidium ολοκληρώθηκε.

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Εξαγόμενη συνομιλία</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Αποτέλεσμα στο Obsidian</p></figcaption></figure>

***

### Παλιά φροντιστήρια (για Cherry Studio < v1.1.13)

#### Βήμα 1: Προετοιμασία Obsidian

1. Δημιουργήστε φάκελο αποθήκευσης (π.χ. "Cherry Studio")
2. Αναγνωρίστε το **όνομα βιβλιοθήκης** (εμφανίζεται κάτω αριστερά)

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

#### Βήμα 2: Ρύθμιση Cherry Studio

Στο μενού _Ρυθμίσεις_ → _Διαχείριση δεδομένων_ → _Ρυθμίσεις Obsidian_:

1. Εισαγάγετε όνομα βιβλιοθήκης και φακέλου
2. (Προαιρετικό) Καθορίστε ετικέτες

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

#### Βήμα 3: Εξαγωγή

**Πλήρης συνομιλία**

Δεξί κλικ συνομιλίας → _Εξαγωγή_ → _Εξαγωγή σε Obsidian_

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Εξαγωγή πλήρους συνομιλίας</p></figcaption></figure>

Ρυθμίσεις μεθόδων:

* **Δημιουργία (αν υπάρχει, αντικατάσταση)**
* **Προσθήκη στην αρχή** (χωρίς Properties)
* **Προσθήκη στο τέλος** (χωρίς Properties)

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Ρυθμίσεις ιδιοτήτων</p></figcaption></figure>

**Ατομική απάντηση**

Κλικ στο μενού ≡ → Εξαγωγή → Εξαγωγή σε Obsidian

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Εξαγωγή ατομικής απάντησης</p></figcaption></figure>

Ακολουθήστε τις [οδηγίες εξαγωγής πλήρους συνομιλίας](obsidian.md#dao-chu-wan-zheng-dui-hua).
