<div align="center">

# HASKI Requirements & Traceability

[![Traceability --> GitHub Pages](https://github.com/HASKI-RAK/haski-requirements/actions/workflows/traceability-pages.yml/badge.svg)](https://github.com/HASKI-RAK/haski-requirements/actions/workflows/traceability-pages.yml)

Automatisiertes Requirements & Traceability Repository mit **Single Source of Truth** für SRS, Anforderungen und Testabdeckung – veröffentlicht als statische Site via MkDocs Material.

👉 Live-Dokumentation: https://haski-rak.github.io/haski-requirements/

</div>

## Inhalte der Site
Die generierte Dokumentation umfasst u.a.:
- Software Requirements SpecificationR (SRS)
- Anforderungen (klassifiziert und mit Metadaten)
- Traceability Matrix (filterbar: Requirement ↔ Tests)

## Repository-Struktur
```
requirements/        # Kanonische Requirement-Dateien (YAML Front Matter + Text)
srs/                  # Master SRS Dokument
scripts/traceability/ # Skripte + RTM.csv (generiert durch build.py)
scripts/              # generate_docs.py (baut docs/ aus Quellen)
docs/                 # Ephemer (wird bei Build generiert, nicht manuell editieren)
tests/                # Test-Strategie, -Plan, -Spezifikationen
architecture/         # Architektur- und Interface-Dokumente
design/               # Software Design Description (SDD)
governance/           # Pläne (CM, Security, Projekt, Risiko, Qualität)
vnv/                  # Verifikation & Validierung (VV-Plan / Report)
scripts/traceability/adapters # Parser/Adapter für Testergebnisse (z.B. Jest)
```

## Workflow & Automatisierung
1. Änderungen an Anforderungen / SRS werden in den jeweiligen Quellordnern gepflegt.
2. Tests referenzieren Anforderungen über Tags, z.B. `verifies=HASKI-REQ-0001`.
3. `scripts/traceability/build.py` aggregiert Requirements + Testergebnis-Metadaten → `scripts/traceability/RTM.csv`.
4. `scripts/generate_docs.py` erzeugt den kompletten `docs/` Baum (SRS-Kopie, Requirement-Index, Traceability HTML mit Filter/Badges).
5. GitHub Action `traceability-pages.yml` baut & deployt die MkDocs Site (strict) nach GitHub Pages.


## ID-Schema & Klassen
Format: `HASKI-REQ-####` (vierstellig). Optionale Klassifikation über Prefix/Tag (z.B. SYS, SW, NFR, IF) kann als zusätzliches Feld aufgenommen werden.


## Traceability Matrix
Die Seite `Traceability` in der Live-Dokumentation bietet:
- Filter nach Freitext & Status
- Farbige Badges (passed / failed / skipped / unknown)
- Rohdaten-Download (`RTM.csv`)

## Neues Repository / Test-Quelle integrieren
Dieser Abschnitt beschreibt, wie ein zusätzliches (externes) Code-/Test-Repository angebunden wird, sodass dessen Testergebnisse in die Traceability Matrix einfließen und auf Quellzeilen verlinkt werden.

### Überblick
1. Tests im Ziel-Repo mit Requirement-IDs annotieren (z.B. `HASKI-REQ-0005`).
2. Einen Test-Report erzeugen (z.B. Jest JSON mit `--json --testLocationInResults`).
3. Report-Datei ins (oder per Pfad referenzierbar vom) `haski-requirements` Repository legen.
4. Adapter (Parser) bereitstellen, falls Format noch nicht unterstützt.
5. `scripts/traceability/config.yaml` erweitern: Eintrag unter `test_reports` und optional GitHub-Link-Mapping unter `github_file_link_mappings`.
6. CI Workflow anpassen / ergänzen: Report generieren, `scripts/generate_docs.py` ausführen (führt auch das Traceability-Build aus), MkDocs deployen.

### 1. Anforderungen in Tests referenzieren
Aktuell genügt, dass die Requirement-ID im Testnamen auftaucht (Pattern `HASKI-REQ-\d+`). Beispiel (Jest):
```ts
test('[HASKI-REQ-0005] speichert Config korrekt', () => { /* ... */ })
```
Falls das Test-Framework keine sprechenden Namen bietet, kann alternativ die ID im Dateinamen oder per Kommentar erscheinen – der Adapter kann ggf. erweitert werden.

### 2. Test-Report erzeugen (Beispiel Jest)
Im Ziel-Repository (z.B. `HASKI-Frontend`):
```bash
jest --json --outputFile reports/jest-results.json --testLocationInResults
```
Der Pfad `reports/jest-results.json` wird später im `config.yaml` referenziert.

### 3. Report-Datei verfügbar machen
Variante A (empfohlen): CI Job im Ziel-Repo lädt Artefakt hoch und der `haski-requirements` Workflow lädt es herunter (per `actions/download-artifact` oder `curl` gegen Raw URL).

Variante B: Monorepo-ähnliches Checkout im `haski-requirements` CI Workflow – zusätzliches `actions/checkout` mit `repository: HASKI-RAK/HASKI-Frontend` in einen Unterordner `frontend/` (aktueller Ansatz bereits vorhanden). Dann liegt die Report-Datei z.B. unter `frontend/reports/jest-results.json`.

### 4. Adapter schreiben (falls neues Format)
Bestehender Adapter: `scripts/traceability/adapters/jest.py` liefert `parse(report_path) -> List[TestResult]`.

Neues Format hinzufügen (Beispiel `pytest` JUnit XML):
1. Datei `scripts/traceability/adapters/pytest_junit.py` anlegen.
2. Parser implementieren, der `TestResult(name, file, line, status, requirements)` Instanzen erzeugt.
3. In `scripts/traceability/build.py` im `gather_tests` Zweig erweitern:
```python
elif rtype == "pytest-junit":
		parsed = pytest_junit.parse(path)
		tests.extend(parsed)
```
4. `test_reports` Eintrag mit `type: pytest-junit` konfigurieren.

### 5. `scripts/traceability/config.yaml` erweitern
Beispiel-Erweiterung:
```yaml
test_reports:
	- type: jest
        path: ../../frontend/reports/jest-results.json
	- type: pytest-junit
		path: ../../api/reports/junit.xml

github_file_link_mappings:
	- local_root: ../../frontend/src
		repo: HASKI-RAK/HASKI-Frontend
		branch: main
		repo_root_subpath: src
	- local_root: ../../api/src
		repo: HASKI-RAK/HASKI-API
		branch: main
		repo_root_subpath: src
```
Optional: In CI einen immutable Commit-SHA verlinken mit
```bash
export TRACEABILITY_GITHUB_COMMIT="$GITHUB_SHA"  # vor generate_docs.py
```
Dadurch zeigen Links auf die exakte Version, nicht nur auf `main`.

### 6. CI Workflow (Skizze)
In `traceability-pages.yml` oder separatem Workflow:
```yaml
jobs:
	traceability:
		runs-on: ubuntu-latest
		steps:
			- uses: actions/checkout@v4
				with:
					repository: HASKI-RAK/haski-requirements
			- name: Checkout Frontend (Tests)
				uses: actions/checkout@v4
				with:
					repository: HASKI-RAK/HASKI-Frontend
					path: frontend
			- name: Install deps (Frontend)
				run: |
					cd frontend
					npm ci
					npx jest --json --outputFile reports/jest-results.json --testLocationInResults
			 - name: Python deps
			 	run: pip install -r requirements.txt
			- name: Build traceability CSV
				run: python scripts/traceability/build.py --debug
			- name: Generate docs
				run: python scripts/generate_docs.py --verbose
			- name: Build & Deploy MkDocs
				run: |
					mkdocs build --strict
					# Deployment Step (GitHub Pages Action / mike / etc.)
```
Weitere Repos analog durch zusätzlichen Checkout + Test-Report-Erstellung.

### Prüfschritte nach Integration
- Stimmt Anzahl der "parsed test(s)" im `--debug` Output?
- Enthält `scripts/traceability/RTM.csv` Zeilen für neue Requirements?
- Werden Links im Traceability-Table korrekt angezeigt?
- Gibt es unverlinkte Dateien (bei `--verbose` würde ein Details-Block erscheinen)?

### Troubleshooting
| Problem | Ursache | Lösung |
|---------|---------|--------|
| Keine Zeilen im RTM | Report nicht gefunden / leer | Pfad in `config.yaml` prüfen, CI-Artefakt bereitstellen |
| Links zeigen auf falschen Pfad | `repo_root_subpath` falsch | Subpfad an tatsächliche Repo-Struktur anpassen |
| Falscher Branch verlinkt | Override nicht gesetzt | `TRACEABILITY_GITHUB_COMMIT` oder `TRACEABILITY_GITHUB_REF` setzen |
| Requirement nicht erkannt | ID fehlt im Testnamen | ID ergänzen oder Adapter verbessern |

### Minimaler manueller Test lokal
```bash
python scripts/traceability/build.py --debug \
	--config scripts/traceability/config.yaml
python scripts/generate_docs.py --verbose
grep HASKI-REQ-0005 scripts/traceability/RTM.csv || echo 'Nicht gefunden'
```

Damit ist ein neuer Test-Provider vollständig angebunden.

## Lokal Bauen & Anzeigen
Voraussetzungen: Python 3.9+, pip

```bash
pip install -r requirements.txt        # mkdocs + plugins + PyYAML
python scripts/generate_docs.py        # docs/ neu erzeugen
mkdocs serve --dev-addr 127.0.0.1:8001 # lokale Vorschau (http://127.0.0.1:8001)
```

CI führt dieselben Schritte automatisch aus (plus Test-/Traceability-Generierung, falls integriert).

## Standards & Tailoring
- ISO/IEC/IEEE 29148 – Struktur & Attribute für Requirements
- ISO/IEC/IEEE 29119-3 – Test-Spezifikationen / Coverage-Nachweis
- ISO/IEC/IEEE 15289 – Informations-Item-Klassen

Abweichungen / Tailoring werden inkrementell dokumentiert (siehe Governance-Dokumente).

## Beiträge & Pflege
1. Requirement ergänzen/ändern in `requirements/`
2. Passende Tests verlinken (Annotation / Tag)
3. Commit & Push → Action baut & deployed
4. Prüfen der Traceability auf der Live-Site

## Lizenz
Siehe `LICENSE`.

---
_Diese README beschreibt die Arbeitsweise & Automatisierung des Repos. Fragen / Ideen gerne via Issue._
