# -*- coding: utf-8 -*-
"""Esquema Excel: controles de apetito por dimension (ejemplo 2 iniciativas)."""
import sys, re, datetime as dt
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import FormulaRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter as L

REPO = sys.argv[1]
OUT = sys.argv[2]
IDS = ["BCP-0312", "BCP-0086"]

rep = pd.read_excel(f"{REPO}/Inputs/Reporte iniciativas IA.xlsx", sheet_name=None)
pb = pd.read_excel(f"{REPO}/Inputs/Playbook Iniciativas IA (20.11.2026).xlsx", sheet_name="IniciativasVistaActual")
pb["cod"] = pb["Código"].astype(str).str.replace(r"\s+", "", regex=True)

# ---------------- estilos ----------------
F = "Arial"
NAVY = "1F3864"; BLUE = "2E75B6"; LIGHT = "DDEBF7"; GREY = "F2F2F2"
def font(**k): return Font(name=F, size=k.pop("size", 9), **k)
HFILL = PatternFill("solid", fgColor=NAVY)
SFILL = PatternFill("solid", fgColor=BLUE)
LFILL = PatternFill("solid", fgColor=LIGHT)
GFILL = PatternFill("solid", fgColor=GREY)
INFILL = PatternFill("solid", fgColor="FFF2CC")
thin = Side(style="thin", color="BFBFBF")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
SEM = {"Verde": "C6EFCE", "Ámbar": "FFEB9C", "Rojo": "FFC7CE", "Sin dato": "E7E6E6"}
SEMF = {"Verde": "006100", "Ámbar": "9C5700", "Rojo": "9C0006", "Sin dato": "595959"}

wb = Workbook()
def sheet(name, tab=None):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    if tab: ws.sheet_properties.tabColor = tab
    return ws

def title(ws, text, sub=None):
    ws["A1"] = text; ws["A1"].font = font(size=14, bold=True, color=NAVY)
    if sub: ws["A2"] = sub; ws["A2"].font = font(size=9, italic=True, color="595959")

def header(ws, row, col, names, fill=HFILL, height=30):
    for i, n in enumerate(names):
        c = ws.cell(row=row, column=col + i, value=n)
        c.font = font(bold=True, color="FFFFFF"); c.fill = fill; c.alignment = CENTER; c.border = BOX
    ws.row_dimensions[row].height = height

def put(ws, r, c, v, fmt=None, inp=False, bold=False, wrap=False, color=None, align=None):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = font(bold=bold, color=("0000FF" if inp else (color or "000000")))
    cell.border = BOX
    if inp: cell.fill = INFILL
    if fmt: cell.number_format = fmt
    cell.alignment = align or (WRAP if wrap else Alignment(vertical="top"))
    return cell

def widths(ws, ws_w):
    for i, w in enumerate(ws_w, 1): ws.column_dimensions[L(i)].width = w

def sem_cf(ws, rng):
    first = rng.split(":")[0].replace("$", "")
    for k in ["Rojo", "Ámbar", "Verde", "Sin dato"]:
        ws.conditional_formatting.add(rng, FormulaRule(
            formula=[f'LEFT({first},{len(k)})="{k}"'],
            fill=PatternFill("solid", fgColor=SEM[k]), font=Font(name=F, color=SEMF[k], bold=True)))

def src_row(ws, row, col, labels):
    for i, s in enumerate(labels):
        c = ws.cell(row=row, column=col + i, value=s)
        c.font = font(size=8, italic=True, color="595959"); c.alignment = CENTER; c.fill = GFILL; c.border = BOX

def clean(v):
    if v is None or (isinstance(v, float) and pd.isna(v)) or v is pd.NaT: return None
    if isinstance(v, str):
        v = v.replace("_x000D_", "").replace("&amp;", "&").strip()
        return v or None
    if isinstance(v, pd.Timestamp): return v.to_pydatetime()
    return v

def todate(v):
    v = clean(v)
    if isinstance(v, str):
        try: return dt.datetime.strptime(v, "%d/%m/%Y")
        except ValueError: return v
    return v

# =====================================================================
# Parametros
# =====================================================================
P = sheet("Parametros", "7F7F7F")
title(P, "Parámetros del esquema", "Fuente: PPT Comité Gobierno IA v35 (S5, S6, S8–S11, S15–S18). Celdas amarillas = editables.")
put(P, 4, 1, "Fecha de corte", bold=True)
put(P, 4, 2, dt.datetime(2026, 11, 25), fmt="dd/mm/yyyy", inp=True)
put(P, 4, 3, "Corte de la base Reporte iniciativas IA (recibida el 25/11/2026). Usada para planes vencidos.", wrap=True)
P.merge_cells("C4:H4")

DIMS = [
    ("RAF-IA-01", "Gobierno de riesgos IA", "Shadow IA, brechas críticas, residual alto/crítico, cambios sin reevaluación", "Nuevo", 0, "1–2", 3, 4, "AI Risk Officer"),
    ("RAF-IA-02", "Legal / Ley IA", "Incumplimientos confirmados y obligaciones de riesgo alto sin evidencia", "Nuevo", 0, "1", 2, 2, "Legal"),
    ("RAF-IA-03", "Ciber / Privacidad", "Vulnerabilidades, incidentes vector IA, obsolescencia, datos personales", "Heredado + 1 nuevo", 2, "3", 4, 4, "Ciberseguridad (Cyber Risk)"),
    ("RAF-IA-04", "Operativo y Resiliencia", "Pérdidas/provisiones IA y disponibilidad", "Heredado", 2, "3", 4, 2, "RNF"),
    ("RAF-IA-05", "Terceros", "Proveedores alto riesgo evaluados y con planes, concentración", "Heredado + 1 nuevo", 2, "3–5", 6, 3, "Terceros"),
    ("RAF-IA-06", "Riesgo de modelo", "Alucinaciones, toxicidad, robustez, deterioro", "Nuevo", 2, "3", 4, 4, "MRM"),
]
r0 = 7
put(P, r0 - 1, 1, "1. Dimensiones y umbrales de cupo (S8)", bold=True, color=NAVY)
header(P, r0, 1, ["Orden", "Código", "Dimensión", "Qué vigila", "Origen", "Apetito (hasta)", "Ámbar", "Límite (desde)", "N.º controles de apetito", "Dueño (S12)", "Casos en rojo fuera de este archivo"])
DIM_ROW = {}
for i, d in enumerate(DIMS):
    r = r0 + 1 + i; DIM_ROW[d[0]] = r
    put(P, r, 1, i + 1); put(P, r, 2, d[0], bold=True); put(P, r, 3, d[1]); put(P, r, 4, d[2], wrap=True)
    put(P, r, 5, d[3]); put(P, r, 6, d[4]); put(P, r, 7, d[5]); put(P, r, 8, d[6])
    put(P, r, 9, f'=COUNTIF($B$18:$B$36,B{r})'); put(P, r, 10, d[8]); put(P, r, 11, 0, inp=True)
DR1, DR2 = r0 + 1, r0 + 6   # 8..13
put(P, 14, 1, "Casos en rojo fuera de este archivo: n.º de iniciativas materiales en producción con rojo en la dimensión (cartera completa). Hoy 0 porque el ejemplo solo tiene 2 iniciativas [Por completar].", wrap=True, color="595959")
P.merge_cells("A14:K14"); P.row_dimensions[14].height = 24

