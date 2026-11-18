import pytest
from inventaire.inventaire import Inventaire, StockInsuffisant, ProduitInexistant
from cas_produits import CAS_PRODUITS


@pytest.mark.parametrize("produit", CAS_PRODUITS)
def test_inventaire_avec_produit(inventaire_avec_produits, produit):
    nom = produit["nom"]
    quantite_initiale = produit["quantite"]

    assert isinstance(inventaire_avec_produits, Inventaire)
    assert len(inventaire_avec_produits._produits) == len(CAS_PRODUITS)
    assert inventaire_avec_produits._produits[nom].quantite == quantite_initiale
    assert inventaire_avec_produits.quantite_totale() == sum(
        p["quantite"] for p in CAS_PRODUITS
    )


@pytest.mark.parametrize("quantite_retiree", [1, 5, 10])
def test_retirer_quantite_valide(inventaire_avec_produits, quantite_retiree):
    inventaire_avec_produits.retirer("Clavier", quantite_retiree)
    produit = inventaire_avec_produits._produits["Clavier"]
    assert produit.quantite == 10 - quantite_retiree


@pytest.mark.parametrize(
    "nom,quantite",
    [
        ("Clavier", 100),
        ("Souris", 10),
    ],
)
def test_retirer_stock_insuffisant(inventaire_avec_produits, nom, quantite):
    with pytest.raises(StockInsuffisant):
        inventaire_avec_produits.retirer(nom, quantite)


def test_retirer_produit_inexistant(inventaire_avec_produits):
    with pytest.raises(ProduitInexistant):
        inventaire_avec_produits.retirer("Webcam", 1)
