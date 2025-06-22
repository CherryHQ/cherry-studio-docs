---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# Πρόσβαση στο Διαδίκτυο μέσω του Volcano Engine

### 1. Σύνδεση/Εγγραφή λογαριασμού «Volcano Engine» <a href="#rclz7" id="rclz7"></a>

Επίσκεψη στην επίσημη ιστοσελίδα: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Επίσημη ιστοσελίδα Volcano Engine</p></figcaption></figure>

### 2. Δημιουργία «Δικής μου Εφαρμογής» «με πρόσβαση στο διαδίκτυο» <a href="#gvzaa" id="gvzaa"></a>

2.1. Συνδεθείτε στο Volcano Engine και μεταβείτε στη σελίδα «Volcano Ark»: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Κάντε κλικ διαδοχικά:**<mark style="color:red;">**«Δικές μου Εφαρμογές» - «Δημιουργία Εφαρμογής» - «Χωρίς κώδικα» - «Ατομική συνομιλία»**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Συμπλήρωση πληροφοριών και δημοσίευση εφαρμογής <a href="#zzdfe" id="zzdfe"></a>

**Όνομα εφαρμογής**: Ονομασία ελεύθερη επιλογής σύμφωνα με τις απαιτήσεις (τα πεδία με<mark style="color:red;">**\* είναι υποχρεωτικά**</mark>, τα υπόλοιπα προαιρετικά)

<mark style="color:red;">**Κρίσιμο σημείο: Ενεργοποίηση πρόσβασης στο διαδίκτυο (πρέπει πρώτα να ενεργοποιηθεί)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Ενεργοποίηση πρόσβασης στο διαδίκτυο (προσοχή στα κόστη και δωρεάν χρήσεις) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Κάντε κλικ στο «Άμεση αγορά» και ακολουθήστε τα βήματα μέχρι την εμφάνιση της παρακάτω οθόνης για επιβεβαίωση ενεργοποίησης.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Επαληθεύστε την κατάσταση - ενεργοποίηση ολοκληρώθηκε</p></figcaption></figure>

Επιστρέψτε στη σελίδα «Συμπλήρωση πληροφοριών εφαρμογής» για συνέχεια.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Ρυθμίσεις «Πρόσβασης στο διαδίκτυο» για προχωρημένους <a href="#sp6uz" id="sp6uz"></a>

Προτάσεις ρύθμισης:
* Για έλεγχο εισόδου/εξόδου: χρησιμοποιήστε «**Προσαρμοσμένη πρόσβαση**»
* Για απλούστερο setup: «**Αυτόματη πρόσβαση**» (προεπιλογή)
* Για υψηλή χρονική ακρίβεια: «**Υποχρεωτική ενεργοποίηση**»

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Δημοσίευση εφαρμογής <a href="#fe1gf" id="fe1gf"></a>

Κάντε κλικ στο κουμπί «Δημοσίευση» για επιτυχή δημιουργία εφαρμογής.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Λήψη API Key <a href="#jtqlu" id="jtqlu"></a>

Κάντε κλικ διαδοχικά: **«Οδηγός API» - «Επιλογή API Key» - «Αντιγραφή»**

Αντιγράψτε το API key και επικολλήστε το στο Cherry Studio (ακολουθήστε τα βήματα):

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Σημείωση: Εάν δεν υπάρχει API key, κάντε κλικ στο «**Δημιουργία API Key**» πριν την αντιγραφή.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Χρήση API Key στο Cherry Studio για πρόσβαση στο διαδίκτυο μέσω deepseek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1. Ανοίξτε το Cherry Studio - «Ρυθμίσεις» - «Οποιοδήποτε όνομα» - «Τύπος: openAI» <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Ρύθμιση URL και κλειδιού <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Προσοχή: Οι διευθύνσεις Beijing node πρέπει να περιέχουν "/" στο τέλος:</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Προσθήκη ονόματος μοντέλου <a href="#qmh3i" id="qmh3i"></a>

Αντιγράψτε το όνομα μοντέλου από τη μικρή ένδειξη για αποφυγή σφαλμάτων.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Προεπισκόπηση αποτελέσματος <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>