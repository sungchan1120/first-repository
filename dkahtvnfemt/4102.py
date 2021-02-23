a, b = map(int, input().split())

while not (a == 0 and b == 0):# 
    if a > b:
        print("Yes")#a가b보다 크면 yes
    else:
        print("No")
    a, b = map(int, input().split())