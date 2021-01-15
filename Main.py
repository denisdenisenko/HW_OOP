from CommissionEmployee import CommissionEmployee
from SalariedCommissionEmployee import SalariedCommissionEmployee
from SalariedCommissionEmployeeManager import SalariedCommissionEmployeeManager
from decimal import Decimal

c = CommissionEmployee('Sue', 'Jones', '333-33-333', Decimal('10000.00'), Decimal('0.06'))


cs = SalariedCommissionEmployee('Sue', 'Jones', '333-33-333',
                                Decimal('10000.00'), Decimal('0.06'), 1000)


csm = SalariedCommissionEmployeeManager ('Denis', 'D', '111-11-111',
                                         Decimal('25000.00'),
                                         Decimal('0.03'), 5000,
                                         Decimal('0.10'),Decimal('0.20'))

employees = [c, cs,csm]
for e in employees:
    print(e)
    print(f'{e.earnings():,.2f}\n')
