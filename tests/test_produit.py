import pytest
from inventaire.produit import Produit


def test_creation_produit():
    p = Produit("Clavier", 50, 10)
    assert p.nom == "Clavier"
    assert p.prix == 50
    assert p.quantite == 10


def test_valeur_stock():
    p = Produit("Clavier", 50, 10)
    assert p.valeur_stock() == 500