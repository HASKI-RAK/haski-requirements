---
id: HASKI-REQ-0086
title: Instrumentierte Standard-UI-Komponenten im Frontend
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
links:
  parents: ["SyRS-FUNC-018"]
  stories:
    - "HASKI-RAK/HASKI-Frontend#285"
    - "HASKI-RAK/HASKI-Frontend#287"
    - "HASKI-RAK/HASKI-Frontend#256"
    - "HASKI-RAK/HASKI-Frontend#111"
  tests:
    - path: "frontend/src/common/components/DefaultAccordion/DefaultAccordion.test.tsx"
      name: "DefaultAccordion renders"
    - path: "frontend/src/common/components/DefaultBox/DefaultBox.test.tsx"
      name: "DefaultBox tests"
    - path: "frontend/src/common/components/DefaultButton/DefaultButton.test.tsx"
      name: "DefaultButton sends statement"
    - path: "frontend/src/common/components/DefaultFab/DefaultFab.test.tsx"
      name: "DefaultFab renders"
    - path: "frontend/src/common/components/DefaultIconButton/DefaultIconButton.test.tsx"
      name: "DefaultIconButton renders"
    - path: "frontend/src/common/components/DefaultLink/DefaultLink.test.tsx"
      name: "DefaultLink renders"
    - path: "frontend/src/common/components/DefaultListItemButton/DefaultListItemButton.test.tsx"
      name: "DefaultListItemButton renders correctly"
    - path: "frontend/src/common/components/DefaultMenu/DefaultMenu.test.tsx"
      name: "DefaultMenu renders correctly"
    - path: "frontend/src/common/components/DefaultMenuItem/DefaultMenuItem.test.tsx"
      name: "DefaultMenuItem renders correctly"
    - path: "frontend/src/common/components/DefaultModal/DefaultModal.test.tsx"
      name: "DefaultModal renders correctly"
    - path: "frontend/src/common/components/DefaultPopover/DefaultPopover.test.tsx"
      name: "DefaultPopover renders correctly"
    - path: "frontend/src/common/components/DefaultRadio/DefaultRadio.test.tsx"
      name: "DefaultRadio renders correctly"
    - path: "frontend/src/common/components/DefaultRadioGroup/DefaultRadioGroup.test.tsx"
      name: "DefaultRadioGroup renders correctly"
    - path: "frontend/src/common/components/DefaultSelect/DefaultSelect.test.tsx"
      name: "DefaultSelect renders correctly"
    - path: "frontend/src/common/components/DefaultStepButton/DefaultStepButton.test.tsx"
      name: "DefaultStepButton renders correctly"
    - path: "frontend/src/common/components/DefaultSwitch/DefaultSwitch.test.tsx"
      name: "DefaultSwitch renders correctly"
    - path: "frontend/src/common/components/DefaultToggleButtonGroup/DefaultToggleButtonGroup.test.tsx"
      name: "DefaultToggleButtonGroup renders correctly"
    - path: "frontend/src/common/components/DefaultTypography/DefaultTypography.test.tsx"
      name: "TextWrapper renders correctly"
    - path: "frontend/src/components/CollapsibleList/CollapsibleList/CollapsibleList.test.tsx"
      name: "CollapsibleList tests"
    - path: "frontend/src/components/CollapsibleList/CollapsibleListEntry/CollapsibleListEntry.test.tsx"
      name: "CollapsibleListEntry tests"
    - path: "frontend/src/components/Searchbar/Searchbar.test.tsx"
      name: "Searchbar tests"
    - path: "frontend/src/components/SkeletonList/SkeletonList.test.tsx"
      name: "SkeletonList component"
    - path: "frontend/src/components/Snackbar/handleError.test.tsx"
      name: "handleError tests"
    - path: "frontend/src/components/Snackbar/SnackbarContainer/SnackbarContainer.test.tsx"
      name: "SnackbarContainer tests"
    - path: "frontend/src/components/Snackbar/SnackbarMessage/SnackbarMessage.test.tsx"
      name: "SnackbarMessage tests"
    - path: "frontend/src/components/Snackbar/SnackbarTransition/SnackbarTransition.test.tsx"
      name: "SnackbarTransition tests"
    - path: "frontend/src/components/ToggleButtonList/ToggleButtonList.test.tsx"
      name: "ToggleButtonList tests"
    - path: "frontend/src/services/connection/NetworkStatus.test.tsx"
      name: "Test useNetworkStatus"
    - path: "frontend/src/services/debounce/debounce.test.tsx"
      name: "Debounce tests"
    - path: "frontend/src/services/PageName/PageName.test.tsx"
      name: "Test usePageName"
---

## Beschreibung

Das Frontend **shall** die in `@common/components` gebündelten Material-UI-Basisbausteine als instrumentierte Wrapper bereitstellen, die über `withXAPI` automatisch Komponentenpfad, Seitennamen und Ereignistyp an das Tracking weitergeben. Die Wrapper **shall** sämtliche ursprünglichen Props sowie verschachtelte Inhalte unverändert durchreichen, damit bestehende Views ohne zusätzlichen Aufwand auf die instrumentierten Varianten wechseln können.

