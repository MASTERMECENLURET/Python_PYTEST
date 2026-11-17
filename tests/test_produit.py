import pytest
from inventaire.produit import Produit


def test_creation_produit(produit_clavier):
    assert produit_clavier.nom == "Clavier"
    assert produit_clavier.prix == 50
    assert produit_clavier.quantite == 10


def test_valeur_stock(produit_clavier):
    assert produit_clavier.valeur_stock() == 500


def test_prix_negatif_leve_erreur():
    with pytest.raises(ValueError):
        Produit("Clavier", -10, 10)