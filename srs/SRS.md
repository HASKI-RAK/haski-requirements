# Software Requirements Specification (SRS)

für das HASKI-System (Frontend, Backend, NodeGrade) nach **ISO/IEC/IEEE 29148:2018** Abschnitt 9.6 „Software Requirements Specification“.

# IEEE Seite 56 - SRS Example Outline

## 1. Einleitung

1.1 Zweck
1.2 Geltungsbereich des Dokuments
1.3 Zielgruppe (Fördergeber, Entwickler, Lehrende, Studierende)
Ergänzung: Die vollständige Stakeholderliste und ihre Needs sind in der [StRS](../strs/StRS.md) dokumentiert. Diese SRS fasst die relevanten Stakeholdergruppen zusammen und leitet daraus Anforderungen ab.
1.4 Definitionen

## 2. Gesamtbeschreibung

2.1 Produktperspektive (Einbettung in HASKI-Gesamtkonzept: Lernraum, LMS, HASKI-System)
2.2 Produktfunktionen (adaptives Lernen, KI-gestützte Bewertung, Feedback, Reporting)
2.3 Benutzerklassen und -merkmale (Studierende, Lehrende, Administratoren)
> Hinweis: Details siehe [StRS](../strs/StRS.md).
### 2.4 Betriebsumgebung
Die Betriebsumgebung spiegelt das Umfeld wider, in dem das HASKI-System technisch entwickelt und eingesetzt wird.
**Hardware-Umgebung:**
- **Entwicklung**: 
KI-Rechner mit GPU-Unterstützung für maschinelles Lernen, Datenverarbeitung und Bereitstellen der entwickelten Software für Entwickler-Teams an allen drei Standorte
  - **CPU**: Intel(R) Xeon(R) W-3335 @ 3.40GHz (16 Cores, 32 Threads, max. 4.0 GHz)
  - **RAM**: 128 GB DDR4 System-Arbeitsspeicher
  - **GPU**: 4 x NVIDIA RTX A6000 (je 48 GB VRAM, 300W TDP)
  - **Speicher**: 1,8 TB SSD-System-Storage
  - **CUDA**: Version 12.2 für GPU-Computing
- **Produktiv**: Server-Infrastruktur an Partnerhochschulen
- **Spezialausstattung**: Eye-Tracking-Labor (OTH Regensburg)

**Software-Umgebung:**
- **LMS**: 
Moodle Instanz gesondert von der produktiven Hochschulumgebung
- **KI-Tools**: HUGIN Researcher für Bayessche Netzwerke.
- **Video-Produktion**: Vyond Premium für Animationsvideos.
- **LaS3**: Cloud-Datenspeicher für Projektaustausch.
- **LRZ**: Cloud-Datenserver für Projektaustausch.
- **GitHub**: Versionsverwaltung und Quellcode-Repository für sowohl Dokumentation, als auch Software und wissenschaftliche Veröffentlichungen.

**Netzwerk-Umgebung:**
- Hochschulinterne Netzwerke für abgekapselte Services ohne direkten Zugriff vom Internet aus.
- Hochschul-Intranet mit Internetanbindung
- HTTPS/TLS-verschlüsselte Kommunikation

### 2.5 Design- und Implementierungsrestriktionen
**2.5.1 Rechtliche Vorgaben**
- **DSGVO-Compliance**: Vollständige Einhaltung der Datenschutz-Grundverordnung.
- **Hochschul-Datenschutz**: Spezifische Richtlinien der Partnerhochschulen.
- **Anonymisierung/Pseudonymisierung**: Schutz personenbezogener Lerndaten.

**2.5.2 Technische Standards**
- **Open Science**: Open Education Resources (OER) und Open Methodology. Veröffentlichung auf GitHub und Youtube.
- **Interoperabilität**: LTI-Standard für LMS-Integration.
- **Web-Standards**: Gängige Protokollelemente und Formate (HTTP, REST, JSON, OAuth 2.0).
- **ISO-IEEE Standards**: Weitere Informationen in Kapitel "Referenzdokumente".

**2.5.3 Projektspezifische Vorgaben**
- **Iterative Entwicklung**: 4 Entwicklungsiterationen über Projektlaufzeit.
- **Multi-Site Deployment**: Einsatz an drei Partnerhochschulen.
- **Hochschuldidaktische Qualität**: Wissenschaftlich fundierte pädagogische Konzepte.

