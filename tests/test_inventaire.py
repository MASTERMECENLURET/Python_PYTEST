import pytest
from inventaire.inventaire import Inventaire, StockInsuffisant, ProduitInexistant
from cas_produits import CAS_PRODUITS
from inventaire.produit import Produit


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


def test_alerte_declenchee_si_stock_bas(mocker):
    notifier = mocker.Mock()
    inv = Inventaire(notifier=notifier)
    inv.ajouter(Produit("Clavier", 50, 6))

    inv.retirer("Clavier", 2)  # stock passe a 4, sous le seuil de 5

    notifier.envoyer_alerte_stock_bas.assert_called_once()


def test_pas_d_alerte_si_stock_suffisant(mocker):
    notifier = mocker.Mock()
    inv = Inventaire(notifier=notifier)
    inv.ajouter(Produit("Clavier", 50, 20))
    inv.retirer("Clavier", 2)  # stock passe a 18, au-dessus du seuil

    notifier.envoyer_alerte_stock_bas.assert_not_called()


def test_alerte_envoyee_avec_le_bon_produit(mocker):
    """Bonus : verifie que le mock recoit bien l'argument attendu."""
    notifier = mocker.Mock()
    inv = Inventaire(notifier=notifier)
    produit = Produit("Clavier", 50, 6)
    inv.ajouter(produit)

    inv.retirer("Clavier", 2)

    notifier.envoyer_alerte_stock_bas.assert_called_once_with(produit)
