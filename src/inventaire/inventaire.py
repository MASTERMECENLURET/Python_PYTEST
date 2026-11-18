from inventaire.produit import Produit
from inventaire.service_notification import ServiceNotification


class ProduitInexistant(Exception):
    """Leve lorsqu'on manipule un produit absent de l'inventaire."""

    pass


class StockInsuffisant(Exception):
    """Leve lorsqu'on tente de retirer plus de stock que ce qui est disponible."""

    pass


class Inventaire:
    """Gere une collection de produits et les operations de stock associees."""

    SEUIL_ALERTE_STOCK_BAS = 5

    def __init__(self, notifier: ServiceNotification | None = None):
        self._produits: dict[str, Produit] = {}
        self._notifier = notifier or ServiceNotification()

    def ajouter(self, produit: Produit) -> None:
        self._produits[produit.nom] = produit

    def retirer(self, nom: str, quantite: int) -> None:
        if quantite <= 0:
            raise ValueError("La quantite doit etre strictement positive")
        if nom not in self._produits:
            raise ProduitInexistant(f"{nom} n'existe pas")

        produit = self._produits[nom]
        if produit.quantite < quantite:
            raise StockInsuffisant(f"Stock insuffisant pour {nom}")

        produit.quantite -= quantite
        if produit.quantite < self.SEUIL_ALERTE_STOCK_BAS:
            self._notifier.envoyer_alerte_stock_bas(produit)

    def quantite_totale(self) -> int:
        return sum(p.quantite for p in self._produits.values())
