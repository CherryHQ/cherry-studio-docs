---
icon: scale-balanced
---

# Cherry Studio Open Source License

The Cherry Studio Community Edition code repository uses the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

The following legal texts are authoritative:

* [LICENSE in the Cherry Studio repository](https://github.com/CherryHQ/cherry-studio/blob/main/LICENSE)
* [Official GNU AGPL v3.0 text](https://www.gnu.org/licenses/agpl-3.0.html)

{% hint style="warning" %}
This page is provided to aid understanding. It is not legal advice and does not amend or replace AGPL-3.0. Actual obligations depend on how the software is used, modified, distributed, and provided over a network. Consult your organization’s legal counsel if you have questions.
{% endhint %}

## Three conclusions to understand first

1. **Open source does not prohibit commercial use.** The official Cherry Studio repository explicitly permits commercial use of the Community Edition when AGPL-3.0 is followed in full.
2. **Commercial use does not automatically permit closed source.** Modifying, distributing, or providing functionality to others over a network may trigger source-code, license-notice, and network-interaction obligations.
3. **Apply for a commercial license if you need exemptions from AGPL-3.0 requirements.** A commercial license is a separate agreement and is not granted by this page.

## What AGPL-3.0 permits

Subject to compliance with the license, AGPL-3.0 permits you to:

* Run the software.
* Read and study the source code.
* Modify the software.
* Copy and redistribute the original or a modified version.
* Charge for the software or use it in a commercial environment.

“Free software” describes the freedom to use, study, modify, and share software. It does not mean that every service, deployment, or support offering must be free of charge.

## When to examine obligations carefully

| Scenario | What to review carefully |
| :--- | :--- |
| Run the official version only on your own device | The full LICENSE, third-party component licenses, disclaimers |
| Use a modified version inside your organization | Scope of modifications, who can access it, whether distribution or remote network interaction occurs |
| Distribute an installer to customers or another party | Notices, license text, and Corresponding Source requirements in AGPL Sections 4–6 |
| Distribute a modified version | Modification notices, licensing under the same license, Corresponding Source |
| Let users interact with a modified version over a network | The AGPL Section 13 requirement to offer Corresponding Source to remote users |
| Integrate it into a closed-source product or service | Work boundaries, form of combination, dependencies, and whether a commercial license is needed |

{% hint style="info" %}
Labels such as “internal use,” “network service,” “plugin,” “separate process,” or “only a small code change” are not enough by themselves to determine compliance. Evaluate the actual architecture, recipients, and applicable law.
{% endhint %}

## Common obligations when distributing software

When distributing Cherry Studio or a modified version, you generally need to consider:

* Preserving applicable copyright and license notices.
* Providing recipients with the AGPL-3.0 license text.
* Clearly marking modified versions and relevant dates.
* Licensing the complete covered work under AGPL-3.0.
* Providing Corresponding Source in a manner permitted by the license.
* Not imposing additional restrictions that conflict with AGPL-3.0.
* Not using technical measures to prevent recipients from exercising rights granted by the license.

Refer to the original text of LICENSE Sections 4–7 for specific requirements and permitted methods of providing source code.

## Providing a modified version over a network

Remote network interaction is one important difference between AGPL-3.0 and GPL v3.

If you modify the program and let users interact with that modified version remotely through a computer network, and that version supports such interaction, AGPL Section 13 requires a prominent opportunity for those users to obtain the version’s **Corresponding Source**. It must be offered from a network server at no charge through a standard or customary means of copying software.

This requirement should not be simplified to “all server code must be public,” nor to “there are no obligations if no installer is distributed.” You need to determine which code constitutes the covered work and its Corresponding Source.

## What is Corresponding Source?

Corresponding Source is not an arbitrary source archive. The license defines it as the preferred form of the work for making modifications and may also include:

* Source code needed to generate, install, and run the object code.
* Scripts that control those activities.
* Interface definitions and related source code on which the work specifically depends.
* Your modifications to the covered work.

System libraries, general-purpose tools, and parts that can be regenerated automatically from other source code may be excluded under the license definitions. Verify this against the actual build and delivery process.

## Third-party components and content

The Cherry Studio repository and installer may contain dependencies, fonts, icons, model information, or other resources under different licenses.

AGPL-3.0 applies to Cherry Studio code that it covers; it does not automatically replace the independent licenses of third-party components. Before redistribution, also inspect:

* Third-party notices included with the repository and installer.
* Each dependency’s own license and NOTICE requirements.
* Separate licenses for trademarks, Logos, images, fonts, and datasets.
* Whether you have the right to redistribute the code and resources you add.

## Trademarks and branding

A software license does not grant trademark rights to the Cherry Studio name, Logo, or other brand assets.

Before releasing a derivative product, repackaging an installer, promoting a partnership, or using official brand materials, confirm the permitted scope of brand use. Do not lead users to believe that a derivative version was officially released or endorsed by Cherry Studio.

## No warranty and limitation of liability

AGPL-3.0 Sections 15–17 contain disclaimers of warranty and limitations of liability. To the extent permitted by law, the software is provided as-is, and the user assumes the risks of quality, performance, and fitness.

If your organization requires a service level, indemnification, dedicated support, or other assurances, establish them in a separate commercial contract instead of inferring them from the open source license.

## Commercial license

If your use cannot comply with AGPL-3.0, or if you need commercial authorization exempt from some of its requirements, contact:

**[bd@cherry-ai.com](mailto:bd@cherry-ai.com)**

In your business inquiry, describe:

* Your organization and product.
* Number of users and deployment scope.
* Whether you modify or redistribute Cherry Studio.
* Whether you provide functionality to customers or users over a network.
* How it is integrated with other closed-source systems.
* The specific exemptions or additional terms you need.

See [Business inquiries](../questions.md) for contact guidance.

{% hint style="warning" %}
Only a commercial license agreement formally signed by both parties determines the scope of commercial authorization. A price inquiry, email exchange, or this page does not itself grant a license.
{% endhint %}

## Compliance checklist

Before a release or launch, confirm at least:

- [ ] The Cherry Studio version and corresponding LICENSE are recorded.
- [ ] Modified files, modification dates, and build sources are traceable.
- [ ] Distribution recipients and remote network users are identified.
- [ ] The covered work and scope of Corresponding Source are determined.
- [ ] The source-code offer satisfies the license requirements and its link works.
- [ ] Required notices remain in the installer, interface, and documentation.
- [ ] Third-party dependencies, assets, and trademark licenses were reviewed separately.
- [ ] Qualified legal advice was obtained for closed-source integration or unclear boundaries.
- [ ] If an exemption is needed, the commercial license has been formally signed.

## Further reading

* [Official GNU AGPL v3.0 text](https://www.gnu.org/licenses/agpl-3.0.html)
* [Why the GNU Affero GPL](https://www.gnu.org/licenses/why-affero-gpl.html)
* [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.html)
* [Cherry Studio source repository](https://github.com/CherryHQ/cherry-studio)
