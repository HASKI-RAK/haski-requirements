# Verifikations- und Validierungsplan (VV-Plan)

## 1 Zweck und Zielsetzung

Dieser Verifikations- und Validierungsplan beschreibt, wie im HASKI‑Projekt nachgewiesen wird, dass:

- die spezifizierten Anforderungen (StrRS, SyRS, SRS, HASKI‑REQ‑Dateien) korrekt umgesetzt sind (Verifikation), und
- das resultierende System für den beabsichtigten Einsatzzweck in der Hochschullehre geeignet ist (Validierung).

Der VV‑Plan verknüpft Anforderungen, Architektur/Design, Tests, Reviews und Pilotierungen zu einem konsistenten Nachweiskonzept.

## 2 Referenzen

- IEEE 29119 – Software Testing (insbesondere Teil 3: Testdokumentation)
- ISO/IEC/IEEE 12207 – Software lifecycle processes
- ISO/IEC 25010 – Qualitätsmodell für Software
- Projektinterne Dokumente:
  - `syrs/SyRS.md`, `srs/SRS.md`, `strs/StRS.md`
  - `architecture/System-AD.md`
  - `design/SDD.md`
  - `governance/Requirements-Management-Plan.md`
  - `governance/Info-Security-Plan.md`
  - `tests/Test-Strategy.md`, `tests/Test-Plan.md`, `tests/Test-Report.md`
  - `traceability/RTM.csv`

## 3 Geltungsbereich

Der VV‑Plan umfasst:

- das HASKI‑System (Backend, Frontend, Datenhaltung),
- Integrationen mit Moodle (inkl. xAPI‑Plugin), NodeGrade und LAAC,
- alle Phasen vom Prototyp bis zum Pilot‑ bzw. produktionsnahen Einsatz.

## 4 Begriffe

- **Verifikation**: Nachweis, dass ein Arbeitsergebnis (z. B. Modul, Schnittstelle) seine spezifizierten Anforderungen erfüllt.
- **Validierung**: Nachweis, dass das System die Bedürfnisse der Stakeholder (Studierende, Lehrende, Admins, Fördergeber) erfüllt.
- **V&V‑Aktivität**: Test, Review, Inspektion, Demo, Pilotversuch o. Ä. mit dokumentiertem Ergebnis.

## 5 V&V-Strategie

Die V&V‑Strategie kombiniert:

- **Dokumenten- und Artefaktreviews** (StrRS, SyRS, SRS, Architektur, Design),
- **Testen auf verschiedenen Ebenen** (Unit, Integration, System, Abnahme) gemäß `tests/Test-Strategy.md`,
- **Traceability‑Analysen** (RTM, Coverage‑Bewertungen),
- **Validierungsaktivitäten mit Endnutzer:innen** (z. B. Usability‑Tests, Pilotveranstaltungen, Feedback‑Workshops).

## 6 Verifikationsaktivitäten

### 6.1 Anforderungsverifikation

- Formale und informelle Reviews von StrRS, SyRS, SRS und HASKI‑REQ‑Dateien (Vollständigkeit, Widerspruchsfreiheit, Testbarkeit).
- Pflege und Review der Traceability (Links `parents`, `tests`, `stories` und `traceability/RTM.csv`).

### 6.2 Architektur- und Designverifikation

- Review von `architecture/System-AD.md` (Konsistenz mit SyRS/SRS, Abdeckung kritischer Qualitätsanforderungen wie Verfügbarkeit, Sicherheit, Datenschutz).
- Review von `design/SDD.md` (Abgleich von Designentscheidungen mit Anforderungen und Architekturprinzipien).

### 6.3 Implementierungsverifikation (Tests)

- Umsetzung automatisierter Tests im Backend/Frontend entsprechend der Teststrategie.
- Regelmäßige Auswertung von Testreports und Coverage‑Berichten.
- Nachweis, dass alle High‑Priority‑Anforderungen mindestens einen verknüpften Testfall besitzen.

## 7 Validierungsaktivitäten

### 7.1 Funktionale Validierung

- Pilotkurse mit realen Studierenden und Lehrenden in ausgewählten Szenarien (z. B. adaptiver Lernpfad in einer Lehrveranstaltung).
- Erhebung von Feedback (z. B. Fragebögen, Interviews) zur Eignung der Funktionen für Lehre und Lernen.

### 7.2 Qualitäts- und Akzeptanzvalidierung

- Bewertung von Usability‑Aspekten (z. B. Navigationsfluss, Verständlichkeit von Fehlermeldungen) anhand von Beobachtungen und Befragungen.
- Validierung von Performance/Verfügbarkeit in praxisnahen Szenarien (z. B. parallele Nutzung in einer Prüfungsphase).

### 7.3 Datenschutz- und Ethics-Validierung

- Prüfung, ob umgesetzte Pseudonymisierungs‑/Anonymisierungsmechanismen (HASKI‑REQ‑0001) den Erwartungen von Datenschutzbeauftragten und Ethikkommissionen entsprechen.
- Review von Analytik‑/KI‑Funktionen (z. B. HASKI‑REQ‑0095) auf Transparenz, Nachvollziehbarkeit und potenzielle Bias‑Risiken.

## 8 Rollen und Verantwortlichkeiten

- **Projektleitung** – Gesamtverantwortung für V&V, Freigabeentscheidungen.
- **V&V-Verantwortliche:r** – Koordination von Reviews, Tests und Validierungsaktivitäten.
- **Requirements Engineer** – Pflege der Traceability, Sicherstellung der Testbarkeit von Anforderungen.
- **Entwicklungsteam** – Umsetzung von Tests, Behebung von Defects.
- **Lehrende/Didaktik-Team** – Validierung der didaktischen Eignung im Lehrbetrieb.
- **Datenschutz/InfoSec** – Validierung von Datenschutz‑ und Sicherheitsaspekten.

## 9 Dokumentation der V&V-Ergebnisse

- Testergebnisse: `tests/Test-Report.md`, Testlogs, CI‑Reports.
- Reviewprotokolle für Anforderungen, Architektur und Design.
- Protokolle/Berichte aus Pilotkursen, Usability‑Tests und Workshops.
- Aktualisierte Traceability‑Matrix (`traceability/RTM.csv`) als Übersicht über den Verifikationsstatus.

## 10 Kriterien für Freigaben

Beispiele für Freigabekriterien (konkret je Release zu definieren):

- Alle Muss‑Anforderungen im Scope des Releases sind verifiziert (Tests durchgeführt und bestanden oder begründete Abweichung dokumentiert).
- Kritische Risiken aus dem Risk‑Management‑Plan sind adressiert oder akzeptiert.
- Ergebnisse aus Pilot‑/Validierungsaktivitäten zeigen ausreichende Akzeptanz und Eignung im Lehrkontext.

## 11 Pflege des VV-Plans

Dieser VV‑Plan wird aktualisiert, wenn sich wesentliche Rahmenbedingungen ändern (z. B. neue Systemkomponenten, geänderte Qualitätsziele, neue Integrationen). Die Verantwortung für die Pflege liegt bei der Projektleitung in Abstimmung mit V&V‑Verantwortlichen und den relevanten Stakeholdern.
