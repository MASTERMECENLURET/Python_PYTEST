import pytest
from inventaire.produit import Produit
from inventaire.inventaire import Inventaire


@pytest.fixture
def produit_clavier():
    return Produit("Clavier", 50, 10)


@pytest.fixture
def inventaire_avec_produits():
    inv = Inventaire()
    inv.ajouter(Produit("Clavier", 50, 10))
    inv.ajouter(Produit("Souris", 20, 3))
    return inv