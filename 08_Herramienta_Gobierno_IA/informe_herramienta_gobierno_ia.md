# Informe · Guía de ruta Gobierno IA (PPT v35)

Fecha: 26/11/2026 · Fuente única: `Inputs/PPT Comité Gobierno IA v35.pptx`

## 1. Enfoque
Dante pidió el 26/11 una **guía de ruta interactiva** para entender el proceso, no un registro de iniciativas. Por eso no hay campos de datos, fechas, responsables, correos ni guardado.

Además, todo el contenido sale de la PPT. Lo que la PPT no define se marca «Por confirmar».

- **Pantalla principal:** el flujo dinámico de los 5 pasos (S3) y las dos rutas (S6), con los escenarios Ley IA, nivel y semáforo. Incluye un recorrido animado y el detalle de cada caja.
- **Rutas y cupo:** la ruta de atención, la de autonomía y el simulador de cupo por dimensión (S6, S7 y S8).
- **Consulta:** el marco (S2, S4, S5 y S12), las dimensiones (S8–S11 y S15–S17) y los anexos (S14 y S18–S22).
- **Datos:** están separados en `data/config_gobierno_ia.json`, embebido en el HTML. La plantilla gráfica es `06_Reporte_HTML/raf_apetito_ia_bcp.html`.

## 2. Pruebas
Prueba automatizada en Chromium. Resultado: todas OK y 0 errores.

| # | Escenario | Recorrido esperado según la PPT | Resultado |
|---|---|---|---|
| C01 | N5 | Registrar → Ley IA → Triaje → Ágil (hasta 10 d.h.) → Evaluar → Autonomías vigentes de RNF → Monitorear → Reevaluación (S6) | ✓ |
| C02 | N4 | Igual, con Ágil de 10–15 d.h. | ✓ |
| C03 | N3, todo verde | Estándar (15–20 d.h.) → Semáforo → Autonomías vigentes de RNF | ✓ |
| C04 | N2, algún ámbar | Estándar (20–25 d.h.) → Gerencia Owner + Gerencia de Riesgos + opinión AI Risk Team | ✓ |
| C05 | N1, rojo bajo el límite | Reforzada (25–30 d.h.) → Comité de Riesgo No Financiero Corp | ✓ |
| C06 | N2, rojo que llega al límite | Estándar → CAR | ✓ |
| C07 | Uso indebido | Registrar → Ley IA → STOP, sin reloj (S5) | ✓ |
| C08 | N2 sin semáforo (caso límite) | Las 4 instancias se muestran como caminos posibles | ✓ |
| C09 | N4 con semáforo rojo (caso límite) | Se ignora el semáforo: RNF vigente, sin cupo (S5) | ✓ |
| Cupo | Terceros: hoy 4 + 1 / hoy 5 + 1 (límite ≥6) | Comité RNF / CAR | ✓ |

- **Plazos:** el reloj y las rutas muestran los mismos días que la S6 y la S18 (N1 25–30, N2 20–25, N3 15–20, N4 10–15, N5 hasta 10).
- **Móvil:** a 390 px de ancho no hay desplazamiento horizontal.

## 3. Cobertura de las slides 1–12

| Slide | Dónde está |
|---|---|
| S1 | Marco (título, bajada y cifras 6 · 19 · 2 · 1) |
| S2 | Marco (qué proponemos, principios, qué necesita el foro, mejora del triaje, alcance) |
| S3 | Flujo de la Guía (5 pasos, gates, etapas, responsables, resultados, reglas) |
| S4 | Marco (filosofía, pirámide, RACI, proporcionalidad) y detalle de «Evaluación» |
| S5 | Marco (3 niveles), STOP en el flujo y caso de uso indebido |
| S6 | Flujo (rutas, reloj, instancias) y Rutas y cupo |
| S7 | Simulador de cupo («Ver un ejemplo») |
| S8–S11 | Dimensiones y simulador de cupo |
| S12 | Marco (qué falta) |
| S13–S22 | «Ver detalle» y Anexos |

## 4. Puntos que la PPT no define (aparecen como «Por confirmar»)
1. **Días por etapa:** solo existe el total de G1 a G3.
2. **Especialidades y controles:** no se dice qué especialidades intervienen en N4–N5, y no hay catálogo de controles por disciplina.
3. **Regla del CAR:** unas slides dicen «excede el apetito» (S3, S6) y otras «llega al límite» (S5, S7). La guía usa el límite, como en el ejemplo de S7.
4. **Quién hace el triaje:** «2.ª línea de riesgos» (S3) o «AI Risk Team» (S18). La guía muestra los dos.
5. **Efecto del «uso de riesgo alto» de la Ley IA:** no se indica cómo afecta la ruta.
6. **Umbrales:** los propios de IA son preliminares y los heredados están por ratificar (S8, S12).

## 5. Ajustes del 26/11 (pedido de Dante)
- Cabecera sin «PPT v35» ni «Propuesta para validación».
- Sin menciones visibles a la PPT, la versión ni las slides (las fuentes quedan en el JSON).
- Sin los casos de la PPT en la Guía, sin el ejemplo en Marco y sin la lista de puntos no definidos en Anexos.

## 6. Ajustes del 27/11 (feedback a Dante)
- **Ejemplo en la Guía:** botón «Ver el ejemplo: chatbot de clientes» con las 4 partes del caso (iniciativa N2, evaluación por disciplina, rojo por dimensión con sus cupos, decisión del CAR). El recorrido animado resalta cada parte.
- **Ruta del apetito en el flujo:** nueva caja entre el semáforo y la decisión. Se enciende cuando hay una métrica en rojo y lleva al Comité RNF (bajo el límite) o al CAR (llega al límite).
- **Pruebas:** N2 con los 5 resultados de evaluación, N4, STOP y el ejemplo dan el camino esperado; 0 errores, sin desplazamiento horizontal a 390 px y sin menciones visibles a la PPT ni a las láminas.
