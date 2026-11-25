# Actividad 7. Análisis de "Reporte iniciativas IA" (BCP)

Corte: 25/11/2026. Confidencial. Fuente: `Inputs/Reporte iniciativas IA.xlsx` (repo). Alcance: solo BCP.

## 1. Conclusión

- **La base es usable y las llaves cruzan al 100%**: todas las evaluaciones, riesgos y planes cruzan con el código del playbook, y planes y controles cruzan con riesgos por ID Riesgo.
- **Los riesgos IA no están separados.** La "Taxonomía" es la taxonomía corporativa de riesgo operacional (11 categorías: Procesamiento, Ciberseguridad, Modelo, Fraude, etc.), no las categorías IA de Percy. Solo "Modelo" es claramente IA. Por palabras clave, unos 75 de 155 riesgos (~48%) describen un riesgo propio de IA (alucinación, sesgo, prompts, Copilot, etc.) [Inferido]; el resto son riesgos tradicionales de la iniciativa.
- **No hay riesgo residual Alto/Crítico en las dimensiones de Walter.** Los 6 Alto/Crítico son de fraude (BCP-0312, BCP-0012, BCP-0477), que no entra en ninguna de las 6 dimensiones.
- **Viabilidad: 3 KCI calculables; KRI 2 y 3 como proxy; KRI 1 y 5 parciales; KRI 4 y 6 no calculables.**

## 2. Contenido por hoja

| Hoja | Filas | Qué trae | Observaciones |
|---|---:|---|---|
| Iniciativas Playbook | 459 | Código, nombre, descripción, estado (fase), tipo de solución | 449 BCP + 10 "SIN CÓDIGO". **Sin Tier, sin proveedor, sin costo**: hay que cruzar con el playbook del 20/11 (448 de 459 cruzan). 68 en go live (Despliegue 46 + Captura de valor 22). |
| Detalle evaluaciones | 162 | Cuestionario por iniciativa, equipo (Consultores 139 / AIR Team 23), estado, fechas | 150 iniciativas evaluadas; 100 cuestionarios finalizados, 24 en proceso, 17 desestimados, 13 stand by. 8 iniciativas con más de un cuestionario. |
| Detalle riesgos | 167 | Riesgo, taxonomía, riesgo residual, exposición residual (S/ 125 MM total) | 155 riesgos únicos en 65 iniciativas. 12 riesgos repetidos entre iniciativas. Residual: Bajo 75, Moderado 66, Relevante 20, Alto 3, Crítico 3. 30 evaluaciones finalizadas no tienen riesgos registrados. |
| Detalle planes | 173 | Plan por riesgo, responsable, fechas, estado | 83 planes únicos (filas = plan × riesgo) en 20 iniciativas; 123 filas son de BCP-0312. **Todos "En curso" y "Aprobado"**: no hay planes cerrados, así que no se mide cierre. 13 reprogramados, 1 vencido. |
| Detalle controles | 208 | Control por riesgo, categoría, naturaleza, tipo | Cubre 72 de 155 riesgos. Única señal IA explícita: categoría "Guardrails y restricciones de IA" (22) y "Control humano – revisión" (21). |

## 3. Viabilidad de los indicadores (mapeo taxonomía → dimensión [Supuesto])

| # | Indicador | Viabilidad | Resultado preliminar | Qué falta |
|---|---|---|---|---|
| KRI1 | Model Risk / MRM | Parcial (proxy) | 15 riesgos "Modelo" en 10 iniciativas; 1 Relevante, 0 Alto/Crítico. 0 materiales evaluados. | Resultado MRM por caso y tolerancias |
| KRI2 | Ciber / Datos / Privacidad | Proxy calculable | 48 riesgos en 21 iniciativas; 0 Alto/Crítico; 8 Relevante (7 iniciativas), 5 sin plan. | Definir "breach crítico" (¿residual ≥ Relevante sin plan?) |
| KRI3 | IA responsable / Cumplimiento | Proxy calculable | 22 riesgos (Cumplimiento/Legal/Laboral) en 16 iniciativas; 4 Relevante, 3 sin plan. | Etiqueta IA (sesgo, transparencia, supervisión humana) |
| KRI4 | Operacional / Autonomía | No calculable | Solo exposición: 67 riesgos operativos/tecnología, 6 Relevante. | Incidentes y límites de autonomía |
| KRI5 | Terceros | Parcial | 87% de las iniciativas con herramienta identificada usan Microsoft (206/236) [Inferido, playbook 20/11]. | Proveedor estructurado, due diligence, exit strategy |
| KRI6 | Uso / Costo | No calculable | Sin datos de costo ni consumo. | Costo por iniciativa y presupuesto |
| KCI1 | Materiales sin evaluar | Calculable (con cruce) | 16 materiales (Tier t1-t2): 15 sin evaluación, 0 finalizadas (94% / 100%). Todos en ideación o diseño. | Tier solo existe en 219 de 459 (48%) |
| KCI2 | Go live sin evaluar | Calculable | 22 de 68 sin evaluación finalizada (32%); 14 sin ninguna evaluación. Antes: 52%. | Confirmar si "evaluada" = cuestionario finalizado |
| KCI3 | Sin proveedor identificado | Calculable (con cruce) | 223 de 459 (49%) sin herramienta identificada [Inferido]. | Campo proveedor en la base |

## 4. Decisiones a validar antes del HTML

1. Etiqueta de riesgo IA: ¿la pide Riesgos (categorías IA de Percy) o usamos el proxy por palabras clave?
2. Mapeo taxonomía → dimensión de Walter, y dónde va Fraude (concentra todos los Alto/Crítico).
3. Umbral de "crítico" para los KRI: con Alto/Crítico todos salen en 0; con ≥ Relevante salen valores.
4. Tier y proveedor: tomarlos del playbook del 20/11 o pedirlos en esta base.
