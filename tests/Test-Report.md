# Testreport nach IEEE 29119-3

## 1 Einleitung

Dieser Testreport fasst die Ergebnisse der Testaktivitäten im HASKI‑Projekt für einen definierten Testzyklus bzw. eine Release‑Version zusammen. Er basiert auf der Teststrategie (`tests/Test-Strategy.md`) und den Testplänen (`tests/Test-Plan.md`) und dient als Nachweis für die Erfüllung der verifizierbaren Anforderungen.

Hinweis: Die nachfolgenden Abschnitte bilden eine Vorlage; konkrete Inhalte werden pro Testzyklus ergänzt.

## 2 Testgegenstand und Testumfang

- Version / Release: _[z. B. HASKI Backend vX.Y.Z, Frontend vA.B.C]_
- Testzeitraum: _[von/bis]_
- Teststufen: _[Unit, Integration, System, Abnahme]_
- Betroffene Komponenten:
  - Backend: _[Module/Services]_
  - Frontend: _[Seiten/Komponenten]_
  - Integrationen: _[Moodle, NodeGrade, LAAC, xAPI]_

## 3 Zusammenfassung der Testergebnisse

- Gesamtstatus: _[Bestanden / Bedingungen / Nicht bestanden]_
- Anzahl geplanter Testfälle: _[N]_
- Anzahl ausgeführter Testfälle: _[N]_
- Davon bestanden: _[N]_
- Davon fehlgeschlagen: _[N]_
- Blockierte / nicht durchgeführte Tests: _[N] (mit Begründung)_

Kurze Management‑Zusammenfassung der wichtigsten Ergebnisse und Risiken.

## 4 Testabdeckung und Traceability

- Überblick über die Abdeckung der Anforderungen (z. B. gemäß `traceability/RTM.csv`).
- Besonders:
  - High‑Priority‑Anforderungen mit Teststatus,
  - sicherheits‑/datenschutzrelevante Anforderungen (z. B. HASKI‑REQ‑0001, 0030),
  - zentrale Funktionsketten (Nutzeranlage, Kursimport, Lernpfadgenerierung).

Optional: Tabellen oder Verweise auf generierte Reports, die detaillierte Zuordnungen (Anforderung → Testfälle → Ergebnis) zeigen.

## 5 Detaillierte Testergebnisse

### 5.1 Unit- und Integrationstests

- Backend: Zusammenfassung der wichtigsten Paket‑/Modulbereiche, Fehlerstatistiken, Besonderheiten.
- Frontend: Komponenten/Services mit besonderem Fokus (z. B. Lernpfad‑UI, Import‑Dialoge).

### 5.2 System- und E2E-Tests

- Beschriebene Szenarien (z. B. „Erstzugriff Nutzer“, „Kurs‑/Topic‑Synchronisation“, „Adaptiver Lernpfad“).
- Für jeden Testfall: Kurzstatus (Bestanden/Nicht bestanden), Referenz auf Defects.

### 5.3 Nicht-funktionale Tests

- Performance‑Messungen (z. B. Antwortzeiten, Lasttest‑Ergebnisse).
- Verfügbarkeitsnachweise (z. B. Monitoring‑Auszüge, Bezug zu HASKI‑REQ‑0030).
- Sicherheitstests (z. B. Penetrationstests, Schwachstellenscans, Datenschutzprüfungen).

## 6 Abweichungen vom Testplan

- Nicht durchgeführte Testaktivitäten (mit Begründung und Bewertung der Auswirkungen).
- Änderungen am Testumfang oder an Testumgebungen gegenüber `tests/Test-Plan.md`.

## 7 Festgestellte Defects und offene Punkte

- Zusammenfassung kritischer und hoher Defects (inkl. Referenz auf Issue‑Tracker).
- Einschätzung des Risikos verbleibender Defects für den Einsatzkontext (insbesondere Lehre/Prüfungen).

## 8 Bewertung und Freigabeempfehlung

- Fachliche/technische Bewertung, ob die Release‑Version den Anforderungen und Qualitätszielen entspricht.
- Einschränkungen oder bekannte Risiken, die bei Einsatz zu berücksichtigen sind.
- Empfehlung: _[Freigabe / Freigabe mit Auflagen / keine Freigabe]_

## 9 Anhänge

- Ggf. automatisiert erzeugte Testreports (JUnit/Jest‑Reports, Coverage‑Berichte),
- Auszüge aus `traceability/RTM.csv`,
- zusätzliche Tabellen/Diagramme zur Testauswertung.
