import pytest
from inventaire.inventaire import Inventaire


def test_inventaire_avec_produit(inventaire_avec_produits):
    assert isinstance(inventaire_avec_produits, Inventaire)
    assert len(inventaire_avec_produits._produits) == 2
    assert inventaire_avec_produits._produits["Clavier"].quantite == 10
    assert inventaire_avec_produits._produits["Souris"].quantite == 3
    assert inventaire_avec_produits.quantite_totale() == 13