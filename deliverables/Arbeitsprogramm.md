# Arbeitsprogramm HASKI

## Arbeitspakete 1–7

## Zweck und Geltungsbereich

Dieses Arbeitsprogramm beschreibt die inhaltlichen Ziele, Aufgaben, Ergebnisse und Abhängigkeiten der Arbeitspakete (AP) 1–7 im Verbundprojekt **„Hochschullehre: Adaptiv, selbstgesteuert, KI-gestützt (HASKI)”**.

Es dient als Grundlage für:

- die Erstellung und Priorisierung von Requirements,
- die operative Planung pro Semester,
- die Abstimmung zwischen den Verbundpartnern
  - Ostbayerische Technische Hochschule Regensburg (OTH R)
  - Technische Hochschule Aschaffenburg (TH AB)
  - Hochschule Kempten (HKE).

---

## Übersicht Arbeitspakete

- **AP 1** – Entwicklung der Modelle (Lernenden-, Tutorielles und Domänen-Modell)
- **AP 2** – Erstellung des HASKI-Systems
- **AP 3** – Erstellung der Moodle-/LMS-Elemente
- **AP 4** – Datenschutz und Datensicherheit
- **AP 5** – Lernräume entwickeln und Erprobung von HASKI
- **AP 6** – Evaluation und Reflexion der Erprobung
- **AP 7** – Dissemination und Transfer

---

## AP 1 – Entwicklung der Modelle

### Ziel

Aufbau und fortlaufende Weiterentwicklung der drei Kernmodelle von HASKI:

- **Lernenden-Modell** (Lerntypen, Lernstände, Präferenzen)
- **Domänen-Modell** (fachliche Inhalte, Aufgaben, Lernressourcen)
- **Tutorielles Modell** (Lernpfade, Feedback-Logik, Prüfungs- und Unterstützungsstrategien)

Die Modelle bilden die fachlich-didaktische und KI-bezogene Grundlage für AP 2, AP 3 und AP 5.

### Beschreibung

- Gemeinsame, standortübergreifende Modellierung für die relevanten Lehrveranstaltungen (z. B. Informatik‑Grundlagen, Software Engineering in verschiedenen Studiengängen).
- Iterative Überarbeitung der Modelle pro Semester auf Basis der Erkenntnisse aus AP 5 (Erprobung) und AP 6 (Evaluation).
- Sicherstellung, dass die Modelle sowohl didaktische Anforderungen (Kompetenzorientierung, Micro-Learning, formative Prüfung) als auch technische Anforderungen (maschinelle Verarbeitbarkeit, Schnittstellen zu HASKI-System und LMS) erfüllen.

### Zentrale Arbeitsschritte

- Analyse der Lehrveranstaltungen, Lernziele, Kompetenzmodelle und typischen Fehlvorstellungen.
- Strukturierung des Domänenwissens in Einheiten (Lerneinheiten, Mikroinhalte, Aufgaben, Quizzes).
- Definition von Parametern und Strukturen für das Lernenden-Modell (z. B. Kompetenzstufen, Lernstile, Verlaufsdaten).
- Spezifikation des Tutoriellen Modells (Regeln und Strategien für adaptive Lernpfade, Feedback-Logik, Prüfungsformate).
- Dokumentation der Modelle (fachlich-didaktisch und technisch).

### Ergebnisse (Deliverables)

- Modell-Dokumentationen (pro Lehrveranstaltung und Semester).
- Maschinell verarbeitbare Modellrepräsentationen für AP 2 (Import ins HASKI-System).
- Änderungsprotokolle der Modelliterationen.

### Beteiligte Rollen / Partner

- Fachdidaktik-KI-Tandems an OTH R, TH AB, HKE.
- Pädagogische Mitarbeiter:innen (Konzeption, Didaktik).
- Technische Mitarbeiter:innen (Modellrepräsentation, Tooling).

### Abhängigkeiten

