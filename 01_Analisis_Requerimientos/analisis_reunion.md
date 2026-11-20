# Análisis de la reunión de requerimientos: indicadores de IA para la alta dirección

> **Confidencial.** Uso interno del equipo de Control de Riesgo de Modelo.
> **Fuente:** grabación y transcripción de Teams del 20/11/2026 ("Radar de seguimiento de actividades Control Riesgo de Modelo", 20 min 36 s).
> **Preparado:** 20/11/2026 · **Estado:** borrador para revisión de Dante.

## Cómo leer este documento

- **Minutos.** `0:03`, `11:59`, `12:43`, etc. (sin símbolo) son las marcas exactas de Teams. `~5:21` es un minuto **estimado** por la posición del texto dentro de una intervención larga. Walter habla de 0:03 a 11:59 y de 12:43 a 19:16 sin más marcas. El margen es de ±1 minuto. Para fechar cada minuto con exactitud iba a transcribir el audio con Whisper local, pero la red del entorno bloquea la descarga del modelo (huggingface.co). Ver sección 0.
- **Etiquetas.** `[Explícito]` = se pidió en la reunión. `[Inferido]` = deducción mía a partir de lo dicho. `[Por confirmar]` = falta el dato. `[Recomendación]` = lo agrego yo y no se pidió.
- **Enfoque confirmado por Dante (20/11).** Nos guiamos por lo que pide Walter: **indicadores de apetito de riesgo de las iniciativas de IA de Credicorp**. No es un reporte de estado clásico con inversión, beneficios e hitos por iniciativa.

---

## 0. Inventario y calidad de las fuentes

| Archivo | Tipo | Lectura |
|---|---|---|
| `Grabaciones/Actividad para el reporte de iniciativas IA.mp4` | Video 1920×1080, 20:36, H.264 + AAC | Se lee. **No hay pantalla compartida**: solo se ven los avatares de 5 participantes (revisé fotogramas en 0:10, 3:00, 7:00, 11:40, 15:00 y 19:10). Todo el contenido está en el audio. |
| `Grabaciones/Actividad para el reporte de iniciativas IA_transcripción.docx` | Transcripción automática de Teams | Se lee completa (≈20.000 caracteres). |
| `Inputs/` | Carpeta vacía (`.gitkeep`) | Todavía no hay datos (playbook ni evaluaciones). |

**Limitación del contraste con la grabación.** Instalé faster-whisper con la aprobación de Dante, pero el entorno no deja descargar el modelo (huggingface.co está bloqueado por la política de red). Por eso no pude transcribir el audio de forma independiente. Las discrepancias de abajo salen de leer la transcripción y de los metadatos del video. `[Por confirmar]`: si se habilita el dominio (o se procesa en el equipo de Dante), repito el contraste y corrijo los minutos.

**Discrepancias y posibles errores de transcripción detectados:**

| Minuto | Texto en la transcripción | Lectura probable | Etiqueta |
|---|---|---|---|
| 0:03 | "Todo mundo y lo cual me va a llevar…" | La grabación empieza **con la conversación ya iniciada**: falta el contexto previo (posiblemente el planteamiento del pedido de la alta dirección). | [Inferido] |
| ~3:57 | "…hay 650 que están completamente registradas. 8 El resto de 200…" | "8" es ruido de transcripción. Además, 800 − 650 = 150, no 200: la cifra es una estimación de Walter ("creo"). | [Por confirmar] |
| ~4:55 | "en gol live" | *go live* (en producción) | [Inferido] |
| ~8:05 | "dice elder, no el equipo Elder" | Nombre de un equipo o persona de riesgo de modelo, poco claro | [Por confirmar] |
| 11:59 | "el Facebook de iniciativas" | "el playbook de iniciativas" | [Inferido] |
| ~11:32 | "los cicadores" | "los indicadores" | [Inferido] |
| ~15:09 | "en el radar de Birf también voy a mencionar" | "Birf" parece ser un equipo o área; no se identifica | [Por confirmar] |
| ~16:02 / ~16:19 | "Chat EPT", "Notebook LLM" | ChatGPT, NotebookLM | [Inferido] |
| ~17:42 | "es 2 de diciembre, maleados" | Palabra ininteligible | [Por confirmar] |
| ~19:00 | "Eso viene del periodo directorio" | "Eso viene del **pedido** del directorio" | [Inferido] |
| 19:16 | "Era coroval." (Dante) | Ininteligible; posiblemente un asentimiento | [Por confirmar] |
| 20:25 | "Jesus." | "Yes." | [Inferido] |
| 20:25–20:36 | La grabación termina mientras Rafael habla del score MRM | Corte al final; ese tema queda fuera del alcance | — |

