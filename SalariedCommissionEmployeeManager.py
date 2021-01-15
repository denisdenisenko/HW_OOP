from decimal import Decimal
from SalariedCommissionEmployee import SalariedCommissionEmployee


class SalariedCommissionEmployeeManager(SalariedCommissionEmployee):
    """An employee who gets paid a salary plus
    commission based on gross sales."""

    def __init__(self, first_name, last_name, ssn,
                 gross_sales, commission_rate, base_salary, ratio1, ratio2):
        """Initialize SalariedCommissionEmployeeManager's attributes."""
        super().__init__(first_name, last_name, ssn,
                         gross_sales, commission_rate, base_salary)
        self.ratio1 = ratio1
        self.ratio2 = ratio2

    @property
    def ratio1(self):
        return self._ratio1

    @property
    def ratio2(self):
        return self._ratio2

    @ratio1.setter
    def ratio1(self, ratio):
        """Set ratio1 or raise ValueError if invalid."""
        if (ratio < Decimal('0.00')) and (ratio > Decimal("100.00")):
            raise ValueError('Ratio must be >= to 0 and <= than 100')
        self._ratio1 = ratio

    @ratio2.setter
    def ratio2(self, ratio):
        """Set ratio2 or raise ValueError if invalid."""
        if (ratio < Decimal('0.00')) and (ratio > Decimal("100.00")):
            raise ValueError('Ratio must be >= to 0 and <= than 100')
        self._ratio2 = ratio

    def bonus_for_managing(self):
        return self.ratio1 * self.base_salary + self.ratio2 * self.gross_sales

    def earnings(self):
        """Calculate earnings."""
        return super().earnings() + self.bonus_for_managing()

    def __repr__(self):
        """Return string representation for repr()."""
        return ('Salaried' + super().__repr__() +
                f'\nBonus for managing : {self.bonus_for_managing():.2f}')
