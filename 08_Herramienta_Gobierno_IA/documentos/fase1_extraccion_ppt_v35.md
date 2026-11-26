# Herramienta de Gobierno IA · Fase 1: extracción de la PPT Comité Gobierno IA v35

**Fuente:** `Inputs/PPT Comité Gobierno IA v35.pptx` (22 slides: 1–12 principales, 13–22 anexos). La PPT **no tiene notas del orador**. Cita: (S*n*). Lo que no está en la PPT va como **[Por confirmar]**.

---

## 1. RAF / marco de apetito de riesgo de IA

**Objetivo (S1, S2, S4, S5).** Un RAF de IA que reutiliza lo que ya existe en el Grupo y mide lo propio de la IA: qué se vigila, cuánto tarda cada iniciativa y quién decide. Declaración: *"usar la IA para mejorar la experiencia del cliente y la eficiencia, protegiendo a los clientes, sus datos y la continuidad del servicio"* (S4, S5).

**Cifras clave (S1):** 6 dimensiones · 19 métricas · 2 rutas · 1 ciclo de vida.

**Qué se propone (S2):** 6 dimensiones (3 heredadas del RAF vigente con foco IA: Ciber, Operativo, Terceros; 3 nuevas: Gobierno de riesgos IA, Legal/Ley IA, Modelo) · 2 rutas sobre el ciclo de vida existente · 1 registro conectado (inventario + base de riesgos + bases de eventos, unidos por el código de iniciativa).

**Principios de diseño (S2):**
1. Reutilizar antes que crear (ciclo de vida, taxonomías, triaje, evaluación RNF, gobierno de métricas de GGR).
2. Medir lo propio de la IA sin forzarlo a dinero: solo 1 de 19 métricas es monetaria.
3. Sin puntaje agregado: el apetito se lee por disciplina y **manda el peor semáforo**.
4. Cada especialidad conserva su metodología.

**Estructura en pirámide (S4):** Dimensión (lo que ve Dirección y el CAR; apetito, ámbar y límite) → Métrica (lo que mide cada disciplina; una métrica en rojo suma a su dimensión) → Control (se evalúa en cada iniciativa; algunos controles son además métricas). Transversal: RACI de controles. A mayor materialidad, más controles (N1 más, N5 menos).

**Alcance (S4, S5, S2):** el apetito aplica a iniciativas **materiales (N1–N3)**; N4–N5 siguen el proceso vigente de RNF y no usan cupo. Marco corporativo para las empresas del Grupo (S2).

**Niveles de apetito (S5):**

| Nivel | Regla | Qué incluye |
|---|---|---|
| **Prohibido** | Sin excepción y sin cupo. La iniciativa se detiene (STOP) y no entra a rutas. | Usos indebidos de la Ley IA y su Reglamento (DS 115-2025-PCM). Ej.: manipulación, inferencia de datos sensibles por biometría, identificación biométrica en tiempo real en espacios públicos, vigilancia masiva, predicción de delitos por perfiles. El listado literal lo valida Legal. |
| **Sin apetito** | El primer caso ya es rojo y se mide en el RAF. | Gobierno: IA material sin registro/dueño/aprobación; cambios materiales sin reevaluación; brechas críticas vencidas. Ciber: datos personales sin base legal ni evaluación de privacidad; incidentes significativos con vector IA †. Legal: obligaciones de riesgo alto sin atención. Terceros: proveedores IA con riesgos AC sin plan vigente †. († heredada del RAF vigente) |
| **Aceptado con condiciones** | Dentro del cupo de cada dimensión. | Iniciativas N1–N3 con brecha dentro del cupo, aprobadas según la ruta de autonomía. Si la dimensión llega a su límite, decide el CAR. |

**Oportunidad de mejora del triaje (S2):** hoy se usa el triaje N1–N5 del AI Risk Team al 100%; la evaluación no distingue el riesgo IA con las 11 categorías. A mejorar: etiquetar riesgos y controles con las 11 categorías; sumar criterios al triaje (exposición del caso de uso, complejidad del modelo, autonomía y supervisión, impacto en clientes); separar IA tradicional de no tradicional. Propuesta de nuevo triaje: ~2 semanas.

---

## 2. Cómo funciona: flujo del proceso (S3)

