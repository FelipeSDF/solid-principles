

from abc import ABC, abstractmethod


class TaxesCalculator(ABC):

    @abstractmethod
    def calculate(self, mount):
        pass


class BrasilianTarifsCalculator(TaxesCalculator):
    def calculate(self, mount) -> float:
        return mount * 0.01


class AmericanTarifsCalculator(TaxesCalculator):
    def calculate(self, mount) -> float:
        return mount * 0.1


brasilianCalculator = BrasilianTarifsCalculator()
americanCalculator = AmericanTarifsCalculator()

if __name__ == '__main__':

    tarifInBrazil = brasilianCalculator.calculate(100)
    tarifInUnitedStates = americanCalculator.calculate(100)

    print(f'with tarifs in Brazil, you have {100 - tarifInBrazil}')
    print(
        f'with tarifs of Uniteds States of America, you have: {100 - tarifInUnitedStates}')
