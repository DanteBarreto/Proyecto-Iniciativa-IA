"""Genera herramienta_gobierno_ia.html a partir de la plantilla y del JSON de configuración.

Uso:  python build_herramienta.py
Lee:  herramienta.src.html, data/config_gobierno_ia.json, logo.svg.html
Escribe: herramienta_gobierno_ia.html (autocontenido, funciona sin servidor)
"""
import json
from pathlib import Path

base = Path(__file__).parent
src = (base / "herramienta.src.html").read_text(encoding="utf-8")
cfg = json.loads((base / "data" / "config_gobierno_ia.json").read_text(encoding="utf-8"))
logo = (base / "logo.svg.html").read_text(encoding="utf-8")
defs, svg = logo.split("\n", 1)

# Validaciones mínimas antes de generar
assert len(cfg["niveles"]) == 5, "Se esperan 5 niveles N1–N5"
assert sum(len(d["metricas"]) for d in cfg["dimensiones"]) >= 1
for n in cfg["niveles"]:
    assert n["slaMax"] is not None and (n["slaMin"] is None or n["slaMin"] <= n["slaMax"]), n["id"]

data = json.dumps(cfg, ensure_ascii=False, indent=1).replace("</", "<\\/")
out = src.replace("/*CONFIG*/", data).replace("<!--LOGO_DEFS-->", defs).replace("<!--LOGO_SVG-->", svg)
(base / "herramienta_gobierno_ia.html").write_text(out, encoding="utf-8")
print("OK:", cfg["meta"]["documento"], "·", sum(len(d["metricas"]) for d in cfg["dimensiones"]), "métricas")
