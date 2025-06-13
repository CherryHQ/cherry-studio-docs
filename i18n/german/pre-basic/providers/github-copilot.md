
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# GitHub Copilot

Zur Verwendung von GitHub Copilot benötigen Sie zunächst einen GitHub-Account und ein Abonnement für GitHub Copilot. Auch die kostenlose Version ist möglich, jedoch unterstützt diese nicht das neueste Claude-3.7-Modell. Details finden Sie auf der [GitHub Copilot Website](https://github.com/features/copilot).

## Device Code abrufen

Klicken Sie auf "Login GitHub", um einen Device Code zu generieren und zu kopieren.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Beispielbild zum Abrufen des Device Codes"><figcaption><p>Device Code abrufen</p></figcaption></figure>

## Device Code im Browser eingeben und autorisieren

Nach erfolgreichem Abrufen klicken Sie auf den Link, um den Browser zu öffnen. Melden Sie sich mit Ihrem GitHub-Konto an, geben Sie den Device Code ein und erteilen Sie die Berechtigung.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Beispielbild zur GitHub-Autorisierung"><figcaption><p>GitHub-Autorisierung</p></figcaption></figure>

Nach erfolgreicher Autorisierung kehren Sie zu Cherry Studio zurück, klicken auf "Connect GitHub". Bei Erfolg werden Ihr GitHub-Benutzername und Avatar angezeigt.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Beispielbild zur erfolgreichen GitHub-Verbindung"><figcaption><p>GitHub-Verbindung erfolgreich</p></figcaption></figure>

## Modellliste über "Manage" abrufen

Klicken Sie auf den unteren Button "Manage", um automatisch die aktuell unterstützte Modellliste abzurufen.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Beispielbild zum Abrufen der Modellliste"><figcaption><p>Modellliste abrufen</p></figcaption></figure>

## Häufige Fragen

### Abrufen des Device Codes fehlgeschlagen. Bitte versuchen Sie es erneut.

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Beispielbild für fehlgeschlagenen Device-Code-Abruf"><figcaption><p>Device Code konnte nicht abgerufen werden</p></figcaption></figure>

Aktuell werden Anfragen über Axios gestellt, das keine SOCKS-Proxy unterstützt. Bitte verwenden Sie System-Proxy oder HTTP-Proxy, oder setzen Sie in CherryStudio gar keinen Proxy, sondern nutzen einen systemweiten Proxy. Stellen Sie zunächst sicher, dass Ihre Internetverbindung funktioniert, um Fehler beim Abrufen des Device Codes zu vermeiden.