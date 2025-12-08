---
id: HASKI-REQ-0054
title: Einzelnen Studierendenkurs abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#131", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_student_course"
    - path: "HASKI-Frontend/src/store/Slices/CourseSlice.test.ts"
      name: "CourseSlice setCourse"
---

## Beschreibung

Das System **shall** die Detaildaten eines belegten Kurses bereitstellen, sobald eine Anwendung diese für einen berechtigten Studierenden benötigt. Die gelieferten Informationen sollen sämtliche Kurseigenschaften umfassen, die für Dashboards, Lernräume oder Reporting relevant sind, ohne dass zusätzliche Nachschlagevorgänge notwendig werden.

## Akzeptanzkriterien

- [x] Für gültige Kurs-/Studierendenkombinationen stehen vollständige Metadaten (z. B. interne Kennung, LMS-Referenz, Bezeichnung, Hochschule) zur Verfügung.
- [x] Anfragen außerhalb der zulässigen Einschreibungen werden konsequent abgewiesen und geben keine Details zu fremden Kursen preis.
- [x] Aktualisierte Kursattribute sind unmittelbar nach Pflege im System sichtbar, sodass gekoppelte Oberflächen immer auf aktuelle Daten zugreifen.

## Rationale

Konfigurierbare Lernräume (SyRS-FUNC-008) benötigen Detailinformationen pro Kurs, etwa für Breadcrumbs, Kursbanner oder die Auswahl von Lernpfaden. Eine abstrahierte Kursdetailabfrage sorgt dafür, dass jede Oberfläche identische Informationen nutzt.

## Hinweise

- Autorisierungsentscheidungen sollen mit der Kursliste und den Topic-Routen konsistent sein.
- Relevante Felder sind im OAS-Schema dokumentiert und sollten versioniert angepasst werden.
