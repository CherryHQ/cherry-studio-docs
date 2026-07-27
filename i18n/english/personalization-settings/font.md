---
icon: book-font
---

# Font Recommendations

Cherry Studio V2 can read fonts installed in the operating system and configure a **Global Font** and **Code Font** separately. Custom CSS is usually unnecessary for changing fonts.

## Choose Fonts in Cherry Studio

1. Install the font in the operating system first.
2. Quit Cherry Studio completely and reopen it.
3. Go to **Settings > General Settings > Display & Language**.
4. Under **Font Settings**, select:
   - **Global Font**: Used for the interface, message body, and most text.
   - **Code Font**: Used for code blocks and code editors.
5. Check that your common languages, numbers, punctuation, and code display correctly.

Both font options have a reset button on the right to restore the default at any time.

{% hint style="info" %}
The font list comes from the operating system. If a newly installed font does not appear, quit Cherry Studio completely first. If it is still missing, restart the operating system to refresh its font cache.
{% endhint %}

## How to Choose

### Global Font

Prioritize:

- Coverage for the languages you use.
- Simplified Chinese, Traditional Chinese, and Japanese glyphs that match your reading habits.
- Clarity at small sizes.
- Complete regular, bold, and italic styles.
- Coordinated height and weight when Latin and CJK text are mixed.

### Code Font

Check:

- Whether `0` and `O`, and `1` and `l` / `I`, are easy to distinguish.
- Whether brackets, quotation marks, slashes, and operators are clear.
- Whether you need Chinese, Japanese, or Russian comments.
- Whether you prefer programming ligatures.

If the code font lacks a character, the system tries to fall back to another font, so character widths or styles may differ within the same code block.

## Body Font Recommendations

| Font | Suitable languages | Characteristics | Official source |
| --- | --- | --- | --- |
| Noto Sans | English, Russian, and many other scripts | Broad coverage for multilingual interfaces | [Noto documentation](https://notofonts.github.io/noto-docs/website/use/) |
| Noto Sans SC | Simplified Chinese | Glyphs for Simplified Chinese | [Noto CJK guide](https://notofonts.github.io/noto-docs/website/use/#which-noto-fonts-should-i-use-for-chinese-japanese-or-korean) |
| Noto Sans TC | Traditional Chinese | Glyphs for Traditional Chinese in Taiwan | [Noto CJK guide](https://notofonts.github.io/noto-docs/website/use/#which-noto-fonts-should-i-use-for-chinese-japanese-or-korean) |
| Noto Sans JP | Japanese | Glyphs for Japanese | [Noto CJK guide](https://notofonts.github.io/noto-docs/website/use/#which-noto-fonts-should-i-use-for-chinese-japanese-or-korean) |
| Source Han Sans | Simplified Chinese, Traditional Chinese, Japanese, and Korean | Adobe's open-source Pan-CJK font with regional variants | [Source Han Sans](https://github.com/adobe-fonts/source-han-sans) |

If you frequently mix English, Russian, and CJK text in one interface, try the Noto family first. It provides font families with similar visual styles across scripts.

{% hint style="warning" %}
The same Han character may use different glyphs in Simplified Chinese, Traditional Chinese, and Japanese. Choose the `SC`, `TC`, or `JP` version that matches your primary reading language.
{% endhint %}

## Code Font Recommendations

| Font | Suitable use | CJK support | Official source |
| --- | --- | --- | --- |
| JetBrains Mono | English and Russian code and terminal content | CJK is not a primary target; CJK comments usually use a fallback font | [JetBrains Mono](https://www.jetbrains.com/lp/mono/) |
| Sarasa Mono | Code with Chinese or Japanese comments | Provides regional variants such as `SC`, `TC`, and `J` | [Sarasa Gothic](https://github.com/be5invis/Sarasa-Gothic) |
| Monaspace | Multiple styles, character variants, and programming ligatures | CJK is not a primary target | [Monaspace](https://github.com/githubnext/monaspace) |

### Quick Selection

- Mainly English or Russian: Try **JetBrains Mono** first.
- Code frequently contains Simplified Chinese: Try **Sarasa Mono SC** first.
- Code frequently contains Traditional Chinese: Try **Sarasa Mono TC** first.
- Code frequently contains Japanese: Try **Sarasa Mono J** first.
- You want different code styles or ligatures: Choose one **Monaspace** family.

Monaspace contains several style-compatible families. Cherry Studio selects only the font family and does not provide font feature switches. Whether certain ligatures or character variants appear also depends on the font version and rendering environment.

## Choose by Documentation Language

| Primary interface language | Global font recommendation | Code font recommendation |
| --- | --- | --- |
| Simplified Chinese | Noto Sans SC / Source Han Sans CN | Sarasa Mono SC |
| Traditional Chinese | Noto Sans TC / Source Han Sans TW | Sarasa Mono TC |
| English | Noto Sans | JetBrains Mono / Monaspace |
| Japanese | Noto Sans JP / Source Han Sans JP | Sarasa Mono J |
| Russian | Noto Sans | JetBrains Mono / Monaspace |

This is only a starting point and does not require an entire team to use the same font. Base the final choice on actual rendering and your organization's typography standards.

## Installation Recommendations

- Download only from the font project's official website or release page.
- Desktop apps generally install `OTF`, `TTF`, `TTC`, or variable font files. Do not prefer web-only `WOFF` / `WOFF2` files.
- Large CJK font packages contain several regions and weights; install only what you need.
- Before updating a font, uninstall the old version to avoid several fonts with the same name in the operating system cache.
- When a team standardizes screenshots or demonstrations, use the same font family and version.

Every project recommended here provides open-source license information on its official page. To repackage a font into a product, template, or commercial deliverable, follow the license included with the font files.

## FAQ

### An installed font is missing from the list

Quit Cherry Studio completely and reopen it. On macOS, confirm that the font is enabled in Font Book. On Windows, check the system font settings. On Linux, refresh the font cache and restart the app.

### Some characters still use another font after selection

The selected font may not contain those characters, so the system is using a fallback font. Choose a font that covers the target language or the corresponding CJK regional variant.

### Chinese or Japanese glyphs look wrong

Check whether you selected the wrong `SC`, `TC`, or `JP` version. Similar names do not imply the same glyph standard.

### Code columns are not aligned

Confirm that the selected font is monospaced and check whether the code contains unsupported CJK or special characters. A fallback font can break monospace alignment.

### The font is too large or too small

Font family and font size are separate. If the entire interface is too large or small, adjust interface zoom on the same page. If only message text is unsuitable, adjust the message font size.

***

### Get Help and Submit Feedback

If you encounter a problem during configuration or use, contact us through the official channels under [Feedback and Suggestions](../question-contact/suggestions.md).
