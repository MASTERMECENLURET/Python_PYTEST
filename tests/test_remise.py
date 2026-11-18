import pytest
from inventaire.remise import RemisePourcentage, RemiseFixe
from cas_remise import CASES


@pytest.mark.parametrize("cas", CASES, ids=[cas["nom"] for cas in CASES])
def test_appliquer_remise(cas):
    if cas["type"] == "pourcentage":
        remise = RemisePourcentage(cas["valeur"])
    else:
        remise = RemiseFixe(cas["valeur"])

    assert remise.appliquer(100) == cas["attendu"]
