---
id: SyRS-INT-005
title: Moodle-Kurslisten integrieren
type: Interface
status: Proposed
stakeholder_priority: High
verification_method: Test
links:
  parents: [StRS-121]
  stories: ["HASKI-RAK/HASKI-Backend#30"]
  children: ["HASKI-REQ-0035", "HASKI-REQ-0068", "HASKI-REQ-0071"]
---

## Beschreibung

Das System **shall** eine Integrationsschnittstelle bereitstellen, über die authentifizierte HASKI-Nutzer:innen ihre im Moodle-LMS geführten Kurse direkt aus HASKI heraus abrufen können. Die Schnittstelle **shall** die lokale User-ID mit der hinterlegten Moodle-ID abgleichen, die Moodle-Webservice-Aufrufe kapseln und die zurückgelieferte Kursliste unverändert (inkl. `id`, `shortname`, `fullname`, Start-/Enddatum und Zeitstempel) an die HASKI-Oberfläche weiterreichen. Fehlerhafte Moodle-Antworten oder ungültige Nutzer-IDs **shall** deterministisch behandelt werden, damit keine inkonsistenten Kurslisten angezeigt werden.
