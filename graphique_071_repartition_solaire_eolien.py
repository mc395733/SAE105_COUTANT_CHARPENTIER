import csv
import matplotlib.pyplot as plt

DATA = "repartition_solaire_eolien_dept.csv"

def fr(x):
    return float(str(x).replace(",", ".")) if x and x != "NA" else 0.0

points = {}

with open(DATA, newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    for nom_dep, lon, lat, filiere, valeur in reader:
        fil = filiere.strip('"')
        x = float(lon)
        y = float(lat)
        mw = fr(valeur)
        points.setdefault(fil, ([], [], []))
        points[fil][0].append(x)
        points[fil][1].append(y)
        points[fil][2].append(max(10, mw / 5))

plt.figure()
for fil in sorted(points.keys()):
    xs, ys, sizes = points[fil]
    plt.scatter(xs, ys, s=sizes, alpha=0.7, label=fil)

plt.title("Graphique 07 — Répartition solaire et éolien (France, départements)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.tight_layout()
plt.savefig("graphique_07_repartition_solaire_eolien.png", dpi=200)
plt.show()

