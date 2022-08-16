class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} = {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


dev_1 = Developer('Skinny', 'Dennis', 80000, 'Python')
dev_2 = Developer('Valds', 'Chillum', 230000, 'Java')
emp_1 = Employee('Jim', 'Lerdal', 80000)
emp_2 = Employee('Angie', 'Lerdal', 50000)

mgr_1 = Manager('Jeff', 'Halloween', 90000, [dev_1])


print("Hello")

print(emp_1 + emp_2)
#print(emp_1.__str__())
#print(emp_1.__repr__())

#mgr_1.add_emp(dev_2)
#mgr_1.print_emps()

#print(isinstance(mgr_1, Developer))

#print(dev_1.prog_lang)
#dev_1.apply_raise()
#print(dev_1.pay)

#emp_1.raise_amount = 1.05
#print(emp_1.__dict__)
#print(Employee.__dict__)