---

## 1. Resumen ejecutivo

- **Walter Paiva Ramos pide, con urgencia, calcular indicadores de apetito de riesgo** sobre "cómo está el grupo en inteligencia artificial", para presentarlos a la alta dirección el **2 de diciembre** (0:26, ~0:48, ~17:42). El pedido "viene del directorio" (~19:00). [Explícito]
- **Estrategia "del final hacia adelante":** primero asegurar un entregable con números y después iterar (umbrales, stakeholders, responsabilidades). En el peor caso, se presentan los indicadores más el estado de las coordinaciones (~0:59–~1:46). [Explícito]
- **Dos fuentes de datos:** (1) el **playbook** completo de iniciativas de IA de **todo Credicorp** a la fecha, vía Lady y Percy Luna o su aplicativo, y (2) las **evaluaciones de riesgo no financiero** por disciplina, vía **Jorge Rivera** (~3:49, ~6:02–~6:25, ~18:14). [Explícito]
- **Los indicadores de riesgo se calculan solo sobre las iniciativas que ya tienen evaluación de riesgo no financiero.** Por ejemplo, el % con riesgo de modelo alto o el % con riesgo legal alto o medio. El inventario completo sirve para los indicadores de gobierno: registro, estados (~10:01–~10:49). [Explícito]
- **No se inventa metodología.** Se usa la evaluación de riesgo no financiero que ya existe. Lo único nuevo son los indicadores de Walter (12:43–~13:48). [Explícito]
- **El formato debe ser "pomposo" pero trazable:** cálculos ordenados en Excel y luego quizás un HTML interactivo "modo calculadora". El aspecto visual es crítico ante los altos directivos (~2:48, ~13:56–~14:47). [Explícito]
- **Equipo:** Dante al 100%, con apoyo de David en el cálculo. Rafael y Rubén cubren el *running* de riesgo de modelo y las labores de Dante. Walter coordina y escala si alguien no colabora (~2:00–~2:32, ~17:25, ~18:35–~19:00). [Explícito]

## 2. Participantes y roles

| Persona | Presente | Rol en este requerimiento | Evidencia |
|---|---|---|---|
| **Walter Paiva Ramos** | Sí | **Solicitante y decisor.** Define los indicadores, umbrales, roles y responsabilidades; lleva las coordinaciones y presenta a la alta dirección. Jefe del equipo [Inferido]. | 0:03–11:59, 12:43–19:16, 19:17 |
| **Dante Barreto** | Sí | **Responsable de la ejecución (100%).** Levanta la información, ordena los datos y produce los cálculos y el entregable. | ~2:00, ~17:25, ~18:00 |
| **David Caruzo** | Sí (no habla) | **Apoyo de cálculo** para Dante; calcula indicadores conforme llega la data. | ~2:00, ~2:16, 19:17 |
| **Rafael Alvarado Trujillo** | Sí | Cubre el *running* de riesgo de modelo y labores de Dante. Reporta el avance del score MRM. | ~2:16, ~17:25, 20:07 |
| **Rubén Erazo Cachique** | Sí | Ídem. Dedicado al score MRM de Mibanco ("mi banco Perú" [Inferido]), riesgo de crédito. | ~2:16, ~17:25, 20:07 |
| **Jorge Rivera** | No | **Fuente de información.** Riesgo no financiero: iniciativas evaluadas, detalle por disciplina y nota final agregada. | ~6:02, ~8:47, 12:22, ~18:35 |
| **Percy Luna** | No | **Fuente de información.** Responsable del playbook. | ~6:25 |
| **Lady** (apellido no mencionado) | No | **Fuente de información.** Encargada del playbook en el equipo de Percy Luna. | ~6:25, ~18:14 |
| **GGR** | No | "Dueño del apetito" de riesgo. Es una sigla [Por confirmar], posiblemente una gerencia de riesgos [Inferido]. | ~12:51 |
| **César Ríos** | No | Recibió una propuesta alternativa de evaluación. No tiene rol directo en este pedido. | ~13:18 |
| **Alta dirección / Directorio** | No | **Audiencia.** El pedido "viene del directorio" [Inferido por la corrección "periodo" → "pedido"]. | 0:26, ~1:34, ~14:47, ~19:00 |
| "Birf" | No | Walter les pedirá apoyar las tareas que Dante deja. | ~15:09, ~17:25 |

