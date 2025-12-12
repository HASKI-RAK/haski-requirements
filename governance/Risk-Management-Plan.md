# Risikomanagement-Plan

# ISO 16085 / Projektrisiken / KI-Risiken

## 1 Zweck und Zielsetzung

Dieser Risikomanagement‑Plan beschreibt das systematische Vorgehen zur Identifikation, Bewertung, Behandlung und Überwachung von Risiken im HASKI‑Projekt, basierend auf ISO/IEC 16085 und ergänzenden Leitlinien zu KI‑Systemen.

Ziele:

- frühzeitige Erkennung von Projektrisiken, Betriebs‑ und Sicherheitsrisiken,
- besonderer Fokus auf Risiken durch KI‑basierte Adaptivität und Learning Analytics,
- Transparenz gegenüber Fördergebern, Partnern und internen Stakeholdern,
- Verzahnung mit Qualitätsmanagement, Info‑Security‑ und CM‑Plan.

## 2 Geltungsbereich

Der Plan umfasst:

- die Entwicklung und den Betrieb des HASKI‑Systems (Backend, Frontend, Datenhaltung),
- Integrationen zu NodeGrade, LAAC und Moodle (inkl. xAPI‑Plugin),
- organisatorische Abläufe im Projekt (z. B. Anforderungsmanagement, Release‑Prozess, Betrieb).

## 3 Normative Referenzen

- ISO/IEC 16085 – System and software engineering — Life cycle processes — Risk management
- ISO/IEC/IEEE 12207 – Software lifecycle processes
- ISO/IEC 27005 – Information security risk management (für Sicherheits‑/Datenschutzrisiken)
- EU‑Leitlinien zu vertrauenswürdiger KI (High-Level Expert Group on AI)
- Projektinterne Dokumente:
  - `governance/Project-Plan.md`
  - `governance/Info-Security-Plan.md`
  - `governance/CM-Plan.md`
  - `syrs/SyRS.md`, `srs/SRS.md`

## 4 Rollen und Verantwortlichkeiten

- **Projektleitung** – übergeordnete Verantwortung, Risikoakzeptanz, Eskalation.
- **Risikomanager:in** (kann in Personalunion mit Projektleitung erfolgen) – Pflege des Risikoregisters, Koordination von Bewertungen und Maßnahmen.
- **Teilprojektleitungen / Work‑Package‑Leads** – Identifikation fachspezifischer Risiken (Backend, Frontend, Analytics, Integration, Evaluation).
- **Datenschutz‑ und Informationssicherheitsbeauftragte** – Bewertung von Datenschutz‑/Security‑Risiken und Kontrollen.
- **Entwicklungsteams** – Meldung technischer Risiken, Einschätzung von Aufwänden/Workarounds.

## 5 Vorgehensmodell im Risikomanagement

Risikomanagement wird iterativ in folgenden Schritten durchgeführt:

1. **Identifikation** – Sammlung potenzieller Risiken (Workshops, Reviews, Lessons Learned, Ticket‑Analyse).
2. **Analyse und Bewertung** – Einschätzung der Eintrittswahrscheinlichkeit und Auswirkung (z. B. Skala 1–5), Ableitung eines Risikolevels.
3. **Planung von Maßnahmen** – Definition von Vermeidungs‑, Reduktions‑, Transfer‑ oder Akzeptanzstrategien.
4. **Umsetzung und Verfolgung** – Zuweisung von Verantwortlichkeiten, Terminierung, Überwachung der Wirksamkeit.
5. **Monitoring und Review** – regelmäßige Aktualisierung des Risikoregisters (z. B. in Meilenstein‑Meetings), Anpassung der Bewertungen.

Das Risikoregister wird projektweit gepflegt (z. B. in einem gemeinsam genutzten Dokument oder Issue‑Board) und verweist bei Bedarf auf detaillierte Analysen oder technische Tickets.

## 6 Risikoarten

- **Projekt‑/Managementrisiken** – Zeitplan, Budget, Personalfluktuation, Abstimmung mit Partnern.
- **Technische Risiken** – Architekturentscheidungen, Performance, Skalierbarkeit, technische Schulden.
- **Integrationsrisiken** – Abhängigkeiten von Moodle‑Versionen, NodeGrade‑/LAAC‑Schnittstellen, xAPI‑Eventqualität.
- **Sicherheits‑ und Datenschutzrisiken** – Datenlecks, Fehlkonfigurationen, unzureichende Pseudonymisierung/Anonymisierung.
- **KI‑spezifische Risiken** – Bias in Algorithmen, unerwartete Lernpfade, mangelnde Erklärbarkeit.
- **Betriebsrisiken** – Verfügbarkeit (insbesondere in Prüfungsphasen), Backup/Wiederherstellung.

## 7 Beispielhafte Risiken und Maßnahmen (Auszug)

| ID  | Risiko                                       | Kategorie      | Eintritt | Auswirkung | Level  | Maßnahmen/Controls                                                  | Verantwortlich     |
| --- | -------------------------------------------- | -------------- | -------- | ---------- | ------ | ------------------------------------------------------------------- | ------------------ |
| R1  | Verzögerungen bei Moodle‑Integration         | Integration    | Mittel   | Hoch       | Hoch   | Frühe Test‑Instanzen, enge Abstimmung mit IT der Hochschule         | TP‑Leitung Backend |
| R2  | Sicherheitslücke im Moodle‑xAPI‑Plugin       | Security       | Niedrig  | Sehr hoch  | Hoch   | Security‑Reviews, Updates, Pen‑Tests, Fallback ohne xAPI            | InfoSec/DevOps     |
| R3  | Unzureichende Pseudonymisierung in Analytics | Datenschutz/KI | Mittel   | Hoch       | Hoch   | Technische Kontrollen gem. Info‑Security‑Plan, Reviews mit DSB      | LAAC/Backend       |
| R4  | Unerwartete Algorithmus‑Bias                 | KI             | Mittel   | Mittel     | Mittel | Testdaten‑Analysen, Monitoring von Outcomes, manuelle Reviews       | Tutoring‑Team      |
| R5  | Ausfall in Prüfungsphase                     | Betrieb        | Niedrig  | Sehr hoch  | Hoch   | Redundanz, Monitoring/Alerting, Notfall‑Prozeduren (HASKI‑REQ‑0030) | DevOps/Operations  |

Die vollständige und fortgeschriebene Liste wird außerhalb dieses Plans geführt.

## 8 Schnittstellen zu anderen Plänen

- **Info-Security-Plan** – liefert Kontrollen und Maßnahmen für Sicherheits‑/Datenschutzrisiken.
- **CM-Plan** – reduziert Risiken durch unkontrollierte Änderungen und unklare Versionen.
- **Project-Plan** – enthält Meilensteine, auf deren Basis zeitliche Risiken bewertet werden.

## 9 Pflege und Review

Der Risikomanagement‑Plan wird bei wesentlichen Änderungen im Projekt (z. B. neue Partner, geänderte Architektur, neue KI‑Funktionalitäten) überprüft und angepasst. Mindestens zu jedem Haupt‑Meilenstein findet ein formelles Risiko‑Review statt.

Verantwortlich für die Aktualisierung sind Projektleitung und Risikomanager:in in Abstimmung mit allen Teilprojekten.
