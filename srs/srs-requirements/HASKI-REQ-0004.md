---
id: HASKI-REQ-0004
title: DSGVO-konforme Verarbeitung und Speicherung personenbezogener Daten
type: Compliance
status: Proposed
stakeholder_priority: High
verification_method: Review
source_id: SyRS-COMP-004
links:
  parents: [SyRS-COMP-004]
---

## Beschreibung

Das HASKI-System **shall** sämtliche personenbezogenen Daten DSGVO-konform erheben, verarbeiten und speichern. Das System **shall** die Grundsätze der Datenschutz-Grundverordnung (EU 2016/679) einhalten, insbesondere:

- Rechtmäßigkeit, Verarbeitung nach Treu und Glauben, Transparenz (Art. 5 Abs. 1 lit. a DSGVO)
- Zweckbindung (Art. 5 Abs. 1 lit. b DSGVO)
- Datenminimierung (Art. 5 Abs. 1 lit. c DSGVO)
- Richtigkeit (Art. 5 Abs. 1 lit. d DSGVO)
- Speicherbegrenzung (Art. 5 Abs. 1 lit. e DSGVO)
- Integrität und Vertraulichkeit (Art. 5 Abs. 1 lit. f DSGVO)

## Akzeptanzkriterien

- [ ] Einwilligung der Nutzer wird vor der Erhebung personenbezogener Daten eingeholt (Art. 6 DSGVO)
- [ ] Datenschutzerklärung ist transparent und vollständig (Art. 13, 14 DSGVO)
- [ ] Nutzer können Auskunft über gespeicherte Daten erhalten (Art. 15 DSGVO)
- [ ] Nutzer können Berichtigung falscher Daten verlangen (Art. 16 DSGVO)
- [ ] Nutzer können Löschung ihrer Daten verlangen ("Recht auf Vergessenwerden", Art. 17 DSGVO)
- [ ] Nutzer können Datenportabilität verlangen (Art. 20 DSGVO)
- [ ] Nutzer können der Datenverarbeitung widersprechen (Art. 21 DSGVO)
- [ ] Personenbezogene Daten werden verschlüsselt gespeichert
- [ ] Zugriff auf personenbezogene Daten ist durch Authentifizierung und Autorisierung geschützt
- [ ] Datenverarbeitungsvorgänge werden protokolliert (Audit-Log)
- [ ] Aufbewahrungsfristen werden eingehalten und Daten werden nach Ablauf gelöscht
- [ ] Technische und organisatorische Maßnahmen (TOMs) sind dokumentiert (Art. 32 DSGVO)
- [ ] Datenschutz-Folgenabschätzung (DSFA) wurde durchgeführt (Art. 35 DSGVO)
- [ ] Auftragsverarbeitungsverträge (AVV) mit Drittanbietern sind vorhanden (Art. 28 DSGVO)
- [ ] Meldeverfahren für Datenschutzverletzungen ist implementiert (Art. 33 DSGVO)
- [ ] Datenschutzbeauftragter wurde bestellt und ist im System dokumentiert (Art. 37-39 DSGVO)

## Rationale

Basierend auf Stakeholder-Anforderung StRS-118 ist die DSGVO-Konformität eine zwingende rechtliche Anforderung für den Betrieb des HASKI-Systems an EU-Hochschulen. Die Nichteinhaltung würde zu:
- Rechtlichen Risiken (Bußgelder bis zu 20 Mio. EUR oder 4% des Jahresumsatzes)
- Vertrauensverlust bei Studierenden und Hochschulleitungen
- Unmöglichkeit des rechtmäßigen Betriebs

Die DSGVO-Konformität ist daher eine fundamentale Compliance-Anforderung, die in allen Systemkomponenten berücksichtigt werden muss.

## Hinweise

- Diese Anforderung ist übergreifend und betrifft Frontend, Backend, Datenbank und alle Datenverarbeitungsprozesse
- Die Implementierung erfordert juristische Beratung durch Datenschutzbeauftragte
- Regelmäßige Audits sind erforderlich, um fortlaufende Compliance sicherzustellen
- Verwandte Anforderung: HASKI-REQ-0001 (Datenschutzerklärung-Einwilligung vor Login)

