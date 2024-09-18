from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self,new_employee):
        self.employees.append(new_employee)
    
    def display_employees(self):
        print('Current Employees:')
        for emp in self.employees:
            print(emp.fname, emp.lname)
        print('-----------------')
    
    def pay_employees(self):
        print('Paying Employees:')
        for emp in self.employees:
            print('Paycheck for: ', emp.fname, emp.lname)
            print(f'Amount: ${emp.calculate_paycheck():,.2f}')


def main():
    my_company = Company()

    employee1 = SalaryEmployee('Sarah', 'Hess', 6000)
    employee2 = HourlyEmployee('Chi', 'Ht', 40, 3)
    employee3 = CommissionEmployee('Htv', 'Gh', 25000, 100, 10)

    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()


main()

