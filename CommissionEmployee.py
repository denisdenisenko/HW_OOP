"""CommissionEmployee base class."""
from decimal import Decimal


class CommissionEmployee:
    """An employee who gets paid commission based on gross sales."""

    def __init__(self, first_name, last_name, ssn,  # ssn stands for social security number
                 gross_sales, commission_rate):
        # Initialize CommissionEmployee's attributes
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales  # validate via property
        self.commission_rate = commission_rate  # validate via property

    @property
    def first_name(self):
        """first_name getter"""
        return self._first_name

    @property
    def last_name(self):
        """last_name getter"""
        return self._last_name

    @property
    def ssn(self):
        """ssn getter"""
        return self._ssn

    @property
    def gross_sales(self):
        """gross sales getter"""
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        """gross sales setter"""
        # Set gross sales or raise ValueError if invalid
        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= to 0')

        self._gross_sales = sales

    @property
    def commission_rate(self):
        """commission rate getter"""
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, rate):
        """Set commission rate or raise ValueError if invalid."""
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError(
                'Interest rate must be greater than 0 and less than 1')

        self._commission_rate = rate

    def earnings(self):
        """Calculate earnings."""
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        """Return string representation for repr()."""
        return ('CommissionEmployee: ' +
                f'{self.first_name} {self.last_name}\n' +
                f'Social security number: {self.ssn}\n' +
                f'Gross sales: {self.gross_sales:.2f}\n' +
                f'Commission rate: {self.commission_rate:.2f}')