- Input: Projektziele, bestehende Lehrmaterialien, Evaluationsergebnisse aus AP 6.
- Output: Modelle als Grundlage für AP 2 (HASKI-System) und AP 3 (LMS-Elemente); Inhalte zur Nutzung in AP 5.

---

## AP 2 – Erstellung des HASKI-Systems

### Ziel

Entwicklung des KI-gestützten HASKI-Softwaresystems als „Herzstück“ des Gesamtkonzepts. Das System soll:

- die Modelle aus AP 1 verarbeiten,
- Lernerinteraktionen aus dem LMS analysieren,
- adaptiv Lernpfade anpassen,
- Feedback für Lernende und Reports für Lehrende bereitstellen.

### Beschreibung

Das HASKI-System besteht aus mehreren Kernkomponenten:

- **Modell-Import und -Verwaltung** (Lernenden-, Domänen-, Tutorielles Modell),
- **Bewertungskomponenten** für Lernerantworten (Quizzes, Freitext, Programmcode, Diagramme),
- **Adaptions-Engine** zur Anpassung von Lernpfaden,
- **Feedback- und Reporting-Komponente** für Lernende und Lehrende,
- **Schnittstellenkomponente** zum LMS (z. B. Moodle),
- **Datenschutz-/Sicherheitskomponenten** gemäß AP 4.

### Zentrale Arbeitsschritte

- Entwurf der Software-Architektur und Definition der Systemkomponenten.
- Implementierung von Schnittstellen zur Aufnahme der Modelle aus AP 1.
- Entwicklung bzw. Integration von KI-Methoden zur automatisierten Bewertung von:
  - Quiz-Antworten,
  - Freitext-Lösungen,
  - Programmcode,
  - Diagrammen (z. B. UML).
- Implementierung der Regeln und Heuristiken für adaptive Lernpfade und Feedback.
- Implementierung der Reporting-Funktionalitäten für Lehrende (aggregierte Lernstände, kritische Inhalte, typische Fehler).
- Einbindung der Datenschutz- und Sicherheitsrichtlinien aus AP 4.
- Test, Qualitätssicherung und iterative Weiterentwicklung über mehrere Ausbaustufen.

### Ergebnisse (Deliverables)

- Laufende HASKI-Systeminstanz (Prototyp → Pilot → stabiler Einsatz).
- API-/Schnittstellenspezifikation zum LMS.
- Technische Dokumentation (Architektur, Betrieb, Erweiterbarkeit).
- Testszenarien und Testberichte pro Entwicklungsiteration.

### Beteiligte Rollen / Partner

- Technische Mitarbeiter:innen an OTH R, TH AB und HKE.
- KI-Expert:innen der Verbundpartner.
- Unterstützung durch Fachdidaktik, um Feedback- und Bewertungslogik fachlich abzusichern.

### Abhängigkeiten

- Input: Modelle aus AP 1, Datenschutzkonzept aus AP 4.
- Output: Funktionale Dienste und Schnittstellen für AP 3 (LMS-Integration) und AP 5 (bzw. reale Lehrszenarien).
- Rückkopplung: Ergebnisse aus AP 6 führen zu Anpassungen in der Systemlogik.

---

## AP 3 – Erstellung der Moodle-/LMS-Elemente

### Ziel

Umsetzung der in AP 1 definierten Domäneninhalte und Lernpfade sowie der Funktionen des HASKI-Systems (AP 2) im LMS (Moodle) an allen drei Standorten.

### Beschreibung

- Erstellung von Lernmaterialien und Aufgaben im LMS (Dokumente, Videos, Podcasts, Aufgaben, Quizzes etc.).
- Abbildung der durch das Tutorielles Modell definierten Lernpfade in Moodle.
- Realisierung der automatischen Übernahme von:
  - Lernpfad-Anpassungen aus dem HASKI-System,
  - Feedback aus dem HASKI-System an die Lernenden.
- Technische Umsetzung der bidirektionalen Kommunikation zwischen HASKI-System und Moodle.
- Sicherstellung von Datenschutz und Datensicherheit gemäß AP 4.

### Zentrale Arbeitsschritte

