import random

def letters_in_string1(letters, st):
    for i in range(len(letters)):
        for j in range(len(st)):
            if letters[i] == st[j]:
                break
            if j == len(st) - 1:
                return False
    return True


def letters_in_string2(letters, st):
    i = 0
    while i < len(letters):
        j = 0
        while j < len(st):
            if letters[i] == st[j]:
                break
            j += 1
            if j == len(st):
                return False
        i += 1
    return True


st = ""
letters_matrix = [[0 for c in range(26)] for r in range(26)]
for i in range(500):
    st += chr(random.randint(ord('a'), ord('z')))
for i in range(len(st) - 1):
    row = ord(st[i]) - ord('a')
    column = ord(st[i + 1]) - ord('a')
    letters_matrix[row][column] += 1


def print_matrix(mat):
    for r in range(len(mat)):
        print(mat[r])


print_matrix(letters_matrix)

rMax = 0
cMax = 0
for r in range(len(letters_matrix)):
    for c in range(len(letters_matrix)):
        if letters_matrix[r][c] > letters_matrix[rMax][cMax]:
            rMax = r
            cMax = c
print(rMax, cMax)
print(chr(rMax + ord('a')), chr(cMax + ord('a')))


def compare_strings(st1, st2):
    length = len(st1)
    if len(st2) < len(st1):
        length = len(st2)
    for i in range(length):
        if ord(st1[i]) != ord(st2[i]):
            return ord(st2[i]) - ord(st1[i])
    return len(st2) - len(st1)


names = ["shimon", "asaf", "gad", "yosef", "dan", "moshe"]
for i in range(len(names) - 1):
    for j in range(i + 1, len(names)):
        if compare_strings(names[i], names[j]) < 0:
            temp = names[j]
            names[j] = names[i]
            names[i] = temp
print(names)


def peaks(arr):
    i = 1
    while i < len(arr) - 1:
        if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
            print(arr[i])
            i += 2
        else:
            i += 1


a = [1, 2, 7, 4, 5, 6, 5, 4, 3, 2]
peaks(a)

def peak_checker(arr):
    i = 0
    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1
    if i == len(arr) - 1 or i == 0:
        return -1
    peak = i
    while i < len(arr) - 1 and arr[i] > arr[i + 1]:
        i += 1
    if i == len(arr) - 1:
        return peak
    return -1


a = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2]
print(peak_checker(a))


a = [0] * 50
for i in range(len(a)):
    a[i] = random.randint(0, 100)
print(a)
counters = [0] * 101
for i in range(len(a)):
    counters[a[i]] += 1
print(counters)

a_index = 0
for i in range(101):
    count = counters[i]
    while count > 0:
        a[a_index] = i
        a_index += 1
        count -= 1
print(a)

def stains_pointer(mat):
    arr = [0] * 10
    for r in range(len(mat) - 1):
        for c in range(len(mat[0]) - 1):
            if mat[r][c] == mat[r][c + 1] and mat[r][c] == mat[r + 1][c] and mat[r][c] == mat[r + 1][c + 1]:
                arr[mat[r][c]] += 1
    return arr


a = [
    [1, 1, 3, 3, 5, 8, 3, 3, 5, 8],
    [1, 1, 8, 8, 5, 5, 8, 3, 5, 5],
    [7, 8, 8, 8, 5, 5, 8, 2, 5, 5],
    [6, 1, 1, 3, 2, 2, 1, 1, 2, 2],
    [5, 1, 1, 2, 2, 2, 1, 1, 2, 2]
]
arr1 = stains_pointer(a)
print(arr1)


def s1_fill_s2(s1, s2):
    if len(s1) % len(s2) != 0:
        return False
    i = 0
    while i < len(s1) // len(s2):
        j = 0
        while j < len(s2):
            if s1[j + i * len(s2)] != s2[j]:
                return False
            j += 1
        i += 1
    return True


x = "abc"
y = "abcabcabcabc"
print(s1_fill_s2(y, x))
x = "aaab"
y = "aaaaaaaaaaaa"
print(s1_fill_s2(y, x))
