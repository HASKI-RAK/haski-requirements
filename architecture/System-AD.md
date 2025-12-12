# System-Architekturbeschreibung (System-AD)

## 1 Zweck und Geltungsbereich

Dieses Dokument beschreibt die Software- und Systemarchitektur des HASKI-Systems (AI‑unterstütztes adaptives Lernen) nach dem Vorbild von ISO/IEC/IEEE 42010. Es dient als gemeinsame Referenz für Entwicklung, Betrieb, Qualitätssicherung und Stakeholder‑Kommunikation.

Die Architekturbeschreibung:

- fokussiert auf die produktive HASKI‑Plattform (Backend, Frontend, Datenhaltung, Integrationen),
- adressiert funktionale und nicht‑funktionale Anforderungen aus SyRS, SyRS‑INT, SyRS‑PERF, SyRS‑SEC sowie der SRS,
- definiert zentrale Architekturentscheidungen, Qualitätsziele und technische Leitplanken.

## 2 Referenzen

- **Normen und Leitlinien**

  - ISO/IEC/IEEE 42010: Systems and software engineering – Architecture description
  - ISO/IEC/IEEE 29148: Requirements engineering
  - ISO/IEC 25010: System and software quality models
  - ISO/IEC 27001: Informationssicherheits-Management (orientierend)

- **Projektinterne Dokumente**
  - `strs/StRS.md` – Stakeholder Requirements Specification
  - `syrs/SyRS.md` – System Requirements Specification
  - `srs/SRS.md` – Software Requirements Specification
  - `governance/Requirements-Management-Plan.md`
  - `governance/Info-Security-Plan.md`
  - `governance/CM-Plan.md`
  - `design/SDD.md` – Software Design Description (detaillierter Entwurf)

## 3 Systemüberblick

HASKI ist ein webbasiertes, serviceorientiertes Lernsystem, das Lernende über adaptive Lernpfade, Learning Analytics und Tutoring‑Funktionen unterstützt. Das System integriert sich mit bestehenden Lernmanagementsystemen (insbesondere Moodle) über standardisierte Protokolle (LTI, OIDC, Webservices).

Das Gesamtsystem besteht grob aus folgenden Subsystemen:

- **HASKI‑Frontend**: Single‑Page‑Application (React/Vite) zur Interaktion von Studierenden, Lehrenden und Administrator:innen.
- **HASKI‑Backend**: Python‑basiertes Backend (Flask‑App) mit Domänenschichten (Domain, Service Layer, Repositories, Unit of Work),
  das Business‑Logik, Persistenz und Integrationen kapselt.
- **Datenbank**: Relationale Datenbank für Nutzer, Kurse, Topics, Learning Elements, Lernpfade, Analytics‑Daten etc.
- **Moodle‑Integration**: LTI/OIDC‑basierte Nutzeranmeldung sowie REST‑/Webservice‑basierte Synchronisation von Kursen, Topics, Learning Elements und Einschreibungen.
- **Monitoring & Operations**: Logging, Health‑Checks, Metriken sowie CI/CD‑Pipelines für Build, Test und Deployment.

## 4 Stakeholder und Anliegen

| Stakeholder               | Rolle/Interesse                                             |
| ------------------------- | ----------------------------------------------------------- |
| Studierende               | Adaptive Lernpfade, stabile Plattform, Datenschutz          |
| Lehrende/Kursersteller    | Verwaltung von Kursen, Topics, Learning Elements, Reporting |
| Tutor:innen/Fachteam      | Konfiguration von Algorithmen, Auswertung von Analytics     |
| Administrator:innen       | Betrieb, Konfiguration, Benutzer‑ und Rechteverwaltung      |
| Projektleitung            | Zielerreichung, Budget, Risiken, ISO‑Konformität            |
| Datenschutz/IT‑Sicherheit | DSGVO‑Konformität, Zugriffsschutz, Protokollierung          |
| DevOps/Operations         | Wartbarkeit, Observability, Deployment‑Automatisierung      |

Zentrale Anliegen sind u. a.:

- Hohe Verfügbarkeit in Lehr‑ und Prüfungszeiten (vgl. HASKI‑REQ‑0030),
- Vertraulichkeit und Schutz personenbezogener Daten (Anonymisierung/Pseudonymisierung),
- Erweiterbarkeit der Lernpfad‑Algorithmen,
- Rückverfolgbarkeit von Anforderungen zu Architekturentscheidungen und Implementierung.

## 5 Architekturprinzipien und -ziele