# Métricas = controles de apetito
MET = [
    # code, dim, nombre, origen, verde, ambar, rojo, sentido, a_desde, r_desde, unidad, como_hoy
    ("GOB-01", "RAF-IA-01", "IA en uso sin registro, dueño o aprobación (Shadow IA)", "Propio IA", "0", "—", "≥1", "Menor es mejor", None, 1, "n.º", "Parcial: registro y PO del Playbook; falta aprobación"),
    ("GOB-02", "RAF-IA-01", "Brechas críticas abiertas", "Propio IA", "0 abiertas", "≥1 en plazo", "≥1 vencida", "Categórico", None, None, "estado", "Proxy: planes de riesgos Alto/Crítico (Detalle planes)"),
    ("GOB-03", "RAF-IA-01", "Riesgo residual alto o crítico", "Propio IA", "Bajo/medio", "Alto", "Crítico", "Categórico", None, None, "estado", "Calculado: peor riesgo residual (Detalle riesgos)"),
    ("GOB-04", "RAF-IA-01", "Cambios materiales sin reevaluación", "Propio IA", "0", "—", "≥1", "Menor es mejor", None, 1, "n.º", "Sin dato: no hay registro de cambios"),
    ("LEG-01", "RAF-IA-02", "Incumplimiento legal confirmado", "Propio IA", "0", "—", "≥1", "Menor es mejor", None, 1, "n.º", "Sin dato: lo confirma Legal"),
    ("LEG-02", "RAF-IA-02", "Obligaciones de riesgo alto sin evidencia", "Propio IA", "Cumple todas", "—", "Falta ≥1", "Menor es mejor", None, 1, "n.º", "Sin dato: no hay checklist de obligaciones"),
    ("CYB-01", "RAF-IA-03", "Vulnerabilidades AC >30 d por activo IA", "Heredado (vig. 20)", "<2%", "2–<5%", "≥5%", "Menor es mejor", 0.02, 0.05, "%", "Sin dato: no hay inventario de activos IA"),
    ("CYB-02", "RAF-IA-03", "Incidentes significativos con vector IA", "Heredado (vig. 21)", "0", "—", "≥1", "Menor es mejor", None, 1, "n.º", "Sin dato: base de incidentes sin etiqueta IA"),
    ("CYB-03", "RAF-IA-03", "Componentes IA obsoletos", "Heredado (vig. 19)", "<5%", "5–<10%", "≥10%", "Menor es mejor", 0.05, 0.10, "%", "Sin dato"),
    ("CYB-04", "RAF-IA-03", "Datos personales sin base legal ni evaluación de privacidad", "Propio IA", "Con respaldo", "En trámite con plan", "Sin respaldo", "Categórico", None, None, "estado", "Sin dato"),
    ("OPS-01", "RAF-IA-04", "Pérdidas operativas por eventos IA", "Heredado (vig. 16)", "<1,1%", "1,1–<1,3%", "≥1,3%", "Menor es mejor", 0.011, 0.013, "%", "Sin dato: eventos sin etiqueta IA; denominador por confirmar"),
    ("OPS-02", "RAF-IA-04", "Disponibilidad de servicios IA críticos", "Heredado (vig. 17)", ">99,5%", "99,0–99,5%", "≤99,0%", "Mayor es mejor", 0.995, 0.99, "%", "Sin dato"),
    ("TER-01", "RAF-IA-05", "Proveedores IA alto riesgo evaluados en 12 m", "Heredado (vig. 22)", "100%", "95–<100%", "<95%", "Mayor es mejor", 1.0, 0.95, "%", "Sin dato: no hay proveedor por iniciativa"),
    ("TER-02", "RAF-IA-05", "Proveedores IA con riesgos AC sin plan", "Heredado (vig. 22)", "0", "—", "≥1", "Menor es mejor", None, 1, "n.º", "Sin dato"),
    ("TER-03", "RAF-IA-05", "Concentración en un proveedor o modelo", "Propio IA", "≤2", "3–5", "≥6", "Menor es mejor", 3, 6, "n.º", "Sin dato"),
    ("MRM-01", "RAF-IA-06", "Alucinaciones financieras materiales", "Propio IA", "<0,25%", "0,25–<0,50%", "≥0,50%", "Menor es mejor", 0.0025, 0.005, "%", "Sin dato: resultados de pruebas MRM"),
    ("MRM-02", "RAF-IA-06", "Respuestas tóxicas", "Propio IA", "<0,20%", "0,20–<0,50%", "≥0,50%", "Menor es mejor", 0.002, 0.005, "%", "Sin dato"),
    ("MRM-03", "RAF-IA-06", "Fallas ante pruebas adversariales", "Propio IA", "<1,0%", "1,0–<2,0%", "≥2,0%", "Menor es mejor", 0.01, 0.02, "%", "Sin dato"),
    ("MRM-04", "RAF-IA-06", "Deterioro del desempeño vs. validación", "Propio IA", "<10%", "10–<15%", "≥15%", "Menor es mejor", 0.10, 0.15, "%", "Sin dato"),
]
put(P, 16, 1, "2. Controles de apetito = 19 métricas (S9–S11, S15–S17). Un rojo envía la iniciativa a la ruta del apetito.", bold=True, color=NAVY)
header(P, 17, 1, ["Código", "Cód. dimensión", "Dimensión", "Control de apetito (métrica)", "Origen", "Verde", "Ámbar", "Rojo",
                  "Regla de cálculo", "Ámbar desde", "Rojo desde", "Unidad", "Cómo se obtiene hoy", "Dueño"])
MET_ROW = {}
for i, m in enumerate(MET):
    r = 18 + i; MET_ROW[m[0]] = r
    put(P, r, 1, m[0], bold=True); put(P, r, 2, m[1])
    put(P, r, 3, f'=INDEX($C${DR1}:$C${DR2},MATCH(B{r},$B${DR1}:$B${DR2},0))')
    put(P, r, 4, m[2], wrap=True); put(P, r, 5, m[3]); put(P, r, 6, m[4]); put(P, r, 7, m[5]); put(P, r, 8, m[6])
    put(P, r, 9, m[7])
    fmt = "0.00%" if m[10] == "%" else "0"
    put(P, r, 10, m[8], fmt=fmt); put(P, r, 11, m[9], fmt=fmt); put(P, r, 12, m[10]); put(P, r, 13, m[11], wrap=True)
    put(P, r, 14, f'=INDEX($J${DR1}:$J${DR2},MATCH(B{r},$B${DR1}:$B${DR2},0))')
M1, M2 = 18, 36
put(P, 37, 1, "Regla: Menor es mejor → Rojo si valor ≥ 'Rojo desde'; Ámbar si ≥ 'Ámbar desde'. Mayor es mejor → Rojo si valor < 'Rojo desde'; Ámbar si < 'Ámbar desde'. Categórico → la especialidad registra Verde/Ámbar/Rojo. OPS-02 y TER-01: límites exactos por confirmar (S10, S17).", wrap=True, color="595959")
P.merge_cells("A37:N37"); P.row_dimensions[37].height = 26

TAX = [("Ciberseguridad", "RAF-IA-03"), ("Seguridad de Información (excluye Ciberseguridad)", "RAF-IA-03"),
       ("Modelo", "RAF-IA-06"), ("Legal", "RAF-IA-02"), ("Cumplimiento", "RAF-IA-02"),
       ("Procesamiento y ejecución de operaciones", "RAF-IA-04"), ("Tecnología", "RAF-IA-04"),
       ("Continuidad del negocio", "RAF-IA-04"), ("Fraude externo", "RAF-IA-04"), ("Fraude interno", "RAF-IA-04"), ("Laboral", "RAF-IA-04")]
put(P, 39, 1, "3. Taxonomía RNF → dimensión (ubica los controles de la evaluación). Propuesta por validar.", bold=True, color=NAVY)
header(P, 40, 1, ["Taxonomía (Detalle riesgos)", "Cód. dimensión", "Dimensión", "Estado"])
for i, (t, d) in enumerate(TAX):
    r = 41 + i
    put(P, r, 1, t); put(P, r, 2, d, inp=True)
    put(P, r, 3, f'=INDEX($C${DR1}:$C${DR2},MATCH(B{r},$B${DR1}:$B${DR2},0))'); put(P, r, 4, "Propuesta [Por confirmar]")
T1, T2 = 41, 51
put(P, 52, 1, "Gobierno de riesgos IA y Terceros no tienen taxonomía RNF equivalente: hoy solo reciben controles de apetito.", color="595959")
P.merge_cells("A52:D52")

RES = [("Bajo", "Verde", 1), ("Moderado", "Verde", 2), ("Relevante", "Verde", 3), ("Alto", "Ámbar", 4), ("Crítico", "Rojo", 5)]
put(P, 54, 1, "4. Riesgo residual → semáforo GOB-03 (S15: bajo/medio verde, alto ámbar, crítico rojo)", bold=True, color=NAVY)
header(P, 55, 1, ["Riesgo residual", "Semáforo GOB-03", "Orden", "Nota"])
for i, (a, b, o) in enumerate(RES):
    r = 56 + i
    put(P, r, 1, a); put(P, r, 2, b, inp=True); put(P, r, 3, o)
    put(P, r, 4, "Relevante no está en la PPT: se asume Verde [Por confirmar]" if a == "Relevante" else "")
R1, R2 = 56, 60

put(P, 62, 1, "5. Tier AIR Team (Playbook) → Nivel de triaje", bold=True, color=NAVY)
header(P, 63, 1, ["TierAIRiskTeam", "Nivel", "Nota"])
for i in range(5):
    r = 64 + i
    put(P, r, 1, f"t{i+1}"); put(P, r, 2, f"N{i+1}", inp=True); put(P, r, 3, "Equivalencia [Por confirmar]")
TI1, TI2 = 64, 68

NIV = [("N1", "Material", "Sí", "Reforzada", "25–30", "Agente que ejecuta pagos y transferencias"),
       ("N2", "Material", "Sí", "Estándar", "20–25", "Chatbot de consultas de clientes"),
       ("N3", "Material", "Sí", "Estándar", "15–20", "Resumen automático de reclamos"),
       ("N4", "No material", "No", "Ágil", "10–15", "Clasificador de tickets internos"),
       ("N5", "No material", "No", "Ágil", "hasta 10", "Asistente de redacción de correos"),
       ("Sin triaje", "Por confirmar", "Por confirmar", "Por confirmar", "Por confirmar", "Sin Tier en el Playbook")]
put(P, 70, 1, "6. Ruta de atención por nivel (S6, S18)", bold=True, color=NAVY)
header(P, 71, 1, ["Nivel", "Materialidad", "¿Cuenta para el apetito?", "Ruta de atención", "SLA G1→G3 (d.h.)", "Ejemplo (S18)"])
for i, n in enumerate(NIV):
    r = 72 + i
    for j, v in enumerate(n): put(P, r, 1 + j, v)
NV1, NV2 = 72, 77

AUT = [("Todo verde", "Autonomías vigentes de RNF", "Sin instancias nuevas del RAF"),
       ("Algún ámbar, ningún rojo", "Gerencia Owner + Gerencia de Riesgos + opinión AI Risk Team", "El ámbar lleva fecha de cierre"),
       ("Rojo y la dimensión queda bajo el límite", "Comité de Riesgo No Financiero Corp", "+ AI Risk Team y condiciones"),
       ("Rojo y la dimensión llega al límite", "CAR", "Se excede el apetito; Directorio informado"),
       ("N4–N5", "Autonomías vigentes de RNF", "No usan cupo"),
       ("Uso indebido (Ley IA)", "STOP", "Sin excepción, fuera de rutas")]
