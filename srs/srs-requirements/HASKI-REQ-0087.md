---
id: HASKI-REQ-0087
title: Visualisierung der Lernereigenschaften (ILS/LIST-K)
type: Interface
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-007
links:
  parents: ["SyRS-FUNC-007"]
  stories:
    - "HASKI-RAK/HASKI-Frontend#154"
  tests:
    - path: "frontend/src/pages/LearnerCharacteristics/LearnerCharacteristics.test.tsx"
      name: "LearnerCharacteristics"
    - path: "frontend/src/services/Questionnaire/fetchILS.test.tsx"
      name: "fetchILS has expected behaviour"
    - path: "frontend/src/services/Questionnaire/fetchListK.test.tsx"
      name: "fetchListK has expected behaviour"
---

## Beschreibung

Das System **shall** eine dedizierte Frontend-Seite bereitstellen, auf der Studierende ihre persönlichen Lernstil- und Lernstrategiewerte aus ILS- und LIST-K-Fragebögen einsehen können. Die Darstellung **shall** über einen Stepper zwei getrennte Ansichten (ILS-Ergebnisse und LIST-K-Ergebnisse) anbieten, zwischen denen Nutzende ohne Datenverlust wechseln können. Beide Ansichten **shall** grafische (Graphen) und tabellarische Visualisierungen kombinieren und eine textuelle Beschreibung der Dimensionen bereitstellen. Während des Ladens **shall** ein Skeleton-Loader angezeigt werden, und bei fehlenden Fragebogendaten **shall** ein informativer Hinweis erscheinen, der zum Ausfüllen der Fragebögen motiviert.

## Akzeptanzkriterien

### Stepper-Navigation und Datenladung

- [x] Die Seite zeigt einen Stepper mit zwei Schritten: „ILS-Ergebnisse" und „LIST-K-Ergebnisse".
- [x] Studierende können per Klick zwischen den Schritten wechseln, ohne dass die Seite neu geladen wird.
- [x] Beim Wechsel zu einem Schritt werden die entsprechenden Fragebogendaten asynchron geladen, sofern sie noch nicht im State vorliegen.
- [x] Während des Ladevorgangs wird ein Skeleton-Loader angezeigt, der drei Platzhalter-Elemente enthält.
- [x] Bei Netzwerkfehlern („Failed to fetch") bleibt der Loader aktiv; bei anderen Fehlern wird ein Hinweis angezeigt, dass keine Daten vorliegen.

### Visualisierung der ILS-Ergebnisse

- [x] Wenn ILS-Daten vorliegen (alle Dimensionswerte > 0), werden Grafik (`GraphILS`), Tabelle (`TableILS`) und Textbeschreibung (`ResultDescriptionILS`) nebeneinander dargestellt.
- [x] Die Grafik zeigt die vier Dimensionen des Felder-Silverman-Modells (Input, Perception, Processing, Understanding) mit ihren Ausprägungen an.
- [x] Die Tabelle listet die Dimensionen und Werte in strukturierter Form auf.
- [x] Wenn keine ILS-Daten vorliegen (z.B. `perception_value == 0`), wird eine Meldung angezeigt, die den Studierenden zum Ausfüllen des ILS-Fragebogens auffordert.

### Visualisierung der LIST-K-Ergebnisse

- [x] Wenn LIST-K-Daten vorliegen (alle Strategiewerte > 0), werden Grafik (`GraphListK`), Tabelle (`TableListK`) und Textbeschreibung (`ResultDescriptionListK`) nebeneinander dargestellt.
- [x] Die Grafik zeigt die Lernstrategien (kognitive, metakognitive, interne/externe Ressourcenmanagementstrategien) als Netzwerkdiagramm oder Balken an.
- [x] Die Tabelle listet die einzelnen Strategiewerte auf.
- [x] Wenn keine LIST-K-Daten vorliegen (z.B. `cogn_str == 0`), wird eine Meldung angezeigt, die zum Ausfüllen des LIST-K-Fragebogens auffordert.

### Navigation und Zusatzfunktionen

- [x] Unterhalb der Visualisierungen befindet sich ein Link „Weitere Informationen", der ein PDF-Dokument zu den Fragebögen in einem neuen Tab öffnet.
- [x] Vor- und Zurück-Buttons ermöglichen die Navigation zwischen den beiden Schritten; die Buttons sind deaktiviert, wenn der erste bzw. letzte Schritt erreicht ist.
- [x] Die Komponente ist memo-optimiert und rendert nur bei tatsächlichen Datenänderungen neu.

### Fehlerbehandlung

- [x] Fehlgeschlagene `fetchILS`- oder `fetchListK`-Aufrufe zeigen eine Snackbar mit einer verständlichen Fehlermeldung an.
- [x] Fehler beim Laden der Nutzerdaten führen ebenfalls zu einer Snackbar-Warnung.
- [x] Die Komponente stürzt bei fehlenden Daten nicht ab, sondern zeigt einen stabilen Zustand (Loading oder „Keine Daten").

## Rationale

SyRS-FUNC-007 verlangt, dass Studierende Zugriff auf ihre persönlichen Lernprofile haben, um Transparenz und Selbstreflexion zu fördern. Die LearnerCharacteristics-Seite setzt diese Anforderung um, indem sie sowohl ILS- als auch LIST-K-Ergebnisse in einer nutzerfreundlichen, visuell ansprechenden Form präsentiert. Die Kombination aus Grafiken, Tabellen und Textbeschreibungen ermöglicht es Studierenden mit unterschiedlichen Präferenzen, die Informationen auf die für sie passende Weise zu erfassen. Die klare Trennung zwischen ILS und LIST-K über den Stepper verhindert Überforderung und erlaubt eine fokussierte Betrachtung der jeweiligen Dimension.

## Hinweise

- Die Komponente nutzt React-Hooks (`useState`, `useEffect`, `useContext`) zur Zustandsverwaltung und zum Datenabruf.
- `GraphILS` und `GraphListK` basieren auf Visualisierungsbibliotheken (z.B. Recharts, D3) und sind eigenständige Komponenten.
- `TableILS` und `TableListK` verwenden Material-UI-Tabellenkomponenten für die strukturierte Darstellung.
- `ResultDescriptionILS` und `ResultDescriptionListK` liefern textuelle Interpretationen der Lernstil- und Strategiewerte.
- Die Skeleton-Loader-Komponente (`SkeletonList`) zeigt drei animierte Platzhalter, um Ladezeiten zu überbrücken.
- Die Seite ist responsive gestaltet und passt sich an verschiedene Bildschirmgrößen an.
- Die Übersetzungen für Meldungen und Labels sind in den i18n-Ressourcen hinterlegt (`components.LearnerCharacteristics.*`).
