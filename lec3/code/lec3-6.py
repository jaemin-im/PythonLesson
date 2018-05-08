list_a = [3, 6, 9, 12]
res1 = []
for n in list_a:
    res1.append(n-1)
print(res1)

res2 = [n-1 for n in list_a]
print(res2)