put(P, 79, 1, "7. Ruta de autonomía: quién decide (S6, S7). Con varios rojos manda la instancia más exigente.", bold=True, color=NAVY)
header(P, 80, 1, ["Resultado de controles de apetito", "Instancia que aprueba", "Condición"])
for i, a in enumerate(AUT):
    for j, v in enumerate(a): put(P, 81 + i, 1 + j, v, wrap=True)

put(P, 88, 1, "8. Estados que cuentan como producción (S8)", bold=True, color=NAVY)
header(P, 89, 1, ["Estado (Reporte)"])
put(P, 90, 1, "5. Despliegue", inp=True); put(P, 91, 1, "6. Captura de valor", inp=True)
widths(P, [16, 14, 22, 40, 16, 12, 12, 12, 14, 12, 12, 9, 38, 16])

# =====================================================================
# BD_Iniciativas
# =====================================================================
ini = rep["Iniciativas Playbook"]
I = sheet("BD_Iniciativas", "2E75B6")
title(I, "BD_Iniciativas · ficha de cada iniciativa", "Datos de 'Reporte iniciativas IA' (hoja Iniciativas Playbook) + Playbook 20.11 (IniciativasVistaActual), cruzados por código limpio. Columnas grises = fórmulas.")
IC = ["Código", "Nombre iniciativa", "Descripción", "Estado", "Tipo de solución", "Empresa", "Tipo de usuario", "Categoría IA",
      "Herramienta", "Fase en Playbook", "Product Owner", "Tier AIR Team", "Nivel (ingreso manual)", "Nivel N1–N5", "Materialidad",
      "¿En producción?", "N.º evaluaciones", "Evaluaciones finalizadas", "N.º riesgos", "Peor riesgo residual", "Planes en curso",
      "Controles de evaluación", "Controles de apetito", "Aprobación de la iniciativa"]
SRC = ["Reporte", "Reporte", "Reporte", "Reporte", "Reporte", "Playbook", "Playbook", "Playbook", "Playbook", "Playbook", "Playbook", "Playbook",
       "Ingreso", "Fórmula", "Fórmula", "Fórmula", "Fórmula", "Fórmula", "Fórmula", "Fórmula", "Fórmula", "Fórmula", "Fórmula", "Ingreso"]
src_row(I, 3, 1, SRC); header(I, 4, 1, IC)
for k, cod in enumerate(IDS):
    r = 5 + k
    a = ini[ini["Código"] == cod].iloc[0]
    b = pb[pb.cod == cod].iloc[0]
    herr = clean(b["HerramientaUsuario"])
    if herr: herr = re.split(r"\s\(\*Nota", herr)[0].strip()
    vals = [cod, clean(a["Nombre Iniciativa"]), clean(a["Descripción Iniciativa"]), clean(a["Estado"]), clean(a["Tipo de solución"]),
            clean(b["Empresa"]), clean(b["Tipo de Usuarios"]), clean(b["Categoría IA"]) or "Sin dato", herr or "Sin dato",
            clean(b["EstadoRegistroValor"]), clean(b["Nombre PO"]) or "Sin dato", clean(b["TierAIRiskTeam"])]
    for j, v in enumerate(vals): put(I, r, 1 + j, v, wrap=(j == 2))
    put(I, r, 13, None, inp=True)
    put(I, r, 14, f'=IF(M{r}<>"",M{r},IF(L{r}="","Sin triaje",IFERROR(INDEX(Parametros!$B${TI1}:$B${TI2},MATCH(L{r},Parametros!$A${TI1}:$A${TI2},0)),"Sin triaje")))')
    put(I, r, 15, f'=IFERROR(INDEX(Parametros!$B${NV1}:$B${NV2},MATCH(N{r},Parametros!$A${NV1}:$A${NV2},0)),"Por confirmar")')
    put(I, r, 16, f'=IF(COUNTIF(Parametros!$A$90:$A$91,D{r})>0,"Sí","No")')
    put(I, r, 17, f'=COUNTIF(BD_Evaluaciones!$B:$B,A{r})')
    put(I, r, 18, f'=COUNTIFS(BD_Evaluaciones!$B:$B,A{r},BD_Evaluaciones!$J:$J,"Finalizado")')
    put(I, r, 19, f'=COUNTIF(BD_Riesgos!$B:$B,A{r})')
    put(I, r, 20, f'=IF(S{r}=0,"Sin riesgos",INDEX(Parametros!$A${R1}:$A${R2},MAX(' + ",".join(
        f'IF(COUNTIFS(BD_Riesgos!$B:$B,A{r},BD_Riesgos!$H:$H,Parametros!$A${R1+i})>0,{i+1},0)' for i in range(5)) + ")))")
    put(I, r, 21, f'=COUNTIFS(BD_Planes!$B:$B,A{r},BD_Planes!$K:$K,"En curso")')
    put(I, r, 22, f'=COUNTIFS(BD_Controles!$B:$B,A{r},BD_Controles!$C:$C,"No")')
    put(I, r, 23, f'=COUNTIFS(BD_Controles!$B:$B,A{r},BD_Controles!$C:$C,"Sí")')
    put(I, r, 24, None, inp=True)
    for c in range(14, 24):
        if c != 24: I.cell(row=r, column=c).fill = GFILL
    I.row_dimensions[r].height = 60
dv = DataValidation(type="list", formula1='"N1,N2,N3,N4,N5"', allow_blank=True); I.add_data_validation(dv); dv.add("M5:M104")
dv2 = DataValidation(type="list", formula1='"Sí,No"', allow_blank=True); I.add_data_validation(dv2); dv2.add("X5:X104")
widths(I, [11, 26, 40, 13, 16, 10, 13, 13, 16, 11, 18, 9, 11, 10, 12, 10, 10, 11, 9, 11, 9, 11, 10, 12])
I.freeze_panes = "B5"

# =====================================================================
# BD_Evaluaciones
# =====================================================================
ev = rep["Detalle evaluaciones"]; ev = ev[ev["ID IA"].isin(IDS)].copy()
ev["_o"] = ev["ID IA"].map({c: i for i, c in enumerate(IDS)}); ev = ev.sort_values(["_o", "FechaCreacion"])
E = sheet("BD_Evaluaciones", "2E75B6")
title(E, "BD_Evaluaciones · cuestionarios de evaluación de riesgos", "Fuente: Reporte iniciativas IA › Detalle evaluaciones (filtrado a las 2 iniciativas del ejemplo).")
EC = ["IDCuestionario", "ID IA", "Equipo evaluador", "Nombre iniciativa", "Descripción", "Gestor", "Consultor", "Fecha creación", "Unidad responsable", "Estado", "Fecha inicio", "Fecha fin", "N.º riesgos"]
src_row(E, 3, 1, ["Reporte"] * 12 + ["Fórmula"]); header(E, 4, 1, EC)
for k, (_, x) in enumerate(ev.iterrows()):
    r = 5 + k
    vals = [str(x["IDCuestionario"]), x["ID IA"], x["Equipo evaluador"], x["NombreIniciativa"], x["Descripcion"], x["Gestor"], x["Consultor"],
            x["FechaCreacion"], x["UnidadResponsable"], x["Estado"], x["Fecha Inicio"], x["Fecha Fin"]]
    for j, v in enumerate(vals):
        v = todate(v)
        put(E, r, 1 + j, v, fmt=("dd/mm/yyyy" if isinstance(v, dt.datetime) else None), wrap=(j == 4))
    put(E, r, 13, f'=COUNTIF(BD_Riesgos!$A:$A,A{r})').fill = GFILL
    E.row_dimensions[r].height = 45
widths(E, [12, 11, 12, 26, 50, 18, 18, 11, 24, 11, 11, 11, 9]); E.freeze_panes = "C5"

# =====================================================================
# BD_Riesgos
# =====================================================================
rk = rep["Detalle riesgos"]; rk = rk[rk["ID IA"].isin(IDS)].copy()
rk["_o"] = rk["ID IA"].map({c: i for i, c in enumerate(IDS)})
rk["_d"] = rk["Taxonomía"].map(dict(TAX)); rk = rk.sort_values(["_o", "_d", "ID Riesgo"])
Rk = sheet("BD_Riesgos", "2E75B6")
title(Rk, "BD_Riesgos · riesgos identificados en la evaluación", "Fuente: Reporte iniciativas IA › Detalle riesgos. La dimensión se asigna por la taxonomía (Parametros, tabla 3).")
RC = ["IdCuestionario", "ID IA", "Equipo evaluador", "Estado cuestionario", "ID Riesgo", "Descripción riesgo", "Taxonomía", "Riesgo residual",
      "Exposición residual (S/)", "Cód. dimensión", "Dimensión", "Semáforo residual (GOB-03)", "N.º controles", "N.º planes"]
src_row(Rk, 3, 1, ["Reporte"] * 9 + ["Fórmula"] * 5); header(Rk, 4, 1, RC)
for k, (_, x) in enumerate(rk.iterrows()):
    r = 5 + k
    vals = [str(x["IdCuestionario"]), x["ID IA"], x["Equipo evaluador"], x["Estado"], x["ID Riesgo"], clean(x["Descripción riesgo"]),
            x["Taxonomía"], x["Riesgo residual"], x["Exposición residual"]]
    for j, v in enumerate(vals): put(Rk, r, 1 + j, v, fmt=("#,##0" if j == 8 else None), wrap=(j == 5))
    for c, f in [(10, f'=IFERROR(INDEX(Parametros!$B${T1}:$B${T2},MATCH(G{r},Parametros!$A${T1}:$A${T2},0)),"Sin mapeo")'),
                 (11, f'=IFERROR(INDEX(Parametros!$C${DR1}:$C${DR2},MATCH(J{r},Parametros!$B${DR1}:$B${DR2},0)),"Sin mapeo")'),
                 (12, f'=IFERROR(INDEX(Parametros!$B${R1}:$B${R2},MATCH(H{r},Parametros!$A${R1}:$A${R2},0)),"Sin dato")'),
                 (13, f'=COUNTIF(BD_Controles!$F:$F,E{r})'),
                 (14, f'=COUNTIF(BD_Planes!$D:$D,E{r})')]:
        put(Rk, r, c, f).fill = GFILL
    Rk.row_dimensions[r].height = 48
