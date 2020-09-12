odd = [1,3,5,7,9]
print(odd)

a = [1,2,3]
print(a)

a[0]
print(a)

a[0] + a[2]
print(a)

a[-1]
print(a)

a = [1,2,3,['a','b','c']]
print(a)

a[0]
print(a)

a[-1][0]
print(a)

a[0]
print(a)
a[-1]
['a','b','c']
print(a)

a[3]
['a','b','c']
print(a)

a[-1][0]
'a'
print(a)

a[-1][1]
print(a)

a = [1,2,3,4,5]
a[0:2]
print(a)

a = "12345"
a[0:2]
'12'
print(a)

a = [1,2,3]
b = [4,5,6,]
print(a + b)

a = [1,2,3]
print(a * 3)

a = [1,2,3]
print(len(a))

a = [1,2,3]
a[2] = 4
print(a)

a = [1,2,3]
del a[1]
print(a)

a = [1,2,3,4,5]
del a[2:]
print(a)

a = [1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

a = ['a','c','b']
a.reverse()
print(a)

a = ['a','c','b']
a.reverse()
print(a)

a = [1,2,3]
print(a.index(3))

print(a.index(1))

a = [1,2,3]
a.insert(0,4)
print(a)

a.insert(3,5)
print(a)

a.remove(3)
print(a)

a = [1,2,3]
a.pop()
print(a)

a = [1,2,3,1]
print(a.count(1))

a = [1,2,3]
a.extend([4,5])
print(a)