| # | Paso | Gate | Etapa del ciclo de vida | Qué pasa | Responsable | Entregable |
|---|---|---|---|---|---|---|
| 1 | Registrar | — | Ideación | Registro en el inventario (Playbook u otra herramienta con los campos corporativos) | 1.ª línea · Programa IA | Código único de iniciativa |
| 2 | Clasificar (triaje) / Pre-assessment | **G1** | Ideación | Nivel N1–N5 (materialidad e impacto) y categoría de la Ley IA | 2.ª línea de riesgos (S18: "AI Risk Team") | Ruta de atención: Ágil, Estándar o Reforzada |
| 3 | Evaluar / Assessment | **G2** | Diseño y desarrollo | Las especialidades evalúan en paralelo, con su metodología y matriz de controles proporcionales | MRM · Legal · Ciber · RNF · Terceros · Cumplimiento | Semáforo por disciplina frente al apetito. Aquí se fija quién aprobará |
| 4 | Decidir | **G3** | Piloto | Se cruza el resultado de controles por especialidad con el nivel de materialidad | Instancia según la ruta de autonomía | Instancia que aprueba: Gerencia, Comité RNF o CAR |
| 5 | Monitorear | — | Despliegue y valor | Tablero de apetito mensual con evaluaciones, incidentes y pérdidas etiquetadas IA | 1.ª y 2.ª línea · AI Risk Officer | Reevaluación ante un rojo o un cambio material |

Reglas del flujo (S3): la evaluación confirma o ajusta la clasificación inicial; en producción, un rojo o un cambio material vuelve a pasar la iniciativa por la ruta. Fuera de las rutas: uso indebido = STOP. El reloj del SLA corre **de G1 a G3**.

---

## 3. Dimensiones, métricas y umbrales (S8–S11; anexos S15–S17)

**Regla general (S8–S11):** una métrica en rojo suma 1 a su dimensión; cada iniciativa cuenta una sola vez por dimensión; solo cuentan iniciativas materiales (N1–N3) en producción (en Gobierno, los casos de IA en uso). Umbrales en n.º de iniciativas con brecha. Los propios de IA son preliminares; los heredados se ratifican con su dueño.

**Umbrales de dimensión (S8):**

| Código | Dimensión | Qué vigila | Origen | Apetito | Ámbar | Límite | N.º métricas |
|---|---|---|---|---|---|---|---|
| RAF-IA-01 | Gobierno de riesgos IA | Shadow IA, brechas críticas, residual alto/crítico, cambios sin reevaluación | Nuevo | 0 | 1–2 | ≥3 | 4 |
| RAF-IA-02 | Legal / Ley IA | Incumplimientos confirmados y obligaciones de riesgo alto sin evidencia | Nuevo | 0 | 1 | ≥2 | 2 |
| RAF-IA-03 | Ciber / Privacidad de Datos | Vulnerabilidades, incidentes vector IA, obsolescencia, datos personales | Heredado + 1 nuevo | ≤2 | 3 | ≥4 | 4 |
| RAF-IA-04 | Operativo y Resiliencia | Pérdidas/provisiones IA y disponibilidad | Heredado | ≤2 | 3 | ≥4 | 2 |
| RAF-IA-05 | Terceros | Proveedores alto riesgo evaluados y con planes, concentración | Heredado + 1 nuevo | ≤2 | 3–5 | ≥6 | 3 |
| RAF-IA-06 | Riesgo de modelo | Alucinaciones, toxicidad, robustez, deterioro | Nuevo | ≤2 | 3 | ≥4 | 4 |

Orden (S8): perímetro → obligaciones → clientes → operación → dependencias → desempeño.

**Métricas por iniciativa (S9–S11; códigos y fórmula en S15–S17):**