sem_cf(Rk, f"L5:L{4+len(rk)}")
widths(Rk, [11, 10, 11, 11, 12, 60, 22, 10, 12, 11, 18, 12, 9, 8]); Rk.freeze_panes = "C5"
RK_LAST = 4 + len(rk)

# =====================================================================
# BD_Planes
# =====================================================================
pl = rep["Detalle planes"]; pl = pl[pl["ID IA"].isin(IDS)].copy()
pl["_o"] = pl["ID IA"].map({c: i for i, c in enumerate(IDS)}); pl = pl.sort_values(["_o", "ID Riesgo", "ID Plan"])
Pl = sheet("BD_Planes", "2E75B6")
title(Pl, "BD_Planes · planes de acción por riesgo", "Fuente: Reporte iniciativas IA › Detalle planes (1 fila = plan × riesgo). Las 3 últimas columnas arman el proxy de GOB-02.")
PC = ["IdCuestionario", "ID IA", "ID Plan", "ID Riesgo", "Riesgo residual", "Descripción del plan", "Unidad responsable", "Responsable",
      "Fin original", "Fin actualizado", "Estado ejecución", "Estado aprobación", "¿Riesgo Alto/Crítico?", "¿Vencido al corte?", "Brecha crítica (proxy)"]
src_row(Pl, 3, 1, ["Reporte"] * 12 + ["Fórmula"] * 3); header(Pl, 4, 1, PC)
for k, (_, x) in enumerate(pl.iterrows()):
    r = 5 + k
    vals = [str(x["IdCuestionario"]), x["ID IA"], x["ID Plan"], x["ID Riesgo"], x["Riesgo Residual"], clean(x["Descripción general del plan"]),
            x["Unidad responsable del plan"], x["Responsable del plan de acción"], todate(x["Fecha de fin original"]), todate(x["Fecha de fin actualizado"]),
            x["Estado de ejecución del plan de acción"], x["Estado de aprobación del plan de acción"]]
    for j, v in enumerate(vals): put(Pl, r, 1 + j, clean(v) if not isinstance(v, dt.datetime) else v, fmt=("dd/mm/yyyy" if j in (8, 9) else None))
    put(Pl, r, 13, f'=IF(OR(E{r}="Alto",E{r}="Crítico"),"Sí","No")').fill = GFILL
    put(Pl, r, 14, f'=IF(AND(K{r}="En curso",J{r}<Parametros!$B$4),"Sí","No")').fill = GFILL
    put(Pl, r, 15, f'=IF(M{r}="No","No aplica",IF(N{r}="Sí","Vencida","En plazo"))').fill = GFILL
widths(Pl, [11, 10, 13, 12, 10, 50, 22, 22, 11, 11, 10, 10, 10, 10, 12]); Pl.freeze_panes = "D5"

# =====================================================================
# BD_Controles (evaluación RNF + controles de apetito)
# =====================================================================
ct = rep["Detalle controles"]; ct = ct[ct["ID Riesgo"].isin(rk["ID Riesgo"])].copy()
riskmap = rk.drop_duplicates("ID Riesgo").set_index("ID Riesgo")
ct["ID IA"] = ct["ID Riesgo"].map(riskmap["ID IA"]); ct["_d"] = ct["ID Riesgo"].map(riskmap["_d"])
rows = []
for cod in IDS:
    for d in [x[0] for x in DIMS]:
        for m in MET:
            if m[1] == d: rows.append(("A", cod, m))
        sub = ct[(ct["ID IA"] == cod) & (ct["_d"] == d)].sort_values(["ID Riesgo", "ID Control"])
        for _, x in sub.iterrows(): rows.append(("R", cod, x))
C = sheet("BD_Controles", "C00000")
title(C, "BD_Controles · controles de la evaluación por dimensión (incluye los controles de apetito)",
      "Controles de evaluación: Reporte › Detalle controles. Controles de apetito: las 19 métricas de la PPT v35, una fila por iniciativa. Amarillo = lo registra la especialidad.")
CC = ["N.º", "ID IA", "¿Métrica de apetito?", "Código métrica", "Equipo evaluador", "ID Riesgo", "ID Control", "Control", "Categoría", "Naturaleza", "Tipo",
      "Taxonomía del riesgo", "Cód. dimensión", "Dimensión", "Regla de cálculo", "Ámbar desde", "Rojo desde", "Valor medido",
      "Resultado (ingreso)", "Semáforo", "Estado del dato", "Dueño / fuente", "Responsable del control (RACI)", "Rojos de apetito (acumulado)"]
src_row(C, 3, 1, ["Fórmula", "Dato", "Dato", "Dato", "Reporte", "Reporte", "Reporte/Fórmula", "Reporte/Parámetro", "Reporte", "Reporte", "Reporte",
                  "Fórmula", "Fórmula", "Fórmula", "Parámetro", "Parámetro", "Parámetro", "Ingreso/Fórmula", "Ingreso", "Fórmula", "Fórmula", "Parámetro", "Ingreso", "Fórmula"])
header(C, 4, 1, CC)
PM = lambda col, r: f'INDEX(Parametros!${col}${M1}:${col}${M2},MATCH(D{r},Parametros!$A${M1}:$A${M2},0))'
for k, (t, cod, x) in enumerate(rows):
    r = 5 + k
    put(C, r, 1, f'=ROW()-4').fill = GFILL
    put(C, r, 2, cod if t == "A" else f'=IFERROR(INDEX(BD_Riesgos!$B$5:$B${RK_LAST},MATCH(F{r},BD_Riesgos!$E$5:$E${RK_LAST},0)),"Sin riesgo")')
    put(C, r, 3, "Sí" if t == "A" else "No", bold=(t == "A"))
    if t == "A":
        m = x
        put(C, r, 4, m[0], bold=True); put(C, r, 5, "Especialidad (G2)"); put(C, r, 6, None)
        put(C, r, 7, f'=B{r}&"-"&D{r}'); put(C, r, 8, "=" + PM("D", r), wrap=True); put(C, r, 9, "Control de apetito")
        put(C, r, 10, None); put(C, r, 11, None); put(C, r, 12, None)
        put(C, r, 13, "=" + PM("B", r)); put(C, r, 15, "=" + PM("I", r))
        put(C, r, 16, f'=IF({PM("J", r)}="","",{PM("J", r)})'); put(C, r, 17, f'=IF({PM("K", r)}="","",{PM("K", r)})')
        fmt = "0.00%" if m[10] == "%" else None
        IROW = f'MATCH(B{r},BD_Iniciativas!$A:$A,0)'
        if m[0] == "GOB-01":
            v = (f'=IFERROR(IF(INDEX(BD_Iniciativas!$K:$K,{IROW})="Sin dato",1,0)+IF(INDEX(BD_Iniciativas!$X:$X,{IROW})="No",1,0),1)')
            put(C, r, 18, v, fmt="0").fill = GFILL
            put(C, r, 21, f'=IF(INDEX(BD_Iniciativas!$X:$X,{IROW})="","Parcial: falta aprobación","Calculado de la base")').fill = GFILL
        elif m[0] == "GOB-02":
            v = (f'=IF(COUNTIFS(BD_Planes!$B:$B,B{r},BD_Planes!$O:$O,"Vencida")>0,"Rojo",'
                 f'IF(COUNTIFS(BD_Planes!$B:$B,B{r},BD_Planes!$O:$O,"En plazo")>0,"Ámbar","Verde"))')
            put(C, r, 18, v).fill = GFILL
            put(C, r, 21, "Proxy: planes de riesgos Alto/Crítico").fill = GFILL
        elif m[0] == "GOB-03":
            v = (f'=IFERROR(INDEX(Parametros!$B${R1}:$B${R2},MATCH(INDEX(BD_Iniciativas!$T:$T,{IROW}),Parametros!$A${R1}:$A${R2},0)),"")')
            put(C, r, 18, v).fill = GFILL
            put(C, r, 21, f'="Calculado: peor residual "&INDEX(BD_Iniciativas!$T:$T,{IROW})').fill = GFILL
        else:
            put(C, r, 18, None, fmt=fmt, inp=True)
            put(C, r, 21, f'=IF(R{r}="","Sin dato","Ingresado")').fill = GFILL
        put(C, r, 19, None).fill = GFILL
        put(C, r, 22, "=" + PM("N", r))
    else:
        put(C, r, 4, None); put(C, r, 5, x["Equipo evaluador"]); put(C, r, 6, x["ID Riesgo"]); put(C, r, 7, int(x["ID Control"]))
        put(C, r, 8, clean(x["Descripción"]), wrap=True); put(C, r, 9, clean(x["Categoría"])); put(C, r, 10, clean(x["Naturaleza del control"]))
        put(C, r, 11, clean(x["Tipo de control"]))
        put(C, r, 12, f'=IFERROR(INDEX(BD_Riesgos!$G$5:$G${RK_LAST},MATCH(F{r},BD_Riesgos!$E$5:$E${RK_LAST},0)),"")')
        put(C, r, 13, f'=IFERROR(INDEX(Parametros!$B${T1}:$B${T2},MATCH(L{r},Parametros!$A${T1}:$A${T2},0)),"Sin mapeo")')
        put(C, r, 15, "Resultado de la evaluación"); put(C, r, 16, None); put(C, r, 17, None)
        put(C, r, 18, None).fill = GFILL
        put(C, r, 19, None, inp=True)
        put(C, r, 21, f'=IF(S{r}="","Sin dato: la base no trae resultado","Ingresado")').fill = GFILL
        put(C, r, 22, "Evaluación RNF (Reporte)")
    put(C, r, 14, f'=IFERROR(INDEX(Parametros!$C${DR1}:$C${DR2},MATCH(M{r},Parametros!$B${DR1}:$B${DR2},0)),"Sin mapeo")')
    put(C, r, 20, (f'=IF(C{r}="Sí",IF(R{r}="","Sin dato",IF(O{r}="Categórico",R{r},IF(O{r}="Menor es mejor",'
                   f'IF(R{r}>=Q{r},"Rojo",IF(AND(P{r}<>"",R{r}>=P{r}),"Ámbar","Verde")),'
                   f'IF(R{r}<Q{r},"Rojo",IF(AND(P{r}<>"",R{r}<P{r}),"Ámbar","Verde"))))),IF(S{r}="","Sin dato",S{r}))'), bold=True, align=CENTER)
    put(C, r, 23, None, inp=True)
    base = f'IF(B{r}=B{r-1},X{r-1},"")' if r > 5 else '""'
    put(C, r, 24, f'={base}&IF(AND(C{r}="Sí",T{r}="Rojo"),IF({base}<>"",", ","")&D{r},"")').fill = GFILL
    for c in (12, 13, 14, 15, 16, 17): C.cell(row=r, column=c).fill = GFILL
    if t == "A":
        for c in (3, 4): C.cell(row=r, column=c).fill = PatternFill("solid", fgColor="FCE4D6")
    C.row_dimensions[r].height = 36
