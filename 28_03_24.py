# import random

# n = int(input("Enter a number : "))
# max_n = n
# min_n = n
# while n != 0:
#     n = int(input("Enter a number : "))
#     if n > max_n:
#         max_n = n
#     if n < min_n:
#         min_n = n
#     print(min_n, max_n)


# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# for i in range(100):
#     index_1 = random.randint(0, len(letters) - 1)
#     index_2 = random.randint(0, len(letters) - 1)
#     temp = letters[index_1]
#     letters[index_1] = letters[index_2]
#     letters[index_2] = temp
# print(letters)
#
# text = "bokertov"
# new_text = ""
# for i in range(len(text)):
#     new_text += letters[ord(text[i]) - ord('a')]
# print(new_text)


# left = [
#     [2, 5, 4, 6],
#     [9, 3, 1, 4],
# ]
# right = [
#     [4, 7, 9],
#     [1, 2, 3],
#     [9, 6, 7],
#     [3, 2, 3],
# ]
# mix = [[0 for c in range(len(right[0]))] for r in range(len(left))]
# for r in range(len(mix)):
#     for c in range(len(mix[0])):
#         for i in range(len(right)):
#             mix[r][c] += left[r][i] * right[i][c]
# print(mix[0])
# print(mix[1])

# a = [4, 2, 8]
# b = [7, 3, 5, 1]
# c = [0] * len(a)
# b_sum = 0
# for i in range(len(b)):
#     b_sum += b[i]
# for i in range(len(a)):
#     c[i] = a[i] * b_sum
# print(c)


# a = [4, 2, 8]
# b = [7, 3, 5, 1]
# c = [0] * len(a)
# for i in range(len(a)):
#     for j in range(len(b)):
#         c[i] += a[i] * b[j]
# print(c)


# a = [
#     [1, 2, 3, 4, 5],
#     [2, 3, 4, 5, 9],
#     [9, 8, 7, 6, 5],
#     [8, 7, 6, 5, 0],
#     [3, 4, 5, 9, 8]
# ]
# print("original:")
# for r in range(len(a)):
#     for c in range(len(a[0])):
#         print(a[r][c], end=" ")
#     print()
# print("transposed:")
# for c in range(len(a[0])):
#     for r in range(len(a)):
#         print(a[r][c], end=" ")
#     print()


# a = [
#     [-4, -6, -1, -2, -9, -60],
#     [5, 6, -9, 1],
#     [7, 6, 5, 4, 3, 2, 0],
# ]
# for r in range(len(a)):
#     c_max = a[r][0]
#     for c in range(1, len(a[r])):
#         if a[r][c] > c_max:
#             c_max = a[r][c]
#     print("row", r+1, "max :", c_max)


# a = [
#     [4, 6, 1, 2, 9, 0],
#     [5, 6, 7, 8, 9, 1],
#     [7, 6, 5, 4, 3, 2],
# ]
# for r in range(len(a)):
#     r_sum = 0
#     for c in range(len(a[r])):
#         r_sum += a[r][c]
#     print("row", r+1, "sum:", r_sum)
