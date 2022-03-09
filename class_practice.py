# practicing with classes! - https://www.youtube.com/watch?v=ZDa-Z5JzLYM and https://www.youtube.com/watch?v=BJ-VvGyQxho
# https://www.youtube.com/watch?v=rq8cL2XMM5M

# instance variables - different per record e.g. name
# class variable - same value for all in the class e.g. everyone getting the same payrise

# regular methods in a class automatically take the instance as the first argument (by convention called self)
# class methods use cls as first argument (class variable name)
# static methods dont pass anything automatically (so more like functions) but they have a logical connection to the
# class

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

    # decorator, causing it to receive class as first variable not self
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # can use class methods as alternative constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee('Jody', 'Broad', 25000)
emp_2 = Employee('Dwayne', 'Johnson', 100000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# how to print employee full name
# print(emp_1.fullname())
#
# # alternative way to print full name
# print(Employee.fullname(emp_2))
#
# # one way to apply a pay rise
# # print(emp_1.pay)
# # emp_1.apply_raise()
# # print(emp_1.pay)
#
#
# # this will just change the raise amount for one single instance (emp_1)
# emp_1.raise_amount = 1.05
#
# # can access in either of these ways
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.__dict__)
# print(emp_1.__dict__)

# print(Employee.num_of_emps)
#
# # using this class method to change the raise amt
# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# # uses class method to break down the string and reassemble into required data
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))

