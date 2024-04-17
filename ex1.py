#   21/03
# #Q2SummerA2023
# t = input("Enter tel number :")
# c = 0
# while (True):
#     c += 1
#     if (len(t) == 11 and t[0] == '0' and t[1] == '5' \
#             and ord(t[2]) < ord('9') \
#             and ord(t[2]) >= ord('0') \
#             and t[3] == '-'):
#         for i in range(4, 11):
#             if (ord(t[i]) <= ord('9') \
#                     and ord(t[i]) >= ord('0')):
#                 break
#     t = input("Enter tel number :")
# print(c)

# #Q1SummerA2023
# def IsPerfect():
#     for i in range(1 ,1000):
#         sumDigits=0
#         ezer=i
#         while(ezer>0):
#             sumDigits+=ezer%10
#             ezer//=10
#         if(i%sumDigits==0):
#             print(i)
# ####    MAIN    ####
# IsPerfect()


# def IsPalindrom(s):
#     left=0
#     right=len(s)-1
#     while(left<right):
#         if(s[left]!=s[right]):
#             return False
#         right-=1
#         left+=1
#     return True

# print(IsPalindrom("abcbam"))

# def F(s):
#     q=""
#     for i in range(len(s)):
#         q=s[i] + 1
#     return q

# e="wert"
# print(F(e))


# s="as"
# s=s+"$$$"
# print(s)
# s="!!!" + s
# print(s)


# def StrToInt(s):
#    t=0
#    i=0
#    while(i<len(s)):
#       t=t*10+(ord(s[i])-48)
#       i+=1
#    return t
# ####    MAIN    ####
# n="4321"
# x=StrToInt(n)
# x*=2
# print(x)
# '''
# t=0
# t=t*10+4        4
# t=t*10+3        43
# t=t*10+2        432
# t=t*10+1        4321
# '''


# def IsSorted(a):
#     for i in range(1, len(a)):
#         if(a[i-1]>a[i]):
#             return False
#     return True

# ####    MAIN    ####
# a=[4,6,15,21,32,48,59]
# u=IsSorted(a)
# print(u)
# print(IsSorted(a))


# def IsSorted(a):
#     for i in range(1, len(a)):
#         if(a[i-1]>a[i]):
#             return 0
#     return 1

# ####    MAIN    ####
# a=[4,6,15,21,32,48,59]
# u=IsSorted(a)
# print(u)
# print(IsSorted(a))


# a=[4,6,5,1,2,8,9,7,11,55]
# n=0
# while(n<len(a)-1):
#     b=n+1
#     while(b<len(a)):
#         if(a[n]>a[b]):
#             temp=a[n]
#             a[n]=a[b]
#             a[b]=temp
#         b+=1
#     n+=1
# print(a)

# a=[3411,3653,41235,47,5,1268,98769,74]
# #a=[4,4,5,2,1,4,5,2]
# for i in range(0, len(a), 1):
#     c=0
#     while(a[i]>0):
#         c+=1
#         a[i]=a[i]//10
#     a[i]=c
# print(a)


# a=[11,33,45,47,53,68,69,74]
# b=[13,16,19,22,34,41,51]
# c=[11]*(len(a)+len(b))
# idxA=0
# idxB=0
# idxC=0
# while(idxA<len(a) and idxB<len(b)):
#     if(a[idxA]<b[idxB]):
#         c[idxC]=a[idxA]
#         idxA+=1
#     else:
#         c[idxC]=b[idxB]
#         idxB+=1
#     idxC+=1
# while(idxA<len(a)):
#     c[idxC]=a[idxA]
#     idxC+=1
#     idxA+=1
# while(idxB<len(b)):
#     c[idxC]=b[idxB]
#     idxC+=1
#     idxB+=1
# print(c)


# a=[22,44,77,99,11,43,67, 87, 12, 32,455,876]
# print(a)        #
# for i in range(1,len(a), 2):
#     if(a[i]>55):
#         print(a[i])

#   28/03 A
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
# m = [
#     [0, 0, 0],
#     [0, 0, 0],
# ]
# for r in range(len(left)):
#     for c in range(len(right[0])):
#         for i in range(len(left[0])):
#
# '''
#                    4 7 9
#                    1 2 3
# 2 5 4 6            9 6 7
# 9 3 1 4            3 2 3
#
#
# 67  ?   ?
# ?   ?   ?
#
# #   2*4+5*1+4*9+6*3 =   67
# '''

# a=[4,2,8]
# b=[7,3,5,1]
# c=[0]*len(a)
# sumB=0
# for i in range(len(b)):
#     sumB+=b[i]
# for i in range(len(a)):
#     c[i]=a[i]*sumB
# print(c)


# # c[0]=4*7+4*3+4*5+4*1  =   4*(7+3+5+1)
# # c[1]=2*7+2*3+2*5+2*1  =   2*(7+3+5+1)
# # c[2]=8*7+8*3+8*5+8*1  =   8*(7+3+5+1)
# # c=[64,32,128]


# a=[4,2,8]
# b=[7,3,5,1]
# c=[0]*len(a)
# for i in range(len(a)):
#    for k in range(len(b)):
#       c[i]=c[i]+a[i]*b[k]
# print(c)


# # c[0]=4*7+4*3+4*5+4*1  =   4*(7+3+5+1)
# # c[1]=2*7+2*3+2*5+2*1  =   2*(7+3+5+1)
# # c[2]=8*7+8*3+8*5+8*1  =   8*(7+3+5+1)
# # c=[64,32,128]


# a=[
#     [1,2,3,4,5],
#     [2,3,4,5,9],
#     [9,8,7,6,5],
#     [8,7,6,5,0],
#     [3,4,5,9,8]
# ]
# for c in range(len(a[0])):
#     for r in range(len(a)):
#         print(a[r][c], end=" ")
#     print()

# '''
# 1 2 9 8 3
# 2 3 8 7 4
# 3 4 7 6 5
# 4 5 6 5 9
# 5 9 5 0 8
# '''


# a=[
#     [-4,-6,-1,-2,-9,-60],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2],
# ]
# for r in range(len(a)):
#     max=a[r][0]
#     print(a[r][0], end=" ")
#     for c in range(1, len(a[r])):
#         print(a[r][c], end=" ")
#         if(max<a[r][c]):
#             max=a[r][c]
#     print("    ", max)

# '''
# -4 -6 -1 -2 -9 -60      -1
# 5 6 7 8 9 1      9
# 7 6 5 4 3 2      7
# '''


# a=[
#     [4,6,1,2,9,0],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2],
# ]
# for r in range(len(a)):
#     sum=0
#     for c in range(len(a[r])):
#         print(a[r][c], end=" ")
#         sum=sum+a[r][c]
#     print("    ", sum)

# '''
# 4 6 1 2 9 0      22
# 5 6 7 8 4 1      36
# 7 6 5 4 3 2      27
# '''

# a=[
#     [4,6,1,2,9,0],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2],
# ]
# #a=[[4,6,1,2,9,0],[5,6,7,8,9,1],[7,6,5,4,3,2]]
# for r in range(len(a)):
#     for c in range(len(a[r])):
#         print(a[r][c], end=" ")
#     print()

