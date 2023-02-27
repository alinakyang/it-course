class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "Name: {}, salary: {}".format(self.name, self.salary)

    def up_salary(self):
        return 1.3 * self.salary


class Manager(Employee):
    def up_salary(self, bonus):
        self.salary = super().up_salary()
        self.salary *= 1 + bonus


obj = Manager('Иван', 1700)
obj.up_salary(0.25)
print(obj)
