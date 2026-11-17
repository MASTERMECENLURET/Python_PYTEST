import pytest

from inventaire.produit import Produit


@pytest.fixture
def produit_clavier():
    return Produit("Clavier", 50, 10)