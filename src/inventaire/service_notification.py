from inventaire.produit import Produit


class ServiceNotification:
    def envoyer_alerte_stock_bas(self, produit: Produit) -> bool:
        # Simule un appel reseau reel ( API SMS / email )
        ...
        return True
