import pytest
from inventaire.inventaire import Inventaire


@pytest.mark.parametrize(
    ("nom", "quantite_initiale"),
    [
        ("Clavier", 10),
        ("Souris", 3),
        ("Tapis", 15),
        ("Lampe", 25),
    ],
)
def test_inventaire_avec_produit(inventaire_avec_produits, nom, quantite_initiale):
    assert isinstance(inventaire_avec_produits, Inventaire)
    assert len(inventaire_avec_produits._produits) == 4
    assert inventaire_avec_produits._produits[nom].quantite == quantite_initiale
    assert inventaire_avec_produits.quantite_totale() == 53