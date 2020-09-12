a="20010331Rainy"
date = a[:8]
weather = a[8:]

print(date)
print(weather)

a= "20010331rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

a = "I eat %d apples." % 3
print(a)

a="I eat %s appies." % "five"
print(a)

number = 3
a = "I eat %d appies." % number

number = 10
day = "three"
a = "I eat %d apples. so I was sick for %s days." % (number, day)
print(a)

a= "I have %s" % 3
print(a)
a= "rate is %s" % 3.234
print(a)

a = "%10s" % "hi"
print(a)

a = "%-10sjane." % 'hi'
print(a)

a = "%10.4f" % 3.42134234
print(a)

a = "I eat {0} apples" .format(3)
print(a)

a = "I eat {0} apples".format("five")
print(a)

number = 3
a= "I eat {0} apples".format(number)
print(a)

number = 10
day ="three"
a="I eat {0} apples. so I was sick for {1} day.".format(number, day)
print(a)
a="I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(a)

a="I ate {0} appies. so I was sick for {day} days.".format(10, day=3)
print(a)

a="{0:<10}".format("hi")
print(a)

a="{0:>10}".format("hi")
print(a)

a="{0:=^10}".format("hi")
print(a)

a="{0:!<10}".format("hi")
print(a)

y= 3.42134234
print(y)

y="{0:10.4f}".format(y)
print(y)

a="{{ and }}".format()
print(a)

name = '홍길동'
age =30
print(f'나에 이름은 {name}입니다. 나이는 {age}입니다.')

age = 30
print(f'나는 내년이면 {age+1}살이 된다')

print(f'{"hi":<10}')

print(f'{"hi":>10}')

print(f'{"hi":^10}')

y = 3.42134234
print(f'{y:0.4f}')

print(f'{{ and }}')

a="hobby"
print(a.count('b'))

a="Python is the best choice"
print(a.find('b'))

a = "Life is too short"
print(a.index('t'))

a = ",".join(['a', 'b', 'c', 'd'])
print(a)


a = "hi"
print(a)

a= "hi"
print(a)

a= "hi"
print(a)

a = "Life is too short"
a.replace("Life", "Your leg")
print(a)

a = "life is too short"
a.split()
print(a)