## 3. Objetivo del reporte

**Mensaje que se busca transmitir** (~1:34, Walter): *"Así estamos en inteligencia artificial. Esto es lo que hemos encontrado. Tengo estos umbrales, tengo estas coordinaciones, estamos en esta situación y al menos los indicadores más críticos vamos a mitigarlos de esta manera."* [Explícito]

En concreto:
1. Mostrar con números la situación de las iniciativas de IA del grupo Credicorp: inventario, calidad del registro, estados y perfil de riesgo. [Explícito]
2. Presentar indicadores de apetito de riesgo de IA, con umbrales preliminares. Walter los compara con el "tablero del score MRM, pero con la mirada de IA y con muchos más equipos" (~4:22). [Explícito]
3. Mostrar el avance de las coordinaciones y roles, aunque estén "al 50%" (~1:11). [Explícito]
4. Proponer cómo mitigar los indicadores más críticos (~1:34). [Explícito]
5. **Decisión que se busca de los directores:** no se dijo. Por el contexto, sería validar el enfoque de indicadores y umbrales y respaldar el plan de mitigación y de cobertura [Inferido] [Por confirmar].

## 4. Requerimientos detallados

Prioridad: **Alta** = condiciona el entregable del 2/12. **Media** = mejora el entregable. **Baja** = deseable.

