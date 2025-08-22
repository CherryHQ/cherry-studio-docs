# Εγκατάσταση Περιβάλλοντος MCP


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




**Το MCP (Model Context Protocol)** είναι ένα ανοιχτού κώδικα πρωτόκολλο που στοχεύει να παρέχει πληροφορίες περιβάλλοντος σε Μεγάλα Γλωσσικά Μοντέλα (LLM) με τυποποιημένο τρόπο. Περισσότερες λεπτομέρειες για το MCP βρίσκονται στο [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Χρήση του MCP στο Cherry Studio

Παρακάτω, χρησιμοποιώντας τη λειτουργία `fetch` ως παράδειγμα, παρουσιάζουμε πώς μπορείτε να χρησιμοποιήσετε το MCP στο Cherry Studio. Μπορείτε να βρείτε λεπτομέρειες στην [τεκμηρίωση](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Προετοιμασία: Εγκατάσταση uv, bun**

{% hint style="warning" %}
Το Cherry Studio χρησιμοποιεί μόνο τα ενσωματωμένα [uv](https://github.com/astral-sh/uv) και [bun](https://github.com/oven-sh/bun), **χωρίς να αξιοποιεί** τα ήδη εγκατεστημένα uv και bun στο σύστημά σας.
{% endhint %}

Στο `Ρυθμίσεις - Διακομιστής MCP`, κάντε κλικ στο κουμπί `Εγκατάσταση` για λήψη και αυτόματη εγκατάσταση. Επειδή η λήψη γίνεται απευθείας από το GitHub, η ταχύτητα μπορεί να είναι αργή και υπάρχει σημαντική πιθανότητα αποτυχίας. Η επιτυχής εγκατάσταση επιβεβαιώνεται από την ύπαρξη αρχείων στον παρακάτω φάκελο.

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Κατάλογος εγκατάστασης εκτελέσιμων προγραμμάτων:**

Windows: `C:\Users\用户名\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Κατάλογος bin</p></figcaption></figure>

**Σε περίπτωση αποτυχίας εγκατάστασης:**

Μπορείτε να δημιουργήσετε συμβολικούς συνδέσμους (soft links) προς τις εντολές του συστήματος σας σε αυτόν τον κατάλογο. Εάν ο κατάλογος δεν υπάρχει, δημιουργήστε τον χειροκίνητα. Εναλλακτικά, μπορείτε να κατεβάσετε χειροκίνητα τα εκτελέσιμα αρχεία:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)