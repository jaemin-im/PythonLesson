'''
# 1
a = input()
b = input()
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print("%.2f" % (a / b))
print(int(a/b))
print(a % b)


# 2
a, b = input().split() # 한 줄 입력이 가능해진다.
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print("%.2f" % (a / b))
print(int(a/b))
print(a % b)

# 3
a, b = map(int, input().split()) # 입력을 받아서 각 변수에 정수로 mapping
print(a + b)
print(a - b)
print(a * b)
print("%.2f" % (a / b))
print(int(a/b))
print(a % b)
'''

# 4
a, b = map(int, input().split())
print(a + b, a - b, a * b, "%.2f" % (a / b), a // b, a % b, sep='\n')
