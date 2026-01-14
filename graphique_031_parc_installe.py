import csv
import matplotlib.pyplot as plt

DATA = "parc_installe.csv"

def fr(x):
    return float(str(x).replace(",", ".")) if x and x != "NA" else 0.0

annees = []
series = {}

with open(DATA, newline="", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter=";"):
        y = int(r["Date"])
        fil = r["Filière"].strip()
        v = fr(r["Valeur (GW)"])
        series.setdefault(fil, {})[y] = v
        if y not in annees:
            annees.append(y)

annees.sort()

plt.figure()
for fil in sorted(series.keys()):
    vals = [series[fil].get(y, 0.0) for y in annees]
    plt.plot(annees, vals, marker="o", label=fil)

plt.title("Graphique 03 — Évolution du parc installé (GW) - France")
plt.xlabel("Année")
plt.ylabel("Puissance installée (GW)")
plt.legend()
plt.tight_layout()
plt.savefig("graphique_03_parc_installe.png", dpi=200)
plt.show()