| Código | Métrica | Origen | Verde | Ámbar | Rojo | Fórmula / cómo se cuenta (anexo) |
|---|---|---|---|---|---|---|
| GOB-01 | IA en uso sin registro, dueño o aprobación (Shadow IA) | Propio IA | 0 | — | ≥1 | Conteo; cruce del registro con fuentes independientes (S15) |
| GOB-02 | Brechas críticas abiertas | Propio IA | 0 abiertas | ≥1 en plazo | ≥1 vencida | Estado; "brecha crítica" por validar con AI Risk Team (S15) |
| GOB-03 | Riesgo residual alto o crítico | Propio IA | Bajo/medio | Alto | Crítico | De la evaluación RNF; consolida el AI Risk Officer (S15) |
| GOB-04 | Cambios materiales sin reevaluación | Propio IA | 0 | — | ≥1 | Conteo de cambios (S15) |
| LEG-01 | Incumplimiento legal confirmado | Propio IA | 0 | — | ≥1 | Confirmado por Legal; escala solo (S15) |
| LEG-02 | Obligaciones de riesgo alto sin evidencia | Propio IA | Cumple todas | — | Falta ≥1 | Transparencia, supervisión humana, registro/documentación; sin ámbar (S15) |
| CYB-01 | Vulnerabilidades AC >30 d por activo IA | Heredado (vig. 20) | <2% | 2–<5% | ≥5% | Vulnerabilidades AC >30 d ÷ activos IA (S16) |
| CYB-02 | Incidentes significativos con vector IA | Heredado (vig. 21) | 0 | — | ≥1 | Conteo; escala solo (S10, S16) |
| CYB-03 | Componentes IA obsoletos | Heredado (vig. 19) | <5% | 5–<10% | ≥10% | Instancias obsoletas ÷ instancias IA (S16) |
| CYB-04 | Datos personales sin base legal ni evaluación de privacidad | Propio IA | Con respaldo | En trámite con plan | Sin respaldo | Estado (S16) |
| OPS-01 | Pérdidas operativas por eventos IA (única monetaria) | Heredado (vig. 16) | <1,1% | 1,1–<1,3% | ≥1,3% | Pérdida + provisiones etiquetadas IA; denominador por confirmar; umbral BCP (S16) |
| OPS-02 | Disponibilidad de servicios IA críticos | Heredado (vig. 17) | >99,5% | 99,0–99,5% | ≤99,0% | % mensual de endpoints (S16) |
| TER-01 | Proveedores IA alto riesgo evaluados en 12 m | Heredado (vig. 22) | 100% | 95–<100% | <95% | Evaluados ÷ total (S17) |
| TER-02 | Proveedores IA con riesgos AC sin plan | Heredado (vig. 22) | 0 | — | ≥1 | Conteo mensual (S17) |
| TER-03 | Concentración en un proveedor o modelo | Propio IA | ≤2 | 3–5 | ≥6 | Grupo más grande; cada iniciativa hereda el color (S17) |
| MRM-01 | Alucinaciones financieras materiales | Propio IA | <0,25% | 0,25–<0,50% | ≥0,50% | Errores ÷ respuestas evaluadas (S17) |
| MRM-02 | Respuestas tóxicas | Propio IA | <0,20% | 0,20–<0,50% | ≥0,50% | Tóxicas ÷ evaluadas (S17) |
| MRM-03 | Fallas ante pruebas adversariales | Propio IA | <1,0% | 1,0–<2,0% | ≥2,0% | Fallidas ÷ ejecutadas (S17) |
| MRM-04 | Deterioro del desempeño vs. validación | Propio IA | <10% | 10–<15% | ≥15% | (validada − actual) ÷ validada (S17) |

**Controles asociados:** la PPT **no lista controles** por dimensión. Solo dice que hay un "set de controles por disciplina", proporcional al nivel N1–N5, con RACI, y que algunos controles alimentan el apetito (S4). El ejemplo de S7 da conteos ilustrativos (MRM 15, Ciber 12, Legal 8, RNF 5), sin nombres. → **[Por confirmar]** en toda la herramienta.

---

## 4. Rutas (S3, S6, S7, S18)

**Ruta de atención: cuánto tarda.** Se asigna en G1 según el nivel de triaje. SLA sugerido en días hábiles, de G1 a G3 (S3, S6, S18):

| Nivel | Materialidad | Qué describe (S18) | Ejemplo (S18) | Ruta | SLA G1→G3 | Cuenta para el apetito |
|---|---|---|---|---|---|---|
| N1 | Material | Afectación financiera directa material; capital, provisiones, solvencia; derechos; decisiones adversas; servicio crítico | Agente que ejecuta pagos y transferencias | Reforzada | 25–30 d.h. | Sí |
| N2 | Material | Interacción directa con cliente; información financiera; decisión material controlada; datos sensibles | Chatbot de consultas de clientes | Estándar | 20–25 d.h. | Sí |
| N3 | Material | Proceso interno con impacto indirecto sobre clientes o resultados | Resumen automático de reclamos | Estándar | 15–20 d.h. | Sí |
| N4 | No material | Automatización interna sin decisión material ni impacto directo sobre clientes | Clasificador de tickets internos | Ágil | 10–15 d.h. | No |
| N5 | No material | Productividad personal y asistencia no vinculante | Asistente de redacción de correos | Ágil | hasta 10 d.h. | No |

