def stair(n):
    if n < 3: return n
    else: return stair(n - 1) + stair(n - 2)

n = int(input("input stair's number : "))
print(stair(n))
