import csv
import matplotlib.pyplot as plt

DATA = "_C3_89volution_du_parc_install_C3_A9_de_production_d_27_C3_A9lectricit_C3_A9_en_France_2025-12-18_13-39.csv"

def fr(x): return float(str(x).replace(",", ".")) if x else 0.0

years = []
series = {} 
with open(DATA, newline="", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter=";"):
        y = int(r["Date"])
        fil = r["Filière"].strip()
        v = fr(r["Valeur (GW)"])
        series.setdefault(fil, {})[y] = v
        if y not in years:
            years.append(y)

years.sort()

plt.figure()
for fil in sorted(series.keys()):
    vals = [series[fil].get(y, 0.0) for y in years]
    plt.plot(years, vals, label=fil)

plt.title("Graphique 03 — Évolution du parc installé (GW) - France")
plt.xlabel("Année")
plt.ylabel("Puissance installée (GW)")
plt.legend()
plt.tight_layout()
plt.savefig("graphique_03_parc_installe.png", dpi=200)
plt.show()
