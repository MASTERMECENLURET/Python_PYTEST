from __future__ import annotations

# code suivant nécessaire pour que le script fonctionne correctement lorsqu'il est exécuté directement depuis l'IDE, mais pas nécessaire lorsqu'il est exécuté depuis le terminal à l'aide d'UV
# import sys
# from pathlib import Path

# PROJECT_ROOT = Path(__file__).resolve().parent
# SRC_DIR = PROJECT_ROOT / "src"

# if str(SRC_DIR) not in sys.path:
#     sys.path.insert(0, str(SRC_DIR))

from inventaire.inventaire import Inventaire, ProduitInexistant, StockInsuffisant
from inventaire.produit import Produit


def demo_inventaire() -> None:
    print("=== Démonstration de la classe Inventaire ===\n")

    inventaire = Inventaire()

    produits = [
        Produit("Clavier", 25.0, 10),
        Produit("Souris", 18.5, 3),
        Produit("Casque", 42.0, 5),
    ]

    for produit in produits:
        inventaire.ajouter(produit)

    print(f"Produits enregistrés : {[p.nom for p in inventaire._produits.values()]}")
    print(f"Quantité totale après ajout : {inventaire.quantite_totale()}\n")

    print("Vérification de quantite_totale()")
    print(f"Total attendu : 18 -> total réel : {inventaire.quantite_totale()}\n")

    print("Retrait de produits")
    inventaire.retirer("Clavier", 2)
    print(f"Clavier restant : {inventaire._produits['Clavier'].quantite}")
    print(f"Quantité totale après retrait : {inventaire.quantite_totale()}\n")

    print("Gestion des erreurs")
    try:
        inventaire.retirer("Souris", 99)
    except StockInsuffisant as exc:
        print(f"Erreur de stock : {exc}")

    try:
        inventaire.retirer("Ordinateur", 1)
    except ProduitInexistant as exc:
        print(f"Erreur de produit : {exc}")


if __name__ == "__main__":
    demo_inventaire()