- **Schichtenarchitektur**: Klare Trennung von Präsentation (Frontend), Anwendungslogik (Service Layer) und Persistenz (Repository‑Schicht).
- **Domain‑Driven Design Light**: Domänenobjekte für zentrale Konzepte (User, Course, Topic, LearningElement, LearningPath, Analytics).
- **API‑Zentrierung**: Alle externen Integrationen (Moodle, weitere LMS) erfolgen über klar definierte REST‑/LTI‑Schnittstellen.
- **Konfigurierbare Adaptivität**: Lernpfad‑Algorithmen sind als konfigurierbare Strategien implementiert und können pro Topic/Student:in gewählt werden.
- **Security & Privacy by Design**: Minimaler Datenumfang, Rollen‑/Rechtemodell, Pseudonymisierung und Verschlüsselung gemäß SyRS‑SEC.
- **Testbarkeit & Traceability**: Hohe Testabdeckung, Zuordnung von Tests zu Anforderungen (RTM) und reproduzierbare Build‑/Deploy‑Pipelines.

## 6 Architektur-Viewpoints und Views

### 6.1 Kontextsicht (Systemkontext)

Das HASKI‑System ist in folgende Umgebung eingebettet:

- **Externe Systeme**

  - Hochschul‑Moodle‑Instanzen (LMS): Quellsystem für Nutzer, Kurse, Topics, Learning Elements.
  - Identity Provider / LTI‑Plattformen: Authentifizierung und Autorisierung via LTI/OIDC.
  - Optionale Analyse‑/Reporting‑Tools.

- **Benutzergruppen**
  - Studierende, Lehrende, Administrator:innen greifen ausschließlich über das Frontend (Browser) auf HASKI zu.

Die Kontextsicht stellt sicher, dass Integrationsschnittstellen (z. B. HASKI‑REQ‑0034, 0035, 0036, 0037) klar von interner Logik getrennt sind.

### 6.2 Logische Sicht

Zentrale logische Komponenten des HASKI‑Backends:

- **Domain Layer**

  - `userAdministration`: User, Roles, Settings, Student/Teacher/Admin‑Domänenobjekte.
  - `domainModel`: Course, Topic, Subtopic, LearningElement, LearningPath.
  - `taskEvaluation`/`tutoringModel`: Algorithmen und Modelle für adaptive Pfade und Empfehlungen.

- **Service Layer** (`service_layer/services.py`)

  - Orchestriert Domänenoperationen (z. B. Import aus Moodle, Erstellen/Aktualisieren von Kursen, Generierung von Lernpfaden).
  - Implementiert Anwendungsfälle gemäß SRS/SyRS (z. B. HASKI‑REQ‑0035, 0036, 0037, 0095).

- **Repository‑ und Persistenzschicht** (`repositories/orm.py`, `repository.py`)

  - Kapselt den Zugriff auf die relationale Datenbank mittels ORM‑Modellen.
  - Stellt transaktionale Operationen (über `unit_of_work`) bereit.

- **API/Entrypoints** (`entrypoints/flask_app.py`)
  - REST‑Endpunkte für Kurse, Topics, Learning Elements, Lernpfade, Einstellungen usw.
  - LTI/OIDC‑Entrypoints für Authentifizierung und Nutzeranlage.

### 6.3 Prozess- und Laufzeitsicht

Typische Abläufe:

1. **Erstzugriff eines Moodle‑Nutzers**

   - LTI/OIDC‑Launch vom LMS → HASKI‑Backend.
   - Service Layer legt bei Bedarf einen neuen Nutzer samt zugehöriger Domänenobjekte an (HASKI‑REQ‑0034).

2. **Kurs‑ und Topic‑Synchronisation**

   - Backend ruft Remote‑Kursstruktur aus Moodle ab (HASKI‑REQ‑0035, 0068).
   - Service Layer erzeugt/aktualisiert Kurse, Topics und Learning Elements (HASKI‑REQ‑0035, 0036, 0037).

3. **Generierung adaptiver Lernpfade**
   - Aufruf der Lernpfad‑API (z. B. durch Frontend oder Hintergrundprozess).
   - Tutoring‑Modell berechnet Pfade anhand ausgewählter Algorithmen und Lernstildaten (HASKI‑REQ‑0095).
   - Pfad wird persistiert und für spätere Abrufe bereitgestellt.

### 6.4 Deployment-Sicht

Ziel‑Deployment (vereinfachte Sicht):

- **Frontend**: Containerisierte React‑App, ausgeliefert über Webserver/Reverse Proxy (z. B. Nginx).
- **Backend**: Python/Flask‑Anwendung in einem oder mehreren Containern, hinter einem HTTP‑Reverse‑Proxy.
- **Datenbank**: Zentraler Datenbankdienst (z. B. PostgreSQL/MariaDB) im gesicherten Netzwerksegment.
- **Moodle**: Externe Systeme, angebunden über HTTPS (LTI/OIDC, REST/Webservices).

