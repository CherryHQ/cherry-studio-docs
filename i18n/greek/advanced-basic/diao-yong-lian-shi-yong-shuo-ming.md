---
icon: route
---
# Οδηγός Χρήσης Trace


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




## Λειτουργίες

Το Trace (ονομάζεται επίσης "trace") παρέχει δυνατότητες ενόρασης στις συνομιλίες, βοηθώντας τους χρήστες να παρατηρήσουν τη συμπεριφορά του μοντέλου, της βάσης γνώσεων, του MCP, της διαδικτυακής αναζήτησης κ.λπ. κατά τη διάρκεια της συνομιλίας. Είναι ένα εργαλείο παρατηρησιμότητας που βασίζεται στο [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), συλλέγοντας, αποθηκεύοντας και επεξεργαζόμενα δεδομένα από την πλευρά του client για οπτικοποίηση, παρέχοντας ποσοτικές εκτιμήσεις για την αντιμετώπιση προβλημάτων και τη βελτιστοποίηση των αποτελεσμάτων.

Κάθε συνομιλία αντιστοιχεί σε ένα trace δεδομένων. Ένα trace αποτελείται από πολλαπλά spans, όπου κάθε span αντιστοιχεί σε μια λογική επεξεργασίας του Cherry Studio, όπως κλήση συνεδρίας μοντέλου, κλήση MCP, κλήση βάσης γνώσεων, κλήση διαδικτυακής αναζήτησης κ.λπ. Το trace εμφανίζεται ως δομή δέντρου με spans ως κόμβους, περιλαμβάνοντας βασικά δεδομένα όπως χρόνος εκτέλεσης και χρήση tokens, ενώ στα span details μπορείτε να δείτε συγκεκριμένα δεδομένα εισόδου/εξόδου.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Ενεργοποίηση Trace

Από προεπιλογή, μετά την εγκατάσταση του Cherry Studio, το Trace είναι κρυφό. Πρέπει να το ενεργοποιήσετε στις "Ρυθμίσεις" > "Γενικές Ρυθμίσεις" > "Λειτουργία Προγραμματιστή", όπως φαίνεται παρακάτω:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Για προηγούμενες συνομιλίες δεν δημιουργούνται αρχεία Trace. Τα αρχεία Trace δημιουργούνται μόνο μετά από νέες ερωτήσεις-απαντήσεις. Τα δεδομένα αποθηκεύονται τοπικά. Για πλήρη διαγραφή Trace, μεταβείτε στις "Ρυθμίσεις" > "Ρυθμίσεις Δεδομένων" > "Κατάλογος Δεδομένων" > "Εκκαθάριση Cache" ή διαγράψτε χειροκίνητα τα αρχεία στον φάκελο ~/.cherrystudio/trace:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Σενάρια Χρήσης

### Προβολή Ολόκληρου του Trace

Στο παράθυρο διαλόγου του Cherry Studio, κάντε κλικ στο Trace για να δείτε ολόκληρη τη ροή δεδομένων. Ανεξάρτητα από το αν χρησιμοποιείται μοντέλο, διαδικτυακή αναζήτηση, βάση γνώσεων ή MCP, μπορείτε να δείτε όλα τα δεδομένα κλήσης στο παράθυρο trace.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Προβολή Μοντέλου στο Trace

Κάντε κλικ στον κόμβο κλήσης μοντέλου για να δείτε λεπτομέρειες εισόδου/εξόδου:

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Προβολή Διαδικτυακής Αναζήτησης στο Trace

Κάντε κλικ στον κόμβο διαδικτυακής αναζήτησης για να δείτε το ερώτημα αναζήτησης και τα επιστρεφόμενα αποτελέσματα:

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Προβολή Βάσης Γνώσεων στο Trace

Κάντε κλικ στον κόμβο βάσης γνώσεων για να δείτε το ερώτημα και την απάντηση:

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Προβολή MCP στο Trace

Κάντε κλικ στον κόμβο MCP για να δείτε παραμέτρους εισόδου και επιστρεφόμενες τιμές:

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Προβλήματα και Προτάσεις

Αυτή η λειτουργία παρέχεται από την ομάδα [EDAS](https://www.aliyun.com/product/edas) της Alibaba Cloud. Για ερωτήσεις ή προτάσεις, συμμετέχετε στην ομάδα DingTalk (ID: 21958624) για άμεση επικοινωνία με τους προγραμματιστές.

\