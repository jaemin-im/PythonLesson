a = input()
b = input()
i = 0
'''
while i < len(b):
    if b[i] != ' ':
        print(a.find(b[i]), end="")
    else:
        print(b[i], end="")
    i = i + 1
'''
for i in b:
    print(a.find(i) if i != ' ' else i, end="")
