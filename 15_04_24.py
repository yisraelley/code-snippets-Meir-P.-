import random


def is_all_twins1(arr):
    if len(arr) % 2:
        return False
    checked = [False] * len(arr)
    count = 0
    for i in range(len(arr)):
        if not checked[i]:
            count = 1
            checked[i] = True
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    count -= 1
                    checked[j] = True
        if count != 0:
            return False
    return True


arr1 = [1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
print(is_all_twins1(arr1))


def is_all_twins2(arr):
    if len(arr) % 2:
        return False
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count != 2:
            return False
    return True


arr1 = [1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
print(is_all_twins2(arr1))


def is_peak(arr, index):
    if index == 0 or index == len(arr) - 1:
        return False
    if arr[index - 1] < arr[index] and arr[index + 1] < arr[index]:
        return True
    return False


a = [1, 2, 3, 4, 5, 5, 6, 4, 5, 6, 2, 3, 3, 2, 1, 2, 1, 3, 4, 2, 3, 1]
print(is_peak(a, 6))

a = [0] * 10
for i in range(10):
    while a[i] // 10 >= a[i] % 10:
        a[i] = random.randint(10, 99)
print(a)


def is_tripled(a):
    if len(a) % 3 != 0:
        return False
    left = 0
    right = len(a) // 3
    while right < len(a) and a[left] == a[right]:
        left += 1
        right += 1
    if right == len(a):
        return True
    return False


r = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(is_tripled(r))
