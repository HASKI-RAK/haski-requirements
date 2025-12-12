# Konfigurations- und Release-Management (IEEE 828)

## 1 Zweck und Zielsetzung

Dieses Dokument definiert das Konfigurations- und Release-Management (CM) für das HASKI‑Projekt in Anlehnung an IEEE 828. Es stellt sicher, dass alle für Entwicklung, Betrieb und Nachweisführung relevanten Artefakte über ihren Lebenszyklus identifizierbar, versioniert, nachvollziehbar änderbar und kontrolliert auslieferbar sind.

Schwerpunkte:

- einheitliche Verwaltung von Anforderungen, Quellcode, Build‑/CI‑Konfiguration und Dokumentation,
- transparente Änderungskontrolle über Git/GitHub,
- definiertes Vorgehen für Releases und Baselines,
- Unterstützung der Normen ISO/IEC/IEEE 29148, 29119, 15289 und 27001.

## 2 Geltungsbereich

Der CM‑Plan gilt für folgende Repositories und Komponenten:

- `haski-requirements` – Anforderungen, Architektur‑ und Governance‑Dokumente, Traceability‑Artefakte,
- `HASKI-Backend` – Backend‑Quellcode, Tests, Build‑ und Deployment‑Konfigurationen,
- `HASKI-Frontend` – Frontend‑Quellcode, Tests, Build‑ und Deployment‑Konfigurationen,
- `NodeGrade` – externe oder verbundene Komponente für Bewertung/Grading, soweit sie Teil der HASKI‑Lieferkette ist,
- `LAAC (Learning Analytics Analyzing Center)` – Analytik‑/Auswertungsplattform, deren Schnittstellen und Konfigurationen mit HASKI abgestimmt werden,
- `Moodle‑xAPI‑Plugin` – Plugin zur Ereigniserfassung im LMS, inkl. seiner Konfiguration und Versionierung im Kontext der HASKI‑Integration.

Er umfasst Entwicklung, Test, Abnahme und Betrieb der HASKI‑Plattform und der angebundenen Systeme (NodeGrade, LAAC, Moodle‑xAPI‑Plugin) in allen Projektphasen, soweit diese im Projektumfang liegen.

## 3 Referenzen

- IEEE 828 – Standard for Configuration Management in Systems and Software Engineering
- ISO/IEC/IEEE 12207 – Software lifecycle processes
- ISO/IEC/IEEE 29148 – Requirements engineering
- ISO/IEC 27001 – Information security management (für CM‑relevante Kontrollen)
- Projektinterne Dokumente:
  - `governance/Project-Plan.md`
  - `governance/Requirements-Management-Plan.md`
  - `governance/Info-Security-Plan.md`
  - `architecture/System-AD.md`
  - `design/SDD.md`

## 4 Begriffe und Abkürzungen

- **CM** – Configuration Management
- **CI/CD** – Continuous Integration / Continuous Delivery
- **Baseline** – freigegebener, versionierter Stand eines oder mehrerer Konfigurationsobjekte
- **Konfigurationsobjekt (KO)** – identifizierbares Artefakt unter CM‑Kontrolle
- **Release** – extern bereitgestellte Version einer Komponente oder des Gesamtsystems

## 5 Rollen und Verantwortlichkeiten

- **Projektleitung**

  - Genehmigung von Baselines und Releases,
  - Priorisierung von Changes.

- **Configuration Manager (CM-Verantwortliche:r)**

  - Pflege dieses CM‑Plans,
  - Definition/Überwachung von Branch‑ und Tagging‑Strategien,
  - Koordination von Release‑Freigaben.

- **Product Owner / Requirements Engineer**

  - Verwaltung der Anforderungen und ihrer Status in `haski-requirements`,
  - Sicherstellung der Traceability (RTM, `links.tests`, `links.stories`).

- **Entwicklungsteam (Backend/Frontend)**

  - Umsetzung von Changes über Pull Requests,
  - Einhaltung der CM‑Regeln (Branches, Reviews, Commits).

- **DevOps/Operations**
  - Umsetzung und Betrieb der CI/CD‑Pipelines,
  - Verwaltung von Build‑/Deployment‑Konfigurationen.

## 6 Konfigurationsobjekte (KOs)

Folgende Artefaktklassen unterliegen dem Konfigurationsmanagement:

- **Anforderungen und Spezifikationen**

  - `strs/`, `syrs/`, `srs/`, `requirements/`, inklusive einzelner HASKI‑REQ‑Dateien,
  - Traceability‑Artefakte (`traceability/`, `rtm/RTM.md`, `traceability/RTM.csv`).

- **Architektur- und Designdokumente**

  - `architecture/System-AD.md`, `design/SDD.md`, Governance‑Pläne.

- **Quellcode und Skripte**

  - Backend: `HASKI-Backend/` (inkl. `domain/`, `service_layer/`, `repositories/`, `entrypoints/`),
  - Frontend: `HASKI-Frontend/` (inkl. `src/`, `vite.config.ts`, `jest.config.ts`),
  - Hilfsskripte (z. B. `scripts/generate_docs.py`, `traceability/build.py`).
  - gegebenenfalls Quellcode/Konfiguration für NodeGrade, LAAC und das Moodle‑xAPI‑Plugin, sofern im Projektrepos oder als gespiegelt verwaltet.

