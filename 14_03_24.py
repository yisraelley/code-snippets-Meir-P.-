# def dividers(n):
#     max_divider = n // 2
#     i = 2
#     while i <= max_divider:
#         if n % i == 0:
#             print(i, end=" ")
#         i += 1
#
#
# def is_primary(n):
#     max_divider = n // 2
#     i = 2
#     while i <= max_divider:
#         if n % i == 0:
#             break
#         i += 1
#     if i > max_divider:
#         print("YES")
#     else:
#         print("NO")
#
#
# def hiluk(x, y):
#     result = 0
#     remainder = x
#     while remainder >= y:
#         remainder -= y
#         result += 1
#     print(x, "/", y, " = ", result, "\t", x, "%", y, " = ", remainder)
#
#
# def mult(x, y):
#     result = 0
#     times = y
#     while times > 0:
#         result += x
#         times -= 1
#     print(x, "*", y, " = ", result)
#
#
# def series_printer(start, stop, step):
#     for i in range(start, stop, step):
#         print(i, end=" ")
#
#
# def numbers_printer(n):
#     for i in range(n):
#         print(i, end=" ")
#
#
# arr = [0, 3, 5, 4, -7, 9, 8, 1, 0, 69]
# max_num = arr[0]
# i = 1
# while i < len(arr):
#     if arr[i] > max_num:
#         max_num = arr[i]
#     i += 1
# print(max_num)
