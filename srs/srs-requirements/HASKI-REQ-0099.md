---
id: HASKI-REQ-0099
title: Initialisierung der Anwendung und Benutzersitzung
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-001
links:
  parents: ["SyRS-FUNC-001"]
  tests:
    - path: "frontend/src/pages/App/App.test.tsx"
      name: "App tests"
---

## Beschreibung

Das System **shall** beim Start der Anwendung die Benutzersitzung initialisieren. Dies umfasst das Laden der Benutzerdaten vom Backend und die Initialisierung des xAPI-Trackings mit dem Benutzerkontext.

## Akzeptanzkriterien

- [x] Beim Start wird der aktuelle Benutzer vom Backend abgerufen (`fetchUser`).
- [x] Wenn der Benutzer erfolgreich geladen wurde, wird der xAPI-Service mit der User-ID initialisiert.
- [x] Wenn das Laden fehlschlägt, wird der Fehler behandelt (z.B. Logging, Fehleranzeige).
- [x] Die Anwendung stellt den Benutzerkontext global bereit.

## Rationale

Eine korrekte Initialisierung ist Voraussetzung für alle weiteren Funktionen, insbesondere für die Personalisierung und das Tracking.

## Hinweise

- Nutzt `useApp` Hook für die Logik.
