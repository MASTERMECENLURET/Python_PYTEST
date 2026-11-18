from inventaire.produit import Produit


class ProduitInexistant(Exception):
    """Leve lorsqu'on manipule un produit absent de l'inventaire."""

    pass


class StockInsuffisant(Exception):
    """Leve lorsqu'on tente de retirer plus de stock que ce qui est disponible."""

    pass


class Inventaire:
    """Gere une collection de produits et les operations de stock associees."""

    def __init__(self):
        self._produits: dict[str, Produit] = {}

    def ajouter(self, produit: Produit) -> None:
        self._produits[produit.nom] = produit

    def retirer(self, nom: str, quantite: int) -> None:
        if nom not in self._produits:
            raise ProduitInexistant(f"{nom} n'existe pas")

        produit = self._produits[nom]
        if produit.quantite < quantite:
            raise StockInsuffisant(f"Stock insuffisant pour {nom}")

        produit.quantite -= quantite

    def quantite_totale(self) -> int:
        return sum(p.quantite for p in self._produits.values())
