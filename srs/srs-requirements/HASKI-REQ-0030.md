---
id: HASKI-REQ-0030
title: System Availability During Lecture and Exam Periods
type: NFR:Performance
status: Approved
traceability: skip
source_id: SyRS-PERF-001
verification_method: Analysis
links:
  parents: ["SyRS-PERF-001"]
---

## Beschreibung

Das HASKI-System **shall** während Vorlesungs- und Prüfungszeiträumen eine Mindestverfügbarkeit von 99 % aufrechterhalten.

## Akzeptanzkriterien

- [x] Die Systemverfügbarkeit (Uptime) wird kontinuierlich überwacht und protokolliert.
- [x] Verfügbarkeitskennzahlen für Vorlesungszeiträume werden berechnet und berichtet.
- [x] Verfügbarkeitskennzahlen für Prüfungszeiträume werden berechnet und berichtet.
- [x] Das System erreicht in definierten Vorlesungszeiträumen eine Verfügbarkeit von mindestens 99 %.
- [x] Das System erreicht in definierten Prüfungszeiträumen eine Verfügbarkeit von mindestens 99 %.
- [x] Geplante Wartungsarbeiten werden außerhalb von Vorlesungs- und Prüfungszeiträumen angesetzt.
- [x] Es existieren Incident-Response-Prozesse, um Ausfallzeiten zu minimieren.
- [x] System-Health-Checks sind automatisiert und werden überwacht.
- [x] Alarmierungsmechanismen für Verfügbarkeitsprobleme sind konfiguriert.
- [x] Verfügbarkeitsberichte werden nach jedem Zeitraum erstellt und geprüft.

## Rationale

Abgeleitet aus der Systemanforderung SyRS-PERF-001 und der Stakeholder-Anforderung StRS-105.

Hohe Verfügbarkeit ist entscheidend für die Akzeptanz durch Studierende und die Kontinuität der Lernprozesse, insbesondere in Prüfungszeiträumen. Systemunterbrechungen würden Lernprozesse stören und das Vertrauen in die Plattform beeinträchtigen. Diese Anforderung stellt sicher, dass Infrastruktur, Deployment-Praktiken und Betriebsprozesse einen zuverlässigen Zugriff auf das HASKI-Lernsystem in den kritischsten akademischen Phasen unterstützen.

## Hinweise

- Dies ist eine systemweite nicht-funktionale Anforderung zur Sicherstellung der betrieblichen Zuverlässigkeit.
- Die Umsetzung umfasst Infrastrukturkonfiguration, Deployment-Praktiken, Monitoring und Incident Management.
- Vorlesungs- und Prüfungszeiträume sind auf Basis der akademischen Kalender der teilnehmenden Institutionen zu definieren.
- Die Verfügbarkeitsberechnung schließt geplante Wartungsfenster aus, sofern diese außerhalb kritischer Zeiträume liegen.
- Relevante Infrastrukturthemen sind u. a. Docker-Deployment, Health Checks, Load Balancing und Backups.
- Verifikation erfolgt über betriebliches Monitoring und Reporting in Pilot- und Produktivphasen.