#   28/03 B
# left=[
#     [2,5,4,6],
#     [9,3,1,4],
# ]
# right=[
#     [4,7,9],
#     [1,2,3],
#     [9,6,7],
#     [3,2,3],
# ]
# m=[
#     [0,0,0],
#     [0,0,0],
#   ]
# for r in range(len(left)):
#     for c in range(len(right[0])):
#         for i in range(len(left[0])):
#             m[r][c]=m[r][c] + left[r][i]*right[i][c]
# print(m[0])
# print(m[1])


# '''
#                    4 7 9
#                    1 2 3
# 2 5 4 6            9 6 7
# 9 3 1 4            3 2 3
#
#
# 67  ?   ?
# ?   ?   ?
#
# #   2*4+5*1+4*9+6*3 =   67
# '''

# a=[4,2,8]
# b=[7,3,5,1]
# c=[0]*len(a)
# sumB=0
# for i in range(len(b)):
#     sumB+=b[i]
# for i in range(len(a)):
#     c[i]=a[i]*sumB
# print(c)


# # c[0]=4*7+4*3+4*5+4*1  =   4*(7+3+5+1)
# # c[1]=2*7+2*3+2*5+2*1  =   2*(7+3+5+1)
# # c[2]=8*7+8*3+8*5+8*1  =   8*(7+3+5+1)
# # c=[64,32,128]


# a=[4,2,8]
# b=[7,3,5,1]
# c=[0]*len(a)
# for i in range(len(a)):
#    for k in range(len(b)):
#       c[i]=c[i]+a[i]*b[k]
# print(c)


# # c[0]=4*7+4*3+4*5+4*1  =   4*(7+3+5+1)
# # c[1]=2*7+2*3+2*5+2*1  =   2*(7+3+5+1)
# # c[2]=8*7+8*3+8*5+8*1  =   8*(7+3+5+1)
# # c=[64,32,128]


# a=[
#     [1,2,3,4,5],
#     [2,3,4,5,9],
#     [9,8,7,6,5],
#     [8,7,6,5,0],
#     [3,4,5,9,8]
# ]
# for c in range(len(a[0])):
#     for r in range(len(a)):
#         print(a[r][c], end=" ")
#     print()

# '''
# 1 2 9 8 3
# 2 3 8 7 4
# 3 4 7 6 5
# 4 5 6 5 9
# 5 9 5 0 8
# '''


# a=[
#     [-4,-6,-1,-2,-9,-60],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2],
# ]
# for r in range(len(a)):
#     max=a[r][0]
#     print(a[r][0], end=" ")
#     for c in range(1, len(a[r])):
#         print(a[r][c], end=" ")
#         if(max<a[r][c]):
#             max=a[r][c]
#     print("    ", max)

# '''
# -4 -6 -1 -2 -9 -60      -1
# 5 6 7 8 9 1      9
# 7 6 5 4 3 2      7
# '''


# a=[
#     [4,6,1,2,9,0],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2],
# ]
# for r in range(len(a)):
#     sum=0
#     for c in range(len(a[r])):
#         print(a[r][c], end=" ")
#         sum=sum+a[r][c]
#     print("    ", sum)

# '''
# 4 6 1 2 9 0      22
# 5 6 7 8 4 1      36
# 7 6 5 4 3 2      27
# '''

# a=[
#     [4,6,1,2,9,0],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2],
# ]
# #a=[[4,6,1,2,9,0],[5,6,7,8,9,1],[7,6,5,4,3,2]]
# for r in range(len(a)):
#     for c in range(len(a[r])):
#         print(a[r][c], end=" ")
#     print()

#   28/03 C
# num = int(input("Enter a number : "))
# max = num
# min = num
# while (num < 100 or num > 999):
#     if (max < num):
#         max = num
#     if (min > num):
#         min = num
#     num = int(input("Enter a number : "))
# if (max < num):
#     max = num
# if (min > num):
#     min = num
#
# print(max, min)

# num=int(input("Enter a number : "))
# max=num
# min=num
# while(num<100 or num>999):
#     if(max<num):
#         max=num
#     if(min>num):
#         min=num
#     num=int(input("Enter a number : "))
# if(max<num):
#     max=num
# if(min>num):
#     min=num

# print(max, min)


# import random
# letters="abcdefghijklmnopqrstuvwxyz"
# hatspan=["a","b","c","d","e","f","g","h","i","j","k","l","m",
#          "n","o","p","q","r","s","t","u","v","w","x","y","z"]
# swapCount=random.randint(22,66)
# for i in range(swapCount):
#     idx1=random.randint(0,len(letters)-1)
#     idx2=random.randint(0,len(letters)-1)
#     ezer=hatspan[idx1]
#     hatspan[idx1]=hatspan[idx2]
#     hatspan[idx2]=ezer
# print(hatspan)

# text="bokertov"
# newText=""
# for i in range(len(text)):
#     idx= ord(text[i])-ord('a')
#     newText=newText + hatspan[idx]
# print(newText)

# '''
# ['a', 's', 't', 'v', 'd', 'r', 'i', 'x', 'u',
#  'k', 'h', 'l', 'w', 'n', 'j', 'f', 'm', 'y',
#  'q', 'g', 'p', 'o', 'b', 'z', 'c', 'e']
# ['s', 'j', 'h', 'd', 'y', 'g', 'j', 'o']
# '''
# ['n','m','b','t','c','z','q','g','r','j','v','k','o',
# 'y','h','l','p','i','u','f','w','s','d','x','a','e']
# print()

# import random
# letters=["a","b","c","d","e","f","g","h","i","j","k","l","m",
#          "n","o","p","q","r","s","t","u","v","w","x","y","z"]
# hatspan=["a","b","c","d","e","f","g","h","i","j","k","l","m",
#          "n","o","p","q","r","s","t","u","v","w","x","y","z"]
# swapCount=random.randint(22,66)
# for i in range(swapCount):
#     idx1=random.randint(0,len(letters)-1)
#     idx2=random.randint(0,len(letters)-1)
#     ezer=hatspan[idx1]
#     hatspan[idx1]=hatspan[idx2]
#     hatspan[idx2]=ezer
# print(hatspan)

# text="bokertov"
# newText=[""]*len(text)
# for i in range(len(text)):
#     idx= ord(text[i])-ord('a')
#     newText[i]=hatspan[idx]
# print(newText)


# '''
# ['a', 's', 't', 'v', 'd', 'r', 'i', 'x', 'u',
#  'k', 'h', 'l', 'w', 'n', 'j', 'f', 'm', 'y',
#  'q', 'g', 'p', 'o', 'b', 'z', 'c', 'e']
# ['s', 'j', 'h', 'd', 'y', 'g', 'j', 'o']
# '''
# #['n','m','b','t','c','z','q','g','r','j','v','k','o',
# # 'y','h','l','p','i','u','f','w','s','d','x','a','e']
# print()


# left=[
#     [2,5,4,6],
#     [9,3,1,4],
# ]
# right=[
#     [4,7,9],
#     [1,2,3],
#     [9,6,7],
#     [3,2,3],
# ]
# m=[
#     [0,0,0],
#     [0,0,0],
#   ]
# for r in range(len(left)):
#     for c in range(len(right[0])):
#         for i in range(len(left[0])):
#             m[r][c]=m[r][c] + left[r][i]*right[i][c]
# print(m[0])
# print(m[1])


