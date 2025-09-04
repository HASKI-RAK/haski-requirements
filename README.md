<div align="center">

# HASKI Requirements & Traceability

[![Traceability --> GitHub Pages](https://github.com/HASKI-RAK/haski-requirements/actions/workflows/traceability-pages.yml/badge.svg)](https://github.com/HASKI-RAK/haski-requirements/actions/workflows/traceability-pages.yml)

Automatisiertes Requirements & Traceability Repository mit **Single Source of Truth** für SRS, Anforderungen und Testabdeckung – veröffentlicht als statische Site via MkDocs Material.

👉 Live-Dokumentation: https://haski-rak.github.io/haski-requirements/

</div>

## Inhalte der Site
Die generierte Dokumentation umfasst u.a.:
- Software Requirements Specification (SRS)
- Anforderungen (klassifiziert und mit Metadaten)
- Traceability Matrix (filterbar: Requirement ↔ Tests)

## Repository-Struktur
```
requirements/        # Kanonische Requirement-Dateien (YAML Front Matter + Text)
srs/                  # Master SRS Dokument
traceability/         # Skripte + RTM.csv (generiert durch build.py)
scripts/              # generate_docs.py (baut docs/ aus Quellen)
docs/                 # Ephemer (wird bei Build generiert, nicht manuell editieren)
tests/                # Test-Strategie, -Plan, -Spezifikationen
architecture/         # Architektur- und Interface-Dokumente
design/               # Software Design Description (SDD)
governance/           # Pläne (CM, Security, Projekt, Risiko, Qualität)
vnv/                  # Verifikation & Validierung (VV-Plan / Report)
traceability/adapters # Parser/Adapter für Testergebnisse (z.B. Jest)
```

## Workflow & Automatisierung
1. Änderungen an Anforderungen / SRS werden in den jeweiligen Quellordnern gepflegt.
2. Tests referenzieren Anforderungen über Tags, z.B. `verifies=HASKI-REQ-0001`.
3. `traceability/build.py` aggregiert Requirements + Testergebnis-Metadaten → `traceability/RTM.csv`.
4. `scripts/generate_docs.py` erzeugt den kompletten `docs/` Baum (SRS-Kopie, Requirement-Index, Traceability HTML mit Filter/Badges).
5. GitHub Action `traceability-pages.yml` baut & deployt die MkDocs Site (strict) nach GitHub Pages.


## ID-Schema & Klassen
Format: `HASKI-REQ-####` (vierstellig). Optionale Klassifikation über Prefix/Tag (z.B. SYS, SW, NFR, IF) kann als zusätzliches Feld aufgenommen werden.


## Traceability Matrix
Die Seite `Traceability` in der Live-Dokumentation bietet:
- Filter nach Freitext & Status
- Farbige Badges (passed / failed / skipped / unknown)
- Rohdaten-Download (`RTM.csv`)

## Lokal Bauen & Anzeigen
Voraussetzungen: Python 3.9+, pip

```bash
pip install -r requirements.txt        # mkdocs + plugins + PyYAML
python scripts/generate_docs.py        # docs/ neu erzeugen
mkdocs serve                           # lokale Vorschau (http://127.0.0.1:8000)
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
