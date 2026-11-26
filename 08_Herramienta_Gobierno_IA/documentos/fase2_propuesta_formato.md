# Herramienta de Gobierno IA · Fase 2: evaluación del formato y propuesta de diseño

**Base validada (Fase 1):** PPT Comité Gobierno IA v35 · plantilla `06_Reporte_HTML/raf_apetito_ia_bcp.html` · salida en `08_Herramienta_Gobierno_IA/` · controles mostrados como en la PPT (pirámide y set proporcional por nivel, sin catálogo).

---

## 1. La plantilla actual, vista como herramienta de gestión

`raf_apetito_ia_bcp.html` tiene tres vistas: **Presentación** (11 slides narradas), **Explorar el RAF** (tablero editable de iniciativas de ejemplo) y **Catálogo y fuentes**.

| Funciona (se conserva) | No funciona para gestión (se cambia) |
|---|---|
| Línea gráfica Credicorp (tinta #202E44, magenta #E93CAC, turquesa #2AD2C9, crema; Inter Tight + Libre Baskerville) y semáforos con ícono | Está pensada para **contar** el marco, no para **gestionar una iniciativa**: el usuario no puede registrar la suya |
| Un solo HTML autocontenido, sin servidor; datos en un bloque `<script id="datos">` | El simulador de rutas vive dentro de una slide; no da fechas, responsables ni ficha |
| Simulador de rutas (Ley IA, N1–N5, semáforo) y tablero que recalcula al instante | Datos de la v18 (N1/N2 de indicadores, otra nomenclatura); no cita la slide de origen |
| Tarjetas de dimensión con barra apetito · ámbar · límite | Nada se guarda: al recargar se pierde lo editado |
| Responsive básico (un breakpoint) | Accesibilidad parcial (18 atributos ARIA); no hay versión imprimible |

**Conclusión:** se reutiliza el estilo, los componentes visuales (tarjetas, semáforos, barras de umbral) y el patrón de datos separados. Cambia la estructura: de "presentación con anexo" a "herramienta con consulta".

---

## 2. Alternativas de formato

| Criterio | A. Mixto actual (slides + interactivo) | B. App de una página con pestañas | C. Asistente paso a paso + panel de consulta |
|---|---|---|---|
| Facilidad de uso | Media: hay que recorrer slides para llegar a lo útil | Alta para quien ya sabe qué busca | **Alta**: guía al usuario nuevo y deja consultar libremente |
| Claridad para no expertos | Alta para entender, baja para actuar | Media: 6 pestañas sin orden de uso | **Alta**: el orden de pasos replica el flujo G1→G3 |
| Interactividad | Baja-media | Alta | **Alta**, con resultado encadenado (la ruta alimenta plazos, especialidades y ficha) |
| Mantenibilidad v36, v37… | Baja: texto de slides mezclado con datos | Alta si los datos van en JSON | **Alta**: misma separación datos/lógica que B |
| Coherencia gráfica | Total | Total (mismo estilo) | Total (mismo estilo) |
| Riesgo | Se sigue leyendo como documento | El usuario no sabe por dónde empezar | Algo más de trabajo de construcción |

## 3. Recomendación: **C, asistente + panel de consulta, en una sola página**

- El usuario típico llega con una pregunta concreta ("¿qué ruta me toca y cuánto tarda?"). El asistente la contesta en 4 pasos y produce la ficha.
- El equipo de gobierno necesita consultar el marco sin pasar por el asistente: el panel de consulta da acceso directo a Marco y flujo, Dimensiones y Anexos.
- Los pasos del asistente siguen el orden de la PPT (Clasificar G1 → Evaluar G2 → Decidir G3), así que la herramienta también enseña el proceso.
- Toma lo bueno de B: todo en un HTML, con navegación por pestañas y los datos en JSON.

### Wireframes

**Pantalla 0 · Inicio**
```
┌──────────────────────────────────────────────────────────────────────┐
│ CREDICORP | Gobierno IA · v35          [Mi iniciativa] [Consultar ▾]  │
├──────────────────────────────────────────────────────────────────────┤
│ Gestiona tu iniciativa de IA: ruta, plazos, responsables y controles │
│  6 dimensiones · 19 métricas · 2 rutas · 1 ciclo de vida   (S1)      │
│ ┌───────────────────────┐  ┌───────────────────────┐                 │
│ │ ▶ Empezar mi iniciativa│  │ ⧉ Abrir una guardada   │                │
│ └───────────────────────┘  └───────────────────────┘                 │
│ Cinco pasos: Registrar → Clasificar G1 → Evaluar G2 → Decidir G3 →   │
│ Monitorear (S3)                    Datos preliminares, en revisión   │
└──────────────────────────────────────────────────────────────────────┘
```

**Asistente · barra fija de pasos**
```
 ① Datos  ─  ② ¿Qué ruta me toca?  ─  ③ Hoja de ruta  ─  ④ Especialidades  ─  ⑤ Ficha
```

**Paso 1 · Datos de la iniciativa**
```
 Código de iniciativa [_______]  Nombre [______________]
 Sistema IA [Chatbot/Voicebot ▾]  Tipo de IA [IA Generativa ▾]   (S14)
 Área / Gerencia owner [_______]  Fecha de inicio G1 [dd/mm/aaaa]
```

**Paso 2 · ¿Qué ruta me toca?**
```
 1. ¿Es un uso indebido según la Ley IA? (ver ejemplos S5)   (•) No ( ) Sí → STOP
 2. Clasificación Ley IA: ( ) Aceptable ( ) Riesgo alto      ⓘ efecto [Por confirmar]
 3. Marca lo que describe tu iniciativa (S18):
    [ ] Afectación financiera directa material, derechos, decisiones adversas… → N1
    [ ] Interacción directa con cliente, info financiera, datos sensibles…   → N2
    [ ] Proceso interno con impacto indirecto en clientes o resultados       → N3
    [ ] Automatización interna sin decisión material                          → N4
    [ ] Productividad personal, asistencia no vinculante                      → N5
 ┌ RESULTADO ─────────────────────────────────────────────────────────┐
 │ N2 · MATERIAL · Ruta ESTÁNDAR · 20–25 días hábiles (S6, S18)        │
 │ Por qué: marcaste "interacción directa con cliente". Cuenta para el │
 │ apetito. Orientativo: el nivel oficial lo asigna el AI Risk Team (G1)│
 └─────────────────────────────────────────────────────────────────────┘
 ▸ Simular quién aprobará (G2): semáforo por disciplina + rojos actuales
   por dimensión → instancia (RNF / Gerencia / Comité RNF / CAR) (S6, S7)
```

**Paso 3 · Hoja de ruta**
```
 Inicio G1: 01/12/2026      Ruta Estándar · 20–25 d.h. (S6)
 ●───────────────●──────────────────●─────────────○
 G1 Clasificar   G2 Evaluar         G3 Decidir     Monitorear (mensual)
 01/12           [Por confirmar]    29/12 – 05/01
 Plazo total G1→G3: 20 a 25 días hábiles · fecha estimada de decisión: 29/12/2026 – 05/01/2027
 ⓘ La PPT fija solo el total; el reparto por etapa está [Por confirmar].
 Feriados considerados: [lista editable]
```

**Paso 4 · Especialidades y responsables**
```
 Etapa        Especialidad / instancia          Responsable        Fecha
 G1 Clasificar 2.ª línea de riesgos · AI Risk Team [__________]   [__/__]
 G2 Evaluar    MRM                                [__________]   [__/__]
               Legal · Ciber · RNF · Terceros · Cumplimiento (S3)  …
 G3 Decidir    Comité de Riesgo No Financiero Corp (según simulación) …
 Monitorear    1.ª y 2.ª línea · AI Risk Officer  [__________]
```

**Paso 5 · Ficha de la iniciativa (imprimible)**
```
 FICHA · INI-XXX Chatbot de clientes          [🖨 Imprimir/PDF] [⬇ Excel] [⬇ Guardar]
 Ruta: Estándar (N2, material) · SLA 20–25 d.h. · G3 estimado 29/12–05/01
 Instancia probable: Comité RNF Corp (simulada)
 Responsables por etapa (tabla) · Métricas que le aplican: 19 de 6 dimensiones
 Controles: set proporcional a N2, con RACI por disciplina (S4) [Detalle por confirmar]
 Pendientes: criterios de triaje en revisión, umbrales preliminares (S2, S8)
```

**Panel de consulta · Explorador de dimensiones**
```
 Buscar [alucinación______]  Dimensión [Todas ▾]  Origen [Todos ▾]  Color [▾]
 ┌ RAF-IA-06 Riesgo de modelo · Nuevo · Apetito ≤2 · Ámbar 3 · Límite ≥4 (S8)
 │  MRM-01 Alucinaciones financieras  ■<0,25%  ■0,25–<0,50%  ■≥0,50%  (S11)
 │  ▸ Ver detalle: numerador, denominador, cómo se cuenta (S17)
 │  ▸ Por qué importa · sustento (S21)
 └ Controles: set por disciplina, proporcional a N1–N5 (S4)
```

**Panel de consulta · Marco RAF y flujo**
```
 Declaración (S4) · Tres niveles: PROHIBIDO | SIN APETITO | CON CONDICIONES (S5)
 Pirámide: Dimensión → Métrica → Control (S4)
 Flujo 5 pasos con responsable y entregable (S3)
 Matriz de rutas: atención (N1–N5) × autonomía (semáforo) (S6) · Ejemplo S7
 ▸ Ver detalle: taxonomía (S14), niveles N1–N5 (S18), sustento y fuentes (S19–S22)
```

---

## 4. Módulos (ajustados a lo que trae la v35)

| Módulo | Qué hace | Ajuste por la PPT |
|---|---|---|
| ¿Qué ruta me toca? | Cuestionario Ley IA + criterios S18 → nivel, ruta, SLA y el porqué | Si se marcan criterios de varios niveles, **manda el más exigente** (regla de la herramienta, a validar). Resultado orientativo |
| Simulador de autonomía | Semáforo por disciplina + rojos actuales por dimensión → instancia | Lógica S6/S7: CAR cuando la dimensión llega al límite |
| Hoja de ruta | Fecha de inicio → rango de fecha de G3 en días hábiles | Solo total G1→G3; etapas sin días = [Por confirmar] |
| Especialidades | Áreas por etapa con campos de responsable y fecha | Las 6 especialidades de G2 (S3); por ruta = [Por confirmar] |
| Explorador de dimensiones | 6 dimensiones → 19 métricas → umbrales → controles, con búsqueda y filtros | Controles como en S4, sin catálogo |
| Marco RAF y flujo | Declaración, 3 niveles, pirámide, flujo, matriz de rutas, ejemplo S7 | Anexos en "Ver detalle" |
| Ficha exportable | Ruta, plazos, responsables, instancia, controles y pendientes | PDF por impresión; Excel como .csv |

Cada dato lleva su fuente (Sn) en un tooltip, y todo [Por confirmar] se ve con una etiqueta ámbar.

---

## 5. Persistencia de datos

| Opción | Cómo funciona | Limitaciones |
|---|---|---|
| **1. Navegador (localStorage)** | Autoguarda las iniciativas en el equipo del usuario | Solo en ese navegador y PC; se pierde si se borran los datos; no se comparte |
| **2. Exportar / importar archivo** | Botón "Guardar" baja un `.json` por iniciativa (y `.csv` para Excel); "Abrir" lo carga | Manual; versiones sueltas si varios editan el mismo archivo |
| **3. Repositorio compartido** (SharePoint/Teams, lista o carpeta) | Todos ven las mismas asignaciones | Requiere servidor o integración con M365 y permisos de TI; deja de ser un HTML autónomo |

**Recomendación:** 1 + 2 ahora (autoguardado y archivo para compartir por correo o carpeta del equipo). La opción 3 queda como siguiente etapa si la herramienta se adopta. Sin servicios externos: nada sale del equipo del usuario.

**Datos del marco (configuración):** van en un bloque JSON documentado dentro del HTML, porque un HTML abierto desde el disco no puede leer un `.json` aparte. Además se entrega `data/config_gobierno_ia.json` como copia de referencia, y un botón "Cargar configuración" permite aplicar una versión nueva (v36…) sin tocar el código.

---

## 6. Decisiones que necesito para construir
1. **Formato:** ¿apruebas la opción C?
2. **Criterios mixtos en el cuestionario:** ¿manda el nivel más exigente? (recomendado; es conservador).
3. **Feriados:** ¿dejo la lista vacía y editable, o cargo los feriados nacionales de Perú 2026–2027?