# '''
#                    4 7 9
#                    1 2 3
# 2 5 4 6            9 6 7
# 9 3 1 4            3 2 3
#
#
# 67  ?   ?
# ?   ?   ?
#
# #   2*4+5*1+4*9+6*3 =   67
# '''

# a=[4,2,8]
# b=[7,3,5,1]
# c=[0]*len(a)
# sumB=0
# for i in range(len(b)):
#     sumB+=b[i]
# for i in range(len(a)):
#     c[i]=a[i]*sumB
# print(c)


# # c[0]=4*7+4*3+4*5+4*1  =   4*(7+3+5+1)
# # c[1]=2*7+2*3+2*5+2*1  =   2*(7+3+5+1)
# # c[2]=8*7+8*3+8*5+8*1  =   8*(7+3+5+1)
# # c=[64,32,128]


# a=[4,2,8]
# b=[7,3,5,1]
# c=[0]*len(a)
# for i in range(len(a)):
#    for k in range(len(b)):
#       c[i]=c[i]+a[i]*b[k]
# print(c)


# # c[0]=4*7+4*3+4*5+4*1  =   4*(7+3+5+1)
# # c[1]=2*7+2*3+2*5+2*1  =   2*(7+3+5+1)
# # c[2]=8*7+8*3+8*5+8*1  =   8*(7+3+5+1)
# # c=[64,32,128]


# a=[
#     [1,2,3,4,5],
#     [2,3,4,5,9],
#     [9,8,7,6,5],
#     [8,7,6,5,0],
#     [3,4,5,9,8]
# ]
# for c in range(len(a[0])):
#     for r in range(len(a)):
#         print(a[r][c], end=" ")
#     print()

# '''
# 1 2 9 8 3
# 2 3 8 7 4
# 3 4 7 6 5
# 4 5 6 5 9
# 5 9 5 0 8
# '''


# a=[
#     [-4,-6,-1,-2,-9,-60],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2],
# ]
# for r in range(len(a)):
#     max=a[r][0]
#     print(a[r][0], end=" ")
#     for c in range(1, len(a[r])):
#         print(a[r][c], end=" ")
#         if(max<a[r][c]):
#             max=a[r][c]
#     print("    ", max)

# '''
# -4 -6 -1 -2 -9 -60      -1
# 5 6 7 8 9 1      9
# 7 6 5 4 3 2      7
# '''


# a=[
#     [4,6,1,2,9,0],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2],
# ]
# for r in range(len(a)):
#     sum=0
#     for c in range(len(a[r])):
#         print(a[r][c], end=" ")
#         sum=sum+a[r][c]
#     print("    ", sum)

# '''
# 4 6 1 2 9 0      22
# 5 6 7 8 4 1      36
# 7 6 5 4 3 2      27
# '''

# a=[
#     [4,6,1,2,9,0],
#     [5,6,7,8,9,1],
#     [7,6,5,4,3,2],
# ]
# #a=[[4,6,1,2,9,0],[5,6,7,8,9,1],[7,6,5,4,3,2]]
# for r in range(len(a)):
#     for c in range(len(a[r])):
#         print(a[r][c], end=" ")
#     print()

#   01/04 A
# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()
# a=[
#     [1,2,3,4,5],
#     [3,4,5,9,8],
#     [7,8,3,2,5],
#     [6,1,4,3,2],
#     [5,4,3,2,1]
#     ]
# b=[
#     [1,2,3,3,1],
#     [3,4,5,4,2],
#     [7,8,3,5,3],
#     [6,1,4,9,4],
#     [5,4,3,8,5]
# ]
#
# for r in range(len(a)):
#     for c in range(len(a)):
#         b[c][len(a)-1-r] = a[r][c]
#
#
# Show(a)
# print()
# Show(b)

#   01/04 B
# def Q14A(a, v):
#     m = 0
#     for r in range(len(a) - 1):
#         for c in range(len(a[0]) - 1):
#             if (a[r][c] == v):
#                 if (a[r][c + 1] == v and a[r + 1][c] == v and a[r + 1][c + 1] == v):
#                     m += 1
#     return m
#
#
# a = [
#     [1, 1, 3, 3, 5, 8, 3, 3, 5, 8],
#     [1, 1, 8, 8, 5, 5, 8, 3, 5, 5],
#     [7, 8, 8, 8, 5, 5, 8, 2, 5, 5],
#     [6, 1, 1, 3, 2, 2, 1, 1, 2, 2],
#     [5, 1, 1, 2, 2, 2, 1, 1, 2, 2]
# ]
# for i in range(10):
#     print(i, Q14A(a, i))

# def Q14A(a, v):
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==v):
#                 if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                     return True
#     return False

# a=[
#     [1,2,3,3,5,8],
#     [3,8,8,3,5,5],
#     [7,8,8,2,5,5],
#     [6,1,1,3,2,2],
#     [5,1,1,2,2,2]
#     ]
# for i in range(10):
#     print(Q14A(a, i))


# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()
# a=[
#     [1,2,3,4,5],
#     [3,4,5,9,8],
#     [7,8,3,2,5],
#     [6,1,4,3,2],
#     [5,4,3,2,1]
#     ]
# b=[
#     [1,2,3,3,1],
#     [3,4,5,4,2],
#     [7,8,3,5,3],
#     [6,1,4,9,4],
#     [5,4,3,8,5]
# ]

# #   Rotate right
# # for r in range(len(a)):
# #     for c in range(len(a)):
# #         b[c][len(a)-1-r] = a[r][c]

# #   Rotate left
# for r in range(len(a)):
#     for c in range(len(a)):
#         b[len(a)-1-c][r] = a[r][c]

# Show(a)
# print()
# Show(b)

#   04/04 A
# def CmpString(s1, s2):
#     l = len(s1)
#     if (len(s1) > len(s2)):
#         l = len(s2)
#     for i in range(l):
#         if (s1[i] != s2[i]):
#             return ord(s1[i]) - ord(s2[i])
#     return len(s1) - len(s2)
#
#
# names = ["shimon", "yosef", "gad", "dan", "gadi"]
# print(names)

# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#     return len(s1)-len(s2)


# print(CmpString("aaa", "bbb"))
# print(CmpString("ccc", "bbb"))
# print(CmpString("aaa", "abb"))
# print(CmpString("axa", "aaaa"))
# print(CmpString("aaaa", "aaa"))
# print(CmpString("aaa", "aaaaaaaa"))

#   04/04 B

# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#     return len(s1)-len(s2)


# print(CmpString("aaa", "bbb"))
# print(CmpString("ccc", "bbb"))
# print(CmpString("aaa", "abb"))
# print(CmpString("axa", "aaaa"))
# print(CmpString("aaaa", "aaa"))
# print(CmpString("aaa", "aaaaaaaa"))


# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(ord(s1[i]) < ord(s2[i])):
#            return -1
#         else:
#            if(ord(s1[i]) > ord(s2[i])):
#                return 1
#     if(len(s1)==len(s2)):
#         return 0
#     else:
#         return len(s1)-len(s2)


# print(CmpString("aaa", "bbb"))
# print(CmpString("ccc", "bbb"))
# print(CmpString("aaa", "abb"))
# print(CmpString("aaa", "aaaa"))
# print(CmpString("aaaa", "aaa"))

