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
    - path: "HASKI-Frontend/src/components/Glossary/GlossaryEntry/GlossaryEntry.test.tsx"
      name: "GlossaryEntry tests"
    - path: "HASKI-Frontend/src/components/Glossary/GlossaryIndex/GlossaryIndex.test.tsx"
      name: "GlossaryIndex tests"
    - path: "HASKI-Frontend/src/components/Glossary/GlossaryList/GlossaryList.test.tsx"
      name: "GlossaryList tests"
---

## Beschreibung

Das HASKI-Frontend **shall** einen Mehrfachauswahl-Filter bereitstellen, mit dem Glossareinträge nach inhaltlichen Tags kombiniert werden können. Die Komponente **shall** alle in den Übersetzungsdateien gepflegten Tags als Auswahloptionen anzeigen, die aktuelle Auswahl als Chips visualisieren und bei Benutzerinteraktionen die Tag-Liste aktualisieren, ohne dass die Seite neu geladen werden muss. Fällt kein Callback zur Auswahlsteuerung an, **shall** die Komponente stabil rendern und lediglich die Anzeige der vorgegebenen Tags übernehmen.

## Akzeptanzkriterien

- [x] Wird der Filter ohne Eingaben gerendert, bleibt die Komponente stabil und verursacht keine Laufzeitfehler.
- [x] Bei übergebenen Optionen listet die Mehrfachauswahl alle Tags und stellt die aktuelle Auswahl als Chips im Eingabefeld dar.
- [x] Das Öffnen der Auswahlliste ermöglicht die Auswahl mehrerer Tags; jedes Tag lässt sich über Checkboxen aktivieren.
- [x] Bei jedem neu ausgewählten Tag ruft die Komponente `setSelectedOptions` mit der um das Tag erweiterten Liste auf.
- [x] Bereits ausgewählte Tags erscheinen als aktiviert und werden beim erneuten Rendern weiterhin angezeigt.
- [x] Ist `setSelectedOptions` nicht gesetzt, werden Auswahlsignale ignoriert, ohne dass die Komponente abstürzt oder den vorhandenen Zustand verändert.

## Rationale

Issue [#196](https://github.com/HASKI-RAK/HASKI-Frontend/issues/196) definiert die Tag-Struktur für das Glossar und verlangt, dass Studierende relevante Begriffe anhand fachlicher Kategorien filtern können. Die Komponente `Filter` bildet diese Anforderung als wiederverwendbares UI-Element ab und wird durch die Tests `Filter.test.tsx` validiert.
