st = input("Enter a string : ")
capital_letters = 0
i = 0
while i < len(st):
    if ord('A') <= ord(st[i]) <= ord('Z'):
        capital_letters += 1
    i += 1
print(capital_letters)

st = input("Enter a string : ")
i = 0
while i < len(st):
    if st[i] != ' ':
        print(st[i], end="")
    else:
        print()
    i += 1

st = input("Enter some words : ")
words = 1
i = 0
while i < len(st):
    if st[i] == ' ':
        words += 1
    i += 1
print("amount of words : ", words)

st = "abcde FGHIJK"
i = 0
while i < len(st):
    print(st[i], ord(st[i]))
    i += 1

arr = [324, 123, 98, 4587, 3, 99]
i = 1
while i < len(arr):
    print(arr[i - 1] - arr[i])
    i += 1

arr = [324, 123, 98, 4587, 3, 99]
print(arr)
i = 0
while i < len(arr):
    x = int(input("Enter a number : "))
    if (x - 10) > arr[i] or (x + 10) < arr[i]:
        arr[i] = x
    i += 1
print(arr)

arr = [324, 123, 98, 4587, 3, 99]
print(arr)
i = 0
while i < len(arr):
    while arr[i] > 9:
        arr[i] //= 10
    i += 1
print(arr)

arr = [324, 123, 908, 4587, 3, 99]
print(arr)
i = 0
while i < len(arr):
    digits_sum = 0
    while arr[i] > 0:
        digits_sum += arr[i] % 10
        arr[i] //= 10
    arr[i] = digits_sum
    i += 1
print(arr)

arr = [4, 5, 8, 7, 9, 2]
print(arr)
i = 0
zugi_sum = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        zugi_sum += arr[i]
    i += 1
print(zugi_sum)

arr = [4, 5, 8, 7, 9, 2]
print(arr)
i = 0
while i < len(arr):
    if arr[i] % 2 == 1:
        arr[i] += 1
    i += 1
print(arr)
