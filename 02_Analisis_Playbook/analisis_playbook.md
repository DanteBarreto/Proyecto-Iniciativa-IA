# Actividad 2: Análisis del playbook de iniciativas IA

> **Fuente:** `Inputs/Playbook Iniciativas IA (20.11.2026).xlsx` · **Hoja vigente:** IniciativasVistaActual · **Corte:** 20/11/2026
> **Soporte trazable:** [playbook_comparacion_estadisticas_indicadores.xlsx](playbook_comparacion_estadisticas_indicadores.xlsx). Cada cifra de este documento sale de una fórmula de ese Excel.
> **Convención:** [Inferido] = deducción nuestra · [Por confirmar] = validar con Lady/Percy Luna o Walter · [Propuesta] = sugerencia nuestra.

---

## 1. Resumen ejecutivo

- **Las 7 hojas son vistas de la misma lista SharePoint ("Inventario iniciativa").** En los registros y columnas comunes los valores son idénticos (0 diferencias celda a celda). Solo cambian las columnas que muestran y la hora de extracción. **IniciativasVistaActual es la correcta para los indicadores:** es una de las dos únicas hojas con la fase y el estado de cada iniciativa.
- **Credicorp tiene 1,004 iniciativas de IA registradas**, de las cuales **786 están en curso** (Activo). El 51% sigue en ideación y **121 están en go live**.
- **Las cifras de Walter cuadran con el playbook [Inferido]:** él estimó ~800 iniciativas y ~650 bien registradas; el playbook tiene 786 activas y 655 activas con el registro completo.
- **KRI más fuerte del playbook:** **52% de las iniciativas en go live (63 de 121) no tiene la evaluación de riesgos finalizada**, y en piloto la cifra sube a 83% (54 de 65). Hay que validarlo con la base RNF de Jorge Rivera, porque el campo del playbook puede estar desactualizado.
- **Incidencias de gobierno:** el 45% de las iniciativas (448) tiene al menos una brecha de registro. La más grande es la carga masiva de **Pacífico Salud (130 iniciativas, 17/11/2026) sin fecha de registro, tipo ni cantidad de usuarios**.
- **Campo de cruce con RNF: `Código`, pero hay que limpiarlo.** 489 códigos tienen saltos de línea, y 3 códigos los comparten iniciativas distintas. Se propone cruzar por código limpio y validar con el nombre o el `ID`.

---

## 2. Comparación entre hojas

| Hoja | Filas | Columnas | Diferencia frente a la vigente | Aporta |
|---|---:|---:|---|---|
| **IniciativasVistaActual** | **1,006** | **28** | — | **Fase (`EstadoRegistroValor`), `Estado`, Tier de riesgo, `ID`** |
| Todos los elementos | 1,006 | 44 | Mismos registros. No tiene `Creado` ni `ID`. | Nombre CR, focal de riesgos (Jorge Rivera figura en 103), campos de valor/costo (vacíos) |
| VistaCompleta | 1,011 | 50 | **+5 de Mibanco Colombia** (IA-004, 008, 009, 018, 019), creadas a las 11:00, después de extraer la vigente. **Sin fase ni estado.** | Metadatos de SharePoint (Modificado, etiquetas) |
| Vista SabIA | 1,011 | 11 | Igual que VistaCompleta en filas. Vista resumida. | Nada nuevo |
| Riesgos | 1,006 | 16 | Mismos registros. Sin fase ni estado. | Nombre y correo CR |
| Checkpoints Empresas | 1,005 | 18 | **Falta BCP-0708** (creado a las 10:51): es una extracción anterior. | CR, Solución |
| Fichas de Iniciativas | 1,005 | 13 | Falta BCP-0708. | Nada nuevo |

**Conclusión:** no hay versiones distintas de la información, solo cortes de tiempo distintos el mismo 20/11. Recomendación: pedir a Lady la vigente **con una hora de corte fija** e incluir Mibanco Colombia, que todavía no figura en ella [Por confirmar].

Detalle en las hojas `Comparacion_Hojas` y `Comparacion_Columnas` del Excel.

---

## 3. Estadísticas descriptivas (IniciativasVistaActual)

### 3.1 Universo (control "1+1=2")

| Concepto | N° |
|---|---:|
| Filas en la hoja | 1,006 |
| (−) Fila vacía (ID 1554) | 1 |
| (−) Registro duplicado (BCP-0685, mismo nombre, ID 1399 y 1400) | 1 |
| **= Iniciativas únicas** | **1,004** |