C_LAST = 4 + len(rows)
sem_cf(C, f"T5:T{C_LAST}")
dv3 = DataValidation(type="list", formula1='"Verde,Ámbar,Rojo"', allow_blank=True); C.add_data_validation(dv3); dv3.add(f"S5:S{C_LAST}")
for code in ("GOB-02", "GOB-03", "CYB-04"): pass
dv4 = DataValidation(type="list", formula1='"Verde,Ámbar,Rojo"', allow_blank=True); C.add_data_validation(dv4)
for k, (t, cod, x) in enumerate(rows):
    if t == "A" and x[0] == "CYB-04": dv4.add(f"R{5+k}")
C.auto_filter.ref = f"A4:X{C_LAST}"
widths(C, [5, 10, 9, 9, 12, 12, 17, 42, 18, 10, 11, 18, 11, 18, 13, 8, 8, 10, 10, 10, 22, 18, 14, 18]); C.freeze_panes = "D5"

# =====================================================================
# Apetito (definida antes del tablón porque el tablón la consulta)
# =====================================================================
A = sheet("Apetito", "C00000")
NROW = 10
title(A, "Apetito · ¿qué iniciativas pasan por la ruta del apetito?",
      "Regla: si algún control de apetito está en Rojo, la iniciativa pasa por la ruta del apetito (S3, S6, S7). Solo cuentan los controles de apetito.")
dimcols = list(range(11, 17))   # K..P
AH = ["Código", "Nombre", "Estado", "Nivel", "Materialidad", "Controles de apetito", "Verde", "Ámbar", "Rojo", "Sin dato"] + \
     [f"=Parametros!$C${DR1+i}" for i in range(6)] + \
     ["Controles en rojo", "¿Pasa por la ruta del apetito?", "Ruta de atención", "SLA G1→G3 (d.h.)", "Instancia que decide", "¿En producción?"] + \
     [f'="Instancia "&Parametros!$B${DR1+i}' for i in range(6)]
A["A4"] = "Iniciativa"; A["F4"] = "Controles de apetito"; A["K4"] = "Peor semáforo por dimensión (solo controles de apetito)"; A["Q4"] = "Resultado"; A["W4"] = "Cálculo de instancia por dimensión (cupo hoy + 1 vs. límite)"
for rng, cell in [("A4:E4", "A4"), ("F4:J4", "F4"), ("K4:P4", "K4"), ("Q4:V4", "Q4"), ("W4:AB4", "W4")]:
    A.merge_cells(rng); A[cell].font = font(bold=True, color="FFFFFF"); A[cell].fill = SFILL; A[cell].alignment = CENTER
header(A, 5, 1, AH, height=42)
for n in range(1, NROW + 1):
    r = 5 + n
    put(A, r, 1, f'=IFERROR(IF(INDEX(BD_Iniciativas!$A$5:$A$104,{n})="","",INDEX(BD_Iniciativas!$A$5:$A$104,{n})),"")', bold=True)
    IR = f'MATCH($A{r},BD_Iniciativas!$A:$A,0)'
    for c, col in [(2, "B"), (3, "D"), (4, "N"), (5, "O")]:
        put(A, r, c, f'=IF($A{r}="","",INDEX(BD_Iniciativas!${col}:${col},{IR}))', wrap=(c == 2))
    put(A, r, 6, f'=IF($A{r}="","",COUNTIFS(BD_Controles!$B:$B,$A{r},BD_Controles!$C:$C,"Sí"))')
    for c, s in [(7, "Verde"), (8, "Ámbar"), (9, "Rojo"), (10, "Sin dato")]:
        put(A, r, c, f'=IF($A{r}="","",COUNTIFS(BD_Controles!$B:$B,$A{r},BD_Controles!$C:$C,"Sí",BD_Controles!$T:$T,"{s}"))', align=CENTER)
    for i, c in enumerate(dimcols):
        dref = f'Parametros!$B${DR1+i}'
        cnt = lambda s: f'COUNTIFS(BD_Controles!$B:$B,$A{r},BD_Controles!$C:$C,"Sí",BD_Controles!$M:$M,{dref},BD_Controles!$T:$T,"{s}")'
        put(A, r, c, f'=IF($A{r}="","",IF({cnt("Rojo")}>0,"Rojo",IF({cnt("Ámbar")}>0,"Ámbar",IF({cnt("Verde")}>0,"Verde","Sin dato"))))', align=CENTER, bold=True)
    put(A, r, 17, f'=IF($A{r}="","",IFERROR(INDEX(BD_Controles!$X:$X,MATCH($A{r},BD_Controles!$B:$B,0)+COUNTIF(BD_Controles!$B:$B,$A{r})-1),""))', wrap=True)
    put(A, r, 18, f'=IF($A{r}="","",IF(I{r}>0,"Sí: ruta del apetito",IF(J{r}>0,"No por ahora (faltan "&J{r}&" datos)","No")))', bold=True, wrap=True)
    put(A, r, 19, f'=IF($A{r}="","",IFERROR(INDEX(Parametros!$D${NV1}:$D${NV2},MATCH(D{r},Parametros!$A${NV1}:$A${NV2},0)),"Por confirmar"))')
    put(A, r, 20, f'=IF($A{r}="","",IFERROR(INDEX(Parametros!$E${NV1}:$E${NV2},MATCH(D{r},Parametros!$A${NV1}:$A${NV2},0)),"Por confirmar"))')
    put(A, r, 22, f'=IF($A{r}="","",INDEX(BD_Iniciativas!$P:$P,{IR}))')
    for i in range(6):
        c = 23 + i; dc = L(dimcols[i])
        hoy = f'(Parametros!$K${DR1+i}+COUNTIFS({dc}$6:{dc}${5+NROW},"Rojo",$V$6:$V${5+NROW},"Sí")-IF(AND({dc}{r}="Rojo",$V{r}="Sí"),1,0))'
        put(A, r, c, f'=IF($A{r}="","",IF({dc}{r}="Rojo",IF({hoy}+1>=Parametros!$H${DR1+i},"CAR","Comité RNF"),""))', align=CENTER)
    put(A, r, 21, (f'=IF($A{r}="","",IF(OR(D{r}="N4",D{r}="N5"),"Autonomías vigentes RNF (no material)",'
                   f'IF(COUNTIF(W{r}:AB{r},"CAR")>0,"CAR",IF(COUNTIF(W{r}:AB{r},"Comité RNF")>0,"Comité de Riesgo No Financiero Corp",'
                   f'IF(H{r}>0,"Gerencia Owner + Gerencia de Riesgos",IF(J{r}>0,"Pendiente: faltan datos","Autonomías vigentes RNF"))))))'), bold=True, wrap=True)
    A.row_dimensions[r].height = 40
sem_cf(A, f"K6:P{5+NROW}")
A.conditional_formatting.add(f"R6:R{5+NROW}", FormulaRule(formula=['LEFT(R6,2)="Sí"'], fill=PatternFill("solid", fgColor=SEM["Rojo"]), font=Font(name=F, bold=True, color=SEMF["Rojo"])))
A.conditional_formatting.add(f"U6:U{5+NROW}", FormulaRule(formula=['OR(U6="CAR",LEFT(U6,6)="Comité")'], fill=PatternFill("solid", fgColor=SEM["Rojo"]), font=Font(name=F, bold=True, color=SEMF["Rojo"])))
put(A, 16, 1, "Supuestos: el cupo cuenta iniciativas en producción con rojo (del archivo + 'casos fuera de este archivo' en Parametros). La PPT cuenta solo materiales N1–N3; aquí no se filtra porque el nivel aún no está en la base [Por confirmar].", wrap=True, color="595959")
A.merge_cells("A16:V16"); A.row_dimensions[16].height = 26

