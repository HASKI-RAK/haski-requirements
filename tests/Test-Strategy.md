# Teststrategie nach IEEE 29119-3

## 1 Zweck und Zielsetzung

Diese Teststrategie beschreibt die übergeordneten Ziele, Prinzipien und Strukturen der Testaktivitäten im HASKI‑Projekt auf Basis von IEEE 29119‑3. Sie dient als Rahmen für detailliertere Testpläne (`tests/Test-Plan.md`), Testspezifikationen und die automatisierte Traceability (`traceability/RTM.csv`).

Ziele:

- Sicherstellung, dass funktionale und nicht‑funktionale Anforderungen (SyRS, SRS, HASKI‑REQ‑Dateien) angemessen verifiziert werden,
- konsistenter Einsatz von Unit‑, Integrations‑, System‑ und Abnahmetests über Backend, Frontend und Integrationen,
- Transparenz der Testabdeckung über die HASKI‑Traceability‑Kette (Anforderung → Testfall → Testergebnis).

## 2 Geltungsbereich

Die Teststrategie gilt für:

- das HASKI‑Backend (`HASKI-Backend/`),
- das HASKI‑Frontend (`HASKI-Frontend/`),
- Integrationen mit Moodle (inkl. xAPI‑Plugin), NodeGrade und LAAC,
- generierte Dokumentation und Traceability‑Artefakte (`scripts/generate_docs.py`, `traceability/`).

## 3 Referenzen

- IEEE 29119‑3 – Test Documentation
- IEEE 29119‑1/2 – Testkonzepte und Testprozesse
- ISO/IEC/IEEE 12207 – Software lifecycle processes
- Projektinterne Dokumente:
  - `tests/Test-Plan.md`
  - `tests/Test-Report.md`
  - `governance/Requirements-Management-Plan.md`
  - `governance/Info-Security-Plan.md`
  - `architecture/System-AD.md`
  - `design/SDD.md`

## 4 Testebenen und Testarten

### 4.1 Testebenen

- **Unit-Tests (Komponententests)**

  - Fokus auf einzelne Funktionen/Klassen im Backend (z. B. in `HASKI-Backend/tests/unit/`) und auf einzelne Frontend‑Komponenten/Services.

- **Integrationstests**

  - Zusammenspiel mehrerer Komponenten/Module (z. B. Service Layer + Repository + ORM, oder Frontend‑Service + Backend‑API).

- **Systemtests / E2E-Tests**

  - Szenarien über das Gesamtsystem hinweg (z. B. Nutzeranlage über LTI, Kursimport, Lernpfadgenerierung) mit Fokus auf Anforderungen aus SRS/SyRS.

- **Abnahmetests**
  - Formale Tests gegen freigegebene Baselines (z. B. Pilot‑/Produktivfreigabe), unterstützt durch die Traceability‑Matrix.

### 4.2 Testarten

- Funktionale Tests (API‑Verhalten, UI‑Funktionen, Business‑Logik),
- Nicht‑funktionale Tests (Performance, Verfügbarkeit, Sicherheit, Usability auf Stichprobenbasis),
- Regressions‑Tests bei Releases,
- Smoke‑Tests nach Deployments.

## 5 Testobjekte

Beispiele für zentrale Testobjekte:

- Anforderungen und Use Cases aus `srs/SRS.md` und `srs/srs-requirements/` (HASKI‑REQ‑XXXX),
- Backend‑Services (z. B. Nutzeranlage, Kurs‑/Topic‑/LE‑Synchronisation, Lernpfad‑Services),
- Frontend‑Seiten/Komponenten (Kursübersicht, Topic‑Editor, Learning‑Path‑Ansicht, Settings),
- Integrationsschnittstellen (Moodle LTI/OIDC, Moodle‑Webservices, NodeGrade/LAAC APIs, xAPI‑Events).

## 6 Traceability und Testfallorganisation

- Testfälle werden so benannt bzw. dokumentiert, dass sie eindeutige Referenzen auf HASKI‑Anforderungen enthalten (z. B. `[HASKI-REQ-0001]` im Testnamen oder in Metadaten).
- Das Tooling in `traceability/` extrahiert diese Referenzen aus Testreports (z. B. Jest‑JSON, Python‑Testausgaben) und verknüpft sie mit Anforderungen in `requirements/` und `srs/srs-requirements/`.
- Die Traceability‑Matrix (`traceability/RTM.csv`) zeigt den Abdeckungsstatus je Anforderung (getestet/nicht getestet, Testfälle, Dateipfade).

## 7 Testdurchführung und Automatisierung

- **Backend**

  - Python‑Unit‑ und Integrationstests mit `pytest`; Abdeckung von Service‑Layer, Domänenlogik und Repositories.
  - E2E‑API‑Tests (z. B. in `HASKI-Backend/tests/e2e/test_api.py`) für zentrale Workflows (Nutzeranlage, Kursimport, Lernpfad‑APIs).

- **Frontend**

  - Jest/Testing‑Library‑Tests für Komponenten und Services (siehe `HASKI-Frontend/reports`, `src/**/*.test.tsx`).
  - Optionale E2E‑Tests mit Browser‑Automatisierung (z. B. Cypress/Playwright, falls eingeführt).

- **Integrationen**
  - Tests gegen Moodle‑Testinstanzen und simulierte NodeGrade/LAAC‑APIs,
  - Validierung von xAPI‑Events (Struktur, Pseudonymisierung, Vollständigkeit).

CI‑Pipelines führen relevante Tests bei jedem Pull Request und auf `main` aus, Ergebnisse dienen als Grundlage für Freigabeentscheidungen.

## 8 Qualitätsziele für Tests

- Angemessene Code‑Coverage auf Unit‑Test‑Ebene, insbesondere für sicherheits‑ und domänenkritische Bereiche,
- Abdeckung aller „High“‑Prioritätsanforderungen (Stakeholder‑Priorität hoch) durch mindestens einen automatisierten Testfall,
- Kein Release ohne erfolgreich durchlaufene Kern‑E2E‑Tests für kritische Szenarien (z. B. Login, Kursübersicht, Lernpfadabruf).

## 9 Pflege und Weiterentwicklung

Die Teststrategie wird in folgenden Fällen überprüft und angepasst:

- Einführung neuer Systemkomponenten oder Integrationen (z. B. zusätzliche LMS, neue Analytics‑Pipelines),
- Anpassung der Architektur (siehe `architecture/System-AD.md`) oder wesentliche Änderungen an Kernanforderungen,
- Erkenntnisse aus Testreports, Defect‑Analysen oder Audits.

Verantwortlich für die Pflege sind Testverantwortliche und Projektleitung gemeinsam mit den Entwicklungsteams.
