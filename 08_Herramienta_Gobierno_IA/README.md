# Guía de ruta Gobierno IA

Guía interactiva para entender qué pasa con una iniciativa de IA según la **PPT Comité Gobierno IA v35**: qué ruta sigue, cuánto tarda, quién evalúa y quién decide. Es un solo archivo HTML que funciona sin servidor. No registra información ni envía datos.

**Todo el contenido sale de la PPT.** En pantalla no se muestran referencias a la PPT ni a sus slides; la slide de origen de cada dato queda registrada en el campo `fuente` del JSON.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `herramienta_gobierno_ia.html` | La guía. Se abre con doble clic en Chrome o Edge. |
| `data/config_gobierno_ia.json` | Los datos de la PPT: pasos, niveles, rutas, instancias, dimensiones, métricas, roles y anexos, cada uno con su slide (campo `fuente`). |
| `herramienta.src.html` + `logo.svg.html` | El código de la guía, sin datos. |
| `build_herramienta.py` | Une el código y el JSON y genera el HTML. |
| `informe_herramienta_gobierno_ia.md` | Enfoque, pruebas y pendientes. |

## Cómo se usa

1. **Guía de ruta**, la pantalla principal. Es el flujo de 5 pasos (S3) con los gates G1, G2 y G3 conectados.
   - Elige el escenario: si es un uso indebido según la Ley IA, el nivel del triaje (N1–N5) y el resultado de la evaluación. El flujo ilumina el camino: ruta de atención, reloj del SLA, especialidades, semáforo, instancia que decide, monitoreo y vuelta a la ruta.
   - **Reproducir** recorre el camino paso a paso con una explicación.
   - **Ver el ejemplo: chatbot de clientes** muestra el caso N2 con un rojo en MRM y otro en Ciberseguridad: se activa la ruta del apetito, cada rojo se mide contra el cupo de su dimensión y decide el CAR.
   - Si alguna métrica sale en rojo, la caja **Ruta del apetito** se enciende entre el semáforo y la instancia que decide.
   - Haz clic en cualquier caja para ver qué pasa, el resultado y quién lo hace.
2. **Rutas y cupo:** la ruta de atención por nivel, la ruta de autonomía y el simulador de cupo por dimensión (cuántos rojos faltan para llegar al límite y que decida el CAR), con un ejemplo.
3. **Marco:** la declaración, los 3 niveles de apetito, la pirámide, las dos rutas, los roles y lo que falta.
4. **Dimensiones:** las 6 dimensiones y las 19 métricas, con búsqueda y filtros. Cada métrica tiene un «Ver detalle» con su fórmula.
5. **Anexos:** taxonomía, niveles, sustento y fuentes.

## Cómo actualizar cuando cambie la PPT (v36, v37…)

1. Edita `data/config_gobierno_ia.json`:
   - `meta.version` y `meta.actualizado`.
   - `niveles`: ruta y días (`slaMin`, `slaMax`, `slaTexto`). En «hasta N días», usa `slaMin: null`.
   - `autonomia`: la instancia de cada resultado (`verde`, `ambar`, `rojo_bajo`, `rojo_limite`).
   - `dimensiones`: los umbrales en texto y en número (`apetitoMax`, `limite`) y sus `metricas`.
   - `pasos`, `roles`, `anexos`.
   - En cada dato, el campo `fuente` con el número de slide nuevo.
2. Ejecuta `python build_herramienta.py` para generar el HTML. El script valida los niveles y los rangos.

Un cambio de días, umbrales, instancias o textos solo requiere editar el JSON. Si la PPT agrega pasos o rutas nuevas, también hay que ajustar el flujo en `herramienta.src.html`: la lista `EDGES` y las columnas de `renderGuia`.
