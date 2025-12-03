---
id: HASKI-REQ-0044
title: Kontaktformular für studierende Supportmeldungen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
links:
  parents:
    - "SyRS-FUNC-011"
  stories:
    - "HASKI-RAK/HASKI-Backend#39"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_contact_form"
    - path: "frontend/src/components/ContactForm/ContactForm.test.tsx"
      name: "Test ContactForm"
    - path: "frontend/src/pages/Contact/Contact.test.tsx"
      name: "Test Contactpage"
    - path: "HASKI-Frontend/src/services/contact/postContactForm.test.tsx"
      name: "postContactForm"
---

## Beschreibung

Das Backend **shall** einen authentifizierten REST-Endpunkt `POST /user/<user_id>/<lms_user_id>/contactform` bereitstellen, über den Studierende strukturierte Support- bzw. Fehlerberichte direkt aus der Lernumgebung absenden können. Die Meldung **shall** mindestens Topic/Kategorie (`report_topic`), Typ (`report_type`) und eine Beschreibung (`report_description`) enthalten, wird mit der internen Nutzer-ID verknüpft und mit einem Zeitstempel persistiert, damit das Betriebsteam die Anfrage nachvollziehen und beantworten kann.

## Akzeptanzkriterien

- [ ] Fehlende Pflichtfelder (`report_topic`, `report_type`, `report_description`) führen zu einer 400-Fehlermeldung mit Hinweis
- [ ] Die übermittelte Meldung wird mit der verknüpften Nutzer-ID gespeichert und als JSON mit den gespeicherten Feldern (`id`, `user_id`, `report_topic`, `report_type`, `report_description`, `date`) zurückgegeben
- [ ] Nur bekannte Nutzer:innen (verifizierbar über `user_id`/`lms_user_id`) dürfen Meldungen absenden; unbekannte IDs führen zu einer `MissingUser`-Fehlermeldung
- [ ] Erfolgreiche Meldungen liefern HTTP-Status `201 Created`
- [ ] Persistierte Meldungen können vom Support über die Datenbank oder Administrationsprozesse ausgelesen und weiterverarbeitet werden

## Rationale

Ein integrierter Kontaktkanal stellt sicher, dass Studierende Probleme ohne Medienbruch melden können. Issue [#39](https://github.com/HASKI-RAK/HASKI-Backend/issues/39) beschreibt hierzu den notwendigen Endpunkt samt Datenbankeintrag, damit Supportteams reproduzierbare Rückmeldungen erhalten und Service-Level einhalten können.