| ID | Requerimiento | Tipo | Prioridad | Solicitado por | Minuto | Criterio de aceptación |
|---|---|---|---|---|---|---|
| R01 | Alcance de empresas: **todo Credicorp**, no solo BCP. | Contenido (alcance) | Alta (explícita) | Walter | ~18:14 | La base y los indicadores incluyen todas las empresas del grupo que figuran en el playbook, con un campo "empresa". |
| R02 | Alcance de iniciativas: **todas las iniciativas de IA del playbook**, en sus distintos estados. | Contenido (alcance) | Alta (explícita) | Walter | ~3:49 | Inventario completo extraído, con conteo total y por estado. |
| R03 | Periodo: foto **a la fecha** ("a fecha hoy"). | Dato (corte) | Alta (explícita) | Walter | ~3:49 | Fecha de corte documentada en la base y en el reporte. Fecha exacta [Por confirmar]. |
| R04 | Extraer el **playbook completo** desde Lady y Percy Luna o el aplicativo ya compartido. | Dato (fuente) | Alta (explícita) | Walter | ~6:25, ~18:14 | Archivo del playbook en `Inputs/`, con su fuente y fecha de extracción. |
| R05 | Obtener de **Jorge Rivera** las iniciativas con **evaluación de riesgo no financiero (RNF)**, con el detalle por disciplina (legal, ciberseguridad, ética, riesgo de modelo, tecnología, etc.) y la **nota final**. | Dato (fuente) | Alta (explícita) | Walter | ~6:02, ~6:54–~9:08 | Base por iniciativa con el nivel de riesgo (bajo/medio/alto) de cada disciplina y la nota agregada, cruzable con el playbook. |
| R06 | Indicadores de **registro y gobierno del playbook**: total registradas, debidamente registradas vs. solo con nombre, y por estado (ideación, piloto, *go live*, etc.). Las brechas se reportan como "incidencias de gobierno". | Contenido (KPI) | Alta (explícita) | Walter | ~3:57–~4:55 | Tabla de conteos y % con su definición de "debidamente registrada" documentada. La definición está [Por confirmar]. |
| R07 | Indicador de **cobertura de la evaluación RNF**: cuántas iniciativas ya tienen evaluación de riesgo no financiero. | Contenido (KPI) | Alta (explícita) | Walter | ~5:21, ~9:28–~9:56 | Conteo y % sobre el universo y sobre las debidamente registradas. |
| R08 | **Indicadores de riesgo por disciplina**, calculados **solo** sobre las iniciativas con evaluación RNF. Ejemplos: % con riesgo de modelo alto; % con riesgo legal alto o medio. | Contenido (KPI) | Alta (explícita) | Walter | ~10:11–~10:27 | Indicadores calculados con el numerador, el denominador y el filtro trazables. |
| R09 | Calcular los **indicadores que Walter "tiene en la cabeza"**. Él los entregará cuando haya data. | Contenido (KPI) | Alta (explícita) | Walter | ~0:11, 19:17 | Lista de indicadores recibida y cada uno calculado. Lista [Por confirmar]. |
| R10 | **Umbrales** por indicador (qué % es bueno o malo). Los define y calibra Walter después de ver los números. | Contenido (KPI) | Media (explícita: va después) | Walter | ~11:14–~11:32 | Cada indicador tiene un umbral preliminar marcado como "en calibración". |
| R11 | Distribución de la **nota final RNF** y de las rutas de aprobación: riesgo medio → comité de riesgo no financiero; riesgo bajo → gerente de área. | Contenido | Media (inferida) | Walter | ~9:08–~9:28 | Conteo de iniciativas por nota final y por ruta de aprobación. [Inferido]: se explicó como mecánica; no se pidió como indicador. |
| R12 | Conocer el **criterio de agregación** que usa Jorge Rivera para la nota final. | Dato (metodología) | Media (explícita: "sería bueno conocerla") | Walter | ~8:47 | Criterio documentado en una página. |
| R13 | **No crear una metodología nueva** de evaluación de riesgo: usar la evaluación RNF existente. | Estilo / restricción | Alta (explícita) | Walter | 12:43–~13:48 | El reporte cita la evaluación RNF como fuente y no la redefine. |
| R14 | **Trazabilidad**: datos "bien ordenaditos" y cálculos donde se vea "1 + 1 = 2". | Formato | Alta (explícita) | Walter | ~13:56–~14:25 | Cada cifra del reporte se rastrea hasta una fila de la base. Hay un diccionario de datos y fórmulas visibles. |
| R15 | **Formato "calculadora" vistoso**: Excel primero y luego quizás un **aplicativo o HTML interactivo**. No basta "una hoja a mano". | Formato | Alta (explícita) | Walter | ~2:48–~3:24, ~13:56, ~14:25 | Excel con los cálculos más una versión visual interactiva. Que el HTML sea obligatorio está [Por confirmar]. |
| R16 | **Presentación con impacto visual** ante altos directivos: que "se vea grande", con esfuerzo y coordinación visibles, y nada "bulky". | Estilo | Alta (explícita) | Walter | ~3:24, ~14:47 | La revisión de Walter aprueba el aspecto visual. |
| R17 | Mostrar el **estado de las coordinaciones y los roles y responsabilidades**, aunque estén parciales. | Contenido | Media (explícita) | Walter | ~1:11, 19:17 | Sección con las coordinaciones, su % de avance y el mapa de roles. Los insumos los da Walter. |
| R18 | **Plan de mitigación** para los indicadores más críticos. | Contenido | Media (explícita) | Walter | ~1:34 | Cada indicador "en rojo" tiene una acción y un responsable propuestos. |
| R19 | **Entregable mínimo asegurado** antes del 2/12: primero los números, luego las iteraciones. | Plazo | Alta (explícita) | Walter | ~0:26–~1:46 | Una versión 1 con los indicadores calculados existe antes de iterar umbrales. |
| R20 | Información del playbook y de RNF levantada **hoy (20/11)**, "rapidísimo". | Plazo | Alta (explícita) | Walter | ~11:32, ~18:00–~18:14 | Pedido enviado a Lady, Percy Luna y Jorge Rivera el 20/11. |
| R21 | Anticipar la objeción de **cobertura parcial** ("estás sacando el apetito con 200 cuando tienes 1000"). Respuesta: se irán adecuando y sirven para calibrar umbrales. | Contenido / mensaje | Media (explícita) | Walter | ~10:49 | El reporte explicita el universo, el subconjunto evaluado y el % de cobertura. |
| — | **No se pidió**: inversión, beneficios, responsables por iniciativa, próximos hitos por iniciativa ni avance por iniciativa. | — | — | — | — | Quedan fuera salvo que Walter lo pida [Por confirmar]. |
| RR1 | [Recomendación] Cortes de los indicadores por **empresa** del grupo y por **estado**. | Contenido | Media | Propuesta | — | Tablas cruzadas empresa × indicador. |
| RR2 | [Recomendación] Embudo **universo → debidamente registradas → con evaluación RNF → riesgo medio/alto**. | Formato | Media | Propuesta | — | Una sola visual que resume la cobertura y el riesgo. |
| RR3 | [Recomendación] Ficha técnica de cada indicador: definición, fórmula, fuente, corte y umbral. | Formato | Alta | Propuesta | — | Una ficha por indicador en el Excel. |
| RR4 | [Recomendación] Control de calidad del cruce playbook ↔ RNF: identificador común e iniciativas que no cruzan. | Dato | Alta | Propuesta | — | Reporte de *matching* con el % de cruce. |

