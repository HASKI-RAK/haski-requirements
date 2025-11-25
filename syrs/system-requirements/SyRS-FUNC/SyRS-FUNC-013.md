---
id: SyRS-FUNC-013
title: Zentrale Verwaltung von Kurs-News
type: Functional
status: Proposed
stakeholder_priority: Medium
verification_method: Demonstration
links:
  parents: [StRS-135]
  children: ["HASKI-REQ-0046"]
---

## Beschreibung

Das System **shall** einen Backend-Service bereitstellen, der kurs- und hochschulbezogene News-Einträge mit den Feldern `university`, `language_id`, `created_at`, `expiration_date` und `news_content` speichert, validiert und über REST-Endpunkte (`POST /news`, `GET /news`) verfügbar macht. Eingehende News **shall** nur für berechtigte Rollen gespeichert werden und **shall** anhand von Universität sowie Sprache gefiltert bereitgestellt werden, damit Newsbanner-Komponenten im Frontend aktuelle Meldungen anzeigen können.
