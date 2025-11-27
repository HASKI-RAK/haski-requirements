---
id: HASKI-REQ-0063
title: Einzelnes Learning Element abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#21", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_le_by_id_for_student"
---

## Beschreibung

Das System **shall** über `GET /user/<user_id>/<lms_user_id>/student/<student_id>/course/<course_id>/topic/<topic_id>/learningElement/<learning_element_id>` die Detaildaten eines einzelnen Learning Elements zurückliefern, sofern der Studierende für Kurs und Topic eingeschrieben ist. Die Antwort **shall** mindestens `id`, `lms_id`, `activity_type`, `classification`, `name`, `university` sowie den Kontext `student_learning_element` enthalten, sodass Frontends Lernfortschritt und Metadaten synchron anzeigen können. Ungültige Referenzen oder fehlende Berechtigungen **shall** deterministisch mit 404 bzw. 403 beantwortet werden, ohne sensible Daten preiszugeben.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 inklusive der genannten Felder.
- [x] Nicht vorhandene Studierende, Kurse, Topics oder Learning-Element-IDs führen zu HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Zugriff auf Learning Elements außerhalb der eigenen Einschreibung wird verweigert (404/403).
- [x] Die Route nutzt dieselbe Moodle-ID-Mapping- und Rollenlogik wie die Listenendpunkte (HASKI-REQ-0062) und entspricht dem OAS-Schema aus GH-30.

## Rationale

Issue [#21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21) beschreibt die Synchronisation von Moodle-Learning-Elements mit dem HASKI-Backend. Viele UI- und Analytics-Komponenten benötigen Detaildaten (z. B. Klassifizierung, Lernfortschritt) zu einem einzelnen Element; ein dedizierter Endpoint verhindert, dass Clients komplette Listen übertragen müssen. Die Anforderung stellt sicher, dass jede Ressource einzeln adressierbar bleibt und zugleich die Enrollment-Schutzmechanismen eingehalten werden.

## Hinweise

- Wird ein Learning Element gelöscht oder dem Kurs entzogen, liefert der Endpoint 404.
- Die Implementierung sollte Logging für alle Fehlerpfade aktivieren, um Inkonsistenzen rasch zu erkennen.
- Schema dient als Grundlage für spätere PATCH/PUT-Anforderungen.
