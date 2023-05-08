
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = (last+first+'@email.com').lower()
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last).capitalize()
    
    def  __str__(self):
        return 'Employee({} {})'.format(self.first, self.last)
    
    def __repr__(self):
        return ('Employee({} {})'.format(self.first, self.last))


emp_1 = Employee('nirajan', 'karki', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())