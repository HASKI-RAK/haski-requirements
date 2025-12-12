---
id: HASKI-REQ-0084
title: Glossareinträge
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
links:
  parents: ["SyRS-FUNC-017"]
  stories:
    - "HASKI-RAK/HASKI-Frontend#196"
  tests:
    - path: "frontend/src/components/Filter/Filter.test.tsx"
      name: "Filter Component"
    - path: "frontend/src/components/Glossary/GlossaryEntry/GlossaryEntry.test.tsx"
      name: "GlossaryEntry tests"
    - path: "frontend/src/components/Glossary/GlossaryIndex/GlossaryIndex.test.tsx"
      name: "GlossaryIndex tests"
    - path: "frontend/src/components/Glossary/GlossaryList/GlossaryList.test.tsx"
      name: "GlossaryList tests"
    - path: "frontend/src/pages/Glossary/Glossary.test.tsx"
      name: "Glossary page tests"
---

## Beschreibung

Das HASKI-Frontend **shall** ein Glossar bereitstellen, das Fachbegriffe erklärt und referenziert. Die Glossarseite **shall** eine Liste von Einträgen anzeigen, die durchsuchbar und filterbar sind.

Das System **shall** einen Mehrfachauswahl-Filter bereitstellen, mit dem Glossareinträge nach inhaltlichen Tags kombiniert werden können. Die Komponente **shall** alle in den Übersetzungsdateien gepflegten Tags als Auswahloptionen anzeigen, die aktuelle Auswahl als Chips visualisieren und bei Benutzerinteraktionen die Tag-Liste aktualisieren, ohne dass die Seite neu geladen werden muss.

## Akzeptanzkriterien

### Glossarseite

- [x] Die Glossarseite zeigt eine Liste von Begriffen und Definitionen an.
- [x] Die Liste kann durchsucht werden.
- [x] Einträge können ein- und ausgeklappt werden ("Collapse All", "Expand All").
- [x] Einträge können nach Tags gefiltert werden.

### Filter-Komponente

- [x] Wird der Filter ohne Eingaben gerendert, bleibt die Komponente stabil und verursacht keine Laufzeitfehler.
- [x] Bei übergebenen Optionen listet die Mehrfachauswahl alle Tags und stellt die aktuelle Auswahl als Chips im Eingabefeld dar.
- [x] Das Öffnen der Auswahlliste ermöglicht die Auswahl mehrerer Tags; jedes Tag lässt sich über Checkboxen aktivieren.
- [x] Bei jedem neu ausgewählten Tag ruft die Komponente `setSelectedOptions` mit der um das Tag erweiterten Liste auf.
- [x] Bereits ausgewählte Tags erscheinen als aktiviert und werden beim erneuten Rendern weiterhin angezeigt.
- [x] Ist `setSelectedOptions` nicht gesetzt, werden Auswahlsignale ignoriert, ohne dass die Komponente abstürzt oder den vorhandenen Zustand verändert.

## Rationale

Issue [#196](https://github.com/HASKI-RAK/HASKI-Frontend/issues/196) definiert die Tag-Struktur für das Glossar und verlangt, dass Studierende relevante Begriffe anhand fachlicher Kategorien filtern können. Die Komponente `Filter` bildet diese Anforderung als wiederverwendbares UI-Element ab und wird durch die Tests `Filter.test.tsx` validiert.
