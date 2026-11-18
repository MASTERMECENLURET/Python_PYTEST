from inventaire.produit import Produit


class ProduitInexistant(Exception):
    def __init__(self, nom: str):
        self.nom = nom
        message = f"Le produit '{nom}' est introuvable dans l'inventaire."
        super().__init__(message)


class StockInsuffisant(Exception):
    def __init__(self, nom: str, quantite_demande: int, quantite_disponible: int):
        self.nom = nom
        self.quantite_demande = quantite_demande
        self.quantite_disponible = quantite_disponible
        message = (
            f"Stock insuffisant pour '{nom}' : "
            f"demande {quantite_demande}, disponible {quantite_disponible}."
        )
        super().__init__(message)


class Inventaire:
    def __init__(self):
        self._produits: dict[str, Produit] = {}

    def ajouter(self, produit: Produit) -> None:
        self._produits[produit.nom] = produit

    def quantite_totale(self) -> int:
        return sum(p.quantite for p in self._produits.values())

    def retirer(self, nom: str, quantite: int) -> None:
        if nom not in self._produits:
            raise ProduitInexistant(nom)

        produit = self._produits[nom]

        if produit.quantite < quantite:
            raise StockInsuffisant(nom, quantite, produit.quantite)

        produit.quantite -= quantite
