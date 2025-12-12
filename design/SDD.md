# Software Design Description (SDD) nach IEEE 1016

## 1 Zweck und Geltungsbereich

Dieses Dokument beschreibt den Softwareentwurf des HASKI‑Systems auf Basis der System‑Architekturbeschreibung (`architecture/System-AD.md`) und der Anforderungen aus SyRS und SRS. Es konkretisiert die logische und physische Struktur der Softwarekomponenten, ihrer Schnittstellen und Interaktionen.

Die SDD richtet sich an:

- Entwickler:innen und Reviewer für Implementierung und Code‑Refactoring,
- Test‑ und QA‑Teams für Ableitung von Testfällen,
- Architekt:innen für die Bewertung von Designentscheidungen,
- Betreibende für Verständnis technischer Abhängigkeiten und Fehlersuche.

## 2 Referenzen

- `architecture/System-AD.md` – System‑Architekturbeschreibung nach ISO/IEC/IEEE 42010
- `syrs/SyRS.md` – System Requirements Specification
- `srs/SRS.md` – Software Requirements Specification
- `governance/Requirements-Management-Plan.md`
- `governance/Info-Security-Plan.md`

## 3 Überblick über die Softwarestruktur

Die HASKI‑Software ist in zwei Hauptartefakte gegliedert:

- **HASKI‑Backend** (`HASKI-Backend/`): Python‑basierter Dienst mit Flask‑App, Domänenschichten und Integrationen.
- **HASKI‑Frontend** (`HASKI-Frontend/`): React‑Single‑Page‑Application mit Komponenten, Services und Zustandsspeicherung.

Beide Artefakte folgen einem schichteten Design mit klaren Zuständigkeiten:

- Präsentationsebene (UI‑Komponenten, Seiten),
- Applikationslogik (Services, Hooks, Use‑Cases),
- Domänen‑/Datenzugriffsschicht (Domain‑Modelle, Repositories, API‑Adapter).

Im Folgenden werden Backend und Frontend getrennt beschrieben.

## 4 Backend-Design

### 4.1 Verzeichnisstruktur und Schichten

Wesentliche Verzeichnisse im `HASKI-Backend/`‑Projekt:

- `entrypoints/`

  - `flask_app.py`: Definition der Flask‑Applikation, Routing, Registrierung von Blueprints und Integrationsendpunkten (REST, LTI/OIDC).
  - `HASKI-OAS.yaml`: OpenAPI‑Spezifikation der bereitgestellten HTTP‑Schnittstellen.

- `domain/`

  - Enthält das Domänenmodell in thematischen Unterordnern (`domainModel`, `learnersModel`, `taskEvaluation`, `tutoringModel`, `userAdministartion`).
  - Kapselt fachliche Konzepte wie User, Course, Topic, LearningElement, LearningPath, Knowledge, LearningAnalytics.

- `service_layer/`

  - `services.py`: Anwendungsfälle (Use Cases) für Kurse, Topics, Learning Elements, Lernpfade usw.
  - `unit_of_work.py`: Transaktionale Aggregation von Repository‑Operationen.

- `repositories/`

  - `orm.py`: ORM‑Definitionen (z. B. SQLAlchemy‑Modelle).
  - `repository.py`: Generische und spezialisierte Repository‑Klassen zur Kapselung des Datenbankzugriffs.

- `utils/`, `errors/`
  - Hilfsfunktionen, Logging, Fehlerklassen und Dekoratoren (z. B. Authentifizierung/Autorisierung).

Diese Struktur realisiert eine klassische **Layered Architecture**:

UI/HTTP → Service Layer → Domain → Repositories/ORM → Datenbank.

### 4.2 Zentrale Backend-Komponenten

#### 4.2.1 Nutzer- und Kursverwaltung

- **User‑Provisionierung** (HASKI‑REQ‑0034)

  - Service‑Funktionen für die automatische Anlage von User, Settings, Student, LearningCharacteristics, LearningStyle, Knowledge, LearningAnalytics, LearningStrategy und StudentCourse bei Erstzugriff.
  - Aufrufbar über LTI/OIDC‑Launch‑Flows und interne Services.

- **Kurs‑ und Topic‑Synchronisation** (HASKI‑REQ‑0035, 0036, 0037)
  - Endpunkte für Import, Aktualisierung und Löschung von Kursen, Topics und Learning Elements aus Moodle.
  - Nutzung von Moodle‑IDs und konsistenten Relationen (`course_topic`, `topic_learning_element`).

#### 4.2.2 Lernpfad- und Tutoring-Modell

- **Learning Path Services** (HASKI‑REQ‑0040, 0059, 0095)

  - Definition eines Algorithmus‑Katalogs und Zuordnung pro Topic/Student:in.
  - Generierung und Persistenz adaptiver Lernpfade.
  - Abruf aktueller Lernpfade für Frontend‑Darstellungen.

- **Tutoring‑Algorithmen**
  - In `tutoringModel/` implementierte Verfahren (z. B. ACO, GA, grafbasierte Ansätze, Nestor, Tyche).
  - Nutzung von Lernstildaten, Wissensständen und Analytics zur Pfadberechnung.

### 4.3 Typische Backend-Sequenzen

#### 4.3.1 Erstzugriff und Nutzeranlage

