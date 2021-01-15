from CommissionEmployee import CommissionEmployee
from SalariedCommissionEmployee import SalariedCommissionEmployee
from SalariedCommissionEmployeeManager import SalariedCommissionEmployeeManager
from decimal import Decimal

commission_employee_1 = CommissionEmployee('Gogo', 'Magogo', '333-33-333', Decimal('13000.00'), Decimal('0.06'))
commission_employee_2 = CommissionEmployee('Soso', 'Masoso', '444-44-444', Decimal('12000.00'), Decimal('0.05'))

salaried_commission_employee_1 = SalariedCommissionEmployee('Mono', 'Manono', '111-11-111', Decimal('13000.00'),
                                                            Decimal('0.04'), 1500)
salaried_commission_employee_2 = SalariedCommissionEmployee('Bobo', 'Babobo', '222-22-222', Decimal('14000.00'),
                                                            Decimal('0.05'), 1600)

salaried_commission_employee_manager_1 = SalariedCommissionEmployeeManager('Denis', 'Denisenko', '999-99-999',
                                                                           Decimal('22000.00'),
                                                                           Decimal('0.04'), 7000,
                                                                           Decimal('0.10'), Decimal('0.20'))

salaried_commission_employee_manager_2 = SalariedCommissionEmployeeManager('Donald', 'Trump', '000-00-000',
                                                                           Decimal('21000.00'),
                                                                           Decimal('0.02'), 8000,
                                                                           Decimal('0.10'), Decimal('0.20'))

employees_array = [commission_employee_1, commission_employee_2, salaried_commission_employee_1,
             salaried_commission_employee_2,
             salaried_commission_employee_manager_1, salaried_commission_employee_manager_2]

for e in employees:
    print(e)
    print(f'{e.earnings():,.2f}\n')