## 5. Decisiones tomadas

| # | Decisión | Quién | Minuto |
|---|---|---|---|
| D1 | Estrategia "del final hacia adelante": primero los indicadores calculados, luego afinar umbrales, stakeholders y responsabilidades. | Walter | ~0:26–~1:46 |
| D2 | Dante se dedica al 100% (y "full time hoy") a levantar la información, con apoyo de David. | Walter | ~2:00, ~17:25, ~18:00 |
| D3 | Rafael y Rubén asumen el *running* de riesgo de modelo y las labores de Dante (validación de riesgo financiero y control). | Walter | ~2:16–~2:32, ~17:25 |
| D4 | El alcance es todo Credicorp, no solo BCP. | Walter | ~18:14 |
| D5 | Los indicadores de riesgo se calculan solo sobre las iniciativas con evaluación RNF, no sobre todo el universo. | Walter | ~10:27 |
| D6 | Se usa la evaluación RNF existente de Jorge Rivera; no se inventa metodología. | Walter | 12:43–~13:48 |
| D7 | Formato de cálculos en Excel, con posible paso a HTML interactivo ("modo calculadora"). | Walter | ~13:56–~14:25 |
| D8 | Walter escribirá a Jorge Rivera para que dé facilidades, y escalará si alguien no colabora. | Walter | ~18:35–~19:00 |
| D9 | Dante tiene libertad para contactar directamente a Lady (playbook). | Walter | ~18:14 |

## 6. Próximas actividades (action items)

| # | Actividad | Responsable | Fecha compromiso | Dependencias | Minuto |
|---|---|---|---|---|---|
| A1 | Extraer el playbook completo de iniciativas de IA de todo Credicorp, a la fecha (de Lady o Percy Luna, o del aplicativo ya compartido). | Dante | Hoy, 20/11 | Disponibilidad de Lady o acceso al aplicativo | ~3:49, ~18:14 |
| A2 | Solicitar a Jorge Rivera las iniciativas con evaluación RNF, con el detalle por disciplina y la nota final. | Dante | Hoy, 20/11 | A3 (aviso de Walter) | ~6:02, ~18:00 |
| A3 | Escribir a Jorge Rivera para avisarle que Dante lo contactará y pedirle facilidades. | Walter | Hoy, 20/11 ("ahora") | — | ~18:35 |
| A4 | Armar los flujos y los roles y responsabilidades. | Walter | Hoy, 20/11 | — | 19:17 |
| A5 | Entregar a Dante la lista de indicadores a calcular. | Walter | Al recibir la data [Por confirmar] | A1, A2 | 19:17 |
| A6 | Calcular los indicadores conforme llega la información. | David (con Dante) | [Por confirmar] | A1, A2, A5 | 19:17 |
| A7 | Calcular los indicadores de registro y de cobertura RNF con los datos levantados. | Dante | [Por confirmar] | A1, A2 | ~4:55, ~9:28 |
| A8 | Averiguar el criterio de agregación de la nota final RNF. | Dante [Inferido] | [Por confirmar] | A2 | ~8:47 |
| A9 | Cubrir el *running* de riesgo de modelo y las labores de Dante. | Rafael, Rubén | Desde hoy | — | ~2:16, ~17:25 |
| A10 | Pedir a "Birf" que apoye en las tareas que Dante deja, y mencionar el tema en su radar y en el de pricing. | Walter | [Por confirmar] | — | ~15:09, ~17:25 |
| A11 | Avisar a Walter de inmediato si alguien no colabora con la información. | Dante | Continuo | — | ~19:00 |
| A12 | Con los números: hablar con los stakeholders, afinar umbrales y asignar responsabilidades. | Walter | Antes del 2/12 [Inferido] | A6 | ~0:59, ~18:14 |
| A13 | Presentar los indicadores a la alta dirección. | Walter | 2/12/2026 | A12 | 0:26, ~17:42 |

