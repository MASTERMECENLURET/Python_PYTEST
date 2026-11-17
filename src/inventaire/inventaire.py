from inventaire.produit import Produit


class Inventaire:
    def __init__(self ):
        self ._produits: dict[str, Produit] = {}

    def ajouter(self , produit: Produit) -> None :
        self ._produits[produit.nom] = produit

    def quantite_totale(self ) -> int:
        return sum(p.quantite for p in self ._produits.values())
