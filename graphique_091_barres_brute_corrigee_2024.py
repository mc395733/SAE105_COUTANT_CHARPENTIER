import csv
import matplotlib.pyplot as plt

DATA = "conso_brute_corrigee.csv"
ANNEE = 2024

def fr(x):
    return float(str(x).replace(",", ".")) if x and x != "NA" else 0.0

mois = list(range(1, 13))
brute = [0.0] * 12
corrigee = [0.0] * 12

with open(DATA, newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    for date_str, filiere, valeur, _ in reader:
        if not date_str:
            continue
        annee = int(date_str[:4])
        if annee != ANNEE:
            continue
        m = int(date_str[5:7])
        i = m - 1
        fil = filiere.strip('"')
        if fil == "Consommation brute":
            brute[i] += fr(valeur)
        elif fil == "Consommation corrigée":
            corrigee[i] += fr(valeur)

x = range(1, 13)
largeur = 0.35

plt.figure()
plt.bar([i - largeur/2 for i in x], brute, width=largeur, label="Brute")
plt.bar([i + largeur/2 for i in x], corrigee, width=largeur, label="Corrigée")

plt.title("Graphique 09 — Consommation brute et corrigée par mois (France " + str(ANNEE) + ")")
plt.xlabel("Mois")
plt.ylabel("Consommation (TWh)")
plt.xticks(x, ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun", "Jul", "Aoû", "Sep", "Oct", "Nov", "Déc"])
plt.legend()
plt.tight_layout()
plt.savefig("graphique_09_barres_brute_corrigee_2024.png", dpi=200)
plt.show()

