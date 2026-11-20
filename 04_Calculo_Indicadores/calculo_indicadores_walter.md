# Actividad 4. Cálculo de los indicadores propuestos por Walter

Corte: 20/11/2026. Confidencial. Fuente: `Inputs/Indicadores_propuesta_Walter.xlsx` (6 KRI), playbook (1,004 iniciativas) y data RNF antigua (12 iniciativas que cruzan).
Excel: `calculo_indicadores_walter.xlsx` (modo calculadora). Hojas clave: **Primer_Ejercicio** (valor, semáforo y dato faltante), Umbrales (propuesta editable), Parametros (supuestos), Calculo (paso a paso) y Faltantes.

## 1. Conclusión

- **Ninguno de los 6 KRI se puede calcular completo hoy.** El 5 (terceros) sale parcial; el 2 y el 3 solo tienen denominador; el 1, el 4 y el 6 no se pueden calcular.
- **Hallazgo clave:** los 22 casos materiales (Tier 1-2) están todos en ideación y ninguno tiene evaluación de riesgos registrada. Además, ninguna de las 12 iniciativas con evaluación RNF antigua es material. **No hay cruce entre "materiales" y "evaluados"**, que es la base de los KRI 1 a 3.
- **El dato más fuerte disponible es la concentración en Microsoft:** 81.5% de las iniciativas activas con plataforma identificada (HHI 0.67) [Inferido].

## 2. Resultado por KRI

| # | Dimensión | Estado | Lo que sí sale hoy | Dato que falta |
|---|---|---|---|---|
| 1 | Model Risk / MRM | No calculable | 22 materiales, 0 evaluados. Ilustrativo RNF: 4 de 12 con riesgo de modelo Alto. | Resultado MRM por caso y tolerancias por métrica |
| 2 | Cyber / Data / Privacy | Solo denominador | 22 materiales activos (17 con clientes externos) [Supuesto: aplicable = material]. Ilustrativo RNF: 6 de 12 con Alto. | Hallazgos abiertos por iniciativa, con criticidad y estado |
| 3 | Responsible AI / Conduct | Solo denominador | 22 materiales activos; 84 activas atienden clientes externos. Ilustrativo RNF: 1 de 12 con Alto. | Deficiencias materiales abiertas; eventos reputacionales |
| 4 | Operational / Autonomy | No calculable | Exposición: hasta 205 activas (26%) se llaman "agente" o automatizan acciones; 12 en go live y 9 materiales [Inferido, cota superior]. | Registro de incidentes y límites de autonomía |
| 5 | Third-Party / Resilience | Parcial | 81.5% en Microsoft; 13 de 22 materiales en Microsoft. 342 activas (44%) no identifican la herramienta. | Proveedor/modelo estructurado, due diligence, exit strategy |
| 6 | AI Usage / Financial | No calculable | Los 305 registros con costo están en 0. | Consumo y costo por iniciativa; presupuesto y límites |

Lo de la data RNF es **ilustrativo**: es riesgo inherente identificado (no hallazgos abiertos), sin fecha y sin casos materiales.

## 3. Primer ejercicio con umbrales propuestos

Umbrales = **propuesta nuestra** para discutir con Walter (hoja Umbrales, celdas amarillas). Verde si el valor ≤ "verde hasta"; ámbar si ≤ "ámbar hasta"; rojo si es mayor.

| ID | Indicador del ejercicio | Valor | Calidad | Verde / Ámbar hasta | Semáforo |
|---|---|---:|---|---|---|
| KRI1 | Evaluadas con riesgo de modelo Alto | 33% (4/12) | Ilustrativo | 0% / 10% | Rojo (ilustrativo) |
| KRI2 | Evaluadas con riesgo ciber/datos Alto | 50% (6/12) | Ilustrativo | 0% / 5% | Rojo (ilustrativo) |
| KRI3 | Evaluadas con riesgo sesgo/legal Alto | 8% (1/12) | Ilustrativo | 0% / 10% | Ámbar (ilustrativo) |
| KRI4 | Eventos fuera de límites (n°) | — | Sin dato | 0 / 2 | Sin dato |
| KRI5 | Concentración en Microsoft | 81.5% (362/444) | Playbook [Inferido] | 50% / 70% | Rojo |
| KRI5b | HHI de proveedores | 0.67 | Playbook [Inferido] | 0.15 / 0.25 | Rojo |
| KRI6 | Casos fuera de presupuesto | — | Sin dato | 5% / 10% | Sin dato |
| KCI1 | Materiales sin evaluación | 100% (22/22) | Playbook | 10% / 25% | Rojo |
| KCI2 | Go live sin evaluación finalizada | 52% (63/121) | Playbook | 5% / 15% | Rojo |
| KCI3 | Activas sin proveedor identificado | 44% (342/786) | Playbook | 10% / 20% | Rojo |

**Lectura:** con data real, los 5 indicadores calculables salen en rojo; los tres primeros son de gobierno (cobertura y registro), no de riesgo materializado. Los KRI 1 a 3 son proxies ilustrativos (riesgo inherente Alto en 12 iniciativas antiguas, ninguna material), no hallazgos abiertos. Matiz del KCI1: los 22 materiales están en ideación, donde la evaluación puede no ser exigible todavía [Por confirmar].

## 4. Supuestos clave

- Material = Tier t1 o t2 del campo TierAIRiskTeam [Supuesto; significado de los tiers por confirmar].
- Crítico (proxy RNF) = criticidad Alto. Mapeo categoría RNF → dimensión de Walter en Parametros [Supuesto].
- Proveedor inferido por palabra clave desde "HerramientaUsuario"; GitHub y Azure se agrupan en Microsoft [Inferido].
- Umbrales: propuesta nuestra, con tolerancia baja en riesgos de cliente y datos [Propuesta; validar con Walter / GGR].

## 5. Qué pedir (prioridad alta)

1. Significado oficial de los Tier y si t1-t2 = material (AI Risk Team).
2. Base GRC con la llave del playbook (Rodrigo Díaz, BCP) y resultados MRM con tolerancias (Jorge Rivera).
3. Hallazgos abiertos de ciber, datos y privacidad por iniciativa.
4. Validación de los umbrales propuestos (Walter / GGR, alineado con Alejandra Mendoza).

Detalle completo en la hoja Faltantes.
