my_dict= {"n":1500,
         "m":2,
         "CLUSTERS":3,
         "ITER":10000,
         "METHOD":"FCM",
         "MEASURE":"EUCLIDEAN",
         "YEARS":51
}
print(my_dict)
my_dict["MEASURE"]="MANHATAN"
my_dict["LOSS FUNCTION"]="NORM_2"
my_dict.pop("YEARS")
s = str(input())
if s in my_dict.values:
    print(f"s có trùng với giá trị của một thông số trong my_dict.")
else:
    print(f"s không trùng với giá trị của thông số nào trong my_dict.")
a = []
for values in my_dict.values:
    a.append(values)
my_set = set(a)
print(my_set)
print(a)