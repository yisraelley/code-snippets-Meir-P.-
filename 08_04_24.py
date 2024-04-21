import random


a = [11, 20, 31, 40, 57, 62, 70, 89, 76]
right = len(a) - 1
left = 0
while left < right:
    while left < len(a) and a[left] % 2 == 0:
        left += 1
    while right > left and a[right] % 2 == 1:
        right -= 1
    ezer = a[left]
    a[left] = a[right]
    a[right] = ezer
print(a)


def binary_search(arr, x):
    low = 0
    up = len(arr) - 1
    while low <= up:
        mid = (low + up) // 2
        if x == arr[mid]:
            return True
        if x < arr[mid]:
            up = mid - 1
        else:
            low = mid + 1
    return False


a = [1] * 10
for i in range(1, len(a)):
    a[i] = a[i - 1] + random.randint(1, 3)
print(a)
print(binary_search(a, 10))