# Cupo por dimensión
put(A, 18, 1, "Cupo por dimensión (S8)", bold=True, color=NAVY)
header(A, 19, 1, ["Código", "Dimensión", "Apetito (hasta)", "Límite (desde)", "Rojos en el archivo (producción)", "Rojos fuera del archivo", "Total", "Estado de la dimensión", "", ""]); A.merge_cells("H19:J19")
for i in range(6):
    r = 20 + i; pr = DR1 + i; dc = L(dimcols[i])
    put(A, r, 1, f'=Parametros!B{pr}'); put(A, r, 2, f'=Parametros!C{pr}'); put(A, r, 3, f'=Parametros!F{pr}'); put(A, r, 4, f'=Parametros!H{pr}')
    put(A, r, 5, f'=COUNTIFS({dc}$6:{dc}${5+NROW},"Rojo",$V$6:$V${5+NROW},"Sí")'); put(A, r, 6, f'=Parametros!K{pr}')
    put(A, r, 7, f'=E{r}+F{r}', bold=True)
    put(A, r, 8, f'=IF(G{r}>=D{r},"Rojo: en el límite",IF(G{r}>C{r},"Ámbar: sobre el apetito","Verde: dentro del apetito"))', bold=True); A.merge_cells(f"H{r}:J{r}")
sem_cf(A, "H20:H25")

# Ficha de la ruta
put(A, 28, 1, "Ruta del apetito · ficha de la iniciativa", bold=True, color=NAVY)
put(A, 29, 1, "Elija la iniciativa ▸", bold=True); put(A, 29, 2, IDS[0], inp=True, bold=True)
dv5 = DataValidation(type="list", formula1=f"=$A$6:$A${5+NROW}", allow_blank=False); A.add_data_validation(dv5); dv5.add("B29")
FR = lambda col: f'=IFERROR(INDEX({col}$6:{col}${5+NROW},MATCH($B$29,$A$6:$A${5+NROW},0)),"")'
ficha = [("Nombre", FR("B")), ("Estado / ¿producción?", f'{FR("C")}'), ("Nivel · materialidad", None), ("¿Pasa por la ruta del apetito?", FR("R")),
         ("Controles en rojo", FR("Q")), ("Ruta de atención · SLA", None), ("Instancia que decide (G3)", FR("U"))]
put(A, 30, 1, "Nombre", bold=True); put(A, 30, 2, FR("B"))
put(A, 31, 1, "Estado · ¿producción?", bold=True); put(A, 31, 2, FR("C") + '&" · "&' + FR("V")[1:])
put(A, 32, 1, "Nivel · materialidad", bold=True); put(A, 32, 2, FR("D") + '&" · "&' + FR("E")[1:])
put(A, 33, 1, "¿Pasa por la ruta del apetito?", bold=True); put(A, 33, 2, FR("R"), bold=True)
put(A, 34, 1, "Controles en rojo", bold=True); put(A, 34, 2, FR("Q"))
put(A, 35, 1, "Ruta de atención · SLA", bold=True); put(A, 35, 2, FR("S") + '&" · "&' + FR("T")[1:] + '&" d.h."')
put(A, 36, 1, "Instancia que decide (G3)", bold=True); put(A, 36, 2, FR("U"), bold=True)
for rr in range(30, 37): A.merge_cells(f"B{rr}:H{rr}")
A.conditional_formatting.add("B33", FormulaRule(formula=['LEFT(B33,2)="Sí"'], fill=PatternFill("solid", fgColor=SEM["Rojo"]), font=Font(name=F, bold=True, color=SEMF["Rojo"])))
put(A, 38, 1, "Pasos de la ruta (S3)", bold=True, color=NAVY)
header(A, 39, 1, ["Paso", "Qué pasa", "Gate", "Responsable", "", "Estado para esta iniciativa", "", ""])
A.merge_cells("D39:E39"); A.merge_cells("F39:H39")
STEPS = [("1. Registrar", "—", "Registro en el inventario con código único", "1.ª línea · Programa IA", '=IF(COUNTIF(BD_Iniciativas!$A:$A,$B$29)>0,"Hecho: está en el Playbook","Pendiente")'),
         ("2. Clasificar (triaje)", "G1", "Nivel N1–N5 y categoría Ley IA; asigna ruta de atención", "AI Risk Team", '=IF(LEFT(B32,10)="Sin triaje","Pendiente: sin nivel","Hecho: "&B32)'),
         ("3. Evaluar", "G2", "Especialidades evalúan controles; semáforo por dimensión; se fija quién aprueba", "MRM · Legal · Ciber · RNF · Terceros · Cumplimiento",
          f'=IFERROR(INDEX($J$6:$J${5+NROW},MATCH($B$29,$A$6:$A${5+NROW},0))&" controles de apetito sin dato","")'),
         ("4. Decidir", "G3", "Se cruza el resultado de controles con el cupo de la dimensión", "Instancia según ruta de autonomía", "=B36"),
         ("5. Monitorear", "—", "Tablero mensual; un rojo o cambio material reabre la ruta", "1.ª y 2.ª línea · AI Risk Officer", "Continuo")]
for i, s_ in enumerate(STEPS):
    r = 40 + i
    put(A, r, 1, s_[0], bold=True, wrap=True); put(A, r, 2, s_[2], wrap=True); put(A, r, 3, s_[1], align=CENTER)
    put(A, r, 4, s_[3], wrap=True); A.merge_cells(f"D{r}:E{r}"); put(A, r, 6, s_[4], wrap=True); A.merge_cells(f"F{r}:H{r}")
    A.row_dimensions[r].height = 32
for rr in range(30, 37):
    A.cell(row=rr, column=1).alignment = WRAP; A.row_dimensions[rr].height = 26
widths(A, [16, 30, 13, 10, 12, 10, 9, 9, 9, 9, 12, 12, 12, 12, 12, 12, 22, 20, 12, 10, 26, 10, 11, 11, 11, 11, 11, 11])
A.freeze_panes = "B6"

# =====================================================================
# Tablon_General
# =====================================================================
Tb = sheet("Tablon_General", "00B050")
title(Tb, "Tablón general · controles por dimensión y semáforo",
      "Una fila por control. El semáforo aparece en la columna de su dimensión. Columna '¿Métrica de apetito?' = Sí identifica los controles de apetito.")
TH = ["Código", "Nombre iniciativa", "Estado", "Nivel", "Categoría IA", "Tipo de usuario", "Tipo de solución", "Empresa", "Herramienta",
      "ID control", "Control", "¿Métrica de apetito?", "Código métrica"] + [f"=Parametros!$C${DR1+i}" for i in range(6)] + \
     ["¿Ruta del apetito?", "Instancia que decide", "Clave iniciativa"]
groups = [("A4:I4", "Información de la iniciativa"), ("J4:M4", "Control"), ("N4:S4", "Dimensiones · semáforo del control"), ("T4:V4", "Resultado")]
for rng, txt in groups:
    Tb.merge_cells(rng); c = Tb[rng.split(":")[0]]; c.value = txt; c.font = font(bold=True, color="FFFFFF"); c.fill = SFILL; c.alignment = CENTER
header(Tb, 5, 1, TH, height=60)
for j in range(14, 20): Tb.cell(row=5, column=j).fill = PatternFill("solid", fgColor="C00000")
TROWS = max(C_LAST - 4 + 20, 100)
for k in range(TROWS):
    r = 6 + k; br = 5 + k
    key = f"$V{r}"
    put(Tb, r, 22, f'=IF(BD_Controles!B{br}="","",BD_Controles!B{br})', color="808080")
    first = f'AND({key}<>"",{key}<>$V{r-1})' if r > 6 else f'{key}<>""'
    IR = f'MATCH({key},BD_Iniciativas!$A:$A,0)'
    for c, col in [(1, "A"), (2, "B"), (3, "D"), (4, "N"), (5, "H"), (6, "G"), (7, "E"), (8, "F"), (9, "I")]:
        put(Tb, r, c, f'=IF({first},INDEX(BD_Iniciativas!${col}:${col},{IR}),"")', bold=(c == 1), wrap=(c in (2,)))
    put(Tb, r, 10, f'=IF({key}="","",BD_Controles!G{br})')
    put(Tb, r, 11, f'=IF({key}="","",BD_Controles!H{br})', wrap=True)
    put(Tb, r, 12, f'=IF({key}="","",BD_Controles!C{br})', align=CENTER)
    put(Tb, r, 13, f'=IF({key}="","",IF(BD_Controles!D{br}="","",BD_Controles!D{br}))', align=CENTER)
    for i in range(6):
        put(Tb, r, 14 + i, f'=IF({key}="","",IF(BD_Controles!M{br}=Parametros!$B${DR1+i},BD_Controles!T{br},""))', align=CENTER, bold=True)
    AR = f'MATCH({key},Apetito!$A$6:$A${5+NROW},0)'
    put(Tb, r, 20, f'=IF({first},IFERROR(INDEX(Apetito!$R$6:$R${5+NROW},{AR}),""),"")', bold=True, wrap=True)
    put(Tb, r, 21, f'=IF({first},IFERROR(INDEX(Apetito!$U$6:$U${5+NROW},{AR}),""),"")', wrap=True)
    Tb.row_dimensions[r].height = 30
