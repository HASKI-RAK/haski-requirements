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
    ]
  parents: ["SyRS-INT-003"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_create_user_from_moodle"
    - path: "frontend/src/common/hooks/University/University.test.tsx"
      name: "useUniversity hook"
---

## Beschreibung

Das System **shall** beim ersten Zugriff eines Moodle-Nutzers über LTI oder OIDC automatisch einen vollständigen HASKI-Nutzeraccount mit allen erforderlichen Stammdaten und initialen Einstellungen anlegen. Das System **shall** alle Nutzerrollen (Administrator, Kursersteller, Lehrkraft, Studierende) unterstützen und die Rollenzuordnung aus den Moodle-Daten übernehmen. Bereits registrierte Nutzer **shall** erkannt werden, sodass keine Dubletten entstehen. Die Nutzeranlage **shall** alle notwendigen Datenbanktabellen für den Betrieb initialisieren.

## Akzeptanzkriterien

- [ ] Das System legt automatisch einen vollständigen Nutzeraccount an, wenn ein Moodle-Nutzer erstmalig auf HASKI zugreift
- [ ] Alle Nutzerrollen (Administrator, Kursersteller, Lehrkraft, Studierende) werden korrekt erkannt und zugeordnet
- [ ] Die Nutzeridentität wird aus den Moodle-Stammdaten übernommen (Name, Rolle, Hochschulzugehörigkeit, LMS-Benutzer-ID)
- [ ] Bereits vorhandene Nutzer werden anhand ihrer Moodle-ID erkannt, es werden keine Duplikate angelegt
- [ ] Die initialen Einstellungen und alle erforderlichen Datenbanktabellen werden automatisch angelegt
- [ ] Neu angelegte Nutzer können unmittelbar nach der Anlage alle Systemfunktionen nutzen
- [ ] Fehlgeschlagene Anlageversuche werden protokolliert und sind administrativ nachvollziehbar
- [ ] Nur authentifizierte Moodle-Zugriffe können Nutzeraccounts anlegen

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
