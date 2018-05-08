import numpy as np
def twoMatrix(isMultiply):
    ai, aj, bi, bj = map(int, input("행렬 A의 행/열, 행렬 B의 행/열을 입력하십시오. : \n").split())
    if aj != bi and isMultiply is True:
        print("행렬 A의 열 개수와 B의 행 개수가 달라 행렬곱을 수행할 수 없습니다.")
        exit()
    elif (ai != bi or aj != bj) and isMultiply is False:
        print("행렬 A와 행렬 B의 크기가 달라 연산을 수행할 수 없습니다.")
        exit()
    tempA = np.zeros((ai, aj))
    tempB = np.zeros((bi, bj))
    for i in range(ai):
        for j in range(aj):
            tempA[i][j] = int(input("1번째 행렬의 {}행 {}열의 요소를 입력하십시오. : ".format(i, j)))
    for i in range(bi):
        for j in range(bj):
            tempB[i][j] = int(input("2번째 행렬의 {}행 {}열의 요소를 입력하십시오. : ".format(i, j)))
    return tempA, tempB
try:
    select = int(input("1. 행렬 덧셈\n2. 행렬 뺄셈\n3. 행렬 행렬곱\n숫자를 입력하십시오. : \n"))
except ValueError:
    print("이상한 값을 넣지 마십시오. 빠가야로\n")
    exit()
if select == 1:
    A, B = twoMatrix(False)
    print("행렬 덧셈의 결과 : \n{}".format(A + B))
elif select == 2:
    A, B = twoMatrix(False)
    print("행렬 뺄셈의 결과 : \n{}".format(A - B))
elif select == 3:
    A, B = twoMatrix(True)
    print("행렬 행렬곱의 결과: \n{}".format(np.dot(A, B)))