TL = 5 + TROWS
sem_cf(Tb, f"N6:S{TL}")
Tb.conditional_formatting.add(f"L6:M{TL}", FormulaRule(formula=['$L6="Sí"'], fill=PatternFill("solid", fgColor="FCE4D6"), font=Font(name=F, bold=True, color="C00000")))
Tb.conditional_formatting.add(f"T6:T{TL}", FormulaRule(formula=['LEFT(T6,2)="Sí"'], fill=PatternFill("solid", fgColor=SEM["Rojo"]), font=Font(name=F, bold=True, color=SEMF["Rojo"])))
# línea separadora entre iniciativas
Tb.conditional_formatting.add(f"A6:V{TL}", FormulaRule(formula=['AND($V6<>"",$V6<>$V5)'], border=Border(top=Side(style="medium", color=NAVY))))
Tb.auto_filter.ref = f"A5:V{TL}"
widths(Tb, [10, 22, 12, 9, 12, 12, 14, 9, 13, 16, 40, 9, 9, 11, 11, 11, 11, 11, 11, 16, 18, 10])
Tb.freeze_panes = "J6"

# =====================================================================
# Faltantes
# =====================================================================
Fa = sheet("Faltantes", "FFC000")
title(Fa, "Qué falta para completar el esquema", "Brechas entre el esquema y lo que traen hoy 'Reporte iniciativas IA' y el Playbook 20.11.")
FH = ["#", "Tema", "Qué pide el esquema", "Qué hay hoy", "Qué falta añadir", "Quién lo da", "Prioridad"]
header(Fa, 4, 1, FH)
FALT = [
    ("Resultado del control", "Semáforo de cada control en cada evaluación", "Detalle controles trae categoría, naturaleza y tipo; no trae resultado ni efectividad", "Campo 'Resultado' (Verde/Ámbar/Rojo) por control y evaluación", "RNF y especialidades", "Alta"),
    ("Marca de control de apetito", "Saber qué control es métrica de apetito", "No existe el campo", "Campo '¿Métrica de apetito?' + código de métrica (GOB-01…MRM-04)", "AI Risk Officer", "Alta"),
    ("Catálogo de controles por dimensión", "Set de controles por dimensión y nivel N1–N5", "La PPT no lista controles; solo las 19 métricas", "Catálogo oficial con controles, dimensión y nivel al que aplican", "AI Risk Officer y dueños de métricas", "Alta"),
    ("Valores de 16 controles de apetito", "Valor medido por iniciativa", "Solo GOB-03 sale de la base; GOB-01 parcial; GOB-02 proxy", "LEG-01/02, CYB-01..04, OPS-01/02, TER-01..03, MRM-01..04, GOB-04", "Legal, Ciber, RNF, Terceros, MRM", "Alta"),
    ("Dimensión del control", "Cada control en una de las 6 dimensiones", "Se infiere por la taxonomía RNF del riesgo (propuesta)", "Validar el mapeo; Gobierno y Terceros no tienen taxonomía equivalente", "RNF / AI Risk Officer", "Alta"),
    ("Riesgos IA", "Distinguir riesgos IA de los RNF generales", "No separados; solo por contexto en 'Descripción riesgo'", "Etiqueta IA y las 11 categorías IA por riesgo y control", "RNF; catálogo de 11 categorías (Percy Luna)", "Media"),
    ("Nivel N1–N5 y materialidad", "Nivel de triaje para ruta de atención, SLA y cupo", "TierAIRiskTeam vacío en las 2 iniciativas; sin campo de materialidad", "Nivel del triaje por iniciativa y definición oficial de material", "AI Risk Team / Walter", "Alta"),
    ("Llave control → iniciativa", "Unir controles con su evaluación sin ambigüedad", "Detalle controles solo trae ID Riesgo; 12 riesgos se repiten entre iniciativas", "Agregar ID IA e IdCuestionario a Detalle controles", "Responsable de la base", "Media"),
    ("Brecha crítica (GOB-02)", "Definición de brecha crítica y su estado", "Proxy: planes de riesgos Alto/Crítico; todos los planes 'En curso'", "Definición oficial y fecha de vencimiento por brecha", "AI Risk Team", "Media"),
    ("Aprobación y cambios (GOB-01, GOB-04)", "Aprobación de la iniciativa y registro de cambios materiales", "Playbook trae registro y PO; no aprobación ni cambios", "Campo de aprobación y log de cambios materiales con reevaluación", "Programa IA (1.ª línea)", "Media"),
    ("Cupo de cartera", "Casos en rojo por dimensión en toda la cartera", "Solo las 2 iniciativas del ejemplo", "Cargar todas las iniciativas evaluadas (o ingresar el conteo en Parametros)", "AI Risk Officer", "Media"),
    ("Consistencia de estado", "Un único estado por iniciativa", "BCP-0312: 'Despliegue' en Reporte vs 'Ideación' en Playbook", "Definir fuente oficial del estado", "Programa IA", "Baja"),
    ("Datos del Playbook", "Categoría IA y herramienta completas", "BCP-0312 sin categoría IA ni herramienta", "Completar campos núcleo del registro", "Programa IA (1.ª línea)", "Baja"),
    ("RACI del control", "Responsable de cada control", "No está en la base", "Responsable y validador por control", "Especialidades", "Baja"),
    ("Umbrales", "Umbrales cerrados", "Propios de IA preliminares; heredados por ratificar; Relevante sin semáforo", "Ratificar umbrales y regla de 'Relevante' en GOB-03", "Dueños de métricas (S12)", "Media"),
]
for i, f in enumerate(FALT):
    r = 5 + i
    put(Fa, r, 1, i + 1, align=CENTER)
    for j, v in enumerate(f): put(Fa, r, 2 + j, v, wrap=True, bold=(j == 0))
    Fa.row_dimensions[r].height = 40
Fa.conditional_formatting.add(f"G5:G{4+len(FALT)}", FormulaRule(formula=['G5="Alta"'], fill=PatternFill("solid", fgColor=SEM["Rojo"]), font=Font(name=F, bold=True, color=SEMF["Rojo"])))
Fa.conditional_formatting.add(f"G5:G{4+len(FALT)}", FormulaRule(formula=['G5="Media"'], fill=PatternFill("solid", fgColor=SEM["Ámbar"]), font=Font(name=F, bold=True, color=SEMF["Ámbar"])))
widths(Fa, [4, 22, 30, 36, 38, 24, 9])
r = 6 + len(FALT)
put(Fa, r, 2, "Estado de los 19 controles de apetito en el ejemplo", bold=True, color=NAVY)
header(Fa, r + 1, 2, ["Estado del dato", "N.º controles (2 iniciativas)"])
for i, s in enumerate(["Calculado", "Parcial", "Proxy", "Sin dato", "Ingresado"]):
    put(Fa, r + 2 + i, 2, s)
    put(Fa, r + 2 + i, 3, f'=COUNTIFS(BD_Controles!$C:$C,"Sí",BD_Controles!$U:$U,"{s}*")')

# =====================================================================
# Diccionario
# =====================================================================
D = sheet("Diccionario", "7F7F7F")
title(D, "Diccionario de datos", "Qué contiene cada campo, de dónde sale y si es dato, fórmula o ingreso.")
header(D, 4, 1, ["Hoja", "Campo", "Tipo", "Fuente / cálculo"])
DIC = []
def add(h, cols, srcs, notes):
    for c, s, n in zip(cols, srcs, notes): DIC.append((h, c, s, n))
add("BD_Iniciativas", IC, SRC, [
    "Reporte › Iniciativas Playbook › Código (= ID IA)", "Reporte › Nombre Iniciativa", "Reporte › Descripción Iniciativa", "Reporte › Estado (fase del ciclo de vida)",
    "Reporte › Tipo de solución", "Playbook › Empresa", "Playbook › Tipo de Usuarios", "Playbook › Categoría IA", "Playbook › HerramientaUsuario (sin la nota del formulario)",
    "Playbook › EstadoRegistroValor", "Playbook › Nombre PO", "Playbook › TierAIRiskTeam", "Lo registra el AI Risk Team si no hay Tier",
    "Ingreso manual; si no, Tier → Nivel (Parametros 5)", "Nivel → materialidad (Parametros 6)", "Estado en lista de producción (Parametros 8)",
    "Conteo en BD_Evaluaciones", "Conteo de estado Finalizado", "Conteo en BD_Riesgos", "Mayor riesgo residual de la iniciativa", "Planes 'En curso'",
    "Controles de evaluación en BD_Controles", "Controles de apetito en BD_Controles", "Sí/No; alimenta GOB-01"])
