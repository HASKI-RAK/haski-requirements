---
id: SyRS-FUNC-015
title: Administrations-API für Nutzerverzeichnis
type: Functional
status: Proposed
stakeholder_priority: Medium
verification_method: Test
links:
  parents: [StRS-137]
  children: ["HASKI-REQ-0064"]
---

## Beschreibung

Das System **shall** einen abgesicherten Backend-Endpunkt bereitstellen, über den verifizierte Administrator:innen das vollständige HASKI-Nutzerverzeichnis mandantenfähig abrufen können. Die API **shall** Moodle-identifizierte Admin-Nutzer gegen die HASKI-User-ID verifizieren, ausschließlich autorisierten Rollen Zugriff gewähren und pro Eintrag konsistente Stammdaten (z. B. Name, Rolle, Hochschule, Betriebsstatus) liefern. Fehlerhafte oder nicht autorisierte Aufrufe **shall** deterministisch mit aussagekräftigen Fehlercodes beantwortet werden, sodass Betriebsteams Audits und Supportfälle ohne Datenexporte durchführen können.