## 7. Fechas e hitos mencionados

| Fecha | Hito | Minuto | Nota |
|---|---|---|---|
| **20/11/2026 (vie)** | Reunión. Inicio del levantamiento de playbook y RNF "hoy". Walter avisa a Jorge Rivera y arma flujos y roles. | ~18:00–19:17 | Explícito |
| "Una semana" | Plazo de trabajo antes de la presentación; Walter debe "hablar con todo el mundo" la semana siguiente. | ~17:42–~18:14 | Entre el 20/11 y el 2/12 hay 12 días corridos (8 hábiles). Qué hito marca "una semana" está [Por confirmar]. |
| **02/12/2026 (mié)** | Presentación a la alta dirección. | 0:26, ~17:42 | Hora, formato de la sesión y tiempo asignado [Por confirmar] |
| Sin fecha | Entregas parciales o revisiones intermedias. | — | No se definieron [Por confirmar] |
| Sin fecha | "Fecha próxima" del score MRM (otro tema). | 19:42 | Fuera de alcance |

## 8. Riesgos, restricciones y sensibilidades

**Riesgos del entregable**
- **Plazo muy corto** (8 días hábiles) y dependencia de terceros: Lady, Percy Luna y Jorge Rivera (~17:42). Mitigación: el escalamiento con Walter (~19:00) y la estrategia del entregable mínimo (D1).
- **Calidad y completitud del playbook:** Walter estima unas 800 iniciativas, de las cuales unas 650 están bien registradas y unas 200 solo con nombre (~3:57). Las cifras no cuadran (800 − 650 = 150), así que la definición de "debidamente registrada" es crítica [Por confirmar].
- **Cruce playbook ↔ RNF:** no se sabe si hay un identificador común [Por confirmar]. Si falla el cruce, falla el indicador de cobertura.
- **Cobertura parcial** de los indicadores de riesgo: se calculan solo sobre las evaluadas, por ejemplo 200 de 1000 (~10:49). Es esperable que un director lo cuestione.
- **Umbrales sin calibrar:** los porcentajes (1%, 2%, 3%, 10%) se dijeron como ejemplo, no como dato (~11:14). No deben presentarse como definitivos.
- **Lista de indicadores no entregada:** está "en la cabeza" de Walter. Mientras no llegue, la ruta crítica depende de él.

**Restricciones**
- Usar solo información y metodologías existentes, sin inventar (12:43, ~15:45).
- Las cifras dichas en la reunión (800, 650, 200, 1000, 500, 10%) son **estimaciones o ejemplos de Walter, no datos**. No se reportan sin validar con las fuentes.

**Sensibilidades políticas (cuidar o evitar ante los directores)**
- **No proponer cambios a la metodología RNF de Jorge Rivera** ni competir con ella. El antecedente de "la mexicana", cuya propuesta alternativa fue rechazada por Walter, Percy Luna y GGR y llevada a César Ríos, muestra que es un tema sensible (12:22–~13:48). **No mencionar este episodio en el reporte.**
- **Encuadrar las brechas del playbook como "incidencias de gobierno", no como fallas de personas o equipos** (~4:22). El equipo de Percy Luna es fuente y aliado [Recomendación].
- **El "adorno" no puede restar trazabilidad:** la forma vistosa debe apoyarse en datos verificables (~14:19).
- **Excluir los comentarios internos ajenos al tema:** la cobertura y los temas de pricing (~15:09), la aprobación "a regañadientes" vinculada a Carlos Ramírez (~15:25) y el método personal de uso de IA de Walter (~16:02–~16:57).
- **Confidencialidad:** la grabación, la transcripción y los datos del playbook y de RNF no se envían a servicios externos.

