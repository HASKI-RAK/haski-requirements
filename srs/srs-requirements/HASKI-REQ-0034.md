---
id: HASKI-REQ-0034
title: Automatische Nutzeranlage aus Moodle-Daten
type: Functional
status: Implemented
source_id: SyRS-INT-003
links:
  stories:
    [
      "HASKI-RAK/HASKI-Backend#85",
      "HASKI-RAK/HASKI-Backend#81",
      "HASKI-RAK/HASKI-Backend#76",
      "HASKI-RAK/HASKI-Backend#21",
      "HASKI-RAK/HASKI-Backend#131",
    ]
  parents: ["SyRS-INT-003", "SyRS-FUNC-001"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_create_user_from_moodle"
    - path: "frontend/src/common/hooks/University/University.test.tsx"
      name: "useUniversity hook"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_admin"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_course_creator"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_settings"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_student"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_empty_user_by_lms_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_user_by_lms_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_teacher"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_user"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_characteristics"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_style"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_strategy"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_knowledge"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_analytics"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_characteristics"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_add_teacher_to_course"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_add_student_to_course"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_add_student_to_course_duplicate"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_add_all_students_to_course"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_add_all_students_to_topics"
    - path: "frontend/src/services/Topic/postAddAllStudentsToTopics.test.ts"
      name: "postAddAllStudentsToTopics has expected behaviour"
    - path: "frontend/src/services/Course/postAddAllStudentsToCourse.test.ts"
      name: "postAddAllStudentsToCourse has expected behaviour"
---

## Beschreibung

Das System **shall** beim ersten Zugriff eines Moodle-Nutzers über LTI oder OIDC automatisch einen vollständigen HASKI-Nutzeraccount mit allen erforderlichen Stammdaten und initialen Einstellungen anlegen. Das System **shall** alle Nutzerrollen (Administrator, Kursersteller, Lehrkraft, Studierende) unterstützen und die Rollenzuordnung aus den Moodle-Daten übernehmen. Bereits registrierte Nutzer **shall** erkannt werden, sodass keine Dubletten entstehen. Die Nutzeranlage **shall** alle notwendigen Datenbanktabellen für den Betrieb initialisieren.

Der Provisionierungsprozess umfasst die Initialisierung folgender Entitäten:

- `User` (Basis-Benutzerdaten aus LTI-Launch)
- `Settings` (Benutzerspezifische Einstellungen)
- `Student` (Rollenspezifische Daten, falls Rolle Student)
- `LearningCharacteristics` (Lernmerkmale)
- `LearningStyle` (Lernstil-Präferenzen, initialisiert mit Standardwerten)
- `Knowledge` (Wissensstand)
- `LearningAnalytics` (Lernfortschrittsdaten)
- `LearningStrategy` (Lernstrategien)
- `StudentCourse` (Verknüpfung zum Kurs)

Ergänzend **shall** das System Benutzende (Lehrkräfte und Studierende) automatisch den importierten Moodle-Kursen und deren Topics zuordnen, sobald sowohl Nutzer- als auch Kursentitäten im HASKI-Datenmodell vorhanden sind. Die Zuordnung **shall** über abgesicherte API-Endpunkte erfolgen, die mit Moodle-LMS-IDs arbeiten und die Beziehung nur einmalig pro Kurs/Benutzer erstellen. Neben Einzelfallzuordnungen **shall** das Backend automatisierte Sync-Endpunkte bereitstellen, die alle in Moodle eingeschriebenen Studierenden für einen Kurs samt zugehöriger Topics in HASKI spiegeln.

## Akzeptanzkriterien

### Nutzeranlage aus Moodle-Daten

- [ ] Das System legt automatisch einen vollständigen Nutzeraccount an, wenn ein Moodle-Nutzer erstmalig auf HASKI zugreift.
- [ ] Alle Nutzerrollen (Administrator, Kursersteller, Lehrkraft, Studierende) werden korrekt erkannt und zugeordnet.
- [ ] Die Nutzeridentität wird aus den Moodle-Stammdaten übernommen (Name, Rolle, Hochschulzugehörigkeit, LMS-Benutzer-ID).
- [ ] Bereits vorhandene Nutzer werden anhand ihrer Moodle-ID erkannt, es werden keine Duplikate angelegt.
- [ ] Die initialen Einstellungen und alle erforderlichen Datenbanktabellen werden automatisch angelegt.
- [ ] Neu angelegte Nutzer können unmittelbar nach der Anlage alle Systemfunktionen nutzen.
- [ ] Fehlgeschlagene Anlageversuche werden protokolliert und sind administrativ nachvollziehbar.
- [ ] Nur authentifizierte Moodle-Zugriffe können Nutzeraccounts anlegen.
- [ ] Alle abhängigen Tabellen (`LearningCharacteristics`, `LearningStyle`, `Knowledge`, `LearningAnalytics`, `LearningStrategy`) werden mit validen Standardwerten initialisiert.
- [ ] Die Integrität der Verknüpfungen (Foreign Keys) ist gewährleistet.
- [ ] Der Vorgang ist idempotent oder prüft auf Existenz, um Duplikate zu vermeiden.

### Einzelne Kurszuordnungen

- [ ] Ein POST-Endpunkt ermöglicht es berechtigten Rollen, eine Lehrkraft anhand der Moodle-ID einem Kurs zuzuweisen; bei gültigen Kurs- und Lehrkraft-IDs wird genau eine Relation erzeugt und mit HTTP 201 quittiert.
- [ ] Ein POST-Endpunkt `POST /lms/course/<course_id>/student/<student_id>` erstellt genau eine Kursmitgliedschaft mit HTTP 201, wenn Kurs- und Studierenden-ID existieren, und liefert Kurs- und Studierenden-IDs sowie initiale Lernstil-Dimensionen zurück.
- [ ] Nicht vorhandene Lehrkräfte, Studierende oder Kurse führen zu HTTP 404 mit erklärender Fehlermeldung.
- [ ] Bereits bestehende Zuordnungen werden nicht dupliziert, sondern liefern einen Validierungsfehler (HTTP 400/409).

### Bulk-Synchronisation von Moodle-Einschreibungen

- [ ] Ein REST-Endpunkt `POST /course/<course_id>/allStudents` synchronisiert alle in Moodle eingeschriebenen Studierenden in die HASKI-Relation `student_course` und liefert bei Erfolg HTTP 201 mit `CREATED`, `course_id` und der Anzahl neu verknüpfter Studierender; ohne neue Zuordnungen wird `CREATED: false` gemeldet.
- [ ] Ein ergänzender Endpunkt `POST /course/<course_id>/topics/allStudents` stellt sicher, dass alle in HASKI erfassten Topics dieses Kurses dieselben Studierenden-Zuordnungen erhalten; die Implementierung ist idempotent und erzeugt keine doppelten Relationen.
- [ ] Für jeden verarbeiteten Studierenden wird geprüft, ob die Moodle-Einschreibung zur Hochschule/Kurs-ID passt; Inkonsistenzen erzeugen keinen Eintrag und werden geloggt.
- [ ] Fehlerhafte Kurs-IDs oder fehlende Referenzdaten lösen nachvollziehbare HTTP-Fehler (z. B. 404) aus, ohne interne Informationen preiszugeben.

## Rationale

Primary implementation: GitHub issue GH-85 "User created when first logged in" spezifiziert die automatische Kontoanlage bei der ersten HASKI-Anmeldung.

Related work:

- GH-81 beschreibt die initial zu befüllenden Tabellen (`haski_user`, `settings`, `student`, `learning_characteristics`, `learning_style`, `knowledge`, `learning_analytics`, `learning_strategy`, `student_course`).

Derived from system requirement SyRS-INT-003 (LTI-Schnittstellen für Moodle-Integration), das die nahtlose Datenübernahme aus Moodle verlangt.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/85
- Related issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/81
- Die Nutzeranlage umfasst folgende Datenstrukturen: Benutzerstammdaten, Einstellungen, Studierendenprofil, Lerncharakteristika, Lernstil, Wissensstand, Lernanalytik, Lernstrategie und Kurszuordnungen
- Die automatische Anlage ist Voraussetzung für alle weiteren Systemfunktionen (Kurseinschreibung, Fragebogen-Bearbeitung, Lernpfad-Berechnung)
- Verifiziert durch E2E-Tests, die alle unterstützten Rollen sowie Fehlerszenarien (fehlende Pflichtfelder, Typfehler, Duplikate) abdecken
