
{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# Εγκατάσταση Περιβάλλοντος MCP

**MCP(Model Context Protocol)** είναι ένα ανοιχτό πρωτόκολλο που στοχεύει στην παροχή πληροφοριών πλαισίου σε μεγάλα γλωσσικά μοντέλα (LLM) με τυποποιημένο τρόπο. Περισσότερες πληροφορίες για το MCP βλέπε [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Χρήση του MCP στο Cherry Studio

Παρακάτω, χρησιμοποιώντας τη λειτουργία `fetch` ως παράδειγμα, θα δείξουμε πώς να χρησιμοποιήσετε το MCP στο Cherry Studio. Μπορείτε να βρείτε λεπτομέρειες στην [τεκμηρίωση](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Προετοιμασία: Εγκατάσταση uv και bun**

{% hint style="warning" %}
Το Cherry Studio χρησιμοποιεί αποκλειστικά το ενσωματωμένο [uv](https://github.com/astral-sh/uv) και [bun](https://github.com/oven-sh/bun), **χωρίς να αξιοποιεί** εκδόσεις αυτών που έχουν ήδη εγκατασταθεί στο σύστημά σας.
{% endhint %}

Στην ενότητα `Ρυθμίσεις - Διακομιστής MCP`, κάντε κλικ στο κουμπί `Εγκατάσταση` για αυτόματη λήψη και εγκατάσταση. Λόγω της άμεσης λήψης από το GitHub, η διαδικασία μπορεί να είναι αργή και με αυξημένη πιθανότητα αποτυχίας. Η επιτυχής εγκατάσταση επαληθεύεται από την παρουσία αρχείων στους φακέλους που αναφέρονται παρακάτω.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Κατάλογοι Εγκατάστασης Εκτελέσιμων Αρχείων:**

- Windows: `C:\Users\<όνομα χρήστη>\.cherrystudio\bin`
- macOS/Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Κατάλογος bin</p></figcaption></figure>

**Εναλλακτική λύση για αποτυχίες εγκατάστασης:**

Μπορείτε να δημιουργήσετε συμβολικούς συνδέσμους (symlinks) για τις εγκατεστημένες εντολές στον παραπάνω κατάλογο. Αν ο φάκελος δεν υπάρχει, θα χρειαστεί να δημιουργηθεί χειροκίνητα. Εναλλακτικά, μπορείτε να κατεβάσετε τα εκτελέσιμα αρχεία απευθείας από:
- Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)
- UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)