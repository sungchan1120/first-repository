s = int(input())
n = 1
while n * (n + 1) / 2 <= s: #n * (n + 1) / 2는 1부터 n까지의 합의 공식이다
    n += 1
print(n-1)
#1부터 차례대로 더해 s보다 커지게 되면 그 개수에서 1을 빼면 된다