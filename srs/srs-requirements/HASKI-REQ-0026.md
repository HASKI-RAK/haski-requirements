---
id: HASKI-REQ-0026
title: Erstellung und Konfiguration von Standard-Lernpfaden mit Scaffolding-Elementen
type: Functional
status: Implemented
source_id: SyRS-FUNC-008
links:
  stories: ["GH-353", "GH-84", "GH-306"]
  parents: ["SyRS-FUNC-008"]
---

## Beschreibung

Das System **shall** Lehrenden die Möglichkeit bieten, konfigurierbare Standard-Lernpfade mit Scaffolding-Elementen zu erstellen, zu bearbeiten und zu verwalten. Der Standard-Lernpfad dient als Grundlage für alle studentischen Lernpfade innerhalb eines Themas und kann mit verschiedenen Algorithmen (z.B. Graph, ACO) zur Personalisierung kombiniert werden.

## Akzeptanzkriterien

### Erstellung und Verwaltung von Standard-Lernpfaden
- [ ] Lehrende können einen Standard-Lernpfad für das HASKI-System erstellen
- [ ] Wenn kein Standard-Lernpfad gesetzt ist, wird der erste Kursersteller aufgefordert, einen zu erstellen
- [ ] Lehrende können einen bestehenden Standard-Lernpfad aktualisieren
- [ ] Die Aktualisierung eines Standard-Lernpfads löst eine Neuberechnung aller abhängigen studentischen Lernpfade aus

### Konfiguration von Scaffolding-Elementen
- [ ] Standardmäßig ist der Lernpfad in der von Lehrenden definierten Reihenfolge (prof-standard) organisiert
- [ ] Lehrende können für jedes Thema und Unter-Thema spezifische Algorithmen auswählen (z.B. Graph, ACO)
- [ ] Die gewählten Algorithmus-Einstellungen werden auf alle Lernpfade der Studierenden angewendet

### Technische Anforderungen
- [ ] Backend-Endpunkte für CRUD-Operationen auf Standard-Lernpfaden sind implementiert
- [ ] Datenbankstruktur unterstützt Speicherung von Standard-Lernpfaden und deren Konfiguration
- [ ] Rollenbasierte Zugriffskontrolle stellt sicher, dass nur autorisierte Lehrende Lernpfade konfigurieren können
- [ ] Frontend-Benutzeroberfläche ermöglicht intuitive Erstellung und Bearbeitung von Lernpfaden

## Rationale

Primary implementation: GitHub issue GH-353: "Teacher can create a Default Learning Path"

Related work:
- GH-84 (Backend): Implementiert Backend-Infrastruktur mit Datenbanktabellen und API-Endpunkten für Standard-Lernpfade
- GH-306 (Frontend): Ermöglicht Auswahl von Algorithmen für Themen, was die Scaffolding-Konfiguration unterstützt

Derived from system requirement SyRS-FUNC-008 and stakeholder requirement StRS-110.

Die Konfigurierbarkeit von Lernräumen mit Scaffolding-Elementen ermöglicht Lehrenden, Lernumgebungen flexibel an unterschiedliche Lernstände und didaktische Konzepte anzupassen. Der Standard-Lernpfad bildet dabei die Grundstruktur, die durch adaptive Algorithmen personalisiert werden kann.

## Hinweise

- Primary issue: [GH-353](https://github.com/HASKI-RAK/HASKI-Frontend/issues/353)
- Related issues: 
  - [GH-84](https://github.com/HASKI-RAK/HASKI-Backend/issues/84) - Backend implementation
  - [GH-306](https://github.com/HASKI-RAK/HASKI-Frontend/issues/306) - Algorithm selection UI
- Backend erfordert neue Datenbanktabellen für Speicherung von Standard-Lernpfaden
- API-Endpunkte müssen rollenbasierte Zugriffsrechte implementieren (nur Lehrende/Tutoren)
- Startup-Skripte müssen DB korrekt initialisieren
- Unit-Test-Abdeckung muss > 90% sein
