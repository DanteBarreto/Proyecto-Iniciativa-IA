# Actividad 3. Revisión de los insumos de riesgo no financiero (RNF)

Corte: 20/11/2026. Fuente: carpeta `Inputs/` del repo (rama main). Uso interno, confidencial.

## 1. Conclusión

- **Con estos 4 archivos no se pueden armar los indicadores de riesgo que pidió Walter.** No traen evaluaciones RNF por iniciativa: falta el nivel por disciplina, la nota final, el criterio de agregación y la ruta de aprobación.
- **Sí sirven como marco:** la taxonomía de 11 categorías de riesgo IA, la escala de criticidad y el mapa de a quién pedir los datos en cada empresa.
- **El match con el playbook funciona, pero sobre una muestra mínima:** 12 de 13 iniciativas cruzan por Código limpio. 6 de esas 12 hoy están descartadas.
- **La pieza clave está en el correo:** en BCP ya existe una llave que vincula el código del playbook con el código de la iniciativa en la GRC (contacto: Rodrigo Díaz Beltrán). Esa extracción es la base RNF que necesitamos.
- **Ojo con el origen:** el correo indica que los 3 Excel los envió Percy Luna (Gobierno IA Corporativo) y que Walter te los reenvió hoy. No vienen de Jorge Rivera ni de una extracción de la GRC [Inferido del correo].

## 2. Qué contiene cada archivo

| Archivo | Qué es | Contenido clave | Uso para el apetito |
|---|---|---|---|
| **Base de Riesgos - v4.xlsx** | Catálogo referencial de riesgos y controles de IA (versión de enero 2026), hecho con las especialidades de riesgo y con apoyo de McKinsey. | 84 riesgos (50 de GenAI y 34 agénticos), 222 filas riesgo-control (153 controles únicos), **11 categorías**. Por riesgo: tipo (causa, evento o consecuencia), unidad especializada sugerida, **criticidad inherente referencial** (Crítico 86, Alto 100, Relevante 15, Moderado 21) y tecnología. | Taxonomía y escala. **No es una evaluación de iniciativas.** |
| **Riesgos por categoría IA.xlsx** | Ejercicio manual antiguo: riesgos y controles asociados a iniciativas concretas. Se discontinuó por falta de una GRC corporativa (según el correo). | **13 iniciativas, 124 riesgos.** 5 hojas por categoría IA: Chatbot/voicebot (5), Text Analysis (1), Knowledge Expert (1), Coding (5, todas Github Copilot) e Image/video (1). Criticidad: Alto 19, Relevante 69, Moderado 33, Bajo 3. Sin fecha [Por confirmar]. | Ejemplo de la granularidad deseada. **No sirve para indicadores** (muestra mínima y desactualizada). |
| **Directorio Riesgos Corporativo vf.xlsx** | Directorio del gobierno de riesgos IA. | Focals de riesgos y ciberseguridad por empresa y comité (estratégico, táctico, operativo); focals de **Modelos** (Jorge Rivera en BCP Perú; también Pacífico, Prima y Mibanco); consultores RNF de BCP por unidad (Q3); calendario de sincronizaciones. Tiene datos personales. | Sirve para saber **a quién pedir** las evaluaciones RNF de cada empresa. Sin datos de riesgo. |
| **Correo .msg** (Walter → Dante, 20/11; hilo del 6 al 20/11) | Hilo "Riesgos IA (Apetito, Evaluación y RACI) – Checkpoint Gobierno IA" (Gobierno IA, Riesgos IA y GGR). Adjunta los 3 Excel. | Ver la sección 3. | Contexto del proceso. |

## 3. Qué dice el correo sobre el proceso

1. **El apetito de riesgo IA aún no está definido.** Se armará una primera versión referencial con una muestra aleatoria de iniciativas de BCP y los campos mínimos que defina Riesgos IA (Alejandra Mendoza). Luciano Bedoya pidió involucrar a GGR.
2. **No hay GRC corporativa.** Cada empresa evalúa en su propio proceso. Solo **BCP tiene la llave playbook ↔ GRC**, que se activó con Rodrigo Díaz. Percy sugiere que Jorge Rivera tendría más detalle.
3. **Propuesta de Percy:** usar las 11 categorías como taxonomía de riesgos IA en todas las evaluaciones, para poder calcular el apetito. También propone evaluaciones proporcionales: más ligeras lejos del umbral y más profundas cerca de él.
4. **Hay una brecha de adopción:** el AI Risk Team se capacitó en estas herramientas, pero no hay trazabilidad de su uso.
5. **Taxonomía de IA (de las soluciones):** Alejandra la presentó el 06/11. Percy pide alinearla con la del inventario (canal: Eliane Rodríguez).
6. **Fecha:** el tema "Apetito, Evaluación de riesgos + RACI" va al **comité de Gobierno del 02/12**, la misma fecha de nuestra presentación.

