---
id: SyRS-FUNC-016
title: Lehrkraftbezogene Kurslisten bereitstellen
type: Functional
status: Proposed
stakeholder_priority: Medium
verification_method: Test
links:
  parents: [StRS-115]
  stories: ["HASKI-RAK/HASKI-Backend#21"]
  children: ["HASKI-REQ-0066"]
---

## Beschreibung

Das System **shall** eine Rollen-spezifische API bereitstellen, über die authentifizierte Lehrkräfte ausschließlich ihre eigenen Kurse abrufen können. Die Schnittstelle **shall** Moodle- und HASKI-IDs gegeneinander validieren, Kurszuordnungen mandantenfähig filtern und bei fehlender Autorisierung deterministisch mit Fehlercodes antworten. Dadurch erhalten Lehrkräfte eine konsistente Grundlage, um kollaborative Lernräume und Scaffolding-Elemente (StRS-115) zu konfigurieren, ohne Einsicht in fachfremde Kurse zu bekommen.
