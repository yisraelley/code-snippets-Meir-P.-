# a = [45, 102, 674, 19, 876, 45]
# temp = a[0]
# for i in range(len(a)-1):
#     a[i] = a[i+1]
# a[len(a)-1] = temp
# print(a)

# a = [-456, 2, -67834, -19, 876, -45]
# max_n = a[0]
# for i in range(len(a)):
#     if max_n < a[i]:
#         max_n = a[i]
# print(max_n)

# a = [456, 102, 67834, 1009, 876, 45]
# for i in range(len(a)):
#     max_digit = a[i] % 10
#     a[i] //= 10
#     while a[i] > 0:
#         if max_digit < a[i] % 10:
#             max_digit = a[i] % 10
#         a[i] //= 10
#     a[i] = max_digit
# print(a)

# a = [456, 102, 67834, 1009, 876, 45]
# for i in range(len(a)):
#     digits_sum = a[i] % 10
#     a[i] //= 10
#     while a[i] > 0:
#         digits_sum += a[i] % 10
#         a[i] //= 10
#     a[i] = digits_sum
# print(a)

# a = [456, 102, 67834, 1009, 876, 45]
# for i in range(len(a)):
#     while a[i] > 9:
#         a[i] //= 10
# print(a)

# a = [456, 12, 67834, 9, 876, 45]
# for i in range(len(a)):
#     digits = 0
#     while a[i] > 0:
#         digits += 1
#         a[i] //= 10
#     a[i] = digits
# print(a)


# def int_to_str(n):
#     st = ""
#     while n > 0:
#         st = chr(ord('0') + n % 10) + st
#         n //= 10
#     return st
#
#
# print(int_to_str(12345) * 2)


# def str_to_int(s):
#     num = 0
#     for i in range(len(s)):
#         num *= 10
#         num += ord(s[i]) - ord('0')
#     return num
#
#
# print(str_to_int("876") + 1)


# rows = 9
# columns = 10
# while rows >= 0:
#     for j in range(rows):
#         print("*", end=" ")
#     j = rows
#     while j < columns:
#         print(rows, end=" ")
#         j += 1
#     print()
#     rows -= 1


# def show(n):
#     for r in range(1, n + 1):
#         for c in range(r):
#             print("*", end=" ")
#         print()


# def mul(a, b):
#     result = 0
#     if a < b:
#         while a > 0:
#             result += b
#             a -= 1
#     else:
#         while b > 0:
#             result += a
#             b -= 1
#     return result


# sum_up = 0
# add_num = 1
# while add_num <= 5:
#     sum_up += add_num
#     add_num += 1
# print(sum_up)


# a = [
#     [3, 5, 6, 6, 9],
#     [3, 5, 4, 1, 2],
#     [7, 4, 5, 6, 7],
#     [1, 2, 3, 4, 0]
# ]
# ordered = 0
# for r in range(len(a)):
#     for c in range(len(a[r]) - 1):
#         if a[r][c] == a[r][c + 1] - 1:
#             ordered += 1
# print(ordered)


# a = [
#     [3, 5, 7, 6, 9],
#     [3, 5, 4, 1, 2, 4, 4, 5],
#     [7, 4, 5, 6, 7, 3],
#     [1, 2, 3],
# ]
# total = 0
# for r in range(len(a)):
#     r_sum = 0
#     for c in range(len(a[r])):
#         r_sum += a[r][c]
#         print(a[r][c], end=" ")
#     print("\t", r_sum)
#     total += r_sum
# print(total)
