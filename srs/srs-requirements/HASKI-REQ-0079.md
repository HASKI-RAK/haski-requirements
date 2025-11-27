---
id: HASKI-REQ-0079
title: Lernprofil-Reset über REST
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-007
links:
  parents: ["SyRS-FUNC-007"]
  stories:
    - "HASKI-RAK/HASKI-Backend#30"
    - "HASKI-RAK/HASKI-Backend#81"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_learning_characteristics"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_learning_analytics"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_learning_style"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_learning_strategy"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_knowledge"
---

## Beschreibung

Das Backend **shall** für jedes Lernprofil eines Studierenden abgesicherte `DELETE`-Endpunkte bereitstellen, über die Administrator:innen oder Berechtigte alle Lerncharakteristika wieder auf ihre Defaultwerte setzen können. `DELETE /user/<user_id>/<lms_user_id>/student/<student_id>/learningCharacteristics` **shall** sämtliche abhängigen Artefakte (Learning-Analytics-Metriken, Lernstil, Lernstrategie, Knowledge) in einem Schritt zurücksetzen und den neu initialisierten Datensatz als JSON mit denselben Strukturen wie der entsprechende `GET`-Endpoint liefern. Die Route **shall** nur konsistente Kombinationen aus interner HASKI-User-ID, verknüpfter Moodle-ID und Student-ID akzeptieren; fehlerhafte Eingaben erzeugen deterministische Fehlermeldungen, ohne Daten zu verändern.

Ergänzend **shall** granularere Resets über `DELETE`-Routen für `learningAnalytics`, `learningStyle`, `learningStrategy` und `knowledge` unterstützt werden, sodass Automationen (z. B. erneute ILS-/LIST-K-Imports) nur einzelne Teilbereiche zurücksetzen können. Alle Endpunkte **shall** sofort mit den in GH-81 definierten Defaultwerten antworten, damit neu importierte Fragebogenergebnisse ohne race conditions eingespielt werden können.

## Akzeptanzkriterien

- [x] Ein valider Aufruf von `DELETE /.../learningCharacteristics` liefert HTTP 200 sowie ein JSON mit den Schlüsseln `learning_style`, `learning_strategy`, `learning_analytics`, `knowledge` und verweist auf die neu initialisierten Defaultdatensätze.
- [x] Die Einzel-Endpoints (`.../learningAnalytics`, `.../learningStyle`, `.../learningStrategy`, `.../knowledge`) liefern jeweils HTTP 200 samt neuem Datensatz und verändern ausschließlich den adressierten Teilbereich.
- [x] Nicht vorhandene oder nicht zusammenpassende `user_id`/`lms_user_id`/`student_id`-Kombinationen werden mit HTTP 404 und der standardisierten Fehlstruktur (`{"error": "...", "message": "..."}`) beantwortet.
- [x] Direkt nach einem Reset liefern die entsprechenden `GET`-Endpoints wieder die Defaultwerte aus GH-81, sodass Lernpfadberechnungen deterministisch weiterlaufen.

## Rationale

GitHub Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) verlangt vollständige CRUD-Unterstützung für alle OAS-definierten Lernprofil-Endpunkte, einschließlich `DELETE`-Operationen. Issue [#81](https://github.com/HASKI-RAK/HASKI-Backend/issues/81) beschreibt die initialen Standardwerte für Lerncharakteristika; dieses Requirement stellt sicher, dass dieselben Defaults per Reset erneut angewendet werden können, um korrupte oder veraltete Lernprofildaten zu bereinigen. Die E2E-Tests `backend/tests/e2e/test_api.py::TestApi::test_reset_learning_characteristics`, `backend/tests/e2e/test_api.py::TestApi::test_reset_learning_analytics`, `backend/tests/e2e/test_api.py::TestApi::test_reset_learning_style`, `backend/tests/e2e/test_api.py::TestApi::test_reset_learning_strategy` und `backend/tests/e2e/test_api.py::TestApi::test_reset_knowledge` prüfen aggregierte wie auch granulare Resets Ende-zu-Ende.

## Hinweise

- Die Implementierung nutzt dieselben Repository-/Servicepfade wie die GET-Endpoints; Resets dürfen keine zusätzlichen Nebenwirkungen (z. B. neue Kursrelationen) erzeugen.
- Autorisierte Rollen (z. B. Lehrende, Administrator:innen) sollen Resets protokollieren, um Supportfällen nachzugehen.
- Weitere Tests für die granularen Teilendpoints sollen hier referenziert werden, sobald sie die jeweilige `DELETE`-Route abdecken.