### 2.6 Annahmen und Abhängigkeiten
**2.6.1 Technische Annahmen**
- Verfügbarkeit stabiler Moodle-Instanzen an allen Standorten.
Die Instanzen werden von jedem Projektpartner eigenständig betrieben und gepflegt.
- Ausreichende Server-Kapazitäten für Betrieb und Entwicklung.
Abgesehen vom KI-Server, bietet jede Hochschule eigene Server-Ressourcen für Hosting und Entwicklung.
- Zuverlässige Internetverbindung für Cloud-Services
Abhängig von Hochschulnetzwerken und IT-Betreuer.

**2.6.2 Fachliche Annahmen**
- Fokus auf Informatik-Domänen (Software Engineering, Programmierung, UML).
- Bereitschaft der Lehrenden zur Adoption neuer Technologien.
- Akzeptanz KI-gestützter Bewertung durch Studierende.

**2.6.3 Projektabhängigkeiten**
- **KI-Methoden**: Bayessche Netzwerke, Deep Learning, NLP.
- **Externe Tools**: HUGIN Researcher, Vyond.
- **Infrastruktur**: Hochschul-IT, Eye-Tracking-Labor.
- **Personal**: Wissenschaftliche Mitarbeiter (pädagogisch/technisch), Projektleiter.
- **Evaluationspartner**: Studierende und Lehrende.

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

## 4. Verifikation und Validierung

### 4.1 Verifikation (Zuordnung Tests ↔ Anforderungen)
**Unit Tests:**
- **KI-Modelle**: Automatisierte Tests für Lerntyp-Klassifikation, Feedback-Generierung
- **API-Schnittstellen**: Vollständige Abdeckung aller REST-Endpoints
- **Datenverarbeitung**: Validierung von Lernpfad-Algorithmen und Bewertungslogik

**Integration Tests:**
- **Moodle-Integration**: End-to-End Tests der LTI-Anbindung
- **NodeGrade-Integration**: Code-Bewertungs-Pipeline von Submission bis Feedback
- **Frontend-Backend**: Vollständige Benutzerinteraktions-Szenarien

**System Tests:**
- **Performance**: Load-Testing mit realistischen Nutzerszenarien
- **Security**: Penetration Testing und Vulnerability Assessment
- **Usability**: Automatisierte UI-Tests für kritische User Journeys

**Requirements Traceability Matrix (RTM):**
- **Bidirektionale Verfolgung**: Jede Anforderung → Tests, jeder Test → Anforderungen
- **Coverage Report**: Automatisierte Berichterstellung über Test-Abdeckung
- **Change Impact Analysis**: Auswirkungsanalyse bei Anforderungsänderungen

### 4.2 Validierung (Feldtests an Hochschulen, Eye-Tracking, Evaluation)
**Feldtests:**
- **Pilotveranstaltungen**: Software Engineering Module an allen drei Standorten
- **Iterative Erprobung**: 4 Evaluationszyklen über Projektlaufzeit
- **Zielgruppen**: Studierende der Informatik, Game Engineering, Mechatronik

**Eye-Tracking-Studien (OTH Regensburg):**
- **UX-Optimierung**: Analyse von Blickbewegungsmustern bei Interface-Nutzung
- **Lernverhalten**: Identifikation optimaler Lernpfad-Präsentationen
- **KI-Feedback Wirksamkeit**: Validierung der Feedback-Qualität durch physiologische Messungen

**Qualitative Evaluation:**
- **Grounded Theory**: Systematische Analyse von Nutzerinterviews und -beobachtungen
- **Focus Groups**: Regelmäßige Feedback-Sessions mit Studierenden und Lehrenden
- **Expert Reviews**: Begutachtung durch externe Hochschuldidaktik-Experten

**Quantitative Evaluation:**
- **Lernfortschritt-Messung**: Vergleich zu traditionellen Lehrmethoden
- **Nutzungsstatistiken**: Engagement-Metriken, Abschlussraten, Zufriedenheit
- **KI-Performance**: Accuracy, Precision, Recall für verschiedene Aufgabentypen

