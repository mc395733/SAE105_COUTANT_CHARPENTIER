import csv
import matplotlib.pyplot as plt

DATA = "conso_hebdomadaire.csv"

def fr(x):
    return float(str(x).replace(",", ".")) if x and x != "NA" else 0.0

semaines = []
valeurs = []

with open(DATA, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=";")
    for r in reader:
        if r.get("maille") == "semaine" and r.get("annee") == "2025":
            s_txt = r.get("semaine", "").strip()
            if not s_txt.isdigit():
                continue
            s = int(s_txt)
            v = fr(r.get("conso_corrigee"))
            semaines.append(s)
            valeurs.append(v)

if not semaines:
    raise SystemExit("Aucune donnée trouvée pour l'année 2025 dans conso_hebdomadaire.csv")

semaines, valeurs = zip(*sorted(zip(semaines, valeurs)))

plt.figure()
plt.plot(semaines, valeurs, marker="o")
plt.title("Graphique 05 — Consommation hebdomadaire corrigée (France 2025)")
plt.xlabel("Semaine")
plt.ylabel("Consommation corrigée (MW moyens)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graphique_05_conso_hebdomadaire_2025.png", dpi=200)
plt.show()