#   04/04 C

# import random
# r=ord('a')
# s=""
# c=chr(random.randint(97,106))
# s=s+c
# c=chr(random.randint(97,106))
# s=s+c
# c=chr(random.randint(97,106))
# s=s+c
# c=chr(random.randint(97,106))
# s=s+c
# print(s)

# #
# m=[
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0]
#     ]


# def S1InS2(s1, s2):
#     if(len(s1)>len(s2)):
#         return False
#     for i in range(len(s1)):
#         for k in range(len(s2)):
#             if(s1[i]==s2[k]):
#                 break
#         if(s1[i]!=s2[k]):
#             return False
#     return True
# print(S1InS2("cea", "casv"))
# print(S1InS2("cxea", "abcdef"))
# print(S1InS2("cjea", "abcdef"))
# print(S1InS2("cea", "cafehb"))


# def S1InS2(s1, s2):
#     if(len(s1)>len(s2)):
#         return False
#     i=0
#     while(i<len(s1)):
#         k=0
#         while(k<len(s2)):
#             if(s1[i]==s2[k]):
#                 break
#             k+=1
#         if(k==len(s2)):
#             return False
#         i+=1
#     return True
# print(S1InS2("cxea", "abcdef"))
# print(S1InS2("cjea", "abcdef"))
# print(S1InS2("ceav", "cae"))

#   04/04 D

# import random
#
#
# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()
#
#
# r = ord('a')
# s = ""
# for i in range(100):
#     c = chr(random.randint(97, 106))
#     s = s + c
# print(s)
# m = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
#   s = "acfweedfaerfgafa
# for i in range(len(s) - 1):
#     sh = ord(s[i]) - 97
#     a = ord(s[i + 1]) - 97
#     m[sh][a] += 1
# Show(m)

#   04/04 E

# import random
#
#
# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()
#
#
# r = ord('a')
# s = ""
# for i in range(3000000):
#     c = chr(random.randint(97, 106))
#     s = s + c
# # print(s)
# m = [[0 for x in range(10)] for y in range(10)]
# for i in range(len(s) - 1):
#     sh = ord(s[i]) - 97
#     a = ord(s[i + 1]) - 97
#     m[sh][a] += 1
# rMax = 0
# cMax = 0
# for r in range(len(m)):
#     for c in range(len(m)):
#         if (m[rMax][cMax] < m[r][c]):
#             rMax = r
#             cMax = c
# print(rMax, cMax)
# print(chr(rMax + 97), chr(cMax + 97))
# Show(m)

# w, h = 8, 5


# def S1InS2(s1, s2):
#     if(len(s1)>len(s2)):
#         return False
#     for i in range(len(s1)):
#         for k in range(len(s2)):
#             if(s1[i]==s2[k]):
#                 break
#         if(s1[i]!=s2[k]):
#             return False
#     return True
# print(S1InS2("cea", "casv"))
# print(S1InS2("cxea", "abcdef"))
# print(S1InS2("cjea", "abcdef"))
# print(S1InS2("cea", "cafehb"))


# def S1InS2(s1, s2):
#     if(len(s1)>len(s2)):
#         return False
#     i=0
#     while(i<len(s1)):
#         k=0
#         while(k<len(s2)):
#             if(s1[i]==s2[k]):
#                 break
#             k+=1
#         if(k==len(s2)):
#             return False
#         i+=1
#     return True
# print(S1InS2("cxea", "abcdef"))
# print(S1InS2("cjea", "abcdef"))
# print(S1InS2("ceav", "cae"))


#   fcea
#   abcdef


# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#     return len(s1)-len(s2)

# names=["khimon", "oosef", "gad", "yosef", "dan", "gadi"]
# print(names)
# for niv in range(len(names)-1):
#     for bod in range(niv+1, len(names)):
#         if(CmpString(names[niv], names[bod])<0):
#             temp=names[bod]
#             names[bod]=names[niv]
#             names[niv]=temp
# print(names)


# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#     return len(s1)-len(s2)

# print(CmpString("aaa", "bbb"))
# print(CmpString("ccc", "bbb"))
# print(CmpString("aaa", "abb"))
# print(CmpString("axa", "aaaa"))
# print(CmpString("aaaa", "aaa"))
# print(CmpString("aaa", "aaaaaaaa"))


# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(ord(s1[i]) < ord(s2[i])):
#            return -1
#         else:
#            if(ord(s1[i]) > ord(s2[i])):
#                return 1
#     if(len(s1)==len(s2)):
#         return 0
#     else:
#         return len(s1)-len(s2)


# print(CmpString("aaa", "bbb"))
# print(CmpString("ccc", "bbb"))
# print(CmpString("aaa", "abb"))
# print(CmpString("aaa", "aaaa"))
# print(CmpString("aaaa", "aaa"))


#   reuven      levi        >0
#   levi        reuven      <0
#   levi        levi        ==0
#   levi        levin        <0
#   levin       levi        >0
#   levarov     levi        ==0
#   ran         binyamin


#   levin '/0'       levi '/0'


# def Q(a):
#     i=1
#     while(i<len(a)-1):
#         if(a[i-1]<a[i] and a[i+1]<a[i]):
#             print(a[i])
#             i+=2
#         else:
#             i+=1
# a=[1,2,7,4,5,6,5,4,3,2]
# Q(a)


# def F(a):
#     i=0
#     while(i<len(a)-1 and a[i]<a[i+1]):
#         i+=1
#     if(i==len(a)-1 or i==0):
#         return -1
#     p=i
#     while(i<len(a)-1 and a[i]>a[i+1]):
#         i+=1
#     if(i==len(a)-1):
#         return p
#     return -1


# a=[1,2,3,4,5,6,5,4,3,2]
# print(F(a))


# import random
# a=[0]*20000
# for i in range(len(a)):
#     a[i]=random.randint(0,100)
# #print(a)
# for niv in range(0, len(a)-1, 1):
#     for bod in range(niv+1, len(a), 1):
#         if(a[bod]<a[niv]):
#             ezer=a[bod]
#             a[bod]=a[niv]
#             a[niv]=ezer
# #print(a)


# import random
# a=[0]*200000
# for i in range(len(a)):
#     a[i]=random.randint(0,100)
# #print(a)
# counters=[0]*101
# for i in range(len(a)):
#     counters[a[i]]+=1
# print()
# print(counters)
# index=0
# for i in range(0, 101, 1):
#     k=0
#     while(k<counters[i]):
#         a[index]=i
#         index+=1
#         k+=1
# print()
# print(a)


# def Q(a):
#     b=[0]*10
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==a[r][c+1] and a[r][c]==a[r+1][c] and a[r][c]==a[r+1][c+1]):
#                 b[a[r][c]]+=1
#     return b
# a=[
#     [1,1,3,3,5,8,3,3,5,8],
#     [1,1,8,8,5,5,8,3,5,5],
#     [7,8,8,8,5,5,8,2,5,5],
#     [6,1,1,3,2,2,1,1,2,2],
#     [5,1,1,2,2,2,1,1,2,2]
#     ]
# r=Q(a)
# print(r)


#   2022 sumer A
# def Q14A(a, v):
#     m=0
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==v):
#                 if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                     m+=1
#     return m