## 4. ¿Alcanza para los indicadores de Walter?

| Indicador | ¿Se puede con estos insumos? | Qué falta |
|---|---|---|
| Cobertura de la evaluación RNF | **Parcial, solo con el playbook** (Status de evaluación de riesgos y TierAIRiskTeam; ver la Actividad 2). Estos archivos no agregan nada. | Lista de iniciativas evaluadas en la GRC, con fecha. |
| % con riesgo alto o medio por disciplina | **No.** No hay niveles por disciplina. Las "unidades especializadas" de la base (Ciberseguridad, Operativo, Cumplimiento, Legal) no cubren riesgo de modelo ni tecnología [Inferido]. | Nivel por disciplina y por iniciativa. |
| Distribución de la nota final | **No.** | Nota final por iniciativa. |
| Ruta de aprobación (comité RNF o gerente de área) | **No.** | Ruta o instancia de aprobación por iniciativa. |
| Criterio de agregación de la nota final | **No.** | Metodología RNF (Jorge Rivera o Metodología RNF de BCP). |
| Perfil por categoría de riesgo IA (11 categorías) | **Solo ilustrativo** con 13 iniciativas. | Que las evaluaciones usen las 11 categorías (hoy es una propuesta). |

**Escalas distintas:** la base usa Crítico/Alto/Relevante/Moderado y el archivo por iniciativa usa Alto/Relevante/Moderado/Bajo. Además, los nombres de las categorías no son idénticos entre archivos (por ejemplo, "Riesgos de terceros" frente a "Riesgo de terceros"). Hay que homologarlos antes de usarlos.

## 5. Match con el playbook (hoja IniciativasVistaActual)

Cruce por Código limpio (sin espacios ni saltos de línea), validado con el nombre y la categoría IA.

| Código RNF | Nombre en RNF | Nombre en el playbook | Fase en el playbook | Status de evaluación | ID | Resultado |
|---|---|---|---|---|---|---|
| BCP-0028 | Contigo emprendedor | Contigo emprendedor | Despliegue | Finalizado | 175 | Match |
| PRIM-0001 | Chatbot Prima AFP | Chatbot Prima | Descartado | Finalizado | 184 | Match |
| YAPE-0001 | Chatbot Yape | Chatbot de experiencia Yape | Despliegue | Finalizado | 192 | Match |
| BCP-0004 | Chatbot FEN | BOT IA FEN | Descartado | Finalizado | 202 | Match |
| BCP-0008 | Voicebot | VoiceBOT | Descartado | Finalizado | 194 | Match |
| BCP-0055 | Agile Monkey | Buscador IA ViaBCP | Despliegue | Finalizado | 137 | Match por código. El nombre difiere; Agile Monkey sería el proveedor [Inferido]. |
| BCP-0049 | Office 365 Copilot | M365 Copilot | Captura de valor | Finalizado | 148 | Match |
| BCP-0002 | Github Copilot | Github Copilot | Descartado | Finalizado | 190 | Match |
| BCP-0015 | Github Copilot | Github Copilot | Descartado | En proceso | 182 | Match |
| BCPB-0003 | Github Copilot | Github Copilot | Despliegue | Finalizado | 181 | Match |
| PSEG-0001 | Github Copilot | Github Copilot | Despliegue | Finalizado | 191 | Match |
| BCP-0054 | Aquají | Aquají | Descartado | No iniciado | 136 | Match. El playbook dice "No iniciado", pero RNF tiene riesgos identificados. |
| **CCAP-0002** | Github Copilot | — | — | — | — | **Sin match.** El código no existe en el playbook. El candidato es CCAP-0013 "Github Copilot" (On hold) [Por confirmar]. |

**Lectura:** el Código funciona como llave cuando se limpia, pero los nombres cambian entre fuentes. Para la base RNF real conviene cruzar por Código limpio, revisar el nombre y pedir que la extracción traiga el código del playbook (la llave que ya existe en BCP).

## 6. Próximos pasos sugeridos

1. **Pedir a Rodrigo Díaz y a Jorge Rivera** la extracción de la GRC de BCP con la llave del playbook: código, nivel por disciplina, nota final, criterio de agregación, ruta de aprobación y fecha.
2. **Para las demás empresas:** usar los focals del Directorio. Plan B: presentar BCP como piloto y explicitar la cobertura parcial.
3. **Confirmar con Walter** si los indicadores se reportan por disciplina (su pedido) o por las 11 categorías IA (propuesta de Percy), o por ambas.
4. **Coordinar con Alejandra Mendoza (Riesgos IA):** su apetito referencial va al mismo comité del 02/12. Conviene no presentar dos versiones distintas [Por confirmar con Walter].
