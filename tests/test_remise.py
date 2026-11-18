import pytest

from inventaire.remise import RemiseFixe, RemisePourcentage


@pytest.mark.parametrize("remise,attendu", [
    (RemisePourcentage(10), 90),
    (RemisePourcentage(50), 50),
    (RemiseFixe(20), 80),
    (RemiseFixe(150), 0),
], ids=["10pct", "50pct", "fixe_20", "fixe_superieure_au_prix"])
def test_appliquer_remise(remise, attendu):
    assert remise.appliquer(100) == attendu