
{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

---
icon: cherries
---

# Αυτόματη εγκατάσταση του MCP

> Για την αυτόματη εγκατάσταση του MCP, απαιτείται η αναβάθμιση του Cherry Studio στην έκδοση v1.1.18 ή νεότερη.

## Εισαγωγή στη λειτουργία

Εκτός από την χειροκίνητη εγκατάσταση, το Cherry Studio περιλαμβάνει το εργαλείο `@mcpmarket/mcp-auto-install`, μία πιο βολική μέθοδο εγκατάστασης διακομιστή MCP. Απλά εισάγετε την σχετική εντολή σε διαλόγους που υποστηρίζουν υπηρεσίες MCP.

{% hint style="warning" %}
**Υπενθύμιση δοκιμαστικής φάσης:**

* Το `@mcpmarket/mcp-auto-install` εξακολουθεί να βρίσκεται σε δοκιμαστική φάση
* Η αποτελεσματικότητα εξαρτάται από την «νοημοσύνη» του μοντέλου· ορισμένα θα προσθέσουν αυτόματα, ενώ άλλα απαιτούν **ακόμα χειροκίνητη τροποποίηση παραμέτρων στις ρυθμίσεις MCP**
* Τα αποτελέσματα αναζήτησης προέρχονται από το @modelcontextprotocol, μπορείτε να προσαρμόσετε αυτή την πηγή (βλ. παρακάτω)
{% endhint %}

## Οδηγίες χρήσης

Για παράδειγμα, μπορείτε να εισάγετε:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Εισαγωγή εντολής για εγκατάσταση διακομιστή MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Διεπαφή διαμόρφωσης διακομιστή MCP</p></figcaption></figure>

Το σύστημα θα αναγνωρίσει αυτόματα την απαίτησή σας και θα ολοκληρώσει την εγκατάσταση μέσω του `@mcpmarket/mcp-auto-install`. Αυτό το εργαλείο υποστηρίζει πολλούς τύπους διακομιστών MCP, συμπεριλαμβανομένων:

* filesystem (σύστημα αρχείων)
* fetch (ανάκτηση δεδομένων)
* sqlite (βάση δεδομένων)
* κ.λπ.

> Η μεταβλητή `MCP_PACKAGE_SCOPES` επιτρέπει προσαρμογή της πηγής αναζήτησης υπηρεσιών MCP. Προεπιλεγμένη τιμή: `@modelcontextprotocol`.

## Εισαγωγή στη βιβλιοθήκη `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Προεπιλεγμένη διαμόρφωση αναφοράς:**

```json
// `axun-uUpaWEdMEMU8C61K` είναι το αναγνωριστικό υπηρεσίας (προσαρμόσιμο)
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "Δείτε λεπτομέρειες στο https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

Το `@mcpmarket/mcp-auto-install` είναι πακέτο npm ανοιχτού κώδικα. Μπορείτε να δείτε λεπτομερείς πληροφορίες και τεκμηρίωση στο [επίσημο npm αποθετήριο](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). Το `@mcpmarket` είναι η επίσημη συλλογή υπηρεσιών MCP του Cherry Studio.
{% endhint %}