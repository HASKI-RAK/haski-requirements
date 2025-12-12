---
id: HASKI-REQ-0005
title: Transparente Dokumentation der Datenverwendung und Einwilligungsprozesse
type: Compliance
status: Proposed
stakeholder_priority: High
verification_method: Review
source_id: SyRS-COMP-005
links:
  stories: ["HASKI-RAK/HASKI-Frontend#128", "HASKI-RAK/HASKI-Frontend#195"]
  parents: ["SyRS-COMP-005"]
  tests:
    - path: "frontend/src/pages/Imprint/Imprint.test.tsx"
      name: "Imprint Component"
    - path: "frontend/src/pages/PrivacyPolicy/PrivacyPolicy.test.tsx"
      name: "Test the PrivacyPolicy page"
---

## Beschreibung

Das HASKI-System **shall** eine transparente, verständliche und leicht zugängliche Dokumentation der Datenverwendung bereitstellen. Das System **shall** die Einwilligungsprozesse für Studierende nachvollziehbar gestalten und jederzeit Zugriff auf Informationen über die Verarbeitung personenbezogener Daten ermöglichen.

Das System **shall** folgende Informationen transparent dokumentieren und den Nutzern zugänglich machen:

- Welche personenbezogenen Daten erhoben werden
- Zu welchen Zwecken die Daten verarbeitet werden
- Wie lange die Daten gespeichert werden
- Mit wem die Daten geteilt werden (falls zutreffend)
- Welche Rechte die Nutzer bezüglich ihrer Daten haben
- Wie Nutzer ihre Rechte ausüben können (Auskunft, Berichtigung, Löschung, etc.)

## Akzeptanzkriterien

- [x] Eine vollständige und verständliche Datenschutzerklärung ist im System verfügbar (DSGVO Art. 13, 14)
- [x] Die Datenschutzerklärung ist in klarer, einfacher Sprache verfasst (DSGVO Art. 12 Abs. 1)
- [x] Die Datenschutzerklärung ist jederzeit über das Hauptmenü/Footer zugänglich
- [x] Nutzer können ihre erteilten Einwilligungen einsehen
- [x] Nutzer können einzelne Einwilligungen widerrufen
- [x] Nutzungsbedingungen (Terms of Service) sind klar dokumentiert
- [x] Eine Übersicht der verarbeiteten Datenkategorien ist verfügbar
- [x] Kontaktinformationen des Datenschutzbeauftragten sind angegeben (DSGVO Art. 13 Abs. 1 lit. b)
- [x] Informationen über Aufbewahrungsfristen sind dokumentiert (DSGVO Art. 13 Abs. 2 lit. a)
- [x] Belehrung über Widerrufsrecht ist klar formuliert (DSGVO Art. 7 Abs. 3)
- [x] Informationen sind auch für nicht eingeloggte Nutzer zugänglich
- [x] Änderungen an der Datenschutzerklärung werden versioniert und dokumentiert
- [x] Nutzer werden über wesentliche Änderungen informiert

## Rationale

Basierend auf Stakeholder-Anforderung StRS-119 ist die transparente Dokumentation der Datenverwendung eine Kernforderung der DSGVO (Art. 7, 12-15) und Grundlage für das Vertrauen der Studierenden in das HASKI-System.

Während HASKI-REQ-0001 den Einwilligungsprozess vor dem Login implementiert, adressiert diese Anforderung die fortlaufende Transparenz und Nachvollziehbarkeit der Datenverarbeitung während der gesamten Nutzung des Systems.

Related work:

- GH-128: Unterstützt die transparente Dokumentation der Datenverwendung
- GH-195: Bereits in HASKI-REQ-0001 verlinkt - Implementiert die initiale Einwilligung, aber nicht die fortlaufende transparente Dokumentation

## Hinweise

- Diese Anforderung ergänzt HASKI-REQ-0001 (initiale Einwilligung) um die fortlaufende Transparenz
- Diese Anforderung ist übergreifend mit HASKI-REQ-0004 (DSGVO-Konformität), da beide GDPR-Compliance sicherstellen
- Die Dokumentation muss regelmäßig geprüft und aktualisiert werden
- Juristische Beratung durch Datenschutzbeauftragte ist erforderlich
- DSGVO-Referenzen: Art. 7 (Einwilligung), Art. 12 (Transparenz), Art. 13-14 (Informationspflichten), Art. 15 (Auskunftsrecht)
