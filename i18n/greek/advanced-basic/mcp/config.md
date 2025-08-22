# Ρύθμιση και χρήση του MCP


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1.  Ανοίξτε τις ρυθμίσεις του Cherry Studio.
2.  Βρείτε την επιλογή `MCP Server`.
3.  Κάντε κλικ στο `Add Server`.
4.  Συμπληρώστε τις παραμέτρους του MCP Server ([αναφορά](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Οι πιθανές παράμετροι είναι:
    *   Όνομα: Προσαρμοσμένο όνομα, π.χ. `fetch-server`
    *   Τύπος: Επιλέξτε `STDIO`
    *   Εντολή: Συμπληρώστε `uvx`
    *   Παράμετροι: Συμπληρώστε `mcp-server-fetch`
    *   (Άλλες παράμετροι ανάλογα με το συγκεκριμένο Server)
5.  Κάντε κλικ στο `Save`.

{% hint style="success" %}
Μετά την παραπάνω ρύθμιση, το Cherry Studio θα κατεβάσει αυτόματα τον απαιτούμενο MCP Server - `fetch server`. Όταν ολοκληρωθεί η λήψη, μπορούμε να ξεκινήσουμε! Σημείωση: Αν η ρύθμιση του mcp-server-fetch αποτύχει, δοκιμάστε να επανεκκινήσετε τον υπολογιστή.
{% endhint %}

### Ενεργοποίηση υπηρεσιών MCP στο chatbox

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

*   Έχει προστεθεί επιτυχώς ο MCP Server στις ρυθμίσεις `MCP Server`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Επίδειξη αποτελεσμάτων**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Όπως φαίνεται, με τη λειτουργία `fetch` του MCP, το Cherry Studio καταλαβαίνει καλύτερα τις προθέσεις του χρήστη, ανακτά σχετικές πληροφορίες από το διαδίκτυο και παρέχει πιο ακριβείς και ολοκληρωμένες απαντήσεις.