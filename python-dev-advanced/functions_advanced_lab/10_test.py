# def fact(n):
#     if n == 1:
#         return 1
#     res = fact(n - 1)
#     return n * res
#
# print(fact(5)) # 120
#
# """
# print(fact(5)) -> #120         # first we have to fill the stack
#                                     then we pop the result
#     fact(5)
#         5 * fact(4) -> 5*(24) -> 120
#             4 * fact(3) -> 4*(6) -> return 24
#                 3 * fact(2) -> 3*(2)=6 -> return 6
#                     2 * fact(1) -> 2*(1)=2 -> return 2
#                         fact(1) -> return 1
# """

