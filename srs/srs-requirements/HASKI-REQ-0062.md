---
id: HASKI-REQ-0062
title: Learning Elements über REST abrufen
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
      name: "TestApi::test_get_les_for_topic_for_student"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_le_by_id_for_student"
  merged_from: ["HASKI-REQ-0063", "HASKI-REQ-0056"]
---

## Beschreibung

Das System **shall** eingeschriebenen Studierenden Learning Elements bereitstellen, sowohl als Liste aller Elemente eines Topics als auch als Einzelabfrage. Damit können Empfehlungssysteme, Dashboards und Tracking-Funktionen identische Daten verwenden, ohne mehrere Datenquellen abgleichen zu müssen.

Ergänzend **shall** das System allen berechtigten Studierenden eine vollständige Liste der Lernelemente eines belegten Kurses liefern. Neben den Stammdaten der Elemente müssen auch die individuellen Lernfortschrittsinformationen enthalten sein, damit Lernräume, Empfehlungen und Visualisierungen direkt mit der gelieferten Struktur arbeiten können.

### Learning Elements pro Topic

Listet sämtliche Learning Elements eines Topics inklusive persönlichem Fortschritt.

### Einzelnes Learning Element

Liefert Detailinformationen zu einem einzelnen Learning Element, sodass UI- und Analytics-Komponenten gezielt mit einem Element arbeiten können, ohne komplette Listen zu laden.

## Akzeptanzkriterien

### Learning Elements pro Topic

- [x] Die Antwort umfasst alle Learning Elements des Topics mit den relevanten Metadaten (z. B. Typ, Klassifikation, Name, LMS-Referenz) und dem zugehörigen `student_learning_element`-Status.
- [x] Topics, zu denen kein legitimer Zugriff besteht, liefern keine Daten.
- [x] Änderungen an Learning Elements werden ohne Zusatzaufwand in der Ausgabe sichtbar.
- [x] Wird kein Learning Element gefunden, wird eine leere Liste zurückgegeben, damit Aufrufer deterministisch reagieren können.

### Einzelnes Learning Element

- [x] Für gültige Kombinationen aus Studierendem, Kurs, Topic und Learning Element werden sämtliche relevanten Metadaten sowie der `student_learning_element`-Kontext geliefert.
- [x] Nicht zugeordnete oder unbekannte Ressourcen werden nicht ausgegeben.
- [x] Die gelieferten Felder entsprechen der zentralen Learning-Element-Spezifikation und können ohne zusätzliche Transformationen verwendet werden.
- [x] Wird ein Learning Element entfernt, liefert die Abfrage keine Daten mehr, wodurch veraltete Verlinkungen frühzeitig auffallen.

### Learning Elements eines Kurses

- [x] Die zurückgegebene Liste umfasst sämtliche Lernelemente des ausgewählten Kurses samt Typ, Klassifikation, Namen und studentischem Status.
- [x] Elemente, die nicht zur Anfrage passen oder nicht freigegeben sind, werden konsequent ausgeblendet.
- [x] Neue oder geänderte Lernelemente erscheinen ohne zusätzliche Synchronisationsschritte in der Ausgabe.

## Rationale

SyRS-FUNC-008 sieht lernpfadfähige Räume vor, in denen pro Topic sämtliche Elemente verfügbar sind. Eine standardisierte Auslieferung verhindert Inkonsistenzen zwischen Frontend, Analytics und Tutoring-Komponenten. Einzelne Lernpfad-Ansichten, Feedbackdialoge oder Auswertungen benötigen zielgerichtete Detailinformationen, wobei jede Ressource isoliert adressiert werden kann und gleichzeitig die geltenden Einschreibungsregeln respektiert werden.

## Hinweise

- Die Datenstruktur entspricht der in der OAS beschriebenen Topic/LE-Spezifikation.
- Die Struktur ist kompatibel zwischen Listen- und Einzelabfrage-Endpunkten, wodurch Frontends dieselben Komponenten wiederverwenden können.
