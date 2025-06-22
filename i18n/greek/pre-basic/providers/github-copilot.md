
{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# GitHub Copilot

Για να χρησιμοποιήσετε το GitHub Copilot, πρέπει πρώτα να έχετε λογαριασμό GitHub και να έχετε εγγραφεί στην υπηρεσία GitHub Copilot. Η δωρεάν έκδοση είναι επίσης αποδεκτή, αλλά δεν υποστηρίζει το νεότερο μοντέλο Claude 3.7. Δείτε περισσότερες λεπτομέρειες στην [επίσημη ιστοσελίδα του GitHub Copilot](https://github.com/features/copilot).

## Λήψη Device Code

Κάντε κλικ στο «Login GitHub» για να λάβετε και να αντιγράψετε το Device Code.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Παράδειγμα εικόνας λήψης Device Code"><figcaption><p>Λήψη Device Code</p></figcaption></figure>

## Συμπλήρωση και εξουσιοδότηση Device Code στο πρόγραμμα περιήγησης

Μετά την επιτυχή λήψη του Device Code, κάντε κλικ στον σύνδεσμο για να ανοίξετε το πρόγραμμα περιήγησης. Συνδεθείτε στον λογαριασμό σας GitHub, εισάγετε το Device Code και εκτελέστε την εξουσιοδότηση.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Παράδειγμα εικόνας εξουσιοδότησης GitHub"><figcaption><p>Εξουσιοδότηση GitHub</p></figcaption></figure>

Μετά την επιτυχή εξουσιοδότηση, επιστρέψτε στο Cherry Studio και κάντε κλικ στο «Connect GitHub». Θα εμφανιστεί το όνομα χρήστη και η εικόνα προφίλ σας από το GitHub.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Παράδειγμα επιτυχούς σύνδεσης GitHub"><figcaption><p>Επιτυχής σύνδεση GitHub</p></figcaption></figure>

## Λήψη λίστας μοντέλων με το κουμπί «Manage»

Πατήστε το κάτω κουμπί «Manage» για να λάβετε αυτόματα τη λίστα των υποστηριζόμενων μοντέλων μέσω δικτύου.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Παράδειγμα λήψης λίστας μοντέλων"><figcaption><p>Λήψη λίστας μοντέλων</p></figcaption></figure>

## Συχνές Ερωτήσεις

### Αποτυχία λήψης Device Code - Δοκιμάστε ξανά

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Παράδειγμα αποτυχίας λήψης Device Code"><figcaption><p>Αποτυχία λήψης Device Code</p></figcaption></figure>

Τα αιτήματα χρησιμοποιούν Axios, το οποίο δεν υποστηρίζει διακομιστές proxy τύπου socks. Χρησιμοποιήστε το συστημικό proxy, HTTP proxy ή καθολικό proxy. Απενεργοποιήστε τυχόν ρυθμίσεις proxy στο CherryStudio και βεβαιωθείτε ότι έχετε σταθερή σύνδεση στο διαδίκτυο.