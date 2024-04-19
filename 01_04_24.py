a = [
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 8],
    [7, 8, 3, 2, 5],
    [6, 1, 4, 3, 2],
    [5, 4, 3, 2, 1]
]
b = [[0 for c in range(5)] for r in range(5)]


def show(mat):
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            print(mat[r][c], end=" ")
        print()


def rotate_to_right(mat1, mat2):
    for r in range(len(mat1)):
        for c in range(len(mat1)):
            mat2[c][len(mat1) - 1 - r] = mat1[r][c]


def rotate_to_left(mat1, mat2):
    for r in range(len(mat1)):
        for c in range(len(mat1)):
            mat2[len(mat1)-1-c][r] = mat1[r][c]


rotate_to_right(a, b)
show(b)
print()
rotate_to_left(a,b)
show(b)


"""
קיץ תשפ"ב – 2022 – מועד א'
שאלה 14
מערך דו-ממדי 2x2 נקרא "כתם" אם כל האיברים שלו שווים לאותו ערך. ה ערך הזה נקרא "צבע הכתם".
לדוגמה: במערך הנתון יש ארבעה "כתמים":
שני "כתמים" של ,0 כתם עם של 1 וכתם של .3
 א. כתבו פעולה המקבלת מערך דו-ממדי של מספרים שלמים וערך value. הפעולה תבדוק אם במערך
קיים "כתם " עם ערך value. אם כן – הפעולה תחזיר true, ולא – הפעולה תחזיר false.
מערך דו-ממדי נקרא "מלוכלך" אם יש בו יותר מ- 3 "כתמים" של צבעים שונים.
"""
mat1 = [
    [1, 1, 3, 3, 5, 8, 3, 3, 5, 8],
    [1, 1, 8, 8, 5, 5, 8, 3, 5, 5],
    [7, 8, 8, 8, 5, 5, 8, 2, 5, 5],
    [6, 1, 1, 3, 2, 2, 1, 1, 2, 2],
    [5, 1, 1, 2, 2, 2, 1, 1, 2, 2]
]


def is_stained(mat, value):
    for r in range(len(mat) - 1):
        for c in range(len(mat[0]) - 1):
            if mat[r][c] == value:
                if mat[r][c + 1] == value and mat[r + 1][c] == value and mat[r + 1][c + 1] == value:
                    return True
    return False


print(is_stained(mat1, 5))
