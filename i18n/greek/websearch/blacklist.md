---
icon: ban
---

{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# Ρύθμιση Λίστας Μαύρης Κουκίδας Δικτύου

Το Cherry Studio υποστηρίζει τη ρύθμιση της λίστας μαύρης κουκίδας με δύο τρόπους: χειροκίνητα και με προσθήκη ροών συνδρομής. Οι κανόνες ρύθμισης παραπέμπουν στο [ublacklist](https://github.com/iorate/ublacklist)

## Χειροκίνητη Ρύθμιση

Μπορείτε να προσθέσετε κανόνες για τα αποτελέσματα αναζήτησης ή να κάνετε κλικ στο εικονίδιο της γραμμής εργαλείων για να αποκλείσετε συγκεκριμένες ιστοσελίδες. Οι κανόνες μπορούν να καθοριστούν με τους παρακάτω τρόπους: [μοτίβο αντιστοίχισης](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (παράδειγμα: `*://*.example.com/*`) ή χρησιμοποιώντας [κανονικές εκφράσεις](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (παράδειγμα: `/example\.(net|org)/`).

## Ρύθμιση Ροών Συνδρομής

Μπορείτε επίσης να εγγραφείτε σε δημόσια σύνολα κανόνων. Αυτή η ιστοσελίδα παραθέτει ορισμένες συνδρομές:\
https://iorate.github.io/ublacklist/subscriptions

Παρακάτω αναφέρονται ορισμένες συστάσεις συνδέσμων ροών συνδρομής:

| Όνομα                                                                                                    | Σύνδεσμος                                                                                                   | Τύπος   |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                                  | Κινέζικα |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)           | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | AI-δημιουργημένη |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Ρύθμιση Ροών Συνδρομής</p></figcaption></figure>