## 9. Ambigüedades y preguntas abiertas (listas para enviar a Walter)

> Walter, para asegurar el entregable del 2/12 te agradeceré confirmar lo siguiente:

1. **Lista de indicadores:** ¿nos puedes compartir la lista de indicadores que tienes pensados (aunque sea preliminar), para preparar la estructura del cálculo mientras llega la data?
2. **Audiencia y sesión del 2/12:** ¿la presentación es ante el Directorio o ante un comité de alta dirección? ¿Cuánto tiempo tendremos y quién presenta?
3. **Decisión esperada:** ¿qué esperas que decidan o aprueben los directores (por ejemplo, el marco de indicadores, los umbrales o el plan de mitigación)?
4. **Formato final:** ¿el entregable es el Excel más un HTML interactivo, o también se necesita una presentación (PPT)? ¿El HTML es obligatorio para el 2/12 o es deseable?
5. **Revisiones intermedias:** ¿en qué fechas quieres revisar avances antes del 2/12? Proponemos el 24/11 (data), el 26/11 (indicadores v1) y el 30/11 (versión final).
6. **Definición de "debidamente registrada":** ¿qué campos mínimos del playbook debe tener una iniciativa para considerarla bien registrada?
7. **Fecha de corte:** ¿usamos como corte la fecha de extracción (20/11 o 23/11)?
8. **Alcance de empresas:** ¿confirmas que entran todas las empresas de Credicorp que figuren en el playbook? ¿Hay alguna que deba excluirse o mostrarse por separado?
9. **Estados del playbook:** ¿los indicadores de estado deben usar las categorías del playbook tal cual (ideación, piloto, *go live*, etc.) o prefieres agruparlas?
10. **Disciplinas RNF:** además de legal, ciberseguridad, ética, riesgo de modelo y tecnología, ¿hay otras disciplinas que deban reportarse por separado?
11. **Umbrales:** ¿muestro los indicadores sin semáforo hasta que definas los umbrales, o propongo umbrales preliminares para que los ajustes?
12. **Coordinaciones y roles:** ¿la sección de coordinaciones y de roles y responsabilidades la armas tú (los flujos de hoy) y nosotros solo la diagramamos?
13. **Plan de mitigación:** ¿el plan para los indicadores críticos lo defines tú, o propongo un borrador con los responsables de cada disciplina?
14. **"Birf":** ¿a qué equipo te refieres? ¿Debemos coordinar algo con ellos para este reporte?
15. **Contacto del playbook:** ¿me confirmas el nombre completo de Lady, y si el aplicativo que te compartimos antes es la fuente oficial?

> Para Jorge Rivera (tras el aviso de Walter):

16. ¿Nos puedes compartir la base de iniciativas con evaluación de riesgo no financiero, con el nivel de riesgo por disciplina y la nota final, y con el identificador de la iniciativa en el playbook?
17. ¿Cuál es el criterio para agregar las evaluaciones de las disciplinas en la nota final?
18. ¿Qué nota final lleva a comité de riesgo no financiero y cuál la aprueba el gerente de área?

---

## 10. Propuesta preliminar (paso 3, sin desarrollar)

### 10.1 Estructura tentativa del reporte