1. LTI/OIDC‑Request trifft in `entrypoints/flask_app.py` ein.
2. Authentifizierungs‑/Authorisierungslogik prüft Token und Kontext.
3. Service‑Funktion zur Nutzeranlage prüft vorhandene User; bei Bedarf werden Domänenobjekte initialisiert.
4. Ergebnis (User‑Kontext) wird an Frontend/Client zurückgegeben.

#### 4.3.2 Kursimport und Topic-Struktur

1. Lehrende stoßen im Frontend den Importfunktion an.
2. Frontend ruft Backend‑Endpunkte für Remote‑Kurse/Topics auf.
3. Service‑Layer erzeugt/aktualisiert Kurs‑, Topic‑ und LE‑Einträge.
4. Repositories persistieren Änderungen innerhalb einer Unit of Work.

#### 4.3.3 Lernpfadgenerierung

1. Frontend oder Hintergrundprozess ruft „Generate Learning Path“ für Student/Kurs/Topic auf.
2. Service‑Layer ermittelt Algorithmuskonfigurationen und Domänenobjekte.
3. Tutoring‑Modul berechnet Pfad und gibt Reihenfolge von Learning Elements zurück.
4. Pfad wird gespeichert und ist über Lese‑Endpunkte abrufbar.

## 5 Frontend-Design

### 5.1 Verzeichnisstruktur

Wichtige Verzeichnisse im `HASKI-Frontend/`‑Projekt:

- `src/pages/`: Seitenkomponenten (z. B. `Home`, `Course`, `Topic`, Einstellungen).
- `src/components/`: Wiederverwendbare Komponenten (z. B. `CourseCard`, `CreateCourse`, `CreateTopic`, Lernpfad‑Editor).
- `src/services/`: API‑Clients für Backend‑Endpunkte (z. B. Kurse, Topics, Learning Elements, Lernpfade, Algorithmen).
- `src/store/`: Zustandsslices (z. B. Kurs‑, Topic‑, Lernpfad‑Slices) auf Basis von Zustand/Redux‑ähnlichen Patterns.
- `src/common/`, `src/shared/`: Hilfsfunktionen, Hooks, UI‑Utilities.

### 5.2 UI-Komponenten und Zustandsverwaltung

- **Kurs‑ und Topic‑Management**

  - Tabellen‑ und Formular‑Komponenten für Kurs‑/Topic‑Anlage, Import und Bearbeitung.
  - Dialoge für Remote‑Import aus Moodle (CreateRemoteTopicsStep, CreateLearningElementsStep).

- **Adaptive Lernpfade**

  - Visualisierung von Lernpfaden (z. B. auf Basis von React Flow),
  - Konfiguration von Algorithmen pro Topic/Student:in,
  - Anzeige des aktuellen Fortschritts und Navigation zwischen Learning Elements.

- **State‑Management**
  - Slices für Kurse, Topics, LEs, Lernpfade, Settings; Caching‑Strategien, um wiederholte API‑Aufrufe zu reduzieren.

### 5.3 Interaktion mit dem Backend

- Alle Backend‑Aufrufe werden über Service‑Module gekapselt (z. B. `CourseService`, `TopicService`, `LearningPathService`).
- Fehlerbehandlung und Benutzerfeedback erfolgen zentral (z. B. Snackbar‑/Toast‑Mechanismus).
- Authentifizierungsinformationen werden aus dem LTI/OIDC‑Kontext bzw. Session‑Informationen bezogen.

## 6 Entwurfsentscheidungen (Design Decisions)

Beispiele für wichtige Entwurfsentscheidungen (Detail‑ADs, verfeinernd zu den System‑ADs):

1. **DD‑001: Verwendung von Unit of Work im Backend**

   - Bündelung von Repository‑Operationen in einer Transaktion, um Konsistenz bei komplexen Import‑/Update‑Vorgängen sicherzustellen.

2. **DD‑002: API‑First Ansatz**

   - Generierung/Validierung von Endpunkten gegen `HASKI-OAS.yaml` zur Sicherstellung konsistenter Schnittstellen gegenüber Frontend und externen Systemen.

3. **DD‑003: Komponentenbasierter Frontend‑Entwurf**

   - Wiederverwendbare UI‑Bausteine für Tabellen, Dialoge, Formulare, so dass neue Domänenfunktionen schneller umgesetzt werden können.

4. **DD‑004: Klare Trennung von Präsentation und Logik**
   - Nutzung von Hooks/Services für Geschäftslogik im Frontend, Präsentationskomponenten bleiben zustandsarm.

## 7 Beziehung zu Anforderungen und Tests

- Für zentrale Anforderungen (z. B. HASKI‑REQ‑0034, 0035, 0036, 0037, 0095) existieren jeweils:
  - klar zuordenbare Backend‑Services und Endpunkte,
  - korrespondierende Frontend‑Funktionen/Seiten,
  - automatisierte Unit‑, Integrations‑ und E2E‑Tests (vgl. `HASKI-Backend/tests`, `HASKI-Frontend/reports`).
- Die Traceability wird über das RTM (`traceability/RTM.csv`) und die `links.tests`‑Einträge in den Anforderungen abgesichert.

## 8 Weiteres Vorgehen

Dieses Dokument bildet den Rahmen für detailliertere, modul‑/komponentenbezogene Entwürfe. Bei Einführung neuer größerer Features (z. B. zusätzliche LMS‑Integrationen, neue Tutoring‑Algorithmen) sind Designentscheidungen und betroffene Komponenten hier zu ergänzen.
