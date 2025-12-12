# Info Security Plan

# Datenschutz, DSGVO, Meilenstein 17

## 1 Zweck und Zielsetzung

Dieses Dokument beschreibt die Informationssicherheits‑ und Datenschutzmaßnahmen des HASKI‑Projekts mit Fokus auf die Anforderungen der Datenschutz‑Grundverordnung (DSGVO) und relevanter ISO/IEC‑Normen. Es dient als Leitlinie für Entwicklung, Betrieb und Kooperation mit Projektpartnern (z. B. Hochschulen, NodeGrade, LAAC, Moodle‑Betreiber:innen).

Ziele:

- Schutz der Vertraulichkeit, Integrität und Verfügbarkeit personenbezogener und studienrelevanter Daten,
- rechtssichere Verarbeitung gemäß DSGVO (insbesondere Art. 5, 6, 25, 32),
- technische und organisatorische Maßnahmen (TOM) für HASKI‑Backend, HASKI‑Frontend, NodeGrade, LAAC und Moodle‑xAPI‑Plugin,
- Unterstützung der Anforderungen aus SyRS‑SEC und den SRS‑Anforderungen (z. B. HASKI‑REQ‑0001, 0030).

## 2 Geltungsbereich

Der Info‑Security‑Plan umfasst:

- das HASKI‑System (Backend, Frontend, Datenbank und Dokumentations‑/Traceability‑Infrastruktur),
- angebundene Systeme im Rahmen des Projekts:
  - NodeGrade (Bewertungs‑/Grading‑Komponente),
  - LAAC (Learning Analytics Analyzing Center),
  - Moodle‑Instanzen der beteiligten Hochschulen inkl. Moodle‑xAPI‑Plugin.

Die konkreten Verantwortlichkeiten an den Schnittstellen werden vertraglich bzw. durch Datenverarbeitungsvereinbarungen (Auftragsverarbeitung/Joint Controllership) geregelt.

## 3 Rechtsgrundlagen und Rollen

- **Rechtsgrundlagen (Beispiele)**

  - Art. 6 Abs. 1 lit. e, f DSGVO (Aufgaben im öffentlichen Interesse, berechtigtes Interesse),
  - Art. 6 Abs. 1 lit. a DSGVO (Einwilligung, z. B. zu erweiterten Analysen),
  - Art. 9 DSGVO, soweit besondere Kategorien personenbezogener Daten betroffen sein könnten (i. d. R. vermeiden).

- **Rollen im Datenschutzkontext**
  - Verantwortliche Stelle(n): beteiligte Hochschulen/Projektträger (gemäß Vereinbarung),
  - Auftragsverarbeiter: HASKI‑Betriebseinheit, ggf. Hosting‑Provider,
  - Mitverantwortliche: Partner wie NodeGrade, LAAC, sofern gemeinsame Zwecke/Mittel bestehen.

## 4 Datenschutzprinzipien (Art. 5 DSGVO)

HASKI orientiert sich an folgenden Grundsätzen:

- Rechtmäßigkeit, Verarbeitung nach dokumentierten Zwecken (Lehre, Evaluation, Forschung),
- Datenminimierung (nur notwendige Merkmale),
- Speicherbegrenzung (Lösch‑/Anonymisierungskonzepte),
- Richtigkeit (Korrekturmöglichkeiten für Nutzer:innen),
- Integrität und Vertraulichkeit (technische und organisatorische Maßnahmen).

Umsetzung in den Anforderungen u. a. durch:

- HASKI‑REQ‑0001 (Einwilligung/Datenschutzhinweise vor Nutzung, Anonymisierung/Pseudonymisierung),
- HASKI‑REQ‑0030 (Verfügbarkeit/Resilienz der Plattform),
- weitere Sicherheits‑ und Protokollierungsanforderungen in SyRS‑SEC.

## 5 Technische und organisatorische Maßnahmen (TOM)

### 5.1 Zugriffskontrolle und Authentifizierung

- Zugriff auf HASKI primär über LTI/OIDC‑basierte Authentifizierung aus Moodle.
- Rollen‑ und Rechtemodell (Studierende, Lehrende, Administrator:innen) im Backend; minimale Rechtevergabe.
- Administrativer Zugriff auf Server/Repos nur für autorisierte Personen (z. B. SSH‑Keys, MFA für GitHub).

### 5.2 Transport- und Speichersicherheit

