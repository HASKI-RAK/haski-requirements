---
id: HASKI-REQ-0083
title: Über-uns-Seite mit Konsortialbildern bereitstellen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-MGMT-005
links:
  stories:
    - "HASKI-RAK/HASKI-Frontend#256"
  parents: ["SyRS-MGMT-005"]
  tests:
    - path: "frontend/src/components/ImageCollection/ImageCollection.test.tsx"
      name: "ImageCollection Component"
    - path: "HASKI-Frontend/src/pages/AboutUs/AboutUs.test.tsx"
      name: "AboutUs"
    - path: "HASKI-Frontend/src/components/TextCard/TextCardLeft/TextCardLeft.test.tsx"
      name: "TextCardRight tests"
    - path: "HASKI-Frontend/src/components/TextCard/TextCardRight/TextCardRight.test.tsx"
      name: "TextCardLeft tests"
    - path: "HASKI-Frontend/src/components/TextStepper/TextStepper.test.tsx"
      name: "TextStepper tests"
    - path: "HASKI-Frontend/src/components/Typewriter/Typewriter.test.tsx"
      name: "Typewriter tests"
    - path: "HASKI-Frontend/src/pages/ProjectDescription/ProjectDescription.test.tsx"
      name: "ProjectDescription tests"
---

## Beschreibung

Das Frontend **shall** auf der Über-uns-Seite ein responsives Bildlayout bereitstellen, das die drei Projektstandorte mit individuellen Bildern visualisiert. Das Layout **shall** auch ohne konfigurierte Bildquellen stabil rendern, damit redaktionelle Anpassungen keinen Darstellungsfehler erzeugen, und bei gesetzten URLs jeweils die bereitgestellten Motive präsentieren.

## Akzeptanzkriterien

- [x] Die Über-uns-Seite zeigt eine dreigeteilte Bildcollage, in der pro Projektstandort ein individuelles Bild mit konsistenter Ausrichtung angezeigt wird.
- [x] Fehlen einzelne Bild-URLs, rendert die Komponente weiterhin stabil und ohne Laufzeitfehler, sodass die Seite redaktionell wartbar bleibt.

## Rationale

Issue [#256](https://github.com/HASKI-RAK/HASKI-Frontend/issues/256) refaktoriert die Über-uns-Seite, um CSS-Layouts durch wiederverwendbare React-Komponenten zu ersetzen. Die Bildcollage visualisiert die HASKI-Konsortialpartner und unterstützt die Disseminationspflicht aus SyRS-MGMT-005.

## Hinweise

- Die Komponente soll semantisch markierte Container verwenden, damit assistive Technologien die Darstellung erfassen können.
- Weitere Seiten dürfen die Collage nur mit konsortialen Motiven verwenden, um den Projektkontext konsistent zu halten.