# a=[
#     [1,1,3,3,5,8,3,3,5,8],
#     [1,1,8,8,5,5,8,3,5,5],
#     [7,8,8,8,5,5,8,2,5,5],
#     [6,1,1,3,2,2,1,1,2,2],
#     [5,1,1,2,2,2,1,1,2,2]
#     ]
# for i in range(10):
#     print(i, Q14A(a, i))


# def Q14A(a, v):
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==v):
#                 if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                     return True
#     return False

# a=[
#     [1,2,3,3,5,8],
#     [3,8,8,3,5,5],
#     [7,8,8,2,5,5],
#     [6,1,1,3,2,2],
#     [5,1,1,2,2,2]
#     ]
# for i in range(10):
#     print(Q14A(a, i))


# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()
# a=[
#     [1,2,3,4,5],
#     [3,4,5,9,8],
#     [7,8,3,2,5],
#     [6,1,4,3,2],
#     [5,4,3,2,1]
#     ]
# b=[
#     [1,2,3,3,1],
#     [3,4,5,4,2],
#     [7,8,3,5,3],
#     [6,1,4,9,4],
#     [5,4,3,8,5]
# ]

# #   Rotate right
# # for r in range(len(a)):
# #     for c in range(len(a)):
# #         b[c][len(a)-1-r] = a[r][c]

# #   Rotate left
# for r in range(len(a)):
#     for c in range(len(a)):
#         b[len(a)-1-c][r] = a[r][c]

# Show(a)
# print()
# Show(b)

#   04/04 F


# def Q3SummerB2021(s1, s2):
#     if (len(s1) % len(s2) != 0):
#         return False
#     a = 0
#     while (a < len(s1)):
#         b = 0
#         while (b < len(s2)):
#             if (s1[a * (len(s2)) + b] != s2[b]):
#                 return False
#             b += 1
#         a += 1
#     return True
#
#
# x = "abc"
# y = "abcabcabcabc"
# print(Q3SummerB2021(y, x))
# import random
# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()

# r=ord('a')
# s=""
# for i in range(3000000):
#     c=chr(random.randint(97,106))
#     s=s+c
# #print(s)
# m= [[0 for x in range(10)] for y in range(10)]
# for i in range(len(s)-1):
#     sh=ord(s[i])-97
#     a=ord(s[i+1])-97
#     m[sh][a]+=1
# rMax=0
# cMax=0
# for r in range(len(m)):
#     for c in range(len(m)):
#         if(m[rMax][cMax]<m[r][c]):
#             rMax=r
#             cMax=c
# print(rMax, cMax)
# print(chr(rMax+97), chr(cMax+97))
# Show(m)


# def S1InS2(s1, s2):
#     if(len(s1)>len(s2)):
#         return False
#     for i in range(len(s1)):
#         for k in range(len(s2)):
#             if(s1[i]==s2[k]):
#                 break
#         if(s1[i]!=s2[k]):
#             return False
#     return True
# print(S1InS2("cea", "casv"))
# print(S1InS2("cxea", "abcdef"))
# print(S1InS2("cjea", "abcdef"))
# print(S1InS2("cea", "cafehb"))


# def S1InS2(s1, s2):
#     if(len(s1)>len(s2)):
#         return False
#     i=0
#     while(i<len(s1)):
#         k=0
#         while(k<len(s2)):
#             if(s1[i]==s2[k]):
#                 break
#             k+=1
#         if(k==len(s2)):
#             return False
#         i+=1
#     return True
# print(S1InS2("cxea", "abcdef"))
# print(S1InS2("cjea", "abcdef"))
# print(S1InS2("ceav", "cae"))


#   fcea
#   abcdef


# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#     return len(s1)-len(s2)

# names=["khimon", "oosef", "gad", "yosef", "dan", "gadi"]
# print(names)
# for niv in range(len(names)-1):
#     for bod in range(niv+1, len(names)):
#         if(CmpString(names[niv], names[bod])<0):
#             temp=names[bod]
#             names[bod]=names[niv]
#             names[niv]=temp
# print(names)


# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#     return len(s1)-len(s2)

# print(CmpString("aaa", "bbb"))
# print(CmpString("ccc", "bbb"))
# print(CmpString("aaa", "abb"))
# print(CmpString("axa", "aaaa"))
# print(CmpString("aaaa", "aaa"))
# print(CmpString("aaa", "aaaaaaaa"))


# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(ord(s1[i]) < ord(s2[i])):
#            return -1
#         else:
#            if(ord(s1[i]) > ord(s2[i])):
#                return 1
#     if(len(s1)==len(s2)):
#         return 0
#     else:
#         return len(s1)-len(s2)


# print(CmpString("aaa", "bbb"))
# print(CmpString("ccc", "bbb"))
# print(CmpString("aaa", "abb"))
# print(CmpString("aaa", "aaaa"))
# print(CmpString("aaaa", "aaa"))


#   reuven      levi        >0
#   levi        reuven      <0
#   levi        levi        ==0
#   levi        levin        <0
#   levin       levi        >0
#   levarov     levi        ==0
#   ran         binyamin


#   levin '/0'       levi '/0'


# def Q(a):
#     i=1
#     while(i<len(a)-1):
#         if(a[i-1]<a[i] and a[i+1]<a[i]):
#             print(a[i])
#             i+=2
#         else:
#             i+=1
# a=[1,2,7,4,5,6,5,4,3,2]
# Q(a)


# def F(a):
#     i=0
#     while(i<len(a)-1 and a[i]<a[i+1]):
#         i+=1
#     if(i==len(a)-1 or i==0):
#         return -1
#     p=i
#     while(i<len(a)-1 and a[i]>a[i+1]):
#         i+=1
#     if(i==len(a)-1):
#         return p
#     return -1


# a=[1,2,3,4,5,6,5,4,3,2]
# print(F(a))


# import random
# a=[0]*20000
# for i in range(len(a)):
#     a[i]=random.randint(0,100)
# #print(a)
# for niv in range(0, len(a)-1, 1):
#     for bod in range(niv+1, len(a), 1):
#         if(a[bod]<a[niv]):
#             ezer=a[bod]
#             a[bod]=a[niv]
#             a[niv]=ezer
# #print(a)


# import random
# a=[0]*200000
# for i in range(len(a)):
#     a[i]=random.randint(0,100)
# #print(a)
# counters=[0]*101
# for i in range(len(a)):
#     counters[a[i]]+=1
# print()
# print(counters)
# index=0
# for i in range(0, 101, 1):
#     k=0
#     while(k<counters[i]):
#         a[index]=i
#         index+=1
#         k+=1
# print()
# print(a)


# def Q(a):
#     b=[0]*10
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==a[r][c+1] and a[r][c]==a[r+1][c] and a[r][c]==a[r+1][c+1]):
#                 b[a[r][c]]+=1
#     return b
# a=[
#     [1,1,3,3,5,8,3,3,5,8],
#     [1,1,8,8,5,5,8,3,5,5],
#     [7,8,8,8,5,5,8,2,5,5],
#     [6,1,1,3,2,2,1,1,2,2],
#     [5,1,1,2,2,2,1,1,2,2]
#     ]
# r=Q(a)
# print(r)


#   2022 sumer A
# def Q14A(a, v):
#     m=0
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==v):
#                 if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                     m+=1
#     return m

