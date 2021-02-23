cases = int(input())

for i in range(cases):
    a,b = map(int, input().split())
    ans = a + b
    print("Case #%s: %s + %s = %s"%(i+1, a, b, ans ))# case #1 #2 하나씩 추가해가면서 %s + %s 는 input넣은 수를 더한다