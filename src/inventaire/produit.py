class Produit:
    """Represente un produit du magasin, avec son prix et sa quantite en stock."""

    def __init__(self, nom: str, prix: float, quantite: int = 0):
        if prix < 0:
            raise ValueError("Le prix ne peut pas etre negatif")
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def valeur_stock(self) -> float:
        """Valeur totale du stock de ce produit (prix * quantite)."""
        return self.prix * self.quantite