# a=[
#     [1,1,3,3,5,8,3,3,5,8],
#     [1,1,8,8,5,5,8,3,5,5],
#     [7,8,8,8,5,5,8,2,5,5],
#     [6,1,1,3,2,2,1,1,2,2],
#     [5,1,1,2,2,2,1,1,2,2]
#     ]
# for i in range(10):
#     print(i, Q14A(a, i))


# def Q14A(a, v):
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==v):
#                 if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                     return True
#     return False

# a=[
#     [1,2,3,3,5,8],
#     [3,8,8,3,5,5],
#     [7,8,8,2,5,5],
#     [6,1,1,3,2,2],
#     [5,1,1,2,2,2]
#     ]
# for i in range(10):
#     print(Q14A(a, i))


# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()
# a=[
#     [1,2,3,4,5],
#     [3,4,5,9,8],
#     [7,8,3,2,5],
#     [6,1,4,3,2],
#     [5,4,3,2,1]
#     ]
# b=[
#     [1,2,3,3,1],
#     [3,4,5,4,2],
#     [7,8,3,5,3],
#     [6,1,4,9,4],
#     [5,4,3,8,5]
# ]

# #   Rotate right
# # for r in range(len(a)):
# #     for c in range(len(a)):
# #         b[c][len(a)-1-r] = a[r][c]

# #   Rotate left
# for r in range(len(a)):
#     for c in range(len(a)):
#         b[len(a)-1-c][r] = a[r][c]

# Show(a)
# print()
# Show(b)

#   04/04 G


# def Q3SummerB2021(s1, s2):
#     if(len(s1)%len(s2)!=0):
#         return False
#     a=0
#     while(a<len(s1)//len(s2)):
#         b=0
#         while(b<len(s2)):
#             if(s1[a*(len(s2))+b]!=s2[b]):
#                 return False
#             b+=1
#         a+=1
#     return True
#
# x = "abc"
# y = "abcabcabcabc"
# print(Q3SummerB2021(y,x))
# x = "aaa"
# y = "aaaaaaaaaaaa"
# print(Q3SummerB2021(y,x))

#   08/04 A

# a=[10,20,31,40,57,62,70,89,77]
# right=len(a)-1
# left=0
# while(left<len(a) and a[left]%2==0):
#     left+=1
# if(left<len(a)-1):
#     while(left<right and a[right]%2==1):
#         right-=1
#     while(left<right):
#         if(a[right]%2==0 and a[left]%2==1):
#             ezer=a[left]
#             a[left]=a[right]
#             a[right]=ezer
#             right-=1
#             left+=1
#         else:


#   08/04 B

# import random
#
#
# def BinariSearch(a):
#     low = 0
#     up = len(a) - 1
#     while (low < up):
#         mid = (low + up) // 2
#         if (x == a[mid]):
#             return mid
#         if (x < a[mid]):
#             up = mid - 1
#         else:
#             low = mid + 1
#     return -1
#
#
# a = [0] * 10000
# a[0] = 2
# for i in range(1, len(a)):
#     a[i] = a[i - 1] + random.randint(1, 6)
# print(a)
# x = int(input("Enter a number : "))
# print(BinariSearch(a))

#   08/04 C

# import random
#
#
# def BinariSearch(a, x):
#     low = 0
#     up = len(a) - 1
#     while (low <= up):
#         mid = (low + up) // 2
#         if (x == a[mid]):
#             return mid
#         if (x < a[mid]):
#             up = mid - 1
#         else:
#             low = mid + 1
#     return -1


# def Search(a, x):
#     for i in range(len(a)):
#         if(a[i]==x):
#             return i
#     return -1

# a = [0] * 100000
# a[0] = 2
# for i in range(1, len(a)):
#     a[i] = a[i - 1] + random.randint(1, 6)
# print(a)
# y = int(input("Enter a number : "))
# print(BinariSearch(a, y))

#   11/04 A

# a = [
#     [3, 5, 7, 6, 9],
#     [3, 5, 4, 1, 2, 4, 4, 5],
#     [7, 4, 5, 6, 7, 3],
#     [1, 2, 3],
# ]
# for r in range(len(a)):
#     for c in range(len(a[r])):
#         print(a[r][c], end=" ")
#     print()
#
# '''
# 3 5 7 6 9
# 3 5 4 1 2 4 4 5
# 7 4 5 6 7 3
# 1 2 3
# '''

# a=[45,102,674,19,876,45]
# #a=[102,674,19,876,45,45]
# temp=a[0]
# for i in range(1, len(a)):
#     a[i-1]=a[i]
# #a[len(a)-1]=temp
# a[i]=temp
# print(a)


# a=[-456,-102,-67834,-19,-876,-45]
# #a=[6,2,8,9,8,5]
# max=a[0]
# for i in range(len(a)):
#     if(max<a[i]):
#         max=a[i]
# print(max)


# a=[456,102,67834,1009,876,45]
# #a=[6,2,8,9,8,5]
# for i in range(len(a)):
#     max=0
#     while(a[i]>0):
#         if(max<a[i]%10):
#             max=a[i]%10
#         a[i]=a[i]//10
#     a[i]=max
# print(a)


# a=[456,102,67834,1009,876,45]
# #a=[15,3,28,10,21,9]
# for i in range(len(a)):
#     sum=0
#     while(a[i]>0):
#         sum=sum+a[i]%10
#         a[i]=a[i]//10
#     a[i]=sum
# print(a)


# a=[456,102,67834,1009,876,45]
# #a=[4,1,6,9,8,4]
# for i in range(len(a)):
#     while(a[i]>9):
#         a[i]=a[i]//10
# print(a)


# a=[456,12,67834,9,876,45]
# #a=[3,2,5,1,3,2]
# for i in range(len(a)):
#     c=0
#     while(a[i]>0):
#         c+=1
#         a[i]=a[i]//10
#     a[i]=c
# print(a)


# def IntToString(n):
#     s=""
#     while(n>0):
#         t=chr((n%10)+48)
#         s=t+s
#         n=n//10
#     return s

# y=6834
# x=IntToString(y)
# x=x+"fdhf"
# print(x)

# x=6834
# y=str(x)
# y=y+"***"
# print(y)


# def StringToInt(s): #   s="6824"
#     num=0
#     ord0=ord('0')   #   48
#     for i in range(len(s)):
#         num = num*10 + ord(s[i])-ord0
#     return num
# qqq=input("Enter a number : ")
# qqq="4561"
# n = StringToInt(qqq)
# n=n+1
# print(n)

# #   3 6 2   ====>   362
# #   0*10 + 3    3
# #   3*10 + 6    36
# #   36*10+ 2    362


# r=9
# t=r+1
# while(r>0):
#     for s in range(r, 0, -1):
#         print("*", end=" ")
#     s=r
#     while(s<t):
#         print(r, end=" ")
#         s+=1
#     # for s in range(r, t, 1):
#     #     print(r, end=" ")
#     print()
#     r-=1

# '''
# *****5
# ****44
# ***333
# **2222
# *11111

# '''


# def Show(n):
#     for r in range(n):    #   (0, n, 1)
#         for c in range(-1, r, 1):
#             print("*", end=" ")
#         print()
# Show(4)
# Show(5)


