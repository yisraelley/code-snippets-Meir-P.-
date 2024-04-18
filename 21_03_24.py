"""
קיץ תשפ"ג – 2023 – מועד א'
                                                                                                שאלה 2
מחרוזת שמייצגת "מספר נייד תקין" היא מחרוזת העונה לשלושה תנאים:
• שלושת התווים ראשונים הם קידומת
                                                  050 ,051 ,052 ,053 ,054 ,055 ,056 ,057, 058.
                                                                                • התו הרביעי הוא מקף .
• שבעת התווים הבאים הם ספרות.
לדוגמה: המחרוזת 050-1230567 היא מספר נייד תקין.
כתבו קטע תוכנית הקולטת מחרוזות עד שתקלט מחרוזת שהיא מספר נייד תקין. יש להדפיס מספר המחרוזות שנקלטו.
"""
tel = ""
counter = 0
correct = False
while not correct:
    tel = input("Enter a tel number :")
    counter += 1
    correct = True
    if len(tel) != 11 or tel[0] != '0' or tel[1] != '5' or tel[2] == '9' or tel[3] != '-':
        correct = False
    else:
        for i in range(2, 11):
            if i == 3:
                i += 1
            if not ord('9') >= ord(tel[i]) >= ord('0'):
                correct = False
print(counter)

"""
קיץ תשפ"ג – 2023 – מועד א'
שאלה 1
מספר שלם חיובי נקרא "מספר מושלם" אם הוא מתחלק בסכום ספרותיו.
לדוגמה: מספר 12 הוא מספר מושלם, מספר 24 הוא מספר מושלם, מספר 25 אינו מספר מושלם.
כתבו קטע תוכנית להדפסת כל המספרים המושלמים מ - 1 עד .1,000
"""


def is_perfect():
    for i in range(1, 1001):
        digits_sum = 0
        temp_i = i
        while temp_i > 0:
            digits_sum += temp_i % 10
            temp_i //= 10
        if i % digits_sum == 0:
            print(i)


is_perfect()

def is_palindrome(st):
    left = 0
    right = len(st) - 1
    while left < right:
        if st[left] != st[right]:
            return False
        right -= 1
        left += 1
    return True


def str_to_int(st):
    result = 0
    i = 0
    while i < len(st):
        result *= 10
        result += ord(st[i]) - ord('0')
        i += 1
    return result


def is_sorted1(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def is_sorted2(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return 0
    return 1


a = [4, 6, 5, 1, 2, 8, 9, 7, 11, 55]
print(a)
i = 0
while i < len(a) - 1:
    j = i + 1
    while j < len(a):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        j += 1
    i += 1
print(a)

a = [3411, 3653, 41235, 47, 5, 1268, 98769, 74]
for i in range(len(a)):
    count = 0
    while a[i] > 0:
        count += 1
        a[i] //= 10
    a[i] = count
print(a)


a = [11, 33, 45, 47, 53, 68, 69, 74]
b = [13, 16, 19, 22, 34, 41, 51]
c = [0] * (len(a) + len(b))
print(a)
print(b)
print(c)
i_a = 0
i_b = 0
i_c = 0
while i_a < len(a) and i_b < len(b):
    if a[i_a] < b[i_b]:
        c[i_c] = a[i_a]
        i_a += 1
    else:
        c[i_c] = b[i_b]
        i_b += 1
    i_c += 1
while i_a < len(a):
    c[i_c] = a[i_a]
    i_c += 1
    i_a += 1
while i_b < len(b):
    c[i_c] = b[i_b]
    i_c += 1
    i_b += 1
print(c)
