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


def test_isolation_entre_tests(produit_clavier):
    produit_clavier.quantite = 0
    assert produit_clavier.quantite == 0


def test_quantite_inchangee_par_le_test_precedent(produit_clavier):
    assert produit_clavier.quantite == 10  # toujours 10 !