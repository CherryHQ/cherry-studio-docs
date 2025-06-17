---
icon: ban
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Konfigurasi Blacklist Pencarian Web

Cherry Studio mendukung dua cara untuk mengkonfigurasi blacklist: manual dan menambahkan sumber berlangganan. Aturan konfigurasi merujuk ke [ublacklist](https://github.com/iorate/ublacklist)

## Konfigurasi Manual

Anda dapat menambahkan aturan ke hasil pencarian atau mengklik ikon bilah alat untuk memblokir situs tertentu. Aturan dapat ditentukan dengan cara berikut: [Pola Pencocokan](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (contoh: `*://*.example.com/*`) atau menggunakan [Ekspresi Reguler](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (contoh: `/example\.(net|org)/`).

## Konfigurasi Berlangganan

Anda juga dapat berlangganan kumpulan aturan publik. Situs ini mencantumkan beberapa sumber berlangganan:\
https://iorate.github.io/ublacklist/subscriptions

Berikut beberapa tautan berlangganan yang direkomendasikan:

| Nama                                                                                                    | Tautan                                                                                                   | Jenis   |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | Chinese |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list_uBlacklist.txt | AI-Generated |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>Konfigurasi Sumber Berlangganan</p></figcaption></figure>