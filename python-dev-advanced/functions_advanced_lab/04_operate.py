# """Write a function called operate that receives
# an operator(+, -, * or /) as first argument and
# multiple numbers as additional arguments (*args).
# The function should return the result of the operator
# applied to all the numbers. For more clarification,
# see the examples below. Submit only the function in the judge system.
# Note: Be careful when you have multiplication and division
#
# -----# TEST CODE #------ -----# OUTPUT #------# COMMENT #----
# print(operate("+", 1, 2, 3))	 6	        1 + 2 + 3 = 6
# print(operate("*", 3, 4))	     12	        3 * 4 = 12
#
# judge -> https://judge.softuni.bg/Contests/Practice/Index/1838#3
#
# """
#
# def operate(operator, *numbers):
#
#     # first check for operator !!! "*" and "/" - result cannot be
#     # zero as starting value
#     def get_initial_value(operator):
#         if operator in ("+", "-"):
#             return 0
#         else:
#             return 1
#
#     result = get_initial_value(operator)
#
#     for x in numbers:
#         if operator == "+":
#             result += x
#         elif operator == "-":
#             result -= x
#         elif operator == "*":
#             result = result * x
#         else:
#             result = result / x
#
#     return result
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
# print(operate("-", 1, 2, 3))
# print(operate("/", 3, 4))
#
# """
# 6
# 12
# -6
# 0.08333333333333333
# """
#
from functools import reduce


def operate(op,*args):
    if op == "+":
        return reduce(lambda a, b: a + b, args)
    if op == "-":
        return reduce(lambda a, b: a - b, args)
    if op == "*":
        return reduce(lambda a, b: a * b, args)
    if op == "/":
        return reduce(lambda a, b: a / b, args)
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
# print(operate("-", 1, 2, 3))
# print(operate("/", 3, 4))
#
# """
# 6
# 12
# -4
# 0.75
# """