| # | Sección | Contenido | Requerimientos |
|---|---|---|---|
| 1 | **Mensaje clave** | "Así estamos en IA": 3 o 4 cifras, el semáforo y la acción principal. | R19, Objetivo |
| 2 | **Alcance y fuentes** | Empresas, fecha de corte, fuentes (playbook, RNF) y embudo de cobertura. | R01–R05, R21, RR2 |
| 3 | **Situación del inventario** | Total de iniciativas, calidad del registro, distribución por estado y por empresa; incidencias de gobierno. | R06, RR1 |
| 4 | **Cobertura de la evaluación RNF** | Cuántas se evaluaron, % de cobertura y distribución de la nota final y de la ruta de aprobación. | R07, R11 |
| 5 | **Perfil de riesgo por disciplina** | Indicadores por disciplina (modelo, legal, ciberseguridad, ética, tecnología…) sobre las evaluadas. | R08, R09 |
| 6 | **Tablero de indicadores de apetito de riesgo** | Indicadores con umbral preliminar (semáforo "en calibración"). | R09, R10 |
| 7 | **Coordinaciones, roles y responsabilidades** | Estado de las coordinaciones (% de avance) y mapa de roles. | R17 |
| 8 | **Indicadores críticos y mitigación** | Acción, responsable y fecha por indicador crítico. | R18 |
| 9 | **Próximos pasos** | Calibración de umbrales, ampliación de la cobertura y frecuencia de seguimiento. | R10, R21 |
| A | **Anexo "calculadora"** | Excel/HTML interactivo con la base, las fórmulas, la ficha de cada indicador y el diccionario de datos. | R14, R15, RR3 |

### 10.2 Plan de trabajo (propuesta) [Inferido: el cronograma no se definió en la reunión]

| Etapa | Fechas | Entregable | Responsable | Depende de |
|---|---|---|---|---|
| E0. Pedido de información | Vie 20/11 | Correos o chats a Lady, Percy Luna y Jorge Rivera; preguntas a Walter | Dante (y aviso de Walter) | — |
| E1. Recepción y limpieza de datos | 20/11 – Lun 23/11 | Base del playbook y base RNF en `Inputs/`, más el diccionario de datos | Dante | E0, respuesta de las fuentes |
| E2. Cruce y calidad | Lun 23/11 – Mar 24/11 | Base consolidada (playbook ↔ RNF) con el reporte de calidad y de *matching* | Dante | E1 |
| E3. Indicadores v1 | Mar 24/11 – Mié 25/11 | Excel "calculadora" v1: registro, cobertura e indicadores por disciplina | Dante y David | E2, lista de Walter (A5) |
| **Revisión 1** | Jue 26/11 | Revisión de los números con Walter | Walter | E3 |
| E4. Umbrales y coordinaciones | Jue 26/11 – Vie 27/11 | Umbrales preliminares, mapa de roles y mitigación | Walter (Dante da soporte) | Revisión 1 |
| E5. Versión visual | Vie 27/11 – Lun 30/11 | HTML interactivo y/o presentación | Dante y David | E3, E4 |
| **Revisión 2** | Lun 30/11 | Versión casi final | Walter | E5 |
| E6. Ajustes y ensayo | Mar 01/12 | Versión final congelada | Equipo | Revisión 2 |
| **Presentación** | **Mié 02/12** | Presentación a la alta dirección | Walter | E6 |

**Ruta crítica:** recepción de la base RNF (Jorge Rivera) → cruce con el playbook → lista de indicadores de Walter → indicadores v1 → umbrales → versión visual → presentación. El riesgo principal está en E1 y A5. Si la base RNF no llega a más tardar el 24/11, el plan B es presentar los indicadores del playbook más el estado de las coordinaciones, como prevé D1.

### 10.3 Información a recolectar

| Información | Detalle mínimo | A quién | Uso |
|---|---|---|---|
| Playbook completo de IA (Credicorp) | ID, nombre, empresa, unidad, estado, fecha de registro, responsable y campos de completitud | Lady / Percy Luna (o el aplicativo) | R02, R06 |
| Definición de estados del playbook y de los campos obligatorios | Catálogo de estados y reglas de registro | Lady / Percy Luna | R06 |
| Base de evaluaciones RNF | ID de la iniciativa (cruce con el playbook), riesgo por disciplina, nota final, fecha de evaluación y ruta de aprobación | Jorge Rivera | R05, R07, R08, R11 |
| Criterio de agregación RNF | Regla para obtener la nota final | Jorge Rivera | R12 |
| Lista de indicadores y umbrales | Nombre, fórmula y umbral tentativo | Walter | R09, R10 |
| Flujos, coordinaciones y roles | Estado de avance de cada coordinación | Walter | R17 |
| Formato y logística del 2/12 | Audiencia, tiempo y formato | Walter | R15, R16 |
| [Recomendación] Referencia del tablero del score MRM | Estructura visual por reutilizar | Rafael / Rubén | R15, R16 |
