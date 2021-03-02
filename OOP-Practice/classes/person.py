from classes import get_time as t

class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        global day

    def get_summary(self):
        day = t.time_now.strftime("%A")
        full_name = self.first_name + ' ' + self.last_name
        return f"Today is {day} \n{t.time_now.strftime('%B %d, %Y')} \n{full_name}'s age is {self.age}"