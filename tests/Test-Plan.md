# Testplan nach IEEE 29119-3

## 1 Einleitung

Dieser Testplan beschreibt die geplanten Testaktivitäten für einen definierten HASKI‑Testzyklus bzw. eine Release‑Version. Er konkretisiert die übergeordnete Teststrategie (`tests/Test-Strategy.md`) und dient als Grundlage für Testdurchführung und Testreport (`tests/Test-Report.md`).

- Version / Release: _[z. B. HASKI Backend vX.Y.Z, Frontend vA.B.C]_
- Testzeitraum: _[von/bis]_
- Ziel dieses Testzyklus: _[z. B. Pilotbetrieb, Produktivsetzung, Feature‑Release]_

## 2 Testgegenstand

### 2.1 Zu testende Komponenten

- Backend:
  - _[z. B. Nutzeranlage, Kurs‑/Topic‑/LE‑Synchronisation, Lernpfad‑Services]_
- Frontend:
  - _[z. B. Kursübersicht, Topic‑Editor, Lernpfad‑Visualisierung, Einstellungen]_
- Integrationen:
  - Moodle (inkl. LTI/OIDC, Webservices, xAPI‑Plugin),
  - NodeGrade,
  - LAAC.

### 2.2 Nicht zu testende Komponenten

- _[z. B. Prototypische Features, externe Systeme außerhalb des Projektumfangs]_

## 3 Testziele und Abnahmekriterien

- Verifikation, dass die in den Testumfang aufgenommenen Anforderungen (HASKI‑REQ‑XXXX) umgesetzt und testbar sind.
- Sicherstellung, dass kritische Systemfunktionen (Login/LTI‑Zugriff, Kursübersicht, Lernpfadabruf) stabil und fehlerfrei funktionieren.
- Überprüfung, dass identifizierte Fehler aus vorherigen Zyklen behoben sind (Regressionstests).

Abnahmekriterien (Beispiele, zu konkretisieren):

- _[x]_ Alle High‑Priority‑Anforderungen im Scope sind durch mindestens einen Testfall abgedeckt und die zugehörigen Tests bestehen.
- _[x]_ Keine offenen kritischen oder hohen Defects für den vorgesehenen Einsatzkontext.
- _[x]_ Kern‑E2E‑Szenarien laufen fehlerfrei durch.

## 4 Testumfang

### 4.1 Funktionaler Umfang

Auflistung der in diesem Zyklus zu testenden Anforderungen/Use Cases, z. B.:

- HASKI‑REQ‑0034 – Automatische Nutzeranlage aus Moodle‑Daten,
- HASKI‑REQ‑0035/0036/0037 – Kurs‑/Topic‑/Learning‑Element‑Synchronisation,
- HASKI‑REQ‑0095 – Adaptive Lernpfadgenerierung,
- HASKI‑REQ‑0001 – Datenschutzeinwilligung und Pseudonymisierung,
- HASKI‑REQ‑0030 – Systemverfügbarkeit in Lehr‑/Prüfungszeiten (Ausschnitt über Testnachweise).

### 4.2 Nicht-funktionaler Umfang

- Performance‑ & Lasttests (sofern geplant),
- Sicherheits‑/Datenschutznachweise (z. B. Prüfung von Rollenmodell, TLS, Pseudonymisierung),
- Usability‑Stichproben (z. B. Navigationsfluss, Fehlermeldungen).

## 5 Testansatz

### 5.1 Testebenen

- Unit‑Tests in Backend und Frontend,
- Integrationstests für Services/Repos und API‑Interaktionen,
- System‑/E2E‑Tests für End‑to‑End‑Szenarien,
- ggf. Abnahmetests mit Fachvertreter:innen.

### 5.2 Testarten

- Funktionale Tests, Regressions‑Tests, Smoke‑Tests,
- ausgewählte nicht‑funktionale Tests gemäß Abschnitt 4.2.

### 5.3 Traceability

- Testfälle werden so spezifiziert/benannt, dass die zugehörigen HASKI‑Anforderungen erkennbar sind.
- Das RTM (`traceability/RTM.csv`) wird nach Abschluss des Zyklus aktualisiert.

## 6 Testumgebung

- Beschreibung der Testumgebungen (z. B. Staging‑System, Test‑Datenbank, Moodle‑Testinstanz, NodeGrade/LAAC‑Stubs oder Testsysteme).
- Hardware/Software‑Konfiguration, relevante Versionen (Datenbank, Laufzeitumgebung, Browser, etc.).

## 7 Testdaten

- Beschreibung der Testdaten (z. B. Beispielkurse, Testnutzer, Topics, Learning Elements),
- Hinweise zu Datenschutz/Pseudonymisierung realer Daten (falls produktionsnahe Daten verwendet werden).

## 8 Testressourcen und Verantwortlichkeiten

- Rollen im Test (Testleitung, Tester:innen, Entwickler:innen für Fehleranalyse),
- Zuständigkeiten für Backend‑, Frontend‑ und Integrationstests.

## 9 Zeitplan und Meilensteine

- geplanter Start/Ende der Testdurchführung,
- Zwischentermine (z. B. Smoke‑Test, Zwischen‑Review, Go/No‑Go‑Meeting).

## 10 Risiken und Annahmen

- Risiken, die die Testdurchführung gefährden können (z. B. fehlende Testumgebung, unvollständige Integrationen),
- Annahmen (z. B. Verfügbarkeit von Testinstanzen, Testdaten, Personal).

## 11 Genehmigung

- Platzhalter für die formale Freigabe des Testplans (z. B. Unterschrift/Bestätigung durch Projektleitung/Testverantwortliche).
