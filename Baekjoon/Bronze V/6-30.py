# 1000 A+B
# num1, num2 = map(int, input().split())
# print(num1 + num2)

# 1001 A-B
# num1, num2 = map(int, input().split())
# print(num1 - num2)

# 1008 A/B
# num1, num2 = map(int, input().split())
# print(num1 / num2)

# 1330 두 수 비교하기
# num1, num2 = map(int, input().split())
# if num1 < num2:
#     print('<')
# elif num1 > num2:
#     print('>')
# else:
#     print('==')

# 2420 사파리월드
# num1, num2 = map(int, input().split())
# print(abs(num1 - num2))

# 2438 별찍기 - 1
# num = int(input())
# for i in range(1, num+1):
#     for j in range(i):
#         print('*', end='')
#     print('')

# 2557 Hello World
# print('Hello World!')

# 2738 행렬 덧셈
# arr1 = []
# arr2 = []
# n, m = map(int, input().split())
#
# for i in range(n):
#     arr1.append(list(map(int, input().split())))
#
# for i in range(n):
#     arr2.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(m):
#         print(arr1[i][j]+arr2[i][j], end=' ')
#     print()

# 2739 구구단
# num = int(input())
# for i in range(1, 10):
#     print(num,'*', i, '=' , num * i)

# 2741 N 찍기
# num = int(input())
# for i in range(1, num+1):
#     print(i)

# 2743 단어 길이 재기
# string = str(input())
# print(len(string))

# 2744 대소문자 바꾸기
# string = str(input())
# result = []
# for i in range(len(string)):
#     if string[i].islower():
#         result.append(string[i].upper())
#     else:
#         result.append(string[i].lower())
#
# for i in range(len(result)):
#     print(result[i], end='')

# 2753 윤년
# year = int(input())
# if ((year % 4 == 0) and (year % 100 != 0)) | ((year % 4 == 0) and (year % 400 == 0)) :
#     print(1)
# else:
#     print(0)

# 2754 학점계산
# score = str(input())
# if score == 'A+':
#     print(4.3)
# elif score == 'A0':
#     print(4.0)
# elif score == 'A-':
#     print(3.7)
# elif score == 'B+':
#     print(3.3)
# elif score == 'B0':
#     print(3.0)
# elif score == 'B-':
#     print(2.7)
# elif score == 'C+':
#     print(2.3)
# elif score == 'C0':
#     print(2.0)
# elif score == 'C-':
#     print(1.7)
# elif score == 'D+':
#     print(1.3)
# elif score == 'D0':
#     print(1.0)
# elif score == 'D-':
#     print(0.7)
# else:
#     print(0.0)

# 5597 과제 안내신 분..?
# arr = []
# ttl = []
#
# for i in range(28):
#     arr.append(int(input()))
#
# for i in range(1, 31):
#     ttl.append(i)
#
# for i in range(len(arr)):
#     if arr[i] in ttl:
#         ttl.remove(int(arr[i]))
#
# if ttl[0] > ttl[1]:
#     print(ttl[1])
#     print(ttl[0])
# else:
#     print(ttl[0])
#     print(ttl[1])

# 7287 등록
# print(15)
# print('smj990203')

# 9086 문자열
# num = int(input())
# arr = []
# for i in range(num):
#     arr.append(str(input()))
#
# for i in range(num):
#     print(arr[i][0]+arr[i][-1])

# 9498 시험 성적
# score = int(input())
# if score >= 90 and score <= 100:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# 10171 고양이
# print('\\    /\\')
# print(' )  ( \')')
# print('(  /  )')
# print(' \\(__)|')

# 10172 개
# print('|\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')

# 10699 오늘 날짜
# import datetime
# d = datetime.datetime.now()
# print(d.strftime("%Y-%m-%d"))

# 10807 개수 세기
# num = int(input())
# data = list(map(int, input().split()))
# find = int(input())
# print(data.count(find))

# 10809 알파벳 찾기
# from string import ascii_lowercase
#
# alphabet_list = list(ascii_lowercase)
# string = str(input())
# arr = []
# for i in range(len(alphabet_list)):
#     if alphabet_list[i] in string:
#         arr.append(string.find(alphabet_list[i]))
#     else:
#         arr.append(-1)
#
# for i in arr:
#     print(i, end=' ')

# 10869 사칙연산
# from math import trunc
#
# num1, num2 = map(int, input().split())
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(trunc(num1 / num2))
# print(num1 % num2)

# 10870 피보나치 수 5
# num = int(input())
# arr = [0, 1]
#
# def fibo(arr, i):
#     arr.append(arr[i] + arr[i+1])
#
# for i in range(num):
#     fibo(arr, i)
# print(arr[num])

# 10871 X보다 작은 수
# n, x = map(int, input().split())
# t = input().split()
#
# for i in range(n):
#     if int(t[i]) < x:
#         print(t[i], end=' ')

# 10872 팩토리얼
# num = int(input())
# if num == 0:
#     print(1)
# else:
#     result = 1
#     for i in range(1, num+1):
#         result = result * i
#     print(result)

# 10950 A+B - 3
# num = int(input())
# arr = []
# for i in range(num):
#     t1, t2 = map(int, input().split())
#     print(t1+t2)

# 10951 A+B - 4
# while(1):
#     try:
#         t1, t2 = map(int, input().split())
#         print(t1 + t2)
#     except:
#         break

# 10952 A+B - 5
# while(1):
#     try:
#         t1, t2 = map(int, input().split())
#         if t1 == 0 and t2 == 0:
#             break
#         print(t1 + t2)
#     except:
#         break

# 10998 AxB
# t1, t2 = map(int, input().split())
# print(t1 * t2)

# 11382 꼬마 정민
# string = input()
# arr = string.split(' ')
# result = 0
# for i in arr:
#     result += int(i)
# print(result)

# 11654 아스키 코드
# string = input()
# print(ord(string))

# 11718 그대로 출력하기
# while(1):
#     try:
#         string = input()
#         print(string)
#     except:
#         break

# 14681 사분면 고르기
# t1 = int(input())
# t2 = int(input())
# if t1 > 0 and t2 > 0:
#     print(1)
# elif t1 < 0 and t2 > 0:
#     print(2)
# elif t1 < 0 and t2 < 0:
#     print(3)
# elif t1 > 0 and t2 < 0:
#     print(4)

# 23037 5의 수난
# num = input()
# result = 0
# for i in range(len(num)):
#     result += int(num[i]) * int(num[i]) * int(num[i]) * int(num[i]) * int(num[i])
#
# print(result)

# 25083 새싹
# print('         ,r\'"7')
# print('r`-_   ,\'  ,/')
# print(' \. ". L_r\'')
# print('   `~\\/')
# print('      |')
# print('      |')

# 15552 빠른 A+B
# import sys
#
# num = int(sys.stdin.readline())
# for i in range(num):
#     t1, t2 = map(int, sys.stdin.readline().split())
#     print(t1 + t2)