### 3.2 Por fase

| Grupo de fase | Fases del playbook | N° | % |
|---|---|---:|---:|
| Ideación | Ideación | 514 | 51.2% |
| Diseño / Desarrollo | Diseño (35), Desarrollo (53) | 88 | 8.8% |
| Piloto | Piloto | 65 | 6.5% |
| **Go live** [Inferido] | Despliegue (107), Captura de valor (14) | **121** | **12.1%** |
| On hold | On hold (Suspendido) | 71 | 7.1% |
| Cerrada | Descartado (117), Dada de baja (28) | 145 | 14.4% |
| **Total** | | **1,004** | 100% |

**En curso (Activo): 786 (78%)** · Suspendido: 70 · Inactivo: 148.

### 3.3 Por empresa

| Empresa | Total | Ideación | Diseño/Des. | Piloto | Go live | On hold | Cerrada |
|---|---:|---:|---:|---:|---:|---:|---:|
| BCP Perú | 621 | 391 | 41 | 28 | 48 | 18 | 95 |
| Pacífico Salud | 130 | 9 | 33 | 29 | 11 | 20 | 28 |
| Pacífico Seguros | 52 | 0 | 0 | 3 | 23 | 15 | 11 |
| Mibanco Perú | 48 | 34 | 3 | 0 | 6 | 5 | 0 |
| Prima AFP | 43 | 20 | 6 | 0 | 10 | 0 | 7 |
| Yape | 35 | 30 | 2 | 0 | 1 | 0 | 2 |
| Grupo Crédito | 29 | 19 | 1 | 2 | 3 | 2 | 2 |
| BCP Bolivia | 21 | 2 | 2 | 3 | 14 | 0 | 0 |
| Credicorp Capital | 17 | 2 | 0 | 0 | 4 | 11 | 0 |
| iO | 7 | 6 | 0 | 0 | 1 | 0 | 0 |
| Culqui | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **1,004** | **514** | **88** | **65** | **121** | **71** | **145** |

BCP Perú concentra el 62%. Mibanco Colombia no figura en la vigente.

### 3.4 Evaluación de riesgos

| Grupo de fase | Finalizado | En proceso | No iniciado | Vacío | Total |
|---|---:|---:|---:|---:|---:|
| Ideación | 12 | 2 | 51 | 449 | 514 |
| Diseño / Desarrollo | 23 | 9 | 29 | 27 | 88 |
| Piloto | 11 | 1 | 40 | 13 | 65 |
| **Go live** | **58** | 5 | 29 | 29 | **121** |
| On hold | 7 | 3 | 48 | 13 | 71 |
| Cerrada | 25 | 7 | 94 | 19 | 145 |
| **Total** | **136** | **27** | **291** | **550** | **1,004** |

- **El playbook cambió de formulario [Inferido].** Hasta 2025 se llenaba `Status de evaluación de riesgos`; desde 2026-T2 se llena `TierAIRiskTeam` (t1 a t5) con el tipo de consultor. Los dos campos nunca coinciden en un mismo registro. La cobertura de riesgo debe leer ambos.
- Tier asignado: 282 iniciativas, casi todas en ideación (t4 = 215; t1-t3 = 47). Significado de los tiers [Por confirmar].

### 3.5 Calidad del registro

- **Completitud por campo:** Empresa, Nombre, Fase y Estado al 100%; PO al 99%; Descripción al 96%; Tipo de usuarios al 82%; Categoría IA al 57%; Área al 69%; DominioNegocio al 12%.
- **`Criticidad de la Información` = "Bajo" en el 100%.** Parece un valor por defecto; no sirve como indicador [Inferido].
- Los campos de valor y costo (en Todos los elementos) están todos en "Pendiente" o en 0.

---

## 4. Incidencias de gobierno

"Debidamente registrada" se define, como propuesta, con **9 campos núcleo completos**: empresa, nombre, descripción, fase, nombre del PO, correo del PO, tipo de usuarios, cantidad de usuarios y fecha de registro [Por confirmar con Walter/Lady].