**Ruta de autonomía: quién decide.** Solo materiales (N1–N3). Se fija en G2 según el semáforo; decide la instancia en G3 (S3, S6):

| Resultado de la evaluación | Instancia que aprueba | Condición |
|---|---|---|
| Todo verde (cada métrica en verde) | Autonomías vigentes de RNF | Sin instancias nuevas del RAF |
| Algún ámbar, ningún rojo | Gerencia Owner + Gerencia de Riesgos + opinión AI Risk Team | El ámbar lleva fecha de cierre |
| Rojo en alguna disciplina y su dimensión queda bajo el límite | Comité de Riesgo No Financiero Corp | + AI Risk Team y condiciones |
| Rojo y su dimensión llegaría al límite | CAR | Se excede el apetito; Directorio informado |
| N4–N5 | Proceso de autonomías vigentes de RNF | — |
| Uso indebido (Ley IA) | STOP | Sin excepción, fuera de rutas |

**Varios rojos (S7):** cada rojo se mide contra el cupo de su dimensión; manda la instancia más exigente. Ejemplo: chatbot N2 (Estándar, 20–25 d.h.); MRM 1 rojo (RAF-IA-06: hoy 1 + 1 = 2, bajo el límite de 4 → Comité RNF) y Ciber 1 rojo (RAF-IA-03: hoy 3 + 1 = 4 = límite → CAR). Decide el CAR.

**Especialidades que intervienen (S3, S14):** evalúan en paralelo en G2: MRM, Legal, Ciber, RNF, Terceros, Cumplimiento. Taxonomía de 1.ª línea: Áreas de Negocio, Tecnología, Ciberseguridad, Data. 2.ª línea: RNF, Riesgo de Modelo, Cyber Risk, Legal, Cumplimiento, Otras.

---

## 5. Roles y responsabilidades

| Rol | Qué hace | Slide |
|---|---|---|
| 1.ª línea · Programa IA | Registra la iniciativa; monitorea | S3 |
| 2.ª línea de riesgos / AI Risk Team | Triaje N1–N5 en G1; opina en ruta ámbar y roja | S3, S6, S18 |
| AI Risk Officer | Consolida riesgo residual (GOB-03); monitoreo; define y aprueba métricas nuevas | S3, S12, S15 |
| Especialidades (MRM, Legal, Ciber, RNF, Terceros, Cumplimiento) | Evalúan en G2 con su metodología; semáforo por disciplina | S3 |
| Legal | Valida el listado literal de usos indebidos; confirma incumplimientos (LEG-01) | S5, S15 |
| Gerencia Owner + Gerencia de Riesgos | Aprueban con algún ámbar (con fecha de cierre) | S6 |
| Comité de Riesgo No Financiero Corp | Aprueba con rojo bajo el límite | S6 |
| CAR | Decide cuando una dimensión llega al límite | S5, S6 |
| Directorio | Informado cuando decide el CAR | S6 |
| Dueños de métricas | Heredadas (Ciber, RNF, Terceros) ratifican umbral; nuevas (AI Risk Officer, Legal, MRM) definen y aprueban | S12 |

---

## 6. Tabla maestra (base de la lógica de la herramienta)

| Ruta de atención | Criterio (triaje) | Etapas con gate | Días (d.h.) | Especialidades | Autonomía (G2→G3) | Controles |
|---|---|---|---|---|---|---|
| **STOP** | Ley IA = uso indebido | Se detiene en G1 | — | Legal valida | Ninguna: prohibido | — |
| **Ágil** | N5 (no material) | G1 → G2 → G3 | hasta 10, de G1 a G3 | [Por confirmar] cuáles intervienen | Autonomías vigentes RNF | Set mínimo, proporcional [Por confirmar] |
| **Ágil** | N4 (no material) | G1 → G2 → G3 | 10–15 | [Por confirmar] | Autonomías vigentes RNF | [Por confirmar] |
| **Estándar** | N3 (material) | G1 → G2 → G3 | 15–20 | MRM, Legal, Ciber, RNF, Terceros, Cumplimiento | Según semáforo: RNF / Gerencia / Comité RNF / CAR | [Por confirmar]; mide 19 métricas |
| **Estándar** | N2 (material) | G1 → G2 → G3 | 20–25 | Ídem | Ídem | [Por confirmar] |
| **Reforzada** | N1 (material) | G1 → G2 → G3 | 25–30 | Ídem | Ídem | Set máximo [Por confirmar] |