### 4.3 Akzeptanzkriterien
**Funktionale Akzeptanz:**
- **Lernpfad-Anpassung**: 80% der Studierenden empfinden Anpassungen als hilfreich
- **Feedback-Qualität**: Durchschnittliche Bewertung ≥ 4.0/5.0 auf Likert-Skala
- **System-Performance**: 95% der Anfragen binnen definierter Antwortzeiten

**Didaktische Akzeptanz:**
- **Lehrenden-Zufriedenheit**: ≥ 75% würden System weiterempfehlen
- **Lerneffektivität**: Messbare Verbesserung der Lernergebnisse vs. Kontrollgruppe
- **Arbeitsersparnis**: ≥ 30% Zeitersparnis bei Bewertungsaufgaben für Lehrende

**Technische Akzeptanz:**
- **Systemstabilität**: < 1% ungeplante Ausfallzeiten während Evaluationsphase
- **Integration**: Nahtlose Einbindung in bestehende Hochschul-IT ohne Disruption
- **Skalierbarkeit**: Erfolgreicher Einsatz mit mindestens 300 Studierenden parallel

## 5. Anhang

### 5.1 Annahmen und Abhängigkeiten

#### 5.1.1 Technische Abhängigkeiten
**Externe Software:**
- **HUGIN Researcher**: Verfügbarkeit und Kompatibilität für Bayessche Netzwerke
- **NodeGrade**: Stabile API für Code-Bewertungsfunktionalität
- **Vyond Premium**: Lizenz-Verfügbarkeit für Video-Produktionsprozess
- **Moodle LMS**: Mindestversion 4.1 mit LTI 1.3 Support an allen Standorten

**Infrastructure-as-a-Service:**
- **Cloud-Provider**: Zuverlässige Services für KI-Compute-Intensive Workloads
- **Hochschul-IT**: Ausreichende Netzwerkbandbreite und Server-Kapazitäten
- **Backup-Services**: Georedundante Datensicherung für Compliance

#### 5.1.2 Organisatorische Abhängigkeiten
**Personal:**
- **Wissenschaftliche Mitarbeiter**: Pädagogische und technische Expertise verfügbar
- **Studentische Hilfskräfte**: Unterstützung bei Content-Erstellung und Testing
- **Projektkoordination**: Effektive Zusammenarbeit zwischen den drei Standorten

**Evaluationspartner:**
- **Studierende**: Bereitschaft zur Teilnahme an Feldtests und Evaluationen
- **Lehrende**: Adoption neuer Technologien und Feedback-Bereitschaft
- **Hochschulleitungen**: Strategische Unterstützung und Ressourcen-Bereitstellung

#### 5.1.3 Rechtliche und Compliance Annahmen
**Datenschutz:**
- **DSGVO**: Keine wesentlichen Änderungen der Datenschutz-Gesetzgebung
- **Hochschul-Richtlinien**: Genehmigung für KI-basierte Lernanalyse
- **Einverständniserklärungen**: Studierenden-Zustimmung zu anonymisierter Datennutzung

**Förderbestimmungen:**
- **BMBF-Richtlinien**: Kontinuierliche Projektförderung gemäß Bewilligungsbescheid
- **Open Science**: Einhaltung der Open Education Resources Verpflichtungen

### 5.2 Glossar
**Adaptives Lernen**: Automatische Anpassung von Lerninhalten und -pfaden basierend auf individuellem Lernverhalten und -fortschritt

**Bayessche Netzwerke**: Probabilistische graphische Modelle zur Repräsentation unsicheren Wissens und zur Inferenz unter Unsicherheit

**Blended Learning**: Didaktisches Konzept, das Präsenzlehre mit digitalen Lernformaten kombiniert

**Domänen-Modell**: Strukturierte Repräsentation fachspezifischen Wissens einschließlich Konzepte, Relationen und Lernmaterialien

**Eye-Tracking**: Technologie zur Messung und Analyse von Blickbewegungen für UX-Research und Lernverhalten-Studien

**Grounded Theory**: Qualitative Forschungsmethodik zur systematischen Theorie-Entwicklung aus empirischen Daten

**Learning Tools Interoperability (LTI)**: IMS Global Standard für die Integration externer Lerntools in Learning Management Systeme

**Micro-Learning**: Pädagogischer Ansatz mit kurzen, fokussierten Lerneinheiten (≤ 15 Minuten)

**NodeGrade**: Spezialisierte Software zur automatisierten Bewertung von JavaScript/Node.js Programmcode