- **Build-, Test- und CI-Konfiguration**

  - `requirements.txt`, `pyproject.toml`, `package.json`, Dockerfiles,
  - GitHub‑Actions‑Workflows, Test‑Konfigurationen.

- **Dokumentation zur Auslieferung**
  - Release‑Notes, Changelogs,
  - Deploy‑Anleitungen (README‑Abschnitte, Wiki‑Seiten).

## 7 Identifikation und Versionsverwaltung

### 7.1 Repository- und Branch-Strategie

- Zentrales Git‑Repository je Komponente (`main` als stabiler Integrations‑Branch).
- Feature‑Branches nach Muster `feature/<kurze-beschreibung>`.
- Optional Release‑Branches nach Muster `release/<version>` bei großen Meilensteinen.
- Hotfix‑Branches nach Muster `hotfix/<kurze-beschreibung>` für dringende Korrekturen.

### 7.2 Versionierung und Tags

- Semantic Versioning für Backend/Frontend (z. B. `v1.2.0`).
- Tags auf `main` markieren freigegebene Releases.
- Anforderungen und Dokumente werden über Git‑Historie versioniert; wichtige Baselines können zusätzlich über Tags oder Branches gekennzeichnet werden (z. B. `baseline/srs-v1`).

## 8 Änderungskontrolle (Change Management)

- Änderungen werden grundsätzlich über GitHub‑Issues und Pull Requests (PRs) initiiert.
- Jeder PR enthält:
  - Referenz auf relevante Anforderungen (z. B. HASKI‑REQ‑XXXX),
  - kurze Beschreibung der Änderung,
  - Verweis auf Tests/Checks.
- Mindestens ein fachlicher/technischer Review ist vor Merge in `main` erforderlich.
- Breaking Changes werden in Release‑Notes dokumentiert und mit erhöhter Versionsnummer ausgeliefert.

## 9 Build-, Test- und Release-Prozess

### 9.1 Continuous Integration

- Bei PRs und Commits auf `main` laufen automatisierte Pipelines (Unit‑Tests, Linting, ggf. E2E‑Tests).
- Fehlgeschlagene Builds blockieren den Merge bzw. markieren den Commit als fehlerhaft.

### 9.2 Release-Erstellung

Typisches Vorgehen für ein Release:

1. Auswahl des Release‑Umfangs (Issues/Anforderungen) und Aktualisierung der Dokumentation (SRS, RTM, System‑AD, SDD).
2. Sicherstellen, dass alle CI‑Pipelines auf `main` erfolgreich sind.
3. Erstellen eines Versionstags (`git tag vX.Y.Z`) und GitHub‑Releases mit Release‑Notes.
4. Ausrollen der Version in die Zielumgebung (z. B. Backend/Frontend‑Deployments, Aktualisierung der generierten HASKI‑Dokumentation).

### 9.3 Baselines

- Formale Baselines werden für wesentliche Meilensteine definiert (z. B. SyRS‑/SRS‑Baseline vor Implementierungsphase, Pilot‑Release, Produktivsetzung).
- Eine Baseline umfasst:
  - definierte Versionsstände der KOs,
  - Kennzeichnung durch Tag/Branch und dokumentierte Freigabeentscheidung.

## 10 Werkzeuge und Infrastruktur

- **Versionsverwaltung**: Git (GitHub‑Organisation `HASKI-RAK`).
- **CI/CD**: GitHub Actions (Build, Test, Deployment, Dokumentations‑Generation).
- **Paket-/Abhängigkeitsmanagement**: `pip`/`poetry` für Python, `npm`/`pnpm` für Frontend.
- **Dokumentations‑Build**: MkDocs über `scripts/generate_docs.py` und `mkdocs.yml`.
- **Issue-Tracking**: GitHub Issues und Projektboards.
  -, sofern relevant für NodeGrade, LAAC und Moodle‑xAPI‑Plugin: zusätzliche Repos/Tools der jeweiligen Betreiber, die in den Projektvereinbarungen benannt sind.

## 11 Auditierung und Berichterstattung

- Regelmäßige Überprüfung der Einhaltung der CM‑Regeln (z. B. durch Projektleitung/CM‑Verantwortliche:n).
- Dokumentation von freigegebenen Baselines und Releases in Meetingprotokollen oder Release‑Übersichten.
- Nutzung von Git‑Logs und Pull‑Request‑Historie als Audit‑Trail.

## 12 Backup und Wiederherstellung

- GitHub‑Repos werden serverseitig gesichert; zusätzlich können Spiegel‑Repos (Read‑only) vorgehalten werden.
- Build‑Artefakte und veröffentlichte Dokumentationsstände werden versioniert, sodass frühere Stände rekonstruierbar sind.
- Wiederherstellungsprozeduren (z. B. Rollback auf letzte stabile Version) werden in den Betriebsdokumenten beschrieben.

## 13 Pflege dieses Plans

Dieser CM‑Plan wird bei wesentlichen Änderungen an Prozessen, Werkzeugen oder Rollen aktualisiert. Verantwortung für die Pflege liegt bei der Projektleitung in Abstimmung mit den CM‑Verantwortlichen und den Entwicklungsteams.
