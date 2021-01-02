#1번
# class UpgradeCalculator(Calculator):#클레스 머시기를 만든다
#     def minus(self, val):#def minus함수를 만들고 그안에 self와minus를 너준다
#         self.value -= val#마지막으로self와value을뺀거는 val이라는걸 알려준다
# #2번        
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100

# #3번

# #4번
# list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))
# #5번
# print(int('0xea', 16))
#6번
# print(list(map(lambda x:x*3, [1,2,3,4])))
#7번
# a = [-8, 2, 7, 5, -3, 5, 0, 1]
# print((a)max(a) + min(a))
#8번
# print(round(17/3, 4))#17나누기3을하고4번쩨줄까지
#9번
# import sys

# numbers = sys.argv[1:]

# result = 0
# for number in numbers:
#     result += int(number)
# print(result)
# #12번
# import time
# print(time.strftime("%y/%m/%d/%h:%m:%s"))
#6장부터끝까지
def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result
print(gugu(2))
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n% 5 == 0:
        result += n
print(result)