Nicht‑funktionale Anforderungen (Performance, Skalierbarkeit, Verfügbarkeit) werden durch horizontale Skalierung des Backends, Caching sowie Datenbank‑Tuning adressiert.

### 6.5 Daten- und Integrationssicht

- **Moodle → HASKI**

  - Nutzer‑, Kurs‑, Topic‑ und Learning‑Element‑Daten werden über dedizierte Endpunkte synchronisiert (HASKI‑REQ‑0034, 0035, 0036, 0037).
  - Einschreibungen und Kurszuordnungen werden über Einzel‑ und Bulk‑Endpunkte übernommen.

- **HASKI intern**
  - Datendomänen sind normalisiert; Referenzen (FKs) sichern Konsistenz zwischen User, Course, Topic, LearningElement und LearningPath.
  - Analytics‑ und Knowledge‑Daten werden mit Learning‑Events verknüpft.

## 7 Architekturentscheidungen (ADs)

Ausgewählte, dokumentationswürdige Architekturentscheidungen:

1. **AD‑001: Serviceorientierte Monolith‑Architektur**

   - Entscheidung zugunsten eines logisch geschichteten Monolithen statt verteilter Microservices, um Komplexität, Betriebsaufwand und Latenzen zu reduzieren.

2. **AD‑002: Nutzung eines relationalen Datenbanksystems**

   - Konsistente, transaktionale Verarbeitung und komplexe Joins sind zentral für Lernpfade, Analytics und Berichte.

3. **AD‑003: Integration über LTI/OIDC und REST**

   - Standardisierte Protokolle minimieren Kopplung an Moodle‑Versionen und erleichtern Multi‑LMS‑Szenarien.

4. **AD‑004: Algorithmus‑Katalog + Zuordnung pro Topic/Student:in**

   - Lernpfad‑Algorithmen werden über einen Katalog verwaltet; Auswahl und Overrides erfolgen pro Topic und ggf. pro Studierender (HASKI‑REQ‑0040, 0095).

5. **AD‑005: Trennung von Benutzeridentität und Lern-/Nutzungsdaten**
   - Umsetzung der Anforderungen aus SyRS‑SEC und HASKI‑REQ‑0001 zur Pseudonymisierung/Anonymisierung.

## 8 Qualitätsanforderungen und -szenarien

- **Verfügbarkeit**: ≥ 99 % in Lehr‑ und Prüfungszeiten (HASKI‑REQ‑0030); erreicht durch redundante Komponenten, Monitoring und definierte Wartungsfenster.
- **Performance**: Antwortzeiten für zentrale User‑Flows (Kursübersicht, Lernpfadabruf) im Sekundenbereich; Algorithmus‑Laufzeiten ggf. asynchron.
- **Sicherheit**: Rollenbasiertes Zugriffskonzept, Transportverschlüsselung (TLS), Logging sicherheitsrelevanter Ereignisse, Minimierung personenbezogener Daten.
- **Wartbarkeit**: Klar getrennte Module, konsistente Coding‑Guidelines, automatisierte Tests und statische Analysen.

## 9 Rückverfolgbarkeit zu Anforderungen

Die in dieser Architekturbeschreibung dargestellten Strukturen und Entscheidungen sind u. a. aus folgenden Anforderungen abgeleitet:

- SyRS‑INT‑003: Moodle‑Integration via LTI/REST (HASKI‑REQ‑0034, 0035, 0036, 0037).
- SyRS‑FUNC‑008: Lernpfad‑fähige Räume, Algorithmenkatalog und Pfadabruf (HASKI‑REQ‑0040, 0059, 0095).
- SyRS‑PERF‑001: Verfügbarkeits‑ und Performance‑Vorgaben (HASKI‑REQ‑0030).
- SyRS‑SEC‑001: Datenschutz, Anonymisierung, Pseudonymisierung (HASKI‑REQ‑0001 u. a.).

Die konkrete Zuordnung einzelner Anforderungen zu Komponenten und Tests erfolgt im RTM (`traceability/RTM.csv`) und in den SDD‑Artefakten.

## 10 Risiken und technische Schulden

- Abhängigkeit von konkreten Moodle‑APIs und ‑Plugins.
- Komplexität der Lernpfad‑Algorithmen und deren Performance bei großen Kursen.
- Technische Schulden bei Legacy‑Teilen der Domänenschicht, die schrittweise refaktoriert werden müssen.

## 11 Begriffe und Abkürzungen

- **LMS** – Learning Management System (z. B. Moodle)
- **LTI** – Learning Tools Interoperability
- **OIDC** – OpenID Connect
- **LE** – Learning Element (Lerneinheit/Aktivität)
- **AD** – Architecture Decision

Dieses Dokument wird im Projektverlauf iterativ gepflegt und bei wesentlichen Architekturänderungen aktualisiert.
