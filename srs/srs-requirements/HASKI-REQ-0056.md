---
id: HASKI-REQ-0056
title: Lernelemente eines Kurses pro Studierenden abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#21", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_les_in_course_for_student"
---

## Beschreibung

Das System **shall** allen berechtigten Studierenden eine vollständige Liste der Lernelemente eines belegten Kurses liefern. Neben den Stammdaten der Elemente müssen auch die individuellen Lernfortschrittsinformationen enthalten sein, damit Lernräume, Empfehlungen und Visualisierungen direkt mit der gelieferten Struktur arbeiten können.

## Akzeptanzkriterien

- [x] Die zurückgegebene Liste umfasst sämtliche Lernelemente des ausgewählten Kurses samt Typ, Klassifikation, Namen und studentischem Status.
- [x] Elemente, die nicht zur Anfrage passen oder nicht freigegeben sind, werden konsequent ausgeblendet.
- [x] Neue oder geänderte Lernelemente erscheinen ohne zusätzliche Synchronisationsschritte in der Ausgabe.

## Rationale

SyRS-FUNC-008 fordert Transparenz über alle Lernressourcen eines Kurses. Eine standardisierte Lernelement-Liste ermöglicht es, Lernräume aufzubauen, Fortschritte darzustellen und Empfehlungen abzuleiten, ohne mehrere Quellen abgleichen zu müssen.

## Hinweise

- Datenhaltung und API-Schema sind in den zentralen Backend-Dokumenten beschrieben; Änderungen betreffen auch Frontend und Analytics.
- Gemeinsame Autorisierungslogik mit Kurs- und Topic-Routen verhindert Inkonsistenzen bei der Sichtbarkeit.
