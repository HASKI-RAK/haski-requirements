---
id: HASKI-REQ-0081
title: LMS-Nutzer entfernen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-003
links:
  parents: ["SyRS-INT-003"]
  stories:
    - "HASKI-RAK/HASKI-Backend#30"
    - "HASKI-RAK/HASKI-Backend#81"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_delete_user"
---

## Beschreibung

Das Backend **shall** den OAS-Endpunkt `DELETE /lms/user/<user_id>/<lms_user_id>` bereitstellen, über den Moodle oder Administrator:innen einen HASKI-Nutzer mitsamt seiner LMS-Verknüpfung entfernen können. Die Route **shall** zunächst prüfen, ob die Kombination aus interner `user_id` und externer `lms_user_id` existiert; nur dann werden der `haski_user`-Datensatz samt abhängiger Einträge (`student`, `teacher`, Lernprofil-Tabellen, Kursrelationen) konsistent gelöscht. Erfolgreiche Aufrufe **shall** eine semantische Bestätigung (`{"message": "deleted"}`) mit HTTP 200 zurückgeben.

## Akzeptanzkriterien

- [x] Erfolgreiche Löschanfragen für Studierende und Lehrende liefern HTTP 200 und geben eine Bestätigungsnachricht zurück.
- [x] Nicht existente oder nicht zusammenpassende `user_id`/`lms_user_id`-Kombinationen führen zu HTTP 404 mit standardisierter Fehlstruktur (`{"error": "...", "message": "..."}`) ohne Seiteneffekte.
- [x] Beim Entfernen werden abhängige Tabellen (`settings`, `student`, `teacher`, Lernprofile, Enrollment-Relationen) konsistent bereinigt, sodass nachfolgende GET- oder POST-Aufrufe keine verwaisten Datensätze finden.
- [x] Alle Operationen sind transaktional; schlägt ein Schritt fehl, wird der ursprüngliche Datensatz vollständig wiederhergestellt.

## Rationale

GitHub Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) fordert vollständige CRUD-Unterstützung für die LMS-Nutzerverwaltung, einschließlich Delete-Operationen. Issue [#81](https://github.com/HASKI-RAK/HASKI-Backend/issues/81) erzeugt beim ersten Login automatisch abhängige Tabellen; dieser Delete-Endpoint entfernt genau diese Strukturen wieder, damit Mandanten personenbezogene Daten auf Anfrage löschen können. Der E2E-Test `backend/tests/e2e/test_api.py::TestApi::test_delete_user` prüft sowohl erfolgreiche Löschungen als auch Fehlerszenarien.

## Hinweise

- Löschanforderungen sollen auditierbar protokolliert werden (DSGVO Art. 17 Nachweis).
- Die Implementation nutzt dieselben Autorisierungschecks wie die korrespondierenden PUT/POST-Endpoints, damit nur berechtigte Systeme Nutzerkonten entfernen.