Pasos 1 (Registrar) y 5 (Monitorear) aplican a todas las rutas, sin días.

---

## 7. Ambigüedades y vacíos

**Críticas para construir la herramienta**
1. **No hay días por etapa.** El SLA es un total de G1 a G3, en rango (S3, S6). La hoja de ruta solo puede mostrar el total; el reparto G1/G2/G3 queda [Por confirmar]. Tampoco hay días para Registrar, Monitorear ni la reevaluación.
2. **Rangos que se tocan:** N4 10–15 y N3 15–20 (y así), comparten el día límite. La herramienta mostraría mínimo y máximo. Falta el calendario de feriados para días hábiles.
3. **Criterios de triaje cualitativos y en revisión** (S18: "en revisión"; S2: nuevo triaje en ~2 semanas). No son excluyentes: un chatbot con datos sensibles encaja en N2 y, si toma decisiones adversas, en N1. El cuestionario sería orientativo; la decisión final es del AI Risk Team.
4. **Ley IA "uso de riesgo alto":** la PPT no dice si fuerza un nivel o una ruta. El supuesto de la v18 (riesgo alto → Comité) no aparece en la v35.
5. **Controles no listados** en ninguna slide. El explorador mostraría dimensiones y métricas completas y los controles como [Por confirmar], salvo que me indiques otra fuente (p. ej., el correo "RV Riesgos IA (Apetito Evaluación y RACI)" en Inputs).
6. **Qué especialidades intervienen por ruta:** S3 nombra 6 en paralelo para todas; no dice si N4–N5 pasan por todas.

**Inconsistencias de texto**
7. **¿CAR al "exceder el apetito" o al "llegar al límite"?** S3 y S6 dicen "se excede el apetito"; S5 y S7 dicen "llega al límite". Con los umbrales de S8 no es lo mismo (ej. Ciber: excede el apetito en 3, llega al límite en 4). La lógica de S6/S7 usa el límite; asumiría eso.
8. **Quién hace el triaje:** "2.ª línea de riesgos" (S3) vs. "AI Risk Team" (S18).
9. **Terminología:** S8–S11 usan Apetito · Ámbar · Límite; S12 usa Apetito · Tolerancia · Límite. Asumiría ámbar = tolerancia.
10. **TER-01:** el anexo dice "amarillo 100% · rojo 95%" (S17) y la principal "verde 100%, ámbar 95–<100%, rojo <95%" (S11). Manda S11.
11. **OPS-02:** ámbar 99,0–99,5% y rojo ≤99,0% se solapan en 99,0% (S10).
12. **Métricas de portafolio vs. iniciativa:** CYB-01, CYB-03 y TER-01 son ratios de cartera, pero la dimensión cuenta iniciativas. No se explica cómo se atribuyen a una iniciativa.

**Umbrales sin valor cerrado**
13. Los umbrales propios de IA son preliminares y los heredados se ratifican (S8, S12). OPS-01: denominador [Por confirmar] y umbral solo de BCP (S16). TER-02: límite "inferido del gráfico" (S17). GOB-02: falta definir "brecha crítica" (S15).
14. **Alcance:** marco corporativo (S2), pero los umbrales heredados son de BCP. Inicialmente solo BCP.

---

## 8. Puntos a confirmar para la Fase 2
- **Plantilla base:** propongo `06_Reporte_HTML/raf_apetito_ia_bcp.html` (ya tiene simulador de rutas y la línea gráfica Credicorp). Alternativas: `apetito_riesgo_ia_bcp.html` o el reporte de 07.
- **Carpeta de salida:** propongo `08_Herramienta_Gobierno_IA/`, siguiendo la numeración del repo.
- **Controles:** ¿los dejo [Por confirmar] o uso otra fuente?