add("BD_Controles", CC, ["Fórmula", "Dato/Fórmula", "Dato", "Dato", "Reporte", "Reporte", "Reporte/Fórmula", "Reporte/Parámetro", "Reporte", "Reporte", "Reporte",
                         "Fórmula", "Fórmula", "Fórmula", "Parámetro", "Parámetro", "Parámetro", "Ingreso/Fórmula", "Ingreso", "Fórmula", "Fórmula", "Parámetro", "Ingreso", "Fórmula"], [
    "Correlativo", "Controles de evaluación: se busca por ID Riesgo en BD_Riesgos", "Sí = control de apetito", "Código de la métrica (Parametros 2)",
    "Reporte › Detalle controles", "Reporte › Detalle controles", "Reporte › ID Control; apetito = ID IA + código", "Reporte › Descripción; apetito = nombre de la métrica",
    "Reporte › Categoría", "Reporte › Naturaleza del control", "Reporte › Tipo de control", "Taxonomía del riesgo (BD_Riesgos)",
    "Apetito: dimensión de la métrica; evaluación: taxonomía → dimensión", "Nombre de la dimensión", "Menor/Mayor es mejor o Categórico", "Umbral ámbar", "Umbral rojo",
    "Valor del control de apetito (GOB-01/02/03 por fórmula; el resto lo registra la especialidad)", "Resultado del control de evaluación (Verde/Ámbar/Rojo)",
    "Semáforo final del control", "Calculado, Parcial, Proxy, Sin dato o Ingresado", "Dueño de la métrica o fuente", "Responsable del control (RACI)", "Lista de controles de apetito en rojo"])
add("Tablon_General", ["Columnas A–I", "Columnas J–M", "Columnas N–S", "Columnas T–U", "Clave iniciativa"], ["Fórmula"] * 5, [
    "Ficha de BD_Iniciativas (solo en la primera fila de cada iniciativa)", "Control de BD_Controles", "Semáforo en la columna de su dimensión",
    "Resultado de la hoja Apetito", "Código en cada fila, para filtrar"])
add("Apetito", ["Controles de apetito", "Peor semáforo por dimensión", "¿Pasa por la ruta del apetito?", "Instancia que decide", "Cupo por dimensión"], ["Fórmula"] * 5, [
    "Conteo por semáforo de los controles de apetito", "Rojo > Ámbar > Verde > Sin dato, solo controles de apetito",
    "Sí si hay ≥1 control de apetito en rojo", "CAR si algún rojo lleva su dimensión al límite; si no, Comité RNF; ámbar → Gerencias (S6, S7)",
    "Rojos en producción + fuera del archivo vs. apetito y límite (S8)"])
for i, d in enumerate(DIC):
    for j, v in enumerate(d): put(D, 5 + i, 1 + j, v, wrap=(j == 3))
widths(D, [16, 28, 16, 70]); D.freeze_panes = "A5"

# =====================================================================
# Inicio
# =====================================================================
S = wb["Sheet"]; S.title = "Inicio"; S.sheet_view.showGridLines = False; S.sheet_properties.tabColor = NAVY
wb.move_sheet("Inicio", offset=-(len(wb.sheetnames) - 1))
title(S, "Esquema de controles de apetito de riesgo IA · BCP", "Ejemplo con 2 iniciativas (BCP-0312 y BCP-0086). Fuentes: Reporte iniciativas IA, Playbook 20.11 y PPT Comité Gobierno IA v35.")
put(S, 4, 1, "Regla", bold=True, color=NAVY)
S["B4"] = "Las métricas de apetito son controles de la evaluación de riesgos, dentro de 6 dimensiones. Cada control tiene semáforo. Si algún control de apetito está en Rojo, la iniciativa pasa por la ruta del apetito."
S["B4"].font = font(size=10); S["B4"].alignment = WRAP; S.merge_cells("B4:L4"); S.row_dimensions[4].height = 30

put(S, 6, 1, "Flujo de información", bold=True, color=NAVY)
def box(r, c, txt, fill, w=2, h=1):
    S.merge_cells(start_row=r, start_column=c, end_row=r + h - 1, end_column=c + w - 1)
    cell = S.cell(row=r, column=c, value=txt); cell.fill = PatternFill("solid", fgColor=fill)
    cell.font = font(bold=True, color="FFFFFF" if fill in (NAVY, BLUE, "C00000", "00B050", "7F7F7F") else "000000"); cell.alignment = CENTER
def arrow(r, c, t="▶"):
    cell = S.cell(row=r, column=c, value=t); cell.font = font(size=14, bold=True, color=NAVY); cell.alignment = CENTER
box(8, 1, "FUENTES\nPlaybook 20.11\n(IniciativasVistaActual)", "D9D9D9", 2, 2)
box(11, 1, "FUENTES\nReporte iniciativas IA\n(5 hojas)", "D9D9D9", 2, 2)
box(14, 1, "FUENTES\nPPT Gobierno IA v35\n(umbrales y rutas)", "D9D9D9", 2, 2)
for rr in (8, 11): arrow(rr, 3)
arrow(14, 3)
box(8, 4, "BD_Iniciativas", BLUE, 2, 1); box(9, 4, "BD_Evaluaciones", BLUE, 2, 1)
box(11, 4, "BD_Riesgos", BLUE, 2, 1); box(12, 4, "BD_Planes", BLUE, 2, 1)
box(14, 4, "Parametros", "7F7F7F", 2, 2)
arrow(10, 6); arrow(12, 6); arrow(14, 6)
box(10, 7, "BD_Controles\ncontroles de evaluación\n+ controles de apetito\n→ semáforo", "C00000", 2, 4)
arrow(10, 9); arrow(13, 9)
box(9, 10, "Tablon_General\niniciativa × dimensión × control", "00B050", 2, 2)
box(12, 10, "Apetito\n¿ruta del apetito? · instancia", "C00000", 2, 2)
box(15, 10, "Faltantes", "FFC000", 2, 1)
for rr in range(8, 16): S.row_dimensions[rr].height = 22

put(S, 18, 1, "Hojas del archivo", bold=True, color=NAVY)
header(S, 19, 1, ["Hoja", "Qué contiene", "", "", "", "Fuente", "", "Alimenta a", ""])
for rg in ("B19:E19", "F19:G19", "H19:I19"): S.merge_cells(rg)
HOJAS = [("Parametros", "Dimensiones, 19 controles de apetito con umbrales, mapeos y rutas", "PPT v35", "Todas"),
         ("BD_Iniciativas", "Ficha de cada iniciativa: estado, nivel, categoría, tipo de usuario, solución, empresa, herramienta", "Reporte + Playbook", "Tablón, Apetito"),
         ("BD_Evaluaciones", "Cuestionarios de evaluación de riesgos", "Reporte › Detalle evaluaciones", "BD_Iniciativas"),
         ("BD_Riesgos", "Riesgos por evaluación, taxonomía, residual y dimensión", "Reporte › Detalle riesgos", "BD_Controles, GOB-03"),
         ("BD_Planes", "Planes de acción por riesgo; proxy de brecha crítica", "Reporte › Detalle planes", "GOB-02"),
         ("BD_Controles", "Todos los controles por dimensión, con marca de apetito y semáforo", "Reporte › Detalle controles + Parametros", "Tablón, Apetito"),
         ("Tablon_General", "Vista general: iniciativa, control y semáforo por dimensión", "Fórmulas", "—"),
         ("Apetito", "Iniciativas en ruta del apetito, instancia que decide, cupo por dimensión y ficha", "Fórmulas", "Tablón"),
         ("Faltantes", "Qué falta añadir para cumplir el esquema", "Análisis", "—"),
         ("Diccionario", "Campo, tipo y fuente", "—", "—")]
for i, h in enumerate(HOJAS):
    r = 20 + i
    c = put(S, r, 1, h[0], bold=True); c.hyperlink = f"#'{h[0]}'!A1"; c.font = font(bold=True, color="0563C1", underline="single")
    put(S, r, 2, h[1], wrap=True); S.merge_cells(f"B{r}:E{r}")
    put(S, r, 6, h[2], wrap=True); S.merge_cells(f"F{r}:G{r}")
    put(S, r, 8, h[3], wrap=True); S.merge_cells(f"H{r}:I{r}")
    S.row_dimensions[r].height = 28

put(S, 31, 1, "Resumen del ejemplo", bold=True, color=NAVY)
summ = [("Iniciativas", '=COUNTA(BD_Iniciativas!A5:A104)'),
        ("Controles totales", '=COUNTA(BD_Controles!B5:B1000)'),
        ("Controles de apetito", '=COUNTIF(BD_Controles!C:C,"Sí")'),
        ("Controles de apetito en rojo", '=COUNTIFS(BD_Controles!C:C,"Sí",BD_Controles!T:T,"Rojo")'),
        ("Iniciativas en ruta del apetito", '=COUNTIF(Apetito!R6:R15,"Sí*")')]
for i, (a, f) in enumerate(summ):
    put(S, 32 + i, 1, a, bold=True); S.merge_cells(f"A{32+i}:B{32+i}"); put(S, 32 + i, 3, f, bold=True, align=CENTER)

put(S, 38, 1, "Leyenda", bold=True, color=NAVY)
lg = S.cell(row=39, column=1, value="Ingreso"); lg.fill = INFILL; lg.font = font(color="0000FF"); lg.border = BOX
S["B39"] = "Celda que registra la especialidad o el usuario"; S["B39"].font = font()
lg = S.cell(row=40, column=1, value="Fórmula"); lg.fill = GFILL; lg.font = font(); lg.border = BOX
S["B40"] = "Calculada; no editar"; S["B40"].font = font()
for i, k in enumerate(["Verde", "Ámbar", "Rojo", "Sin dato"]):
    c = S.cell(row=41 + i, column=1, value=k); c.fill = PatternFill("solid", fgColor=SEM[k]); c.font = font(bold=True, color=SEMF[k]); c.border = BOX
S["B44"] = "Sin dato = la base no trae el valor (ver Faltantes)"; S["B44"].font = font()
widths(S, [16, 16, 6, 14, 14, 6, 16, 16, 6, 14, 14, 6])

for ws in wb.worksheets:
    ws.sheet_view.zoomScale = 90
wb.save(OUT)
print("ok", len(rows), "controles", C_LAST)
