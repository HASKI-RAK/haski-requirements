---
id: HASKI-REQ-0069
title: Nutzerstammdaten per LMS-ID abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-003
merged_from: ["HASKI-REQ-0075", "HASKI-REQ-0081"]
links:
  parents: ["SyRS-INT-003"]
  stories: ["HASKI-RAK/HASKI-Backend#30", "HASKI-RAK/HASKI-Backend#81"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_user_by_id"
---

## Beschreibung

Das Backend **shall** einen abgesicherten GET-Endpunkt `GET /user/<user_id>/<lms_user_id>` bereitstellen, der die kanonischen Stammdaten eines HASKI-Nutzers anhand der Kombination aus lokaler User-ID und zugehöriger Moodle-ID zurückliefert. Die Antwort **shall** mindestens `id`, `name`, `university`, `role`, `lms_user_id` sowie den aktuellen `settings`-Block enthalten, damit Frontend- und Service-Komponenten dieselben Profilinformationen verwenden können. Fehlende oder nicht zueinander passende IDs **shall** eine deterministische Fehlermeldung (`{"error": "...", "message": "..."}`) erzeugen, ohne weitere Daten preiszugeben.

Ergänzend **shall** das Backend einen OAS-konformen Endpunkt `PUT /lms/user/<user_id>/<lms_user_id>` bereitstellen, über den Moodle das Stammdatenprofil eines bereits angelegten HASKI-Nutzers aktualisieren kann (z. B. Namensänderung, neue Hochschulzuordnung). Die Route **shall** die Kombination aus interner `user_id` und verknüpfter `lms_user_id` prüfen, bevor Änderungen an den Tabellen `haski_user` und `settings` vorgenommen werden, damit nur existierende Profile angepasst werden und Rollenzuordnungen sowie Einstellungen konsistent bleiben.

Schließlich **shall** das Backend den OAS-Endpunkt `DELETE /lms/user/<user_id>/<lms_user_id>` bereitstellen, über den Moodle oder Administrator:innen einen HASKI-Nutzer mitsamt seiner LMS-Verknüpfung entfernen können. Die Route **shall** zunächst prüfen, ob die Kombination aus interner `user_id` und externer `lms_user_id` existiert; nur dann werden der `haski_user`-Datensatz samt abhängiger Einträge (z. B. `student`, `teacher`, Lernprofil-Tabellen, Kursrelationen) konsistent gelöscht und eine semantische Bestätigung (`{"message": "deleted"}`) zurückgegeben.

## Akzeptanzkriterien

### Nutzerstammdaten lesen

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und geben exakt den in GH-30 beschriebenen Payload (inkl. `settings`) für den adressierten Nutzer zurück.
- [x] Ungültige oder nicht verknüpfte Kombinationen aus `user_id` und `lms_user_id` resultieren in HTTP 404 mit der beschriebenen Fehlstruktur, ohne interne Details zu offenbaren.
- [x] Der Endpunkt akzeptiert ausschließlich authentifizierte Nutzer (z. B. aus einer bestehenden Session) und stellt sicher, dass nur berechtigte Rollen eigene oder delegierte Profile lesen können.
- [x] Alle gelieferten Attribute spiegeln die von GH-81 initialisierten Stammdaten wider; Änderungen an Einstellungen werden unmittelbar reflektiert.
- [x] Antwortschema bleibt OAS-konform, sodass Frontend-Komponenten keine zusätzlichen Mappings implementieren müssen.

### Nutzerstammdaten aus Moodle aktualisieren

- [x] Ein vollständiger Request mit `name` und `university` liefert HTTP 201 sowie ein JSON mit `id`, `name`, `university`, `lms_user_id`, `role` und `settings`.
- [x] Fehlende Pflichtfelder oder falsche Datentypen führen zu HTTP 400 mit der standardisierten Fehlstruktur (`{"error": "...", "message": "..."}`) und verursachen keine Datenänderung.
- [x] Nicht existente Kombinationen aus `user_id` und `lms_user_id` werden mit HTTP 404 beantwortet und offenbaren keine internen Details.
- [x] Bereits gespeicherte Rollenzuordnungen und Settings bleiben bei einem Update unverändert erhalten, damit Berechtigungen und UI-Präferenzen konsistent bleiben.

### LMS-Nutzer entfernen

- [x] Erfolgreiche Löschanfragen für Studierende und Lehrende liefern HTTP 200 und geben eine Bestätigungsnachricht zurück.
- [x] Nicht existente oder nicht zusammenpassende `user_id`/`lms_user_id`-Kombinationen führen zu HTTP 404 mit standardisierter Fehlstruktur (`{"error": "...", "message": "..."}`) ohne Seiteneffekte.
- [x] Beim Entfernen werden abhängige Tabellen (`settings`, `student`, `teacher`, Lernprofile, Enrollment-Relationen) konsistent bereinigt, sodass nachfolgende GET- oder POST-Aufrufe keine verwaisten Datensätze finden.
- [x] Alle Operationen sind transaktional; schlägt ein Schritt fehl, wird der ursprüngliche Datensatz vollständig wiederhergestellt.

## Rationale

GitHub Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) definiert im Basic-Setup-OAS sämtliche Nutzerendpunkte. Damit die Moodle-LTI-Integration (SyRS-INT-003) konsistent auf Nutzerprofile zugreifen kann, benötigt HASKI einen deterministischen Lookup über die gekoppelte LMS-ID. Issue [#81](https://github.com/HASKI-RAK/HASKI-Backend/issues/81) stellt sicher, dass bei der ersten Anmeldung vollständige Stammdaten und Settings vorliegen, die dieser Endpunkt unmittelbar zurückliefert.

## Hinweise

- Die Antwort enthält bewusst keine sensiblen Felder wie Passwörter oder interne Role-IDs; diese werden serverseitig gefiltert.
- Validierungsfehler sollen klar zwischen „MissingUser" und allgemeinen Autorisierungsproblemen unterscheiden, damit Supportfälle schneller eingegrenzt werden können.
- E2E-Verifikation: `backend/tests/e2e/test_api.py::TestApi::test_get_user_by_id`.
