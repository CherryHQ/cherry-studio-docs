---
icon: ban
---
# Ρύθμιση Μαύρης Λίστας Δικτυακής Αναζήτησης


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




Το Cherry Studio υποστηρίζει ρύθμιση μαύρης λίστας με δύο τρόπους: χειροκίνητα και μέσω προσθήκης πηγών συνδρομής. Οι κανόνες ρύθμισης αναφέρονται στο [ublacklist](https://github.com/iorate/ublacklist).

## Χειροκίνητη Ρύθμιση

Μπορείτε να προσθέσετε κανόνες στα αποτελέσματα αναζήτησης ή να κάνετε κλικ στο εικονίδιο της γραμμής εργαλείων για να αποκλείσετε συγκεκριμένους ιστότοπους. Οι κανόνες μπορούν να καθοριστούν χρησιμοποιώντας [μοτίβα αντιστοίχισης](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (παράδειγμα: `*://*.example.com/*`) ή [κανονικές εκφράσεις](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (παράδειγμα: `/example\.(net|org)/`).

## Ρύθμιση Πηγών Συνδρομής

Μπορείτε επίσης να εγγραφείτε σε δημόσια σύνολα κανόνων. Αυτός ο ιστότοπος παραθέτει ορισμένες συνδρομές:\
https://iorate.github.io/ublacklist/subscriptions

Ακολουθούν ορισμένες προτεινόμενες συνδέσεις πηγών συνδρομής:

| Όνομα                                                                                                    | Σύνδεσμος                                                                                                   | Τύπος   |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | Κινέζικα   |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt | Δημιουργημένο από ΤΝ |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Ρύθμιση Πηγών Συνδρομής</p></figcaption></figure>