- Konfiguration des LMS pro Standort (Kurse, Rollen, Rechte).
- Erstellung und Pflege der Lernressourcen und Aufgaben gemäß Domänen-Modell.
- Implementierung der Integrationslogik (z. B. via Plugins, Webservices, LTI, REST-APIs).
- Implementierung der Darstellung von adaptiven Lernpfaden im LMS aus Sicht der Lernenden.
- Implementation der Feedback-Anzeige und ggf. Benachrichtigungsmechanismen.
- Technische Tests, Lasttests und Vorbereitung auf den Einsatz in AP 5.

### Ergebnisse (Deliverables)

- HASKI-fähige Moodle-Kurse an OTH R, TH AB und HKE.
- Funktionsfähige Anbindung an das HASKI-System (Import/Export von Daten).
- LMS-spezifische Dokumentation (Anleitung für Lehrende und Admins).

### Beteiligte Rollen / Partner

- Technische Mitarbeiter:innen (Moodle-/LMS-Administration, Entwicklung).
- Lehrende und pädagogische Mitarbeiter:innen (Inhalte, Aufgaben, Kurseinstellungen).
- Datenschutzbeauftragte (Review der Konfiguration).

### Abhängigkeiten

- Input: Modelle (AP 1), HASKI-Systemfunktionen (AP 2), Datenschutzkonzept (AP 4).
- Output: Fertige Kurse und Integrationen für die Erprobung in AP 5.
- Rückkopplung: Ergebnisse aus AP 6 können zu Anpassungen der LMS-Konfiguration führen.

---

## AP 4 – Datenschutz und Datensicherheit entwickeln

### Ziel

Entwicklung und Abstimmung eines datenschutz- und sicherheitskonformen Gesamtkonzepts für HASKI gemäß DSGVO und hochschulspezifischen Vorgaben.

### Beschreibung

- Betrachtung aller Prozesse, in denen personenbezogene Daten verarbeitet werden:
  - Lernverhalten und Interaktionsdaten,
  - Prüfungs-/Aufgabendaten,
  - personenbezogene Stammdaten.
- Entwicklung von Konzepten zur Anonymisierung und Pseudonymisierung, wo möglich sinnvoll.
- Sicherstellung von Transparenz und Nachvollziehbarkeit der Datenverarbeitung für Lernende und Lehrende.
- Definition von technischen und organisatorischen Maßnahmen (TOM) für alle Standorte.

### Zentrale Arbeitsschritte

- Erhebung der datenschutzrelevanten Prozesse in AP 1–3 und AP 5–6.
- Erstellung eines konsolidierten Datenschutz- und Datensicherheitskonzepts für HASKI.
- Abstimmung mit den Datenschutzbeauftragten aller drei Hochschulen.
- Ableitung von Anforderungen für:
  - das HASKI-System (AP 2),
  - die LMS-Konfiguration (AP 3),
  - den praktischen Einsatz in Lehrveranstaltungen (AP 5).
- Dokumentation und regelmäßige Aktualisierung des Konzepts (bspw. bei Systemänderungen).

### Ergebnisse (Deliverables)

- Abgestimmtes Datenschutz- und Datensicherheitskonzept für HASKI.
- Richtlinien und Checklisten für die technische Umsetzung in AP 2 und AP 3.
- Informationsmaterialien für Lernende und Lehrende (Transparenz über Datenverarbeitung).

### Beteiligte Rollen / Partner

- Federführung: OTH Regensburg.
- Mitwirkung: TH Aschaffenburg, Hochschule Kempten.
- Datenschutzbeauftragte der drei Hochschulen.
- Technische und pädagogische Mitarbeiter:innen (für Prozessbeschreibung und Umsetzung).

### Abhängigkeiten

- Input: Grobkonzepte der Modelle (AP 1), System- und LMS-Architekturen (AP 2, AP 3).
- Output: Verbindliche Rahmenbedingungen für Umsetzung in AP 2, AP 3 und Einsatz in AP 5.
- Rückkopplung: Änderungen aus AP 2/3 (neue Features) können Anpassungen des Konzepts notwendig machen.

