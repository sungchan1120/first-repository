V = int(input())
vote = list(str(input()))

A = B = 0
for v in vote:
   if v == 'A':#a가b보다많으면 a
       A += 1
    else:
       B += 1#b가 a보다 많으면 b

if A > B:
   print('A')
elif A == B:
   print('Tie')#같으면 tie
else:
   print('B')
