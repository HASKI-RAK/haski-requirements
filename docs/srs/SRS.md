# Software Requirements Specification (SRS)

<!-- Generated copy from srs/SRS.md -->

# Software Requirements Specification (SRS)

für das HASKI-System (Frontend, Backend, NodeGrade) nach **ISO/IEC/IEEE 29148:2018** Abschnitt 9.6 „Software Requirements Specification“.

## 1. Einleitung

1.1 Zweck
1.2 Geltungsbereich des Dokuments
1.3 Zielgruppe (Fördergeber, Entwickler, Lehrende, Studierende)
1.4 Referenzen (Projektbeschreibung, Teilvorhaben, Arbeitsprogramm, Normen)
1.5 Definitionen, Abkürzungen, Glossar

## 2. Gesamtbeschreibung

2.1 Produktperspektive (Einbettung in HASKI-Gesamtkonzept: Lernraum, LMS, HASKI-System)
2.2 Produktfunktionen (adaptives Lernen, KI-gestützte Bewertung, Feedback, Reporting)
2.3 Benutzerklassen und -merkmale (Studierende, Lehrende, Administratoren)
2.4 Betriebsumgebung (LMS Moodle, Frontend-Web, Backend-Services, NodeGrade-Tool)
2.5 Design- und Implementierungsrestriktionen (z. B. DSGVO, Open-Source-Strategie, Interoperabilität mit Moodle)
2.6 Annahmen und Abhängigkeiten (Bayessche Netzwerke, ML-Modelle, Infrastruktur an Hochschulen)

## 3. Externe Schnittstellenanforderungen

3.1 Benutzeroberflächen (Frontend Web-UI, Dozierenden-Reports)
3.2 Hardware-Schnittstellen (Server, Eye-Tracking-Labor bei OTH R)
3.3 Software-Schnittstellen (Moodle-API, NodeGrade-Integration, KI-Modelle)
3.4 Kommunikationsschnittstellen (REST APIs, Authentifizierung, Protokolle)

## 4. Systemfunktionen

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

## 5. Nicht-funktionale Anforderungen

5.1 Usability (Micro-Learning, barrierefrei, studierendenzentriert)
5.2 Performance (Antwortzeit Feedback ≤ 2 s, Skalierung für große Gruppen)
5.3 Sicherheit & Datenschutz (DSGVO, Pseudonymisierung, Anonymisierung)
5.4 Zuverlässigkeit & Verfügbarkeit
5.5 Wartbarkeit & Erweiterbarkeit
5.6 Portabilität (Deployment an Partnerhochschulen, Cloud/On-Premise)

## 6. Datenanforderungen

6.1 Logische Datenbankanforderungen (Lernpfade, Aufgaben, Feedback, User-Modelle)
6.2 Datensicherung und -archivierung
6.3 Datenschutzanforderungen

## 7. Designbeschränkungen

7.1 Standards-Compliance (ISO, IEEE, OER, Open Science)
7.2 Entwicklungsumgebung (z. B. Python, Node.js, React, Moodle-Plugins)
7.3 Vorgaben aus Arbeitsprogramm (Iterationen, Meilensteine)

## 8. Qualitätsanforderungen

8.1 Verifikation (Zuordnung Tests ↔ Anforderungen)
8.2 Validierung (Feldtests an Hochschulen, Eye-Tracking, Evaluation)
8.3 Akzeptanzkriterien

## 9. Anhang

* Glossar
* Abkürzungen
* Referenzdokumente (Projektbeschreibung, Arbeitsprogramm, Teilvorhabenbeschreibung, Normen)