---

## AP 5 – Lernräume entwickeln und Erprobung von HASKI

### Ziel

Entwicklung, Durchführung und laufende Anpassung von HASKI-basierten Lernräumen in realen Lehrveranstaltungen an allen drei Standorten.

### Beschreibung

- Nutzung der in AP 1–3 erstellten Modelle, Systeme und LMS-Kurse in der Lehre.
- Umsetzung von Blended-Learning-Szenarien, in denen:
  - Lernende das HASKI-unterstützte Moodle nutzen,
  - Lehrende Lernräume konzipieren, Lernpfade auswählen und die Lernenden begleiten.
- Fokussierung auf verschiedene Studiengänge (u. a. Mechatronik, Informatik, Game Engineering, Wirtschaftsinformatik, sichere Systeme), um unterschiedliche Zielgruppen und Anforderungen abzudecken.

### Zentrale Arbeitsschritte

- Auswahl der Pilotveranstaltungen je Semester und Standort.
- Konzeption der Lernräume (Präsenz- und Online-Anteile, Aufgabenformate, Prüfungssetups).
- Einführung der Lernenden in HASKI, Moodle und die spezifischen Lernpfade.
- Durchführung der Veranstaltungen mit Einsatz von HASKI (Datenerfassung, Feedback, Reporting).
- Laufende Unterstützung der Lernenden (fachlich, technisch, organisatorisch).
- Dokumentation der Erfahrungen als Input für AP 6.

### Ergebnisse (Deliverables)

- Durchgeführte HASKI-gestützte Lehrveranstaltungen pro Semester und Standort.
- Dokumentierte Lehr-/Lernszenarien (Lernräume) inklusive eingesetzter Methoden und Materialien.
- Erfahrungsberichte der Lehrenden und erste Rückmeldungen der Studierenden (Input für AP 6).

### Beteiligte Rollen / Partner

- Lehrende der beteiligten Module.
- Pädagogische Mitarbeiter:innen (didaktische Gestaltung, Coaching).
- Technische Mitarbeiter:innen (Support, Systembetrieb).
- Studierende als Nutzer:innen der Lernräume.

### Abhängigkeiten

- Input: Modelle (AP 1), HASKI-System (AP 2), Moodle-Kurse (AP 3), Datenschutzkonzept (AP 4).
- Output: Nutzungs- und Erfahrungsdaten für die Evaluation in AP 6.
- Rückkopplung: Erkenntnisse aus AP 6 führen zur Anpassung von Lernräumen und Requirements in AP 1–3.

---

## AP 6 – Evaluation und Reflexion der Erprobung

### Ziel

Wissenschaftlich fundierte Evaluation der HASKI-Einsätze in den Lernräumen (AP 5) und Ableitung von Verbesserungsmaßnahmen für Modelle (AP 1), System (AP 2) und LMS-Umsetzung (AP 3).

### Beschreibung

- Systematische Erhebung von qualitativen und quantitativen Daten zur Wirksamkeit der HASKI-Lernumgebung:
  - Lernfortschritt und Kompetenzaufbau,
  - Nutzererfahrungen (User Experience),
  - Akzeptanz seitens Lernender und Lehrender.
- Anwendung geeigneter Evaluationsmethoden (z. B. Grounded Theory, Kompetenzmessinstrumente, Fragebögen, Interviews, Logfile-Analysen).
- Reflexion der Ergebnisse im Verbund und Ableitung konkreter Entwicklungsimpulse.

### Zentrale Arbeitsschritte

1. **Konzeptionsphase**

   - Entwicklung des Evaluationskonzepts (Fragestellungen, Methoden, Instrumente).
   - Erstellung der Evaluationsinstrumente (Fragebögen, Leitfäden, Auswertungsdesigns).

2. **Durchführungsphase**

   - Erhebung der Daten in den HASKI-Lernräumen (Befragungen, Tests, Beobachtungen, Systemlogs).
   - Durchführung von Feedbackrunden mit Lehrenden und Lernenden.

