# Software Requirements Specification (SRS)

für das HASKI-System (Frontend, Backend, NodeGrade) nach **ISO/IEC/IEEE 29148:2018** Abschnitt 9.6 „Software Requirements Specification“.

# IEEE Seite 56 - SRS Example Outline

## 1. Einleitung

1.1 Zweck
1.2 Geltungsbereich des Dokuments
1.3 Zielgruppe (Fördergeber, Entwickler, Lehrende, Studierende)
Ergänzung: Die vollständige Stakeholderliste und ihre Needs sind in der [StRS](StRS.md) dokumentiert. Diese SRS fasst die relevanten Stakeholdergruppen zusammen und leitet daraus Anforderungen ab.
1.4 Definitionen

## 2. Gesamtbeschreibung

2.1 Produktperspektive (Einbettung in HASKI-Gesamtkonzept: Lernraum, LMS, HASKI-System)
2.2 Produktfunktionen (adaptives Lernen, KI-gestützte Bewertung, Feedback, Reporting)
2.3 Benutzerklassen und -merkmale (Studierende, Lehrende, Administratoren)
> Hinweis: Details siehe [StRS](StRS.md).
2.4 Betriebsumgebung (LMS Moodle, Frontend-Web, Backend-Services, NodeGrade-Tool)
2.5 Design- und Implementierungsrestriktionen (z. B. DSGVO, Open-Source-Strategie, Interoperabilität mit Moodle)
2.6 Annahmen und Abhängigkeiten (Bayessche Netzwerke, ML-Modelle, Infrastruktur an Hochschulen)

## 3. Anforderungen
### 3.1 Systemfunktionen
> Note: SSOT: Folder `requirements` contains individual requirement files (e.g., HASKI-REQ-0001.md).
* 4.1 Modellverwaltung (Lernenden-, Tutorien-, Domänen-Modell)
* 4.2 KI-gestützte Aufgabenbewertung (Freitext, Code, Diagramme, Quizzes)
* 4.3 Feedbackgenerierung für Studierende
* 4.4 Reporting für Lehrende
* 4.5 Adaptives Lernpfad-Management
* 4.6 Moodle-Integration (Synchronisation von Inhalten und Pfaden)

Jede Funktion sollte beschrieben werden mit:

* Beschreibung
* Eingaben
* Verarbeitung
* Ausgaben
* Anforderungen (z. B. Performance, Genauigkeit)

### 3.2 Performance (Antwortzeit Feedback ≤ 2 s, Skalierung für große Gruppen)

### 3.3 Usability (Micro-Learning, barrierefrei, studierendenzentriert)

### 3.4 Externe Schnittstellenanforderungen

3.1 Benutzeroberflächen (Frontend Web-UI, Dozierenden-Reports)
3.2 Hardware-Schnittstellen (Server, Eye-Tracking-Labor bei OTH R)
3.3 Software-Schnittstellen (Moodle-API, NodeGrade-Integration, KI-Modelle)
3.4 Kommunikationsschnittstellen (REST APIs, Authentifizierung, Protokolle)

### 3.5 Logische Datenbankanforderungen (Lernpfade, Aufgaben, Feedback, User-Modelle)

3.5.1 Datensicherung und -archivierung
3.5.2 Datenschutzanforderungen

### 3.6 Designbeschränkungen

3.6.1 Standards-Compliance (ISO, IEEE, OER, Open Science)
3.6.2 Entwicklungsumgebung (z. B. Python, Node.js, React, Moodle-Plugins)
3.6.3 Vorgaben aus Arbeitsprogramm (Iterationen, Meilensteine)

### 3.7 Software system Attribute

3.7.1 Sicherheit & Datenschutz (DSGVO, Pseudonymisierung, Anonymisierung)
3.7.2 Zuverlässigkeit & Verfügbarkeit
3.7.3 Wartbarkeit & Erweiterbarkeit
3.7.4 Portabilität (Deployment an Partnerhochschulen, Cloud/On-Premise)

### 3.8 Zusätzliche Informationen

## 4. Verifikation

4.1 Verifikation (Zuordnung Tests ↔ Anforderungen)
4.2 Validierung (Feldtests an Hochschulen, Eye-Tracking, Evaluation)
4.3 Akzeptanzkriterien

## 5. Anhang

### 5.1 Annahmen und Abhängigkeiten

* Glossar
* Referenzdokumente (Projektbeschreibung, Arbeitsprogramm, Teilvorhabenbeschreibung, Normen)
* Anhang A (optional): Stakeholderliste (Kurzfassung)
  - Tabellen-Auszug (Top-10 Stakeholder) mit Verweis auf [StRS](StRS.md) für die vollständige Liste.

### 5.2 Acronyme und Abkürzungen
* Abkürzungen