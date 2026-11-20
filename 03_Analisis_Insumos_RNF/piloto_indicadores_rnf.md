# Piloto de viabilidad: indicadores de riesgo con data RNF antigua

Corte: 20/11/2026. **Ilustrativo:** la data es un ejercicio manual antiguo, sin fecha, de 13 iniciativas, y no representa el apetito real.
Excel: `piloto_indicadores_rnf.xlsx` (modo calculadora: los supuestos están en amarillo en la hoja Parametros y todo se recalcula).

## 1. Conclusión

- **Técnicamente es viable.** Con una base RNF por iniciativa que traiga el código del playbook, todos los indicadores de Walter (cobertura, nivel por disciplina, nota final y ruta) salen por fórmula, de forma trazable.
- **La decisión de método pesa más que la data.** Con la misma información, la regla de agregación cambia el resultado de 7 iniciativas con nota Alta a ninguna. Sin el criterio real de RNF, los indicadores no son defendibles.
- **Con esta data, la ruta de aprobación no discrimina:** el 100% iría a comité RNF.

## 2. Resultados ilustrativos (12 iniciativas que cruzan)

| Indicador | Valor |
|---|---|
| Cobertura RNF sobre el universo del playbook | 1.2% (12 / 1,004) |
| Evaluadas en go live | 50% (6 / 12) |
| Evaluadas en RNF sin "Finalizado" en el playbook | 17% (2 / 12): BCP-0015 y BCP-0054 |
| Riesgo alto o medio: riesgo de modelo | 100% (12) · solo alto: 33% (4) |
| Riesgo alto o medio: ciberseguridad | 83% (10) · solo alto: 33% (4) |
| Riesgo alto o medio: legal / cumplimiento | 58% (7) · solo alto: 33% (4) |
| Riesgo alto o medio: ética | 50% (6) · solo alto: 8% (1) |
| Riesgo alto o medio: operativo / tecnología | 42% (5) · solo alto: 0% |
| Nota final Alta (método máximo) | 58% (7 / 12) |
| Go live con nota final Alta | 3 de 6: Chatbot Yape, Buscador IA ViaBCP y M365 Copilot |
| Ruta: comité RNF | 100% (12 / 12) |

## 3. Qué aprendimos para la base real

1. **El criterio de agregación lo cambia todo.** Con el máximo (peor caso) salen 7 Altas y 5 Medias; con el promedio, 12 Medias y ninguna Alta. Necesitamos la regla real de Jorge Rivera.
2. **La disciplina no viene en la data.** La inferí desde la categoría de riesgo IA [Supuesto]. La base real debe traer la disciplina evaluadora, o se puede usar la propuesta de Percy (11 categorías) y mapearla.
3. **Hay evaluaciones "de plantilla":** las 5 iniciativas de Github Copilot tienen exactamente los mismos riesgos y niveles. Parece una evaluación por categoría IA, no por iniciativa [Inferido].
4. **No sabemos si el nivel es inherente o residual.** La columna "Criticidad*" remite a una nota al pie que no está en el archivo [Por confirmar]. Para el apetito importa el nivel residual.
5. **Las escalas no están homologadas:** Alto/Relevante/Moderado/Bajo en esta base y Crítico/Alto/Relevante/Moderado en la Base v4. Pasé a 3 niveles con Relevante = Medio [Supuesto].
6. **El playbook se desfasa respecto de RNF** (2 de 12). La cobertura debe medirse con la base RNF, no con el campo del playbook.

## 4. Campos mínimos que pedir para la base real

Código del playbook (o la llave GRC de BCP) · empresa · fecha de evaluación · nivel por disciplina (legal, ciberseguridad, ética, riesgo de modelo, tecnología) · nivel inherente y residual · nota final · regla de agregación · ruta o instancia de aprobación y fecha.
