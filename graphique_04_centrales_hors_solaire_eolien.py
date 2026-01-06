import csv
import matplotlib.pyplot as plt

DATA = "R_C3_A9partition_des_principales_installations_de_production_d_27_C3_A9lectricit_C3_A9_en_France_2C_hors_solaire_et__C3_A9olien__2025-12-18_13-22.csv"

def fr(x): return float(str(x).replace(",", ".")) if x else 0.0

points = {} 
with open(DATA, newline="", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter=";"):
        fil = r["Filière"].strip()
        lon = float(r["Longitude"])
        lat = float(r["Latitude"])
        mw = fr(r["Valeur (MW)"])
        points.setdefault(fil, ([], [], []))
        points[fil][0].append(lon)
        points[fil][1].append(lat)
        points[fil][2].append(max(10, mw / 200)) 
plt.figure()
for fil in sorted(points.keys()):
    lons, lats, sizes = points[fil]
    plt.scatter(lons, lats, s=sizes, label=fil, alpha=0.7)

plt.title("Graphique 04 — Installations principales (hors solaire/éolien)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.tight_layout()
plt.savefig("graphique_04_centrales_hors_solaire_eolien.png", dpi=200)
plt.show()