| Incidencia | Registros | Comentario |
|---|---:|---|
| Núcleo incompleto (no "debidamente registrada") | 185 | 130 son de la carga de Pacífico Salud |
| … de ellas, registro mínimo (≤ 6 de 9 campos, "solo nombre") | 141 | 130 de Pacífico Salud |
| Sin triage de riesgo (sin Status ni Tier) | 268 | |
| Sin fecha de registro | 130 | Toda la carga de Pacífico Salud del 17/11/2026 |
| Código con saltos de línea | 489 | Formato; se corrige con TRIM/CLEAN, pero rompe un cruce directo |
| Fase con salto de línea ("\nIdeación") | 23 | Se cuenta mal si no se limpia |
| Empresa fuera de catálogo ("YAPE" vs "Yape") | 18 | |
| **Código compartido por iniciativas distintas** | 6 (3 códigos) | BCPB-0016, CCAP-0001, CCAP-0003 |
| Registro duplicado | 2 (1 código) | BCP-0685 |
| Prefijo del código ≠ empresa | 3 | Culqui con código BCP; CDSB en BCP Bolivia [Por confirmar] |
| Estado incoherente con la fase | 3 | Ej.: Despliegue "Inactivo" |
| Fila vacía | 1 | ID 1554 |
| **Iniciativas con ≥ 1 incidencia** (sin contar el formato del código) | **448 (45%)** | Detalle por empresa en el Excel |

Coincidencia con Walter [Inferido]: él habló de ~200 "solo con nombre"; el playbook tiene 185 sin el registro completo.

---

## 5. Indicadores propuestos (primer alcance)

Todos están calculados en la hoja `Indicadores_Propuestos`, con numerador, denominador y fórmula visibles. **Los umbrales de apetito los define Walter [Por confirmar].**

### A. Gobierno del inventario (pedidos por Walter)

| ID | Indicador | Valor |
|---|---|---:|
| G1 | Iniciativas de IA registradas | **1,004** |
| G2 | % en curso (Activo) | 78.3% (786) |
| G3 | % debidamente registradas | 81.6% (819) |
| G3b | % de las activas debidamente registradas | 83.3% (655 / 786) |
| G4 | Registro mínimo ("solo nombre") | 14.0% (141) |
| G5 | % con ≥ 1 incidencia de gobierno | 44.6% (448) |
| G6 | En go live | 12.1% (121) |
| — | Distribución por fase y por empresa | Tablas 3.2 y 3.3 |

### B. Riesgo, con lo que ya tiene el playbook [Propuesta]

| ID | Indicador | Valor |
|---|---|---:|
| **R1** | **% en go live sin evaluación de riesgos finalizada** | **52.1% (63 / 121)** |
| R2 | % en piloto sin evaluación finalizada | 83.1% (54 / 65) |
| R3 | Con clientes externos, en piloto o go live, sin evaluación finalizada | 68.2% (15 / 22) |
| R4 | % de activas sin triage de riesgo | 29.9% (235 / 786) |
| R5 | % de activas con herramienta no estandarizada ("Ninguna - voy a usar algo más") | 7.9% (62 / 786) |
| R6 | % de activas sin actualizar su estado hace más de 180 días | 12.5% (98 / 786) |
| R7 | Tier t1-t3 sobre las que tienen tier | 16.7% (47 / 282) |

### C. Cruce con la evaluación RNF de Jorge Rivera

| ID | Indicador | Estado |
|---|---|---|
| X1 | % de iniciativas con evaluación RNF (cobertura) | Pendiente de la base RNF |
| X2+ | % con riesgo alto/medio por disciplina (legal, modelo, ciber, etc.), solo sobre las evaluadas | Pendiente |

**Campo de cruce recomendado:** `Código` limpio (columna AC de la hoja Base), validado con el nombre de la iniciativa. Como respaldo técnico, el `ID` de SharePoint, que sí es único. Hay que pedirle a Jorge Rivera que su base traiga el código del playbook. Además, R1 y R2 se deben recalcular con la base RNF, que es la fuente oficial de la evaluación.

---

## 6. Por confirmar

1. **Walter:** ¿aceptas la definición de "debidamente registrada" con los 9 campos núcleo, y "solo nombre" como 6 o menos?
2. **Walter:** ¿"go live" = Despliegue + Captura de valor?
3. **Walter:** umbrales de apetito para R1, R2, G3 y G5.
4. **Lady:** ¿qué significan los tiers t1 a t5? ¿El "Status de evaluación de riesgos" del playbook se sigue actualizando?
5. **Lady:** ¿la carga de Pacífico Salud del 17/11 se completará? ¿Mibanco Colombia entra en la vigente?
6. **Lady:** corregir los 3 códigos compartidos y el duplicado BCP-0685; confirmar el prefijo CDSB y el caso de Culqui.
7. **Jorge Rivera:** ¿su base RNF usa el código del playbook?
