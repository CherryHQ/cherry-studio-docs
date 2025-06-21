
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# LLM Arena Rangliste (Echtzeitaktualisierung)

Diese Rangliste basiert auf Daten von Chatbot Arena (lmarena.ai) und wird automatisch generiert.

> **Datenaktualisierungszeit**: 2025-06-21 09:44:44 UTC / 2025-06-21 17:44:44 CST (Peking-Zeit)

{% hint style="info" %}
Klicken Sie auf den **Modellnamen** in der Rangliste, um zu dessen Detailseite oder Testseite zu gelangen.
{% endhint %}

## Rangliste

|   Rang (UB) |   Rang (StyleCtrl) | Modellname                                                                                                                                       |   Punkte | Konfidenzintervall | Stimmen      | Anbieter                    | Lizenz                   | Wissensstand   |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro-Preview-06-05](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-06-05)                        | 1480 | +6/-6   | 8,825   | Google                 | Proprietary             | Keine Daten     |
|        ... |               ... | ...                                                                                                                                             | ...  | ...     | ...     | ...                    | ...                     | ...          |
|      201 |             201 | [FastChat-T5-3B](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0)                                                                        |  883 | +8/-12  | 4,288   | LMSYS                  | Apache 2.0              | 2023/4   |
|      203 |             204 | [StableLM-Tuned-Alpha-7B](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)                                                     |  855 | +11/-14 | 3,336   | Stability AI           | CC-BY-NC-SA-4.0         | 2023/4   |
|      203 |             201 | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                                            |  838 | +11/-12 | 3,480   | Databricks             | MIT                     | 2023/4   |
|      204 |             202 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                             |  815 | +12/-10 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## Erläuterungen

- **Rang (UB)**: Rang basierend auf dem Bradley-Terry-Modell. Diese Rangordnung spiegelt die Gesamtleistung des Modells in der Arena wider und liefert eine **obere Grenzschätzung** der Elo-Punktzahl, um das Wettbewerbspotenzial zu verstehen.
- **Rang (StyleCtrl)**: Rang nach Kontrolle des Gesprächsstils. Ziel ist es, Verzerrungen durch Antwortstile (z.B. ausführlich/knapp) zu reduzieren und die Kernfähigkeiten reiner zu bewerten.
- **Modellname**: Name des Large Language Models (LLM). Enthält verlinkte Referenzen.
- **Punkte**: Elo-Bewertung basierend auf Nutzervotes. Höhere Werte zeigen bessere Leistung. Dynamisch und spiegelt relative Stärke im Wettbewerbsumfeld wider.
- **Konfidenzintervall**: 95%-Konfidenzintervall der Elo-Punktzahl (z.B. `+6/-6`). Kleinere Intervalle deuten auf stabilere Bewertungen hin. Quantifiziert die Bewertungsgenauigkeit.
- **Stimmen**: Gesamtzahl der erhaltenen Votes. Höhere Zahlen erhöhen meist die statistische Zuverlässigkeit.
- **Anbieter**: Entwicklungsorganisation oder Unternehmen.
- **Lizenz**: Lizenztyp (z.B. Proprietär, Apache 2.0, MIT).
- **Wissensstand**: Trainingsdaten-Abschneidedatum. **Keine Daten** bedeutet unbekannt oder nicht angegeben.

## Datenquelle und Aktualisierungsfrequenz

Daten werden automatisch vom Projekt [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) generiert, das Informationen von [lmarena.ai](https://lmarena.ai/) bezieht. Diese Rangliste wird täglich via GitHub Actions aktualisiert.

## Haftungsausschluss

Dieser Bericht dient nur zu Informationszwecken. Die Ranglistendaten sind dynamisch und basieren auf Nutzerpräferenzen im Chatbot Arena während bestimmter Zeiträume. Datenintegrität und -genauigkeit hängen von Quellendaten und der Verarbeitung durch `fboulnois/llm-leaderboard-csv` ab. Unterschiedliche Modelle haben unterschiedliche Lizenzen – bitte beachten Sie die offiziellen Hinweise der Anbieter.