Zusätzlich **shall** das Frontend wiederverwendbare UI-Hilfskomponenten bereitstellen, die über verschiedene Seiten hinweg konsistente Benutzerinteraktionen und Ladezustände ermöglichen. Die `Searchbar`-Komponente **shall** eine debounced Sucheingabe mit konfigurierbarem Timeout anbieten, um unnötige Backend-Anfragen zu vermeiden und Filteroperationen zu optimieren. Die `SkeletonList`-Komponente **shall** animierte Platzhalter-Elemente rendern, die während des Ladens von Daten angezeigt werden und ein nahtloses Nutzererlebnis schaffen.

## Akzeptanzkriterien

### Instrumentierte xAPI-Wrapper

- [x] `DefaultAccordion`, `DefaultButton`, `DefaultFab`, `DefaultIconButton`, `DefaultListItemButton`, `DefaultMenu`, `DefaultMenuItem`, `DefaultModal`, `DefaultPopover`, `DefaultRadio`, `DefaultRadioGroup`, `DefaultSelect`, `DefaultStepButton`, `DefaultSwitch`, `DefaultToggleButtonGroup`, `DefaultTypography`, `ImageWrapper` und `NodeWrapper` nutzen `withXAPI`, um `componentFilePath` und `componentType` für xAPI-Statements zu setzen.
- [x] Die Wrapper rufen `usePageName` auf und ergänzen die übergebenen Props unverändert um die Tracking-Metadaten, sodass bestehende Views ohne Anpassungen funktionieren.
- [x] Die Tests `DefaultAccordion renders`, `DefaultBox tests`, `DefaultButton sends statement`, `DefaultFab renders`, `DefaultIconButton renders`, `DefaultLink renders`, `DefaultListItemButton renders correctly`, `DefaultMenu renders correctly`, `DefaultMenuItem renders correctly`, `DefaultModal renders correctly`, `DefaultPopover renders correctly`, `DefaultRadio renders correctly`, `DefaultRadioGroup renders correctly`, `DefaultSelect renders correctly`, `DefaultStepButton renders correctly`, `DefaultSwitch renders correctly`, `DefaultToggleButtonGroup renders correctly` und `TextWrapper renders correctly` schlagen nicht fehl und belegen die renderstabilen instrumentierten Wrapper.

### Searchbar

- [x] Die `Searchbar` rendert ein Textfeld mit optionalem Label und akzeptiert eine `setSearchQuery`-Callback-Funktion (verifiziert durch "Searchbar tests").
- [x] Eingaben in die Searchbar werden mit einem konfigurierbaren Timeout (Standard: 300ms) debounced, sodass die `setSearchQuery`-Funktion erst nach Eingabepause aufgerufen wird.
- [x] Die Komponente rendert fehlerfrei auch ohne übergebene Props und zeigt ein Standardverhalten.
- [x] Änderungen an der Sucheingabe triggern `setTimeout` mit dem konfigurierten Timeout-Wert.

### SkeletonList

- [x] Die `SkeletonList` rendert standardmäßig drei animierte Skeleton-Elemente (Material-UI Skeleton) (verifiziert durch "SkeletonList component").
- [x] Die Komponente kann optional eine konfigurierbare Anzahl von Skeleton-Elementen anzeigen.
- [x] Die Skeleton-Elemente nutzen Material-UI-Animation für eine konsistente Ladeanzeige über alle Ansichten hinweg.
- [x] Die Komponente stürzt bei fehlenden Props nicht ab und rendert stabil.

## Rationale

Issues [#285](https://github.com/HASKI-RAK/HASKI-Frontend/issues/285) und [#287](https://github.com/HASKI-RAK/HASKI-Frontend/issues/287) führen eine zentrale xAPI-Instrumentierung der UI-Basisbibliothek ein und ergänzen Testabdeckung für die Wrapper. Die vorliegende Anforderung stellt sicher, dass die instrumentierten Komponenten ohne Laufzeitfehler nutzbar bleiben und konsistente Tracking-Daten liefern.

Wiederverwendbare UI-Hilfskomponenten reduzieren Code-Duplikation und stellen konsistente Benutzerinteraktionen über das gesamte Frontend sicher. Die `Searchbar` optimiert Performance durch Debouncing und verhindert unnötige Server-Anfragen bei schneller Eingabe. Die `SkeletonList` verbessert die wahrgenommene Performance, indem sie während Ladezeiten strukturierte Platzhalter anzeigt statt leerer Bereiche oder generischer Spinner.

## Hinweise

- `Searchbar` nutzt React-State und `setTimeout` für Debouncing; bei Verwendung in Listen mit vielen Elementen sollte Performance-Impact evaluiert werden.
- `SkeletonList` wird in mehreren Kontexten verwendet (z. B. HASKI-REQ-0087 für LearnerCharacteristics-Ladeanimationen, HASKI-REQ-0041 für Topic-Listen).
- Die Komponenten folgen dem Material-UI-Theming-System und passen sich automatisch an Hell/Dunkel-Modi an.
