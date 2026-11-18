from abc import ABC, abstractmethod


class Remise(ABC):
    @abstractmethod
    def appliquer(self, prix: float) -> float: ...


class RemisePourcentage(Remise):
    def __init__(self, pourcentage: float):
        self.pourcentage = pourcentage

    def appliquer(self, prix: float) -> float:
        return prix * (1 - self.pourcentage / 100)


class RemiseFixe(Remise):
    def __init__(self, montant: float):
        self.montant = montant

    def appliquer(self, prix: float) -> float:
        return max(0, prix - self.montant)
