import math
import random

# def plus_minus_sum(n):
#     numbers_sum = 0
#     i = 1
#     while i < n:
#         if i % 2 == 0:
#             numbers_sum -= i
#             print(i, " + ", end=" ")
#         else:
#             numbers_sum += i
#             print(i, " - ", end=" ")
#         i += 1
#     if n % 2 == 0:
#         numbers_sum -= n
#     else:
#         numbers_sum += n
#     print(n, " = ", numbers_sum)
#     return numbers_sum


# def series_sum(n):
#     result = 0
#     i = 1
#     while i <= n:
#         result += i
#         i += 1
#     return result


# def is_prime(n):
#     if n % 2 == 0:
#         print("NO")
#     else:
#         sqrt_n = int(math.sqrt(n))
#         i = 3
#         while i <= sqrt_n:
#             if n % i == 0:
#                 print("NO")
#                 break
#             i += 2
#         if i > sqrt_n:
#             print("YES")


# def show_dividers(n):
#     sqrt_n = int(math.sqrt(n))
#     for i in range(2, sqrt_n+1):
#         if i == n/i:
#             print(i)
#             break
#         if n % i == 0:
#             print(i, n // i, end=" ")


# def mul(x, y):
#     result = 0
#     while y > 0:
#         result += x
#         y -= 1
#     return result


# def hezka(x, y):
#     result = 1
#     while y > 0:
#         result = mul(result, x)
#         y = y - 1
#     return result


# '''
# אביב תשפ"א – 2021 – מועד א'
# שאלה 1
# כתוב קטע תוכנית שיקלוט 40 מספרים חיוביים ושלמים:
#                          א. עבור כל מספר תלת ספרתי שנקלט, יש להדפיס את סכום ספרותיו.
#     ב. על הקוד לחשב ולהדפיס את כמות המספרים הזוגיים שנקלטו ואת סכום המספרים האי זוגיים שנקלטו.
# '''
# zugiim = 0
# lo_zugiim_sum = 0
# for i in range(10):
#     num = int(input("Enter a number : "))
#     if 99 < num < 1000:
#         print(num % 10 + (num // 10) % 10 + num // 100)
#     if num % 2 == 0:
#         zugiim += 1
#     else:
#         lo_zugiim_sum += num
# print(zugiim)
# print(lo_zugiim_sum)


# '''
#                                                               קיץ תש"ף – 2020 – מועד א'
#                                                                                שאלה 1
#          כתוב קטע בפעולה ראשית main שיקלוט מספרים שלמים . הקלט יסתיים כאשר ייקלט המספר 0.
# על התוכנית לחשב ולהדפיס:
#                                                                 - כמה מספרים נקלטו.
# - כמה מספרים זוגיים נקלטו.
# - ממוצע מספרים חיוביים שנקלטו.
#                                         הערה: אפשר להניח שיש לפחות מספר אחד חיובי.
# '''
# num = int(input("Enter a number : "))
# all_count = 0
# zugiim_count = 0
# positives_count = 0
# positives_sum = 0
# while num != 0:
#     all_count += 1
#     if num % 2 == 0:
#         zugiim_count += 1
#     if num > 0:
#         positives_count += 1
#         positives_sum += num
#     num = int(input("Enter a number : "))
# print(all_count)
# print(zugiim_count)
# print(positives_sum / positives_count)
