n, m = map(int, input().split())
danhsach = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happy = 0

for num in danhsach:
    if num in A:
        happy += 1
    elif num in B:
        happy -= 1
print(happy)


