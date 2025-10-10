---
icon: file-code
---
# Προσαρμοσμένο CSS


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




Με την προσαρμογή του CSS μπορείτε να τροποποιήσετε την εμφάνιση του λογισμικού σύμφωνα με τις προτιμήσεις σας, όπως εδώ:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>Προσαρμοσμένο CSS</p></figcaption></figure>

```css
:root {
  --color-background: #1a462788;
  --color-background-soft: #1a4627aa;
  --color-background-mute: #1a462766;
  --navbar-background: #1a4627;
  --chat-background: #1a4627;
  --chat-background-user: #28b561;
  --chat-background-assistant: #1a462722;
}

#content-container {
  background-color: #2e5d3a !important;
}
```

### Ενσωματωμένες Μεταβλητές

```css
:root {
  font-family: "汉仪唐美人" !important; /* γραμματοσειρά */
}

/* Χρώμα κειμένου για επεκτεταμένη βαθιά σκέψη */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Μεταβλητές θέματος */
:root {
  --color-black-soft: #2a2b2a; /* Σκούρο χρώμα φόντου */
  --color-white-soft: #f8f7f2; /* Ανοιχτό χρώμα φόντου */
}

/* Σκούρο θέμα */
body[theme-mode="dark"] {
  /* Χρώματα */
  --color-background: #2b2b2b; /* Σκούρο χρώμα φόντου */
  --color-background-soft: #303030; /* Ανοιχτό χρώμα φόντου */
  --color-background-mute: #282c34; /* Ουδέτερο χρώμα φόντου */
  --navbar-background: var(-–color-black-soft); /* Χρώμα φόντου γραμμής πλοήγησης */
  --chat-background: var(–-color-black-soft); /* Χρώμα φόντου συνομιλίας */
  --chat-background-user: #323332; /* Χρώμα φόντου χρήστη */
  --chat-background-assistant: #2d2e2d; /* Χρώμα φόντου βοηθού */
}

/* Συγκεκριμένα στυλ για σκούρο θέμα */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Χρώμα φόντου περιεχομένου */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Χρώμα φόντου μηνυμάτων */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Χρώμα φόντου πλαισίου εισαγωγής */
    border: 1px solid #5e5d5940; /* Χρώμα περιγράμματος πλαισίου εισαγωγής */
    border-radius: 8px; /* Ακτίνα περιγράμματος πλαισίου εισαγωγής */
  }

  /* Στυλ κώδικα */
  code {
    background-color: #e5e5e20d; /* Χρώμα φόντου κώδικα */
    color: #ea928a; /* Χρώμα κειμένου κώδικα */
  }

  pre code {
    color: #abb2bf; /* Χρώμα κειμένου μορφοποιημένου κώδικα */
  }
}

/* Ανοιχτόχρωμο θέμα */
body[theme-mode="light"] {
  /* Χρώματα */
  --color-white: #ffffff; /* Λευκό */
  --color-background: #ebe8e2; /* Ανοιχτό χρώμα φόντου */
  --color-background-soft: #cbc7be; /* Ανοιχτό χρώμα φόντου */
  --color-background-mute: #e4e1d7; /* Ουδέτερο χρώμα φόντου */
  --navbar-background: var(-–color-white-soft); /* Χρώμα φόντου γραμμής πλοήγησης */
  --chat-background: var(-–color-white-soft); /* Χρώμα φόντου συνομιλίας */
  --chat-background-user: #f8f7f2; /* Χρώμα φόντου χρήστη */
  --chat-background-assistant: #f6f4ec; /* Χρώμα φόντου βοηθού */
}

/* Συγκεκριμένα στυλ για ανοιχτόχρωμο θέμα */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Χρώμα φόντου περιεχομένου */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Χρώμα φόντου μηνυμάτων */
  }

  .inputbar-container {
    background-color: #ffffff; /* Χρώμα φόντου πλαισίου εισαγωγής */
    border: 1px solid #87867f40; /* Χρώμα περιγράμματος πλαισίου εισαγωγής */
    border-radius: 8px; /* Ακτίνα περιγράμματος πλαισίου εισαγωγής, αλλάξτε σύμφωνα με προτιμήσεις */
  }

  /* Στυλ κώδικα */
  code {
    background-color: #3d39290d; /* Χρώμα φόντου κώδικα */
    color: #7c1b13; /* Χρώμα κειμένου κώδικα */
  }

  pre code {
    color: #000000; /* Χρώμα κειμένου μορφοποιημένου κώδικα */
  }
}
```

Περισσότερες μεταβλητές θέματος: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Σχετικές Προτάσεις

Βιβλιοθήκη θεμάτων Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Κινεζικά θεμέλια για το Cherry Studio: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)