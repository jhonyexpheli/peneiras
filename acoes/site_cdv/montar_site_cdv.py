"""Versão de apresentação ao Clube do Valor (layout, paleta e fontes do Clube, sem logotipo).
Monta dist_cdv/: index.html e artifact.html (site_cdv/app.html com site/motor.js e site_cdv/carteira.js embutidos) + base.json.
A versão original (site/) não é alterada. Uso: python site_cdv/montar_site_cdv.py"""
from pathlib import Path
import shutil
RAIZ = Path(__file__).resolve().parents[1]
dist = RAIZ / "dist_cdv"; dist.mkdir(exist_ok=True)
app = (RAIZ / "site_cdv" / "app.html").read_text("utf-8")
motor = (RAIZ / "site" / "motor.js").read_text("utf-8")
carteira = (RAIZ / "site_cdv" / "carteira.js").read_text("utf-8")
corpo = app.replace("/*MOTOR*/", motor).replace("/*CARTEIRA*/", carteira)
(dist / "artifact.html").write_text(corpo, "utf-8")
(dist / "index.html").write_text(
    '<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    '</head>\n<body>\n' + corpo + '\n</body>\n</html>\n', "utf-8")
shutil.copy(RAIZ / "data" / "base.json", dist / "base.json")
print("dist_cdv/index.html e dist_cdv/base.json prontos")
