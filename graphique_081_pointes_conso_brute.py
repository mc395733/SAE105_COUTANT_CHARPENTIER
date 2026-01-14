import csv
import matplotlib.pyplot as plt

DATA = "pointes_conso_brute.csv"

def fr(x):
    return float(str(x).replace(",", ".")) if x and x != "NA" else 0.0

annees = []
pointes = []

with open(DATA, newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    for date_str, libelle, valeur in reader:
        if not date_str:
            continue
        annee = int(date_str[:4])
        annees.append(annee)
        pointes.append(fr(valeur))

if not annees:
    raise SystemExit("Aucune donnée trouvée dans pointes_conso_brute.csv")

annees, pointes = zip(*sorted(zip(annees, pointes)))

plt.figure()
plt.stem(annees, pointes)
plt.title("Graphique 08 — Pointes de consommation brute d'électricité (France)")
plt.xlabel("Année")
plt.ylabel("Pointe de consommation (GW)")
plt.tight_layout()
plt.savefig("graphique_08_pointes_conso_brute.png", dpi=200)
plt.show()


