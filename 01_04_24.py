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


a = [
    [1, 1, 3, 3, 5, 8, 3, 3, 5, 8],
    [1, 1, 8, 8, 5, 5, 8, 3, 5, 5],
    [7, 8, 8, 8, 5, 5, 8, 2, 5, 5],
    [6, 1, 1, 3, 2, 2, 1, 1, 2, 2],
    [5, 1, 1, 2, 2, 2, 1, 1, 2, 2]
]


def find_groups(arr, n):
    count = 0
    for r in range(len(arr) - 1):
        for c in range(len(arr[0]) - 1):
            if arr[r][c] == n:
                if arr[r][c + 1] == n and arr[r + 1][c] == n and arr[r + 1][c + 1] == n:
                    count += 1
    return count


def is_group(arr, n):
    for r in range(len(arr) - 1):
        for c in range(len(arr[0]) - 1):
            if arr[r][c] == n:
                if arr[r][c + 1] == n and arr[r + 1][c] == n and arr[r + 1][c + 1] == n:
                    return True
    return False


print(find_groups(a, 5))
print(is_group(a, 5))
