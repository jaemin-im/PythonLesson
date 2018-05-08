'''
# 일반 코드
ai = input("행렬 A의 행/열, 행렬 B의 행/열을 입력하십시오. : \n")
aj = input()
bi = input()
bj = input()
ai = int(ai)
aj = int(aj)
bi = int(bi)
bj = int(bj)

if aj != bi:
    print("A_j와 B_i가 달라 행렬곱을 수행할 수 없습니다.")
    exit()

A = [[0 for columns in range(aj)] for rows in range(ai)]
B = [[0 for columns in range(bj)] for rows in range(bi)]
R = [[0 for columns in range(bj)] for rows in range(ai)]

for i in range(ai):
    for j in range(aj):
        A[i][j] = int(input("{}행 {}열의 요소를 입력하십시오. : ".format(i, j)))
for i in range(bi):
    for j in range(bj):
        B[i][j] = int(input("{}행 {}열의 요소를 입력하십시오. : ".format(i, j)))

print(A)
print(B)
print(R)
choose = input("입력한 행렬이 위와 같은지 확인하십시오. 정확합니까? Y / N\n")

if choose == 'N' or choose == 'n':
    print("프로그램을 다시 실행시켜 재입력하십시오.")
    exit()

for i in range(len(R)):
    for j in range(len(R[0])):
        for k in range(len(A[0])):
            R[i][j] += A[i][k] * B[k][j]

print(R)
'''
# 축소한 코드
import numpy as np

ai, aj, bi, bj = map(int, input("행렬 A의 행/열, 행렬 B의 행/열을 입력하십시오. : \n").split())
if aj != bi:
    print("A_j와 B_i가 달라 행렬곱을 수행할 수 없습니다.")
A = np.zeros((ai, aj))
B = np.zeros((bi, bj))
R = np.zeros((ai, bj))

for i in range(ai):
    for j in range(aj):
        A[i][j] = int(input("{}행 {}열의 요소를 입력하십시오. : ".format(i, j)))
for i in range(bi):
    for j in range(bj):
        B[i][j] = int(input("{}행 {}열의 요소를 입력하십시오. : ".format(i, j)))

print(A)
print(B)
print(R)
choose = input("입력한 행렬이 위와 같은지 확인하십시오. 정확합니까? Y / N\n")

if choose == 'N' or choose == 'n':
    print("프로그램을 다시 실행시켜 재입력하십시오.")
    exit()

print(np.dot(A, B))
