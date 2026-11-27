# Esquema de controles de apetito por dimensión (27/11/2026)

**Regla:** las métricas de apetito son controles de la evaluación de riesgos, dentro de las 6 dimensiones. Cada control tiene un semáforo. Si algún control de apetito está en rojo, la iniciativa pasa por la ruta del apetito.

**Archivo:** `esquema_controles_apetito_ia_bcp.xlsx`, con 11 hojas vinculadas por fórmulas y un ejemplo de 2 iniciativas.

## Flujo
Playbook 20.11 + Reporte iniciativas IA → BD_Iniciativas, BD_Evaluaciones, BD_Riesgos, BD_Planes → BD_Controles → Tablon_General y Apetito. Los umbrales y las rutas salen de la PPT v35 (hoja Parametros).

## Resultado del ejemplo
- **BCP-0312:** 2 controles de apetito en rojo, GOB-03 (riesgo residual Crítico) y GOB-02 (proxy: plan de un riesgo Crítico vencido). Entra a la ruta del apetito y decide el Comité RNF.
- **BCP-0086:** sin rojos y con 16 controles sin dato.

## Lo que falta (detalle en la hoja Faltantes)
- La base no trae el resultado de cada control ni la marca de qué control es métrica de apetito.
- Solo 3 de los 19 controles salen de la base.
- Faltan el nivel N1–N5 y la llave ID IA en Detalle controles.

## Supuestos por validar
- Mapeo de la taxonomía RNF a cada dimensión.
- "Relevante" cuenta como verde en GOB-03.
- Equivalencia Tier t1–t5 → N1–N5.
