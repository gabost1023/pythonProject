a = [1-x for x in range(1,11)]
b = [4**i for i in range(8)]
c = [x for x in b if x%2==0]

print(a)
print(b)
print(c)