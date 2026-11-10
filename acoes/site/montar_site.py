"""Monta dist/: index.html (app.html com motor.js e carteira.js embutidos) + base.json ao lado.
Uso: python site/montar_site.py"""
from pathlib import Path
import shutil
RAIZ = Path(__file__).resolve().parents[1]
dist = RAIZ / "dist"; dist.mkdir(exist_ok=True)
app = (RAIZ / "site" / "app.html").read_text("utf-8")
motor = (RAIZ / "site" / "motor.js").read_text("utf-8")
carteira = (RAIZ / "site" / "carteira.js").read_text("utf-8")
corpo = app.replace("/*MOTOR*/", motor).replace("/*CARTEIRA*/", carteira)
# artifact.html: só o corpo (o publicador do Claude acrescenta o esqueleto).
(dist / "artifact.html").write_text(corpo, "utf-8")
# index.html: documento completo para hospedar como site estático.
(dist / "index.html").write_text(
    '<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    '</head>\n<body>\n' + corpo + '\n</body>\n</html>\n', "utf-8")
shutil.copy(RAIZ / "data" / "base.json", dist / "base.json")
print("dist/index.html e dist/base.json prontos")
