# a= "this is programming language"
# print(a[::-1])
s = "programmings"
print("String before:", s)
a = s.split()
res = []
for i in a:
    x = i[0].upper()+i[1:-1]+i[-1].upper()
    res.append(x)
res = " ".join(res)
print("String after:", res)