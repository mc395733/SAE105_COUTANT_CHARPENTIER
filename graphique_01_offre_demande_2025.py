import csv
from datetime import datetime
import matplotlib.pyplot as plt

PROD = "evolutionproduction.csv"
CONSO = "evolutionconsommation.csv"

def fr(x): return float(str(x).replace(",", ".")) if x else 0.0

prod = {}
with open(PROD, newline="", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter=";"):
        if r.get("Date","").startswith("2025") and r.get("Filière","") == "Production totale":
            m = r["Date"][:7]
            prod[m] = prod.get(m, 0.0) + fr(r.get("Valeur (TWh)",""))

conso = {}
with open(CONSO, newline="", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter=";"):
        if r.get("maille") == "semaine" and r.get("annee") == "2025":
            m = datetime.strptime(r["date_jour"], "%Y-%m-%d").strftime("%Y-%m")
            twh = fr(r.get("conso_corrigee","")) * 168 / 1_000_000
            conso[m] = conso.get(m, 0.0) + twh

mois = sorted(set(prod) & set(conso))
plt.plot(mois, [prod[m] for m in mois], marker="o", label="Production (TWh)")
plt.plot(mois, [conso[m] for m in mois], marker="o", label="Consommation (TWh)")
plt.title("Graphique 01 — Offre et demande (France 2025)")
plt.xlabel("Mois")
plt.ylabel("Énergie (TWh)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("graphique_01_offre_demande_2025.png", dpi=200)
plt.show()
