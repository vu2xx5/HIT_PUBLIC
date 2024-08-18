n = int(input("Nhap n: "))
step = 1

def tongchuso(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong
while n // 10 != 0:
    step+=1
    n = tongchuso(n)
print(n, step)