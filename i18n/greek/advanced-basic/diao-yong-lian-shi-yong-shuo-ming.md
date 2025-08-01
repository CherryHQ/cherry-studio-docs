---
icon: route
---
# Οδηγίες χρήσης της αλυσίδας κλήσεων


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




## Λειτουργικότητα

Η αλυσίδα κλήσεων (επίσης γνωστή ως "trace") παρέχει δυνατότητα παρακολούθησης των διαλόγων, βοηθώντας τους χρήστες να ανιχνεύουν την απόδοση του μοντέλου, της βάσης γνώσεων, του MCP, της διαδικτυακής αναζήτησης κ.λπ. κατά τη διάρκεια της συνομιλίας. Είναι ένα εργαλείο παρατηρησιμότητας που υλοποιείται με βάση το [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), το οποίο συλλέγει, αποθηκεύει και επεξεργάζεται δεδομένα από την πλευρά του χρήστη για οπτικοποίηση, προσφέροντας ποσοτικές μετρήσεις για εντοπισμό προβλημάτων και βελτιστοποίηση.

Κάθε διάλογος αντιστοιχεί σε ένα trace δεδομένων, και κάθε trace αποτελείται από πολλαπλά spans. Κάθε span αντιστοιχεί σε μια λογική επεξεργασίας του Cherry Studio, όπως κλήση μοντέλου συνομιλίας, κλήση MCP, πρόσβαση σε βάση γνώσεων ή διαδικτυακή αναζήτηση. Το trace εμφανίζεται ως δένδρο με spans ως κόμβους, παρουσιάζοντας βασικά δεδομένα όπως χρόνοι εκτέλεσης και ποσότητα token. Στις λεπτομέρειες span μπορούν να προβληθούν ειδικά inputs/outputs.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Ενεργοποίηση Trace

Από προεπιλογή, μετά την εγκατάσταση του Cherry Studio, το Trace είναι απενεργοποιημένο. Για ενεργοποίηση, μεταβείτε στους "Ρυθμίσεις" > "Γενικές ρυθμίσεις" > "Λειτουργία προγραμματιστή" όπως φαίνεται:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Τα Trace δεδομένα δημιουργούνται μόνο για νέες συνομιλίες μετά την ενεργοποίηση. Τα δεδομένα αποθηκεύονται τοπικά, και για πλήρη διαγραφή μπορείτε να χρησιμοποιήσετε: "Ρυθμίσεις" > "Ρυθμίσεις δεδομένων" > "Κατάλογος δεδομένων" > "Καθαρισμός cache" ή να διαγράψετε χειροκίνητα τα αρχεία στον φάκελο \~/.cherrystudio/trace:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Χαρακτηριστικά χρήσης

### Πλήρης προβολή αλυσίδας

Κάντε κλικ στο εικονίδιο αλυσίδας κλήσεων στο παράθυρο διαλόγου του Cherry Studio για προβολή πλήρους αλυσίδας. Ανεξάρτητα από το αν χρησιμοποιήθηκε μοντέλο, διαδικτυακή αναζήτηση, βάση γνώσεων ή MCP, όλα τα στοιχεία θα εμφανιστούν.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Λεπτομέρειες μοντέλου

Για προβολή λεπτομερειών μοντέλου στην αλυσίδα, κάντε κλικ στον αντίστοιχο κόμβο κλήσης μοντέλου για δείγματα εισόδου/εξόδου.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Διαδικτυακή αναζήτηση

Για ανάλυση αποτελεσμάτων διαδικτυακής αναζήτησης, κάντε κλικ στον κόμβο αναζήτησης. Στις λεπτομέρειες εμφανίζονται το ερώτημα αναζήτησης και τα επιστρεφόμενα αποτελέσματα.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Βάση γνώσεων

Για εξέταση λειτουργίας βάσης γνώσεων, επιλέξτε τον αντίστοιχο κόμβο. Στις λεπτομέρειες φαίνεται το ερώτημα που υποβλήθηκε και η απάντηση του συστήματος.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### MCP κλήσεις

Για παρακολούθηση MCP (Model Calling Protocol), κάντε κλικ στον κόμβο MCP. Στις λεπτομέρειες εμφανίζονται οι παράμετροι κλήσης και η απόκριση του εργαλείου.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Ερωτήσεις και προτάσεις

Η τρέχουσα λειτουργικότητα αναπτύχθηκε από την ομάδα [EDAS](https://www.aliyun.com/product/edas) της Alibaba Cloud. Για ερωτήσεις ή προτάσεις, συμμετέχετε στην ομάδα DingTalk (ID: 21958624) για άμεση επικοινωνία με τους προγραμματιστές.

\