# def Mul(a, b):
#     if(a<b):
#         r=0
#         while(a>0):
#             r=r+b
#             a-=1
#     else:
#         r=0
#         while(b>0):
#             r=r+a
#             b-=1
#     return r

# print(Mul(5, 6))
# print(Mul(5, 6))


# d=0
# r=1
# while(r<5):
#     d=d+r
#     print(d, r)
#     r+=1
# print((d+r), r)
# #   d=0     1   3   6   10
# #   r=1     2   3   4   5

# #                   1   1
# #                   3   2
# #                   3   2
# #                   10  4
# #                   10  5

#   11/04 B

# a = [
#     [3, 5, 6, 6, 9],
#     [3, 5, 4, 1, 2],
#     [7, 4, 5, 6, 7],
#     [1, 2, 3, 4, 0]
# ]
# m = 0
# for r in range(len(a)):
#     for c in range(len(a[r]) - 1):
#         if (a[r][c] + 1 == a[r][c + 1]):
#             m += 1
# print(m)

# a=[
#     [3,5,7,6,9],
#     [3,5,4,1,2,4,4,5],
#     [7,4,5,6,7,3],
#     [1,2,3],
# ]
# total=0
# for r in range(len(a)):
#     sum=0
#     for c in range(len(a[r])):
#         sum=sum+a[r][c]
#         print(a[r][c], end=" ")
#     total+=sum
#     print("      ", sum)
# print(total)
# '''
# 3 5 7 6 9
# 3 5 4 1 2 4 4 5
# 7 4 5 6 7 3
# 1 2 3
# 96
# '''


# a=[
#     [3,5,7,6,9],
#     [3,5,4,1,2,4,4,5],
#     [7,4,5,6,7,3],
#     [1,2,3],
# ]
# for r in range(len(a)):
#     sum=0
#     for c in range(len(a[r])):
#         sum=sum+a[r][c]
#         print(a[r][c], end=" ")
#     print("      ", sum)

# '''
# 3 5 7 6 9        30
# 3 5 4 1 2 4 4 5        28
# 7 4 5 6 7 3        32
# 1 2 3        6
# '''


# a=[
#     [3,5,7,6,9],
#     [3,5,4,1,2,4,4,5],
#     [7,4,5,6,7,3],
#     [1,2,3],
# ]
# for r in range(len(a)):
#     for c in range(len(a[r])):
#         print(a[r][c], end=" ")
#     print()

# '''
# 3 5 7 6 9
# 3 5 4 1 2 4 4 5
# 7 4 5 6 7 3
# 1 2 3
# '''


# a=[45,102,674,19,876,45]
# #a=[102,674,19,876,45,45]
# temp=a[0]
# for i in range(1, len(a)):
#     a[i-1]=a[i]
# #a[len(a)-1]=temp
# a[i]=temp
# print(a)


# a=[-456,-102,-67834,-19,-876,-45]
# #a=[6,2,8,9,8,5]
# max=a[0]
# for i in range(len(a)):
#     if(max<a[i]):
#         max=a[i]
# print(max)


# a=[456,102,67834,1009,876,45]
# #a=[6,2,8,9,8,5]
# for i in range(len(a)):
#     max=0
#     while(a[i]>0):
#         if(max<a[i]%10):
#             max=a[i]%10
#         a[i]=a[i]//10
#     a[i]=max
# print(a)


# a=[456,102,67834,1009,876,45]
# #a=[15,3,28,10,21,9]
# for i in range(len(a)):
#     sum=0
#     while(a[i]>0):
#         sum=sum+a[i]%10
#         a[i]=a[i]//10
#     a[i]=sum
# print(a)


# a=[456,102,67834,1009,876,45]
# #a=[4,1,6,9,8,4]
# for i in range(len(a)):
#     while(a[i]>9):
#         a[i]=a[i]//10
# print(a)


# a=[456,12,67834,9,876,45]
# #a=[3,2,5,1,3,2]
# for i in range(len(a)):
#     c=0
#     while(a[i]>0):
#         c+=1
#         a[i]=a[i]//10
#     a[i]=c
# print(a)


# def IntToString(n):
#     s=""
#     while(n>0):
#         t=chr((n%10)+48)
#         s=t+s
#         n=n//10
#     return s

# y=6834
# x=IntToString(y)
# x=x+"fdhf"
# print(x)

# x=6834
# y=str(x)
# y=y+"***"
# print(y)


# def StringToInt(s): #   s="6824"
#     num=0
#     ord0=ord('0')   #   48
#     for i in range(len(s)):
#         num = num*10 + ord(s[i])-ord0
#     return num
# qqq=input("Enter a number : ")
# qqq="4561"
# n = StringToInt(qqq)
# n=n+1
# print(n)

# #   3 6 2   ====>   362
# #   0*10 + 3    3
# #   3*10 + 6    36
# #   36*10+ 2    362


# r=9
# t=r+1
# while(r>0):
#     for s in range(r, 0, -1):
#         print("*", end=" ")
#     s=r
#     while(s<t):
#         print(r, end=" ")
#         s+=1
#     # for s in range(r, t, 1):
#     #     print(r, end=" ")
#     print()
#     r-=1

# '''
# *****5
# ****44
# ***333
# **2222
# *11111

# '''


# def Show(n):
#     for r in range(n):    #   (0, n, 1)
#         for c in range(-1, r, 1):
#             print("*", end=" ")
#         print()
# Show(4)
# Show(5)


# def Mul(a, b):
#     if(a<b):
#         r=0
#         while(a>0):
#             r=r+b
#             a-=1
#     else:
#         r=0
#         while(b>0):
#             r=r+a
#             b-=1
#     return r

# print(Mul(5, 6))
# print(Mul(5, 6))


# d=0
# r=1
# while(r<5):
#     d=d+r
#     print(d, r)
#     r+=1
# print((d+r), r)
# #   d=0     1   3   6   10
# #   r=1     2   3   4   5

# #                   1   1
# #                   3   2
# #                   3   2
# #                   10  4
# #                   10  5

#   15/04 A

# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")


#   15/04 B

# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i<len(s)-1):
#        print("NO")
#     else:
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            print("YES")
#         else:
#            print("NO")
# print(m)


# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")
#     else:
#        print("NO")

#   15/04 C

# def A(l):
#     if (len(l) % 2 == 1):
#         return False
#     else:
#         c = -11
#         t = [0] * len(l)
#         for a in range(len(l)):
#             if (t[a] == 0):
#                 c = 1
#                 t[a] = 1
#                 for b in range(a + 1, len(l)):
#                     if (l[a] == l[b]):
#                         c += 1
#                         t[b] = 1
#             if (c != 2):
#                 return False
#         return True
#
#
# l = [1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# print(A(l))

# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         for a in range(len(l)):
#             c=0
#             for b in range(len(l)):
#                 if(l[a]==l[b]):
#                     c+=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# t=[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
# A(l)


# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i==len(s)-1):
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            m+=1
# print(m)


# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")
#     else:
#        print("NO")

#   15/04 D

# s = input("Enter a string : ")
# c = 0
# while (s[0] != 'Z' and s[len(s) - 1] != 'Z'):
#     if (s[0] == 'X' and s[len(s) - 1] == 'X'):
#         c += 1
#     s = input("Enter a string : ")
# print(c)

# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         c=-11
#         t=[0]*len(l)
#         for a in range(len(l)):
#             if(t[a]==0):
#                 c=1
#                 t[a]=1
#                 for b in range(a+1, len(l)):
#                     if(l[a]==l[b]):
#                         c+=1
#                         t[b]=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# print(A(l))


# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         for a in range(len(l)):
#             c=0
#             for b in range(len(l)):
#                 if(l[a]==l[b]):
#                     c+=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# t=[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
# A(l)


# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i==len(s)-1):
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            m+=1
# print(m)


# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")
#     else:
#        print("NO")

#   15/04 E

# n1 = int(input("Enter first number : "))
# n2 = int(input("Enter second number : "))
# c = 0
# s = 0
# e = 0
# while (n1 * (-1) != n2):
#     c += 2
#     if (n1 > 0):
#         s += n1
#     if (n2 > 0):
#         s += n2
#     if (n1 == n2):
#         e += 1
#     n1 = int(input("Enter first number : "))
#     n2 = int(input("Enter second number : "))
# print(c, s, e)

# def IsPeak(arr, index):
#     if(index==0 or index==len(arr)-1):
#         return False
#     if(arr[index-1]<arr[index] and arr[index+1]<arr[index]):
#         return True
#     return False
# a=[1,2,3,4,5,5,6,4,5,6,2,3,3,2,1,2,1,3,4,2,3,1]
# c=0
# for i in range(1, len(a)-1):
#     if(IsPeak(a, i)==True):
#         c+=1
# print(c)

# s=input("Enter a string : ")
# c=0
# while(s[0]!='Z' and s[len(s)-1]!='Z'):
#     if(s[0]=='X' and s[len(s)-1]=='X'):
#         c+=1
#     s=input("Enter a string : ")
# print(c)


# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         c=-11
#         t=[0]*len(l)
#         for a in range(len(l)):
#             if(t[a]==0):
#                 c=1
#                 t[a]=1
#                 for b in range(a+1, len(l)):
#                     if(l[a]==l[b]):
#                         c+=1
#                         t[b]=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# print(A(l))


# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         for a in range(len(l)):
#             c=0
#             for b in range(len(l)):
#                 if(l[a]==l[b]):
#                     c+=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# t=[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
# A(l)


# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i==len(s)-1):
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            m+=1
# print(m)


# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")
#     else:
#        print("NO")

#   15/04 F

# def F(a):
#     if (len(a) % 3 != 0):
#         return False
#     left = 0
#     right = len(a) // 3
#     while (right < len(a) and a[left] == a[right]):
#         left += 1
#         right += 1
#
#
# r = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# import random
# def G(num):
#     a=[0]*num
#     for i in range(num):
#         x=random.randint(10, 99)
#         while(x//10>=x%10):
#             x=random.randint(10, 99)
#         a[i]=x
#     print(a)
# G(22)


# import random
# def G(num):
#     a=[0]*num
#     for i in range(num):
#         asarot=random.randint(1,8)
#         ahadot=random.randint(asarot+1,9)
#         a[i]=asarot*10+ahadot
#     print(a)
# G(22)
#   36


# n1=int(input("Enter first number : "))
# n2=int(input("Enter second number : "))
# c=0
# s=0
# e=0
# while(n1*(-1)!=n2):
#    c+=2
#    if(n1>0):
#       s+=n1
#    if(n2>0):
#       s+=n2
#    if(n1==n2):
#       e+=1
#    n1=int(input("Enter first number : "))
#    n2=int(input("Enter second number : "))
# print(c, s, e)


# def IsPeak(arr, index):
#     if(index==0 or index==len(arr)-1):
#         return False
#     if(arr[index-1]<arr[index] and arr[index+1]<arr[index]):
#         return True
#     return False
# a=[1,2,3,4,5,5,6,4,5,6,2,3,3,2,1,2,1,3,4,2,3,1]
# c=0
# for i in range(1, len(a)-1):
#     if(IsPeak(a, i)==True):
#         c+=1
# print(c)

# s=input("Enter a string : ")
# c=0
# while(s[0]!='Z' and s[len(s)-1]!='Z'):
#     if(s[0]=='X' and s[len(s)-1]=='X'):
#         c+=1
#     s=input("Enter a string : ")
# print(c)


# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         c=-11
#         t=[0]*len(l)
#         for a in range(len(l)):
#             if(t[a]==0):
#                 c=1
#                 t[a]=1
#                 for b in range(a+1, len(l)):
#                     if(l[a]==l[b]):
#                         c+=1
#                         t[b]=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# print(A(l))


# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         for a in range(len(l)):
#             c=0
#             for b in range(len(l)):
#                 if(l[a]==l[b]):
#                     c+=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# t=[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
# A(l)


# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i==len(s)-1):
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            m+=1
# print(m)


# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")
#     else:
#        print("NO")

#   15/04 G

# def F(a):
#     if (len(a) % 3 != 0):
#         return False
#     left = 0
#     right = len(a) // 3
#     while (right < len(a) and a[left] == a[right]):
#         left += 1
#         right += 1
#     if (right == len(a)):
#         return True
#     return False
#
#
# r = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(F(r))

# import random
# def G(num):
#     a=[0]*num
#     for i in range(num):
#         x=random.randint(10, 99)
#         while(x//10>=x%10):
#             x=random.randint(10, 99)
#         a[i]=x
#     print(a)
# G(22)


# import random
# def G(num):
#     a=[0]*num
#     for i in range(num):
#         asarot=random.randint(1,8)
#         ahadot=random.randint(asarot+1,9)
#         a[i]=asarot*10+ahadot
#     print(a)
# G(22)
#   36


# n1=int(input("Enter first number : "))
# n2=int(input("Enter second number : "))
# c=0
# s=0
# e=0
# while(n1*(-1)!=n2):
#    c+=2
#    if(n1>0):
#       s+=n1
#    if(n2>0):
#       s+=n2
#    if(n1==n2):
#       e+=1
#    n1=int(input("Enter first number : "))
#    n2=int(input("Enter second number : "))
# print(c, s, e)

# def IsPeak(arr, index):
#     if(index==0 or index==len(arr)-1):
#         return False
#     if(arr[index-1]<arr[index] and arr[index+1]<arr[index]):
#         return True
#     return False
# a=[1,2,3,4,5,5,6,4,5,6,2,3,3,2,1,2,1,3,4,2,3,1]
# c=0
# for i in range(1, len(a)-1):
#     if(IsPeak(a, i)==True):
#         c+=1
# print(c)

# s=input("Enter a string : ")
# c=0
# while(s[0]!='Z' and s[len(s)-1]!='Z'):
#     if(s[0]=='X' and s[len(s)-1]=='X'):
#         c+=1
#     s=input("Enter a string : ")
# print(c)


# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         c=-11
#         t=[0]*len(l)
#         for a in range(len(l)):
#             if(t[a]==0):
#                 c=1
#                 t[a]=1
#                 for b in range(a+1, len(l)):
#                     if(l[a]==l[b]):
#                         c+=1
#                         t[b]=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# print(A(l))


# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         for a in range(len(l)):
#             c=0
#             for b in range(len(l)):
#                 if(l[a]==l[b]):
#                     c+=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# t=[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
# A(l)


# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i==len(s)-1):
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            m+=1
# print(m)


# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")
#     else:
#        print("NO")
