import pytest
from inventaire.produit import Produit
from inventaire.inventaire import Inventaire


@pytest.fixture
def produit_clavier():
    return Produit("Clavier", 50, 10)


@pytest.fixture
def inventaire_avec_produits(produit_clavier):
    inv = Inventaire()
    inv.ajouter(produit_clavier)
    inv.ajouter(Produit("Souris", 20, 3))
    return inv