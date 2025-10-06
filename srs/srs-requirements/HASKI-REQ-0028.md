---
id: HASKI-REQ-0028
title: LTI-basierte Moodle-Integration mit Authentifizierung
type: Interface
status: Implemented
source_id: SyRS-INT-003
links:
  stories: ["GH-19", "GH-138", "GH-42", "GH-83", "GH-146"]
  parents: ["SyRS-INT-003"]
---

## Beschreibung

Das System **shall** über standardisierte LTI 1.3 Schnittstellen (Learning Tools Interoperability) eine nahtlose Integration mit Moodle ermöglichen. Die LTI-Verbindung **shall** für die Authentifizierung und Autorisierung von Nutzern verwendet werden und **shall** nur autorisierte Moodle-Plattformen akzeptieren.

Die LTI-Integration **shall** folgende Funktionalitäten bereitstellen:
- Authentifizierung von Nutzern über LTI-Launch aus Moodle
- Sicherer Datenaustausch über JWT-basierte Token
- Cookie-basiertes Session-Management für authentifizierte Nutzer
- Zugriffskontrolle auf API-Endpunkte basierend auf LTI-Authentifizierung
- Ablehnung von nicht autorisierten Nutzern und Plattformen

## Akzeptanzkriterien

### Funktionale Anforderungen

- [ ] Das System implementiert LTI 1.3 Verbindung für Authentifizierung in HASKI mittels pylti-Bibliothek
- [ ] Die LTI-Verbindung ist als API-Endpunkt implementiert
- [ ] LTI setzt Cookies korrekt für authentifizierte Sessions
- [ ] LTI akzeptiert nur die spezifizierte Moodle-Plattform (keine anderen Plattformen)
- [ ] LTI kann Nutzer ablehnen, die nicht berechtigt sind, HASKI zu betreten
- [ ] Ein Authentifizierungs-Decorator ist über API-Endpunkten implementiert
- [ ] Das System prüft Zugriffsberechtigung und implementiert 401 Unauthorized Fehler
- [ ] LTI-Konfiguration wird aus Environment-Datei geladen
- [ ] Frontend ist mit LTI verbunden und konfiguriert
- [ ] HASKI agiert als Plattform zur Integration von Moodle-Aktivitäten

### Qualitätsanforderungen

- [ ] Code entspricht Python-Standard (Linting bestanden)
- [ ] Alle Pytest-Tests bestehen
- [ ] Namensgebung ist aussagekräftig und konsistent
- [ ] Unit Test Coverage > 90%
- [ ] Dokumentation der LTI-Integration ist erstellt
- [ ] UML-Klassendiagramme und Komponentendiagramme sind aktualisiert

### Sicherheitsanforderungen

- [ ] Session Management ist sicher implementiert
- [ ] JWT-Token werden korrekt validiert
- [ ] Nur autorisierte Moodle-Instanzen werden akzeptiert
- [ ] API-Endpunkte sind durch LTI-Authentifizierung geschützt

## Rationale

Primary implementation: GitHub issue GH-19: "[Technical] Implement LTI Connection for Moodle"

Related work:
- GH-138 (Frontend): LTI connection and configuration on frontend side
- GH-42 (Backend): API access control implementation using LTI authentication
- GH-83 (Frontend): HASKI as platform to integrate Moodle activities, session management
- GH-146 (Frontend): LTI registration in webapp (open issue for future enhancements)

Derived from system requirement SyRS-INT-003 and stakeholder requirement StRS-121.

Die LTI-Integration ermöglicht die nahtlose Einbettung von HASKI in bestehende Moodle-Infrastrukturen und reduziert Implementierungshürden für Hochschulen.

## Hinweise

- Primary issue: [GH-19](https://github.com/HASKI-RAK/HASKI-Backend/issues/19) - Implementiert LTI 1.3 Verbindung mit pylti-Bibliothek
- Related issues:
  - [GH-138](https://github.com/HASKI-RAK/HASKI-Frontend/issues/138) - Frontend LTI Konfiguration
  - [GH-42](https://github.com/HASKI-RAK/HASKI-Backend/issues/42) - API Access Control mit LTI
  - [GH-83](https://github.com/HASKI-RAK/HASKI-Frontend/issues/83) - HASKI als Plattform
  - [GH-146](https://github.com/HASKI-RAK/HASKI-Frontend/issues/146) - LTI Registration (offen)
- Technische Bibliothek: [pylti1.3](https://github.com/dmitry-viskov/pylti1.3)
- Standard: IMS Global Learning Consortium – LTI 1.3 Standard
- LTI-Konfiguration erfolgt über .env-Datei (siehe GH-64)
- Authentifizierung erfolgt über Cookie-basiertes Session-Management
- API-Endpunkte verwenden Decorator-Pattern für Zugriffskontrolle
