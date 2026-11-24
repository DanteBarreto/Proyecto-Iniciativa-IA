# Actividad 6. Prototipos del reporte HTML de apetito de riesgo IA

Corte: 24/11/2026. Confidencial. **Usan datos de ejemplo** (120 iniciativas ficticias EJ-xxx de BCP): no representan la situación real.

## 1. Archivos

| Archivo | Formato | Uso recomendado |
|---|---|---|
| `apetito_riesgo_ia_bcp.html` | Híbrido: 7 diapositivas + anexo interactivo + metodología | Presentación guiada en sala a la alta dirección |
| `dashboard_apetito_ia_bcp.html` | Dashboard de una sola página con filtros | Exploración autónoma y seguimiento periódico |

Ambos son un solo archivo que se abre con doble clic en el navegador, sin servidor.

## 2. Contenido

- Los 6 KRI de Walter y 3 KCI de gobierno, con semáforo según los umbrales propuestos en `04_Calculo_Indicadores` (editables en el archivo).
- Mapa de calor de las 11 categorías de riesgo del catálogo vigente y su mapeo a las 6 dimensiones de apetito.
- Estilo: logo y paleta de grupocredicorp.com (magenta #E93CAC, tinta #202E44, turquesa #2AD2C9, crema #FAF7F3).

## 3. Cómo pasar a datos reales

1. Reemplazar la lista `iniciativas` del bloque `<script id="datos">` con la base GRC BCP a junio 2026 (campos en la pestaña Metodología del híbrido).
2. Poner `meta.esEjemplo = false` y actualizar `meta.corte`. Las marcas de "datos de ejemplo" desaparecen y los títulos se recalculan.

## 4. Supuestos

- Material = Tier 1 o 2 [Supuesto]. KRI 1 a 3 sobre materiales con evaluación finalizada, nivel residual.
- Las 3 categorías marcadas como "nueva" (confianza entre agentes, resiliencia y observabilidad, seguridad de los datos) serían las que no están en la base de junio [Supuesto; confirmar con Percy Luna].
