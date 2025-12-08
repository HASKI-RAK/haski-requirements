---
id: HASKI-REQ-0003
title: Open-Source-Lizenzierung von Quellcode und Lehrmaterialien
type: Compliance
status: Proposed
stakeholder_priority: High
verification_method: Review
source_id: SyRS-COMP-003
links:
  stories: []
  parents: ["SyRS-COMP-003"]
---

## Beschreibung

Das HASKI-System **shall** den gesamten Quellcode und alle erstellten Lehrmaterialien unter einer Open-Source-Lizenz verfügbar machen. Die Lizenz **shall** es Hochschulen ermöglichen, die Software und Materialien frei zu nutzen, zu modifizieren und weiterzuverbreiten.

## Akzeptanzkriterien

- [x] Alle Quellcode-Repositories (Frontend, Backend) sind unter einer anerkannten Open-Source-Lizenz veröffentlicht
- [x] Die LICENSE-Datei ist in jedem Repository vorhanden und korrekt
- [x] Alle Lehrmaterialien sind mit einer geeigneten Creative-Commons-Lizenz versehen
- [x] Die package.json/setup.py Dateien enthalten korrekte Lizenzangaben
- [x] Alle Abhängigkeiten sind kompatibel mit der gewählten Open-Source-Lizenz (keine Lizenzkonflikte)
- [x] Die Repositories sind als öffentlich (public) konfiguriert
- [x] Die README-Dateien enthalten klare Lizenzhinweise und Nutzungsbedingungen
- [x] Drittanbieter-Code und Bibliotheken sind korrekt attributiert

## Rationale

Basierend auf Stakeholder-Anforderung StRS-117 muss das HASKI-System als Open-Source-Software verfügbar sein, um:

- Langfristige Nachhaltigkeit und Weiterentwicklung zu gewährleisten
- Institutionelle Nutzung durch Hochschulen zu ermöglichen
- Transparenz und Vertrauen in das KI-gestützte Lernsystem zu schaffen
- Die Förderrichtlinien der Bund-Länder-Initiative zur KI in der Hochschulbildung zu erfüllen
- Eine größere Wirkung im Hochschulbereich durch breite Verfügbarkeit zu erzielen

Die Open-Source-Lizenzierung ist eine zentrale Compliance-Anforderung des Projekts und essentiell für die institutionelle Akzeptanz.
