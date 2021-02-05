a,b,c = map(int, input().split(''))
if(a >= b):
    if(a >= c):
        if(b >= c):
            print(b)
        else:
            print(c)#a가c보다크면c를 출력
    else:
        print(a)
else:
    if(b >= c):
        if(a >= c):
            print(a)
        else:
            print(c)
    else:
        print(b)
        