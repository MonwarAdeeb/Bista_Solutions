from classes import person as p


class Employee(p.Person):

    def __init__(self, first_name, last_name, age, employee_id):
        super().__init__(first_name, last_name, age)
        self.employee_id = employee_id

    def get_summary(self):
        return f"{super().get_summary()}, Employee ID: {self.employee_id}\n"