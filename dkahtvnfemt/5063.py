n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())
    a = e - c
    if r < a:
        print("advertise")
    elif r == a:
        print("does not matter")
    else:
        print("do not advertise")
#r, e, c를 입력받고, e와 c를 뺀 값을 a에 저장한
#r과 a를 비교해서 a가 더 크면 advertise를 같으면 do not advertise를 r이 더 크면 does not matter를 출력한다