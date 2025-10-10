---
description: 数据设置→Obsidian配置
icon: gem
---
# Οδηγός Ρύθμισης του Obsidian


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




Το Cherry Studio υποστηρίζει ενσωμάτωση με το Obsidian για εξαγωγή ολόκληρων συζητήσεων ή μεμονωμένων μηνυμάτων στη βιβλιοθήκη του Obsidian.

{% hint style="warning" %}
Η διαδικασία αυτή **δεν απαιτεί** εγκατάσταση πρόσθετων πρόσθετων στο Obsidian. Ωστόσο, καθώς η εισαγωγή από το Cherry Studio στο Obsidian χρησιμοποιεί παρόμοια αρχές με το Obsidian Web Clipper, συνιστάται η χρήση της **πιο πρόσφατης έκδοσης** του Obsidian (τρέχουσα έκδοση τουλάχιστον > **1.7.2**) για την αποφυγή [αποτυχιών εισαγωγής μεγάλων συζητήσεων](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Πιο Πρόσφατος Οδηγός

{% hint style="info" %}
Σε σύγκριση με την παλαιότερη έκδοση, η νέα λειτουργία εξαγωγής στο Obsidian **επιλέγει αυτόματα τη διαδρομή της βιβλιοθήκης**, χωρίς να απαιτείται χειροκίνητη εισαγωγή ονόματος βιβλιοθήκης ή φακέλου.
{% endhint %}

### Βήμα 1: Ρύθμιση του Cherry Studio

Ανοίξτε στο Cherry Studio: _Ρυθμίσεις_ → _Ρυθμίσεις Δεδομένων_ → _Ρύθμιση Obsidian_. Στην αναπτυσσόμενη λίστα θα εμφανιστούν αυτόματα τα ονόματα βιβλιοθηκών Obsidian που έχουν ανοιχτεί στον υπολογιστή σας. Επιλέξτε την επιθυμητή βιβλιοθήκη:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Βήμα 2: Εξαγωγή Συζήτησης

#### Εξαγωγή Ολόκληρης Συζήτησης

Στο περιβάλλον συζήτησης του Cherry Studio, κάντε δεξί κλικ στη συζήτηση, επιλέξτε _Εξαγωγή_ και πατήστε _Εξαγωγή στο Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Θα εμφανιστεί παράθυρο για ρύθμιση των **Ιδιοτήτων (Properties)**, της **θέσης φακέλου** στο Obsidian και της **μεθόδου επεξεργασίας**:

* **Βιβλιοθήκη**: Επιλέξτε άλλη βιβλιοθήκη από την αναπτυσσόμενη λίστα
* **Διαδρομή**: Επιλέξτε φάκελο αποθήκευσης
* Ιδιότητες (Properties):
  * Ετικέτες (tags)
  * Χρόνος δημιουργίας (created)
  * Προέλευση (source)
* **Μέθοδοι επεξεργασίας**:
  * **Δημιουργία νέας (αν υπάρχει, αντικατάσταση)**: Δημιουργεί νέα σημείωση στον επιλεγμένο φάκελο, με αντικατάσταση υπαρχόντων
  * **Προσθήκη στην αρχή**: Προσθέτει περιεχόμενο στην αρχή υπάρχουσας σημείωσης
  * **Προσθήκη στο τέλος**: Προσθέτει περιεχόμενο στο τέλος υπάρχουσας σημείωσης

{% hint style="info" %}
Μόνο η πρώτη μέθοδος συμπεριλαμβάνει Ιδιότητες (Properties), οι υπόλοιπες όχι.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Ρύθμιση ιδιοτήτων</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Επιλογή διαδρομής</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Επιλογή μεθόδου επεξεργασίας</p></figcaption></figure>

Μετά την επιλογή, πατήστε "ΟΚ" για την εξαγωγή.

#### Εξαγωγή Μεμονωμένου Μηνύματος

Για μεμονωμένο μήνυμα, πατήστε το _μενού τριών γραμμών_ κάτω από το μήνυμα, επιλέξτε _Εξαγωγή_ και πατήστε _Εξαγωγή στο Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Εξαγωγή μεμονωμένου μηνύματος</p></figcaption></figure>

Θα εμφανιστεί το ίδιο παράθυρο ρυθμίσεων όπως παραπάνω. Ακολουθήστε τις [οδηγίες εξαγωγής ολόκληρης συζήτησης](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Επιτυχής Εξαγωγή

🎉 Συγχαρητήρια! Ολοκληρώσατε τη ρύθμιση και την εξαγωγή στο Obsidian. Απολαύστε τη!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Εξαγωγή στο Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Αποτέλεσμα εξαγωγής</p></figcaption></figure>

***

## Παλαιός Οδηγός (για Cherry Studio < v1.1.13)

### Βήμα 1: Προετοιμασία του Obsidian

Δημιουργήστε έναν φάκελο (π.χ. "Cherry Studio") για αποθήκευση εξαγόμενων συζητήσεων:

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Σημειώστε το όνομα της βιβλιοθήκης (στο πλαίσιο).

### Βήμα 2: Ρύθμιση του Cherry Studio

Στο μενού _Ρυθμίσεις_ → _Ρυθμίσεις Δεδομένων_ → _Ρύθμιση Obsidian_, εισάγετε το όνομα **βιβλιοθήκης** και **φακέλου** από το [Βήμα 1](obsidian.md#di-yi-bu):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

Το πεδίο "Καθολικές Ετικέτες" είναι προαιρετικό.

### Βήμα 3: Εξαγωγή Συζήτησης

#### Εξαγωγή Ολόκληρης Συζήτησης

Κάντε δεξί κλικ στη συζήτηση → _Εξαγωγή_ → _Εξαγωγή στο Obsidian_.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Εξαγωγή ολόκληρης συζήτησης</p></figcaption></figure>

Ρυθμίστε τις **Ιδιότητες (Properties)** και επιλέξτε **μέθοδο επεξεργασίας**:

* **Δημιουργία νέας (αν υπάρχει, αντικατάσταση)**
* **Προσθήκη στην αρχή**
* **Προσθήκη στο τέλος**

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Ρύθμιση ιδιοτήτων</p></figcaption></figure>

{% hint style="info" %}
Μόνο η πρώτη μέθοδος συμπεριλαμβάνει Ιδιότητες (Properties).
{% endhint %}

#### Εξαγωγή Μεμονωμένου Μηνύματος

Πατήστε _μενού τριών γραμμών_ → _Εξαγωγή_ → _Εξαγωγή στο Obsidian_.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Εξαγωγή μεμονωμένου μηνύματος</p></figcaption></figure>

Ακολουθήστε τις [οδηγίες εξαγωγής](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Επιτυχής Εξαγωγή

🎉 Συγχαρητήρια! Η εξαγωγή ολοκληρώθηκε επιτυχώς.

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Εξαγωγή στο Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Αποτέλεσμα εξαγωγής</p></figcaption></figure>