---
icon: download
---

# Client Downloads

Cherry Studio provides installation packages for Windows, macOS, and Linux. To keep specific version numbers from becoming outdated, this page lists only permanent official entry points. After opening a download page, select the latest stable release and a file that matches your system architecture.

## Official download links

* [Cherry Studio website download page](https://cherry-ai.com/download)
* [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases)
* [Latest stable release on GitHub](https://github.com/CherryHQ/cherry-studio/releases/latest)

{% hint style="warning" %}
Download installation packages only from the Cherry Studio website, the official `CherryHQ/cherry-studio` repository, or a mirror explicitly listed on the download page. Do not run an installer from an unknown source, one that has been repackaged, or one that asks you to disable security software.
{% endhint %}

## Choose a stable or preview release

| Type | How to identify it | Recommended for |
| :--- | :--- | :--- |
| Stable release | Marked **Latest** in GitHub Releases; the version number usually does not include `alpha`, `beta`, or `rc` | Everyday use; recommended |
| Pre-release | Marked **Pre-release**; the version number may include `alpha`, `beta`, or `rc` | Users who want to test new features early |
| Daily preview build | From the official [V2 Daily Preview Build](https://github.com/CherryHQ/cherry-studio/actions/workflows/v2-daily-preview-build.yml) | Development, testing, and issue reproduction |

A preview release may contain unfinished data migrations, interface changes, or compatibility changes. Back up your data before installation, and prefer a stable release for environments with important data.

## Windows

### Choose an architecture

Open **Settings → System → About** and check “System type”:

* If it shows `x64` or “x64-based processor,” download `x64`.
* If it shows `ARM64` or “ARM-based processor,” download `arm64`.

Most Intel and AMD computers use `x64`. Only Windows on ARM devices use `arm64`.

### Choose a package

| File type | Description |
| :--- | :--- |
| `*-x64-setup.exe` / `*-arm64-setup.exe` | Installer; lets you choose the installation directory and creates shortcuts |
| `*-x64-portable.exe` / `*-arm64-portable.exe` | Portable version; suitable when you do not want to run an installation process |

{% hint style="warning" %}
Cherry Studio does not support Windows 7. Install it on a supported version of Windows.
{% endhint %}

See the [Windows Installation Guide](../pre-basic/installation/windows.md) for installation steps and operating system security prompts.

## macOS

Open **Apple menu → About This Mac** and check “Chip” or “Processor”:

* If it shows an Apple M-series chip, download `arm64`.
* If it shows an Intel processor, download `x64`.

| File type | Description |
| :--- | :--- |
| `*-arm64.dmg` / `*-x64.dmg` | Recommended graphical installer |
| `*-arm64.zip` / `*-x64.zip` | Compressed archive |

Apple Silicon packages support Apple chips such as M1, M2, M3, and M4. If you choose the wrong architecture, the application may not open or may run only through a compatibility layer.

See the [macOS Installation Guide](../pre-basic/installation/macos.md) for installation steps and prompts such as “developer cannot be verified.”

## Linux

Run the following in a terminal:

```bash
uname -m
```

* If the output is `x86_64`, select `x86_64` or `amd64`.
* If the output is `aarch64` / `arm64`, select `arm64` / `aarch64`.

Official releases usually provide:

| File type | Recommended use |
| :--- | :--- |
| `.AppImage` | Run directly across distributions |
| `.deb` | Debian, Ubuntu, and their derivatives |
| `.rpm` | Fedora, RHEL, Rocky Linux, and other RPM-based distributions |

Architecture labels vary by format. For example, x64 is often written as `amd64` in a `.deb` filename and may appear as `x86_64` in an AppImage filename.

## Verify the download

1. Confirm that the file came from an official domain or `github.com/CherryHQ/cherry-studio`.
2. Recheck the operating system, architecture, and package format.
3. If the release page provides a SHA-256 digest, compare it with the local file digest before running the file.
4. Back up Cherry Studio data before updating to or testing a preview release.

### Calculate SHA-256

{% tabs %}
{% tab title="Windows PowerShell" %}
```powershell
Get-FileHash .\Cherry-Studio-installer-filename -Algorithm SHA256
```
{% endtab %}

{% tab title="macOS" %}
```bash
shasum -a 256 ~/Downloads/Cherry-Studio-installer-filename
```
{% endtab %}

{% tab title="Linux" %}
```bash
sha256sum ~/Downloads/Cherry-Studio-installer-filename
```
{% endtab %}
{% endtabs %}

The output must exactly match the SHA-256 value for the corresponding file in the official release. If it does not match, do not run the file; download it again from an official source.

## Next steps

* [Installation Guide](../pre-basic/installation/)
* [Configure Model Services](../pre-basic/providers/)
* [Chat](preview/chat.md)
