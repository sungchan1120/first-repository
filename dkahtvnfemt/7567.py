import sys
sys.stdin = open("input.txt", 'r')

s = input()
l = 10#그릇 높이
p = s[0]
for i in range(1, len(s)):
    l += (5 if s[i] == p else 10)#
    p = s[i]
print(l)