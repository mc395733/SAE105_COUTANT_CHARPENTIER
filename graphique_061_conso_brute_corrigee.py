import csv
import matplotlib.pyplot as plt

DATA = "conso_brute_corrigee.csv"

def fr(x):
    return float(str(x).replace(",", ".")) if x and x != "NA" else 0.0

annees = []
brute = []
corrigee = []

with open(DATA, newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    for date_str, filiere, valeur, _ in reader:
        if not date_str:
            continue
        annee = int(date_str[:4])
        if annee < 1995 or annee > 2025:
            continue
        if filiere.strip('"') == "Consommation brute":
            if annee not in annees:
                annees.append(annee)
                brute.append(0.0)
                corrigee.append(0.0)
            i = annees.index(annee)
            brute[i] += fr(valeur)
        elif filiere.strip('"') == "Consommation corrigée":
            if annee not in annees:
                annees.append(annee)
                brute.append(0.0)
                corrigee.append(0.0)
            i = annees.index(annee)
            corrigee[i] += fr(valeur)

if not annees:
    raise SystemExit("Aucune donnée trouvée dans conso_brute_corrigee.csv")

annees, brute, corrigee = zip(*sorted(zip(annees, brute, corrigee)))

plt.figure()
plt.plot(annees, brute, marker="o", label="Consommation brute")
plt.plot(annees, corrigee, marker="o", label="Consommation corrigée")
plt.title("Graphique 06 — Consommation brute et corrigée (France)")
plt.xlabel("Année")
plt.ylabel("Consommation (TWh)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graphique_06_conso_brute_corrigee.png", dpi=200)
plt.show()

