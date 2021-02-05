T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)
#t를 입력 받고 t를 300초,60초,10초로 나눈다