3. **Auswertungs- und Reflexionsphase**
   - Analyse der Daten (qualitativ/quantitativ).
   - Ableitung von Stärken, Schwächen und Verbesserungspotenzialen.
   - Formulierung von Empfehlungen und Requirements für AP 1–3.
   - Dokumentation pro Evaluationszyklus.

### Ergebnisse (Deliverables)

- Evaluationskonzept und -dokumente.
- Evaluationsberichte pro Semester und Standort (inkl. zusammengeführter Verbundsicht).
- Maßnahmenkatalog / Anforderungsliste für Anpassungen in AP 1–3.

### Beteiligte Rollen / Partner

- Pädagogische Mitarbeiter:innen (Konzeption und Durchführung der Evaluation).
- Lehrende der Pilotszenarien (Reflexion der Lehrpraxis).
- Technische Mitarbeiter:innen (Bereitstellung und Auswertung von Systemdaten).
- Studierende (Rückmeldungen als zentrale Datengrundlage).

### Abhängigkeiten

- Input: Ergebnisse und Daten aus AP 5; ggf. System- und Modellinformationen aus AP 1–3.
- Output: Evaluations- und Reflexionsberichte sowie konkrete Änderungsbedarfe für AP 1–3.
- Rückkopplung: Iterative Verbesserung des Gesamtsystems pro Projektjahr/Semester.

---

## AP 7 – Dissemination und Transfer

### Ziel

Bekanntmachung des HASKI-Konzepts, der Ergebnisse und Erfahrungen in relevanten Communities und Transfer der entwickelten Ansätze in andere Lehrgebiete und Hochschulen.

### Beschreibung

- Sichtbarmachung von HASKI in nationalen und internationalen Netzwerken der Software-Engineering- und Hochschuldidaktik-Community.
- Veröffentlichung und Bereitstellung von:
  - Lehrmaterialien (z. B. Lernvideos, Aufgaben) als Open Educational Resources (OER),
  - methodischen Beschreibungen zur Datenverarbeitung (Open Methodology),
  - Forschungsergebnissen (z. B. zu adaptiven Lernumgebungen, KI-Feedback, Evaluation).
- Durchführung von Workshops, Vorträgen und Schulungsangeboten für Lehrende.

### Zentrale Arbeitsschritte

- Planung einer Disseminationsstrategie (Zielgruppen, Kanäle, Zeitplan).
- Einreichung und Präsentation von Beiträgen bei relevanten Konferenzen und Tagungen (z. B. EDUCON, ICSE, ECSEE, DeLFI).
- Mitwirkung in Netzwerken (z. B. Didaktikzentrum der bayerischen Hochschulen, Netzwerk Lehren, Fachgruppen der GI).
- Organisation und Durchführung von Workshops, Schulungen und Infoveranstaltungen für Hochschullehrende.
- Aufbau und Pflege einer Projektwebsite als zentrale Informations- und Materialplattform.
- Dokumentation aller Disseminations- und Transferaktivitäten.

### Ergebnisse (Deliverables)

- Konferenz- und Tagungsbeiträge, Workshops und Vorträge.
- OER-Materialien (z. B. Lernvideos, Aufgaben, Kurs-Templates).
- Projektwebsite mit öffentlich zugänglicher Dokumentation (Methodik, Ergebnisse, Materialien).
- Nachweis der erreichten Zielgruppen und des Transfers (z. B. Nutzung von HASKI-Elementen an weiteren Lehrstühlen/Hochschulen).

### Beteiligte Rollen / Partner

- Projektleitung und Teilprojektleitungen der drei Hochschulen.
- Alle beteiligten Mitarbeiter:innen (Inhaltserstellung, Präsentationen).
- Kommunikationsstellen / Öffentlichkeitsarbeit der Hochschulen.

### Abhängigkeiten

- Input: Ergebnisse, Materialien und Erfahrungen aus AP 1–6.
- Output: Externe Reichweite, Nutzung und Weiterentwicklung von HASKI über das Verbundprojekt hinaus.

---
