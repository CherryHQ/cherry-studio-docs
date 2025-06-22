---
icon: file-code
---

{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}

# Προσαρμοσμένο CSS

Με το προσαρμοσμένο CSS, μπορείτε να αλλάξετε την εμφάνιση του λογισμικού ώστε να ταιριάζει καλύτερα στις προτιμήσεις σας, όπως φαίνεται παρακάτω:

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

/* χρώμα γραμματοσειράς για την ανάπτυξη βαθιάς σκέψης */
.ant-collapse-content-box .markdown {
  color: red;
}

/* μεταβλητές θέματος */
:root {
  --color-black-soft: #2a2b2a; /* σκούρο χρώμα φόντου */
  --color-white-soft: #f8f7f2; /* ανοιχτό χρώμα φόντου */
}

/* σκούρο θέμα */
body[theme-mode="dark"] {
  /* Χρώματα */
  --color-background: #2b2b2b; /* σκούρο χρώμα φόντου */
  --color-background-soft: #303030; /* ανοιχτό χρώμα φόντου */
  --color-background-mute: #282c34; /* ουδέτερο χρώμα φόντου */
  --navbar-background: var(-–color-black-soft); /* χρώμα φόντου γραμμής πλοήγησης */
  --chat-background: var(–-color-black-soft); /* χρώμα φόντου συζήτησης */
  --chat-background-user: #323332; /* χρώμα φόντου συζήτησης χρήστη */
  --chat-background-assistant: #2d2e2d; /* χρώμα φόντου συζήτησης βοηθού */
}

/* ειδικά στυλ για σκούρο θέμα */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* χρώμα φόντου περιέκτη περιεχομένων */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* χρώμα φόντου μηνυμάτων */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* χρώμα φόντου γραμμής εισαγωγής */
    border: 1px solid #5e5d5940; /* χρώμα περιγράμματος γραμμής εισαγωγής */
    border-radius: 8px; /* ακτίνα περιθωρίου γραμμής εισαγωγής */
  }

  /* στυλ κώδικα */
  code {
    background-color: #e5e5e20d; /* χρώμα φόντου κώδικα */
    color: #ea928a; /* χρώμα κειμένου κώδικα */
  }

  pre code {
    color: #abb2bf; /* χρώμα κειμένου προμορφωμένου κώδικα */
  }
}

/* ανοιχτό θέμα */
body[theme-mode="light"] {
  /* Χρώματα */
  --color-white: #ffffff; /* λευκό */
  --color-background: #ebe8e2; /* ανοιχτό χρώμα φόντου */
  --color-background-soft: #cbc7be; /* ανοιχτό χρώμα φόντου */
  --color-background-mute: #e4e1d7; /* ουδέτερο χρώμα φόντου */
  --navbar-background: var(-–color-white-soft); /* χρώμα φόντου γραμμής πλοήγησης */
  --chat-background: var(-–color-white-soft); /* χρώμα φόντου συζήτησης */
  --chat-background-user: #f8f7f2; /* χρώμα φόντου συζήτησης χρήστη */
  --chat-background-assistant: #f6f4ec; /* χρώμα φόντου συζήτησης βοηθού */
}

/* ειδικά στυλ για ανοιχτό θέμα */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* χρώμα φόντου περιέκτη περιεχομένων */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* χρώμα φόντου μηνυμάτων */
  }

  .inputbar-container {
    background-color: #ffffff; /* χρώμα φόντου γραμμής εισαγωγής */
    border: 1px solid #87867f40; /* χρώμα περιγράμματος γραμμής εισαγωγής */
    border-radius: 8px; /* ακτίνα περιθωρίου γραμμής εισαγωγής, αλλάξτε στο μέγεθος που προτιμάτε */
  }

  /* στυλ κώδικα */
  code {
    background-color: #3d39290d; /* χρώμα φόντου κώδικα */
    color: #7c1b13; /* χρώμα κειμένου κώδικα */
  }

  pre code {
    color: #000000; /* χρώμα κειμένου προμορφωμένου κώδικα */
  }
}
```

Περισσότερες μεταβλητές θέματος μπορείτε να βρείτε στον πηγαίο κώδικα: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Σχετικές Προτάσεις

Αποθήκη θεμάτων του Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Κοινή χρήση κινεζικών θεμάτων για το Cherry Studio: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)