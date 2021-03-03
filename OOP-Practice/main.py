#!/usr/bin/python3

from classes import person
from classes import employee

person1 = person.Person('Abdullah Al', "Mamun", 26)
print(person1.get_summary())

employee1 = employee.Employee("Monwar", "Adeeb", 25, 19)
print(employee1.get_summary())