- Verpflichtende TLS‑Verschlüsselung für alle HTTP‑Verbindungen zwischen Browser, HASKI, NodeGrade, LAAC und Moodle.
- Verschlüsselte Speicherung sensibler Identifikatoren (z. B. Pseudonymisierungs‑Mapping‑Tabellen) im Backend.
- Regelmäßige Datensicherungen (Backups) und dokumentierte Wiederherstellungsprozesse (vgl. `CM-Plan.md`).

### 5.3 Pseudonymisierung und Anonymisierung

- Umsetzung gemäß HASKI‑REQ‑0001 (erweiterte Fassung):
  - Pseudonymisierung von Lern‑ und Nutzungsdaten: Trennung von direkten Identifikatoren und Nutzungsdaten, verschlüsselte Zuordnungstabellen mit streng beschränktem Zugriff.
  - Möglichkeit zur Voll‑Anonymisierung für Forschungszwecke (Entfernung aller Zuordnungsinformationen).
- LAAC und NodeGrade arbeiten nach Möglichkeit auf pseudonymisierten bzw. anonymisierten Datensätzen; Re‑Identifikation wird technisch/organisatorisch verhindert.

### 5.4 Logging, Monitoring und Incident-Handling

- Protokollierung sicherheitsrelevanter Ereignisse (z. B. Anmeldeversuche, Rollenänderungen, Fehlersituationen an Schnittstellen).
- Monitoring von Verfügbarkeit und Performance (vgl. HASKI‑REQ‑0030) mit Alarmierung bei Abweichungen.
- Definierter Incident‑Response‑Prozess (Erkennung, Meldung, Analyse, Behebung, Lessons Learned); Dokumentation von Datenschutzvorfällen gemäß Art. 33/34 DSGVO.

### 5.5 Rechte der Betroffenen

- Prozesse zur Auskunft, Berichtigung, Löschung, Einschränkung und Datenübertragbarkeit werden auf Ebene der verantwortlichen Hochschulen beschrieben.
- HASKI stellt technische Funktionen bereit, um:
  - Nutzerkonten zu löschen oder zu anonymisieren,
  - Analytics‑/Lernpfad‑Daten pro Person zurückzusetzen (vgl. Tests wie `test_reset_knowledge_by_student_id`, `test_reset_learning_analytics_by_student_id`).

## 6 Datenschutz-Folgenabschätzung (DSFA)

Für Szenarien mit hohem Risiko (z. B. umfassende Learning‑Analytics‑Auswertungen, Profiling, externe Datenanreicherungen) ist durch die verantwortliche Stelle eine Datenschutz‑Folgenabschätzung nach Art. 35 DSGVO durchzuführen. HASKI unterstützt dies durch:

- transparente Dokumentation der verarbeiteten Datenkategorien und Verarbeitungszwecke,
- technische Optionen zur Pseudonymisierung/Anonymisierung,
- Protokollierung von Datenflüssen (z. B. Richtung NodeGrade, LAAC).

## 7 Zusammenarbeit mit Partnern (NodeGrade, LAAC, Moodle)

- Abschluss geeigneter Verträge (Auftragsverarbeitung oder gemeinsame Verantwortlichkeit) zwischen Hochschulen, HASKI‑Betrieb und Partnern.
- Festlegung von Verantwortlichkeiten für:
  - Betroffenenanfragen,
  - technische Sicherheit,
  - Logging und Incident‑Handling.
- Dokumentation der Schnittstellen (z. B. xAPI‑Events, Datenexporte) in Architektur‑/Designdokumenten und im Verzeichnis von Verarbeitungstätigkeiten der jeweiligen Verantwortlichen.

## 8 Schulung und Sensibilisierung

- Regelmäßige Schulungen für Entwicklungsteam und Betrieb zu Secure Coding, DSGVO‑Grundlagen und internen Richtlinien.
- Sensibilisierung der Lehrenden/Administrator:innen für den Umgang mit Reports, Analytics‑Daten und Exporten.

## 9 Pflege und Review dieses Plans

Der Info‑Security‑Plan wird mindestens zu folgenden Anlässen überprüft und bei Bedarf aktualisiert:

- wesentliche Architektur‑ oder Technologieänderungen (z. B. neue Integrationen oder Hosting‑Modelle),
- Einführung neuer Features mit Datenschutz‑Relevanz (z. B. zusätzliche Analytics‑Auswertungen),
- Ergebnisse aus Audits, Penetrationstests oder Datenschutzvorfällen.

Die Verantwortung für die Pflege liegt bei der Projektleitung in Abstimmung mit Datenschutzbeauftragten und Informationssicherheitsverantwortlichen der beteiligten Institutionen.
