a=[ i for i in range(3)]
print(a)
b=[ j for j in range(4,7)]
print(b)
print(id(a))
print(id(b))
if a==b:
    print(True)
else:
    print(False)