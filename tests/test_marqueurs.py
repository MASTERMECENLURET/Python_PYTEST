import pytest
import os
from inventaire.service_notification import ServiceNotification
from inventaire.produit import Produit


# --- 7.1 : skip -- fonctionnalite pas encore implementee ---------------------


@pytest.mark.skip(reason="Inventaire.valeur_totale() n'est pas encore implementee")
def test_valeur_totale_inventaire(inventaire_avec_produits):
    # Clavier : 50 * 10 = 500, Souris : 20 * 3 = 60
    assert inventaire_avec_produits.valeur_totale() == 560


# --- 7.2 : skipif -- test d'integration soumis a une condition ---------------


@pytest.mark.skipif(
    "NOTIFICATION_API_KEY" not in os.environ,
    reason="necessite la variable d'environnement NOTIFICATION_API_KEY",
)
def test_service_notification_reel():
    service = ServiceNotification()
    assert service.envoyer_alerte_stock_bas(Produit("Clavier", 50, 3)) is True


# --- 7.3 : xfail -- bug connu, pas encore corrige ----------------------------


@pytest.mark.xfail(reason="bug connu : retirer() accepte une quantite negative")
def test_retirer_quantite_negative_leve_erreur(inventaire_avec_produits):
    with pytest.raises(ValueError):
        inventaire_avec_produits.retirer("Clavier", -5)