**Scaffolding**: Pädagogische Methode der schrittweisen Lernunterstützung mit gradueller Reduktion der Hilfestellungen

**Tutorielles Modell**: KI-Komponente zur Steuerung von Lernpfaden, Feedback-Generierung und Adaptionsentscheidungen

### 5.3 Referenzdokumente
**Projektdokumente:**
- Projektbeschreibung HASKI (Version 1.0, 2022)
- Teilvorhabenbeschreibung HASKI-KE (Version 1.0, 2022)
- Arbeitsprogramm und Zeitplan (governance/Project-Plan.md)
- Requirements Management Plan (governance/Requirements-Management-Plan.md)

**Standards und Normen:**
- ISO/IEC/IEEE 29148:2018 - Systems and software engineering — Life cycle processes — Requirements engineering
- ISO/IEC 25010:2011 - Systems and software Quality Requirements and Evaluation (SQuaRE)
- IEEE 830-1998 - IEEE Recommended Practice for Software Requirements Specifications
- IMS Learning Tools Interoperability v1.3 Implementation Guide

**Wissenschaftliche Grundlagen:**
- Feldhoff, A. et al. (2019): So will ich lernen! Nutzeranforderungen an die Qualifizierung für Arbeit 4.0
- Franken, R.; Franken S. (2020): Wissen, Lernen und Innovation im digitalen Unternehmen
- Konrad, K.; Traub, S. (2018): Selbstgesteuertes Lernen - Grundlagen und Tipps

**Datenschutz und Rechtliches:**
- Datenschutz-Grundverordnung (DSGVO) EU 2016/679
- Hochschul-spezifische Datenschutzrichtlinien der Partnerhochschulen
- BMBF Richtlinie zur Bund-Länder-Initiative zur Förderung der KI in der Hochschulbildung

### 5.4 Stakeholder-Übersicht (Top-10)
> **Vollständige Liste**: Siehe [Stakeholder Requirements Specification (StRS)](../strs/StRS.md)

| Priorität | Stakeholder | Hauptinteressen | Einfluss |
|-----------|-------------|-----------------|----------|
| 1 | Studierende | Adaptives Lernen, Feedback | Hoch |
| 2 | Lehrende | Bewertungsunterstützung, Reports | Hoch |
| 3 | OTH Regensburg | Projektleitung, KI-Expertise | Hoch |
| 4 | TH Aschaffenburg | Bayessche Netzwerke, HUGIN | Hoch |
| 5 | HS Kempten | Content-Produktion, Videos | Hoch |
| 6 | BMBF | Projekterfolg, Compliance | Hoch |
| 7 | Datenschutzbeauftragte | DSGVO-Compliance | Hoch |
| 8 | IT-Administration | Integration, Performance | Mittel |
| 9 | Hochschulleitungen | Lehrqualität, ROI | Mittel |
| 10 | Wissenschaftliche Mitarbeiter | Entwicklung, Evaluation | Hoch |

### 5.5 Abkürzungen und Akronyme
- **AI/KI**: Artificial Intelligence / Künstliche Intelligenz
- **API**: Application Programming Interface
- **BMBF**: Bundesministerium für Bildung und Forschung
- **CI/CD**: Continuous Integration / Continuous Deployment
- **CNN**: Convolutional Neural Network
- **DSGVO**: Datenschutz-Grundverordnung
- **GPU**: Graphics Processing Unit
- **HASKI**: Hochschullehre: Adaptiv, selbstgesteuert, KI-gestützt
- **HKE**: Hochschule Kempten
- **LMS**: Learning Management System
- **LTI**: Learning Tools Interoperability
- **ML**: Machine Learning
- **NLP**: Natural Language Processing
- **OER**: Open Educational Resources
- **OTH R**: Ostbayerische Technische Hochschule Regensburg
- **QTI**: Question & Test Interoperability
- **REST**: Representational State Transfer
- **RNN**: Recurrent Neural Network
- **RTM**: Requirements Traceability Matrix
- **SCORM**: Shareable Content Object Reference Model
- **SRS**: Software Requirements Specification
- **StRS**: Stakeholder Requirements Specification
- **THAB**: Technische Hochschule Aschaffenburg
- **UML**: Unified Modeling Language
- **UX**: User Experience
- **WCAG**: Web Content Accessibility Guidelines