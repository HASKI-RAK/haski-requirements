---
id: HASKI-REQ-0025
title: Lernfortschritts-Reports für Kurse und Themen generieren
type: Functional
status: Approved
source_id: SyRS-FUNC-007
links:
  parents: ["SyRS-FUNC-007"]
---

## Beschreibung

Das System **shall** Reports über Lernfortschritte, Schwierigkeiten und Kompetenzen der Studierenden generieren. Die Reports **shall** über Dashboard-Komponenten bereitgestellt werden und aussagekräftige Visualisierungen der Lernentwicklung ermöglichen.

Das System **shall** Lernfortschrittsdaten erfassen, analysieren und in aggregierter Form präsentieren, um Lehrenden und Studierenden Einblicke in den Lernprozess zu geben.

## Akzeptanzkriterien

### Dashboard-Reports
- [ ] Dashboard-Komponente zeigt Lernfortschritte der Studierenden an
- [ ] Reports visualisieren identifizierte Schwierigkeiten im Lernprozess
- [ ] Kompetenzentwicklung wird nachvollziehbar dargestellt
- [ ] Reports sind für Lehrende und Studierende zugänglich

### Datenerfassung und -analyse
- [ ] Lernfortschrittsdaten werden systematisch erfasst
- [ ] Schwierigkeiten werden anhand von Learning Analytics identifiziert
- [ ] Kompetenzentwicklung wird über Zeit getrackt
- [ ] Daten werden aggregiert und aussagekräftig aufbereitet

### Qualitätsanforderungen
- [ ] Reports sind verständlich und interpretierbar
- [ ] Visualisierungen sind benutzerfreundlich gestaltet
- [ ] Datenschutz und Datensicherheit sind gewährleistet
- [ ] Unit Test Coverage ist größer als 90%

## Rationale

Derived from system requirement SyRS-FUNC-007, which traces back to stakeholder requirement StRS-109. 

Lehrende benötigen aussagekräftige Reports über den Lernstand ihrer Studierenden, um gezielt unterstützen und den Lehrprozess optimieren zu können. Die Dashboard-basierte Implementierung ermöglicht eine flexible und erweiterbare Visualisierung von Lernfortschritten, Schwierigkeiten und Kompetenzentwicklung.

Diese Anforderung wird in zukünftigen Dashboard-Komponenten realisiert, die umfassende Learning Analytics integrieren und sowohl für Lehrende als auch für Studierende zugänglich machen.

## Hinweise

- Diese Anforderung ist für die zukünftige Implementierung vorgesehen
- Die Realisierung erfolgt über Dashboard-Komponenten
- Reports sollen umfassende Einblicke in Lernfortschritte, Schwierigkeiten und Kompetenzen bieten
- Die Implementierung muss Learning Analytics Daten aus verschiedenen Quellen integrieren
- Datenschutzaspekte müssen bei der Report-Generierung berücksichtigt werden
- Die Visualisierungen sollen sowohl für Lehrende als auch für Studierende nutzbar sein
