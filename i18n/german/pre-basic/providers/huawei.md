
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Huawei Cloud

1.  Gehen Sie zu [Huawei Cloud](https://auth.huaweicloud.com/authui/login), um ein Konto zu erstellen und sich anzumelden

2.  Klicken Sie auf [diesen Link](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage), um die MaaS-Konsole aufzurufen

3.  Autorisierung

<details>

<summary>Autorisierungsschritte (bereits autorisiert? Überspringen)</summary>

1.  Nach dem Aufruf der Seite aus Schritt 2: Gemäß der Aufforderung zur Autorisierungsseite navigieren (IAM-Unterbenutzer → Delegierten hinzufügen → Normaler Benutzer klicken)

![](<../../.gitbook/assets/image (49).png>)

2.  Nach dem Klicken auf "Erstellen" zur Seite aus Schritt 2 zurückkehren  
3.  Warnung über unzureichende Zugriffsberechtigung erhalten: "Hier klicken" in der Aufforderung auswählen  
4.  Bestehende Autorisierung hinzufügen und bestätigen  

![](<../../.gitbook/assets/image (50).png>)

Hinweis: Diese Methode eignet sich für Einsteiger. Sie müssen keine umfangreichen Inhalte lesen – folgen Sie einfach den Aufforderungen. Wenn Sie die Autorisierung problemlos durchführen können, führen Sie sie nach eigenem Ermessen durch.

</details>

4.  In der Seitenleiste "Berechtigungsmanagement" auswählen: API-Schlüssel erstellen und kopieren

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Dann neuen Anbieter in CherryStudio anlegen  

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Nach dem Anlegen den Schlüssel einfügen  

5.  In der Seitenleiste "Modellbereitstellung" wählen: Alle Ressourcen einlösen  

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

6.  Auf "Aufrufen" klicken  

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Adresse an Position ① kopieren und in die Anbieteradresse von CherryStudio einfügen. Am Ende ein "#" hinzufügen  
Am Ende ein "#" hinzufügen  
Am Ende ein "#" hinzufügen  
Am Ende ein "#" hinzufügen  
Am Ende ein "#" hinzufügen  

Warum ein "#"? [Hier nachlesen](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)  

> Selbstverständlich können Sie den Link ignorieren und einfach dem Tutorial folgen;  
> Alternativ können Sie die Methode zum Entfernen von v1/chat/completions verwenden – wenn Sie sich auskennen, ist jede Vorgehensweise akzeptabel. Bei Unsicherheit unbedingt dem Tutorial folgen.  

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Dann den Modellnamen an Position ② kopieren. In CherryStudio auf "+ Hinzufügen" klicken, um ein neues Modell anzulegen  

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>  

Modellnamen eingeben: Keine Ergänzungen, keine Anführungszeichen – exakt wie im Beispiel kopieren.  

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>  

Auf "Modell hinzufügen" klicken, um den Vorgang abzuschließen.  

{% hint style="info" %}
In Huawei Cloud benötigt jedes Modell einen eigenen Anbieter, da die Adressen variieren. Wiederholen Sie daher die obigen Schritte für jedes Modell.  
{% endhint %}