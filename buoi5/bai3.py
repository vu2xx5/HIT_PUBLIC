import random
import json
account={}
my_list=[ 'CNTT', 'KHMT', 'KTPM', 'HTTT']
n=int(input("Nhap so tai khoan phai lap: "))
codinh=2023600001
for i in range(n):
    msv=codinh + i
    matkhau=random.choice(my_list)
    password=matkhau+str(msv)
    tk= f"account{i+1}"
    account[tk]= {
        'username': msv,
        'password': password
    }
print("Dict chua tk cua sv la:")
print(json.dumps(account, indent=2))