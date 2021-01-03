#1번
# a = "a:b:c:d"
# b = a.split(":")
# c = "#".join(b)
# print(c)
#2번
# a = {'a':90, 'b':80}
# a.gat('c',70)
# print (a)
#4번
# a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# result = 0
# while a:
#     mark = a.pop()
#     if mark >= 50:
#         result += mark
# print(result)
# #6번
# print(65+45+2+3+45+8)
# #7번
# print(':: 2단 ::')
# for i in range(1, 10):  # 1부터 9까지
#     print(f'2 x {i} = {2*i}')
# #8번
# f = open('abc.txt', 'r')
# lines = f.readlines()    
# f.close()

# lines.reverse()          

# f = open('abc.txt', 'w')
# for line in lines:
#     line = line.strip()  
#     f.write(line)
#     f.write('\n')        
# f.close()
#9번
# print((70+60+55+75+95+90+80+80+85+100)/10)
# #10번
# class Calculator:
#     def __init__(self, numberList): 
#         self.numberList = numberList

#     def sum(self): 
#         result = 0
#         for num in self.numberList: 
#             result += num
#         return result

#     def avg(self):
#         total = self.sum()
#         return total / len(self.numberList)

# cal1 = Calculator([1,2,3,4,5]) 
# print (cal1.sum())
# print (cal1.avg())

# cal2 = Calculator([6,7,8,9,10]) 
# print (cal2.sum())
# print (cal2.avg())
# #12번
# result = 0

# try:
#     [1, 2, 3][3]
#     "a"+1
#     4 / 0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4

# print(result)
# #13번
# data = "4546793"
# numbers = list(map(int, data))   
# result = []

# for i, num in enumerate(numbers):
#     result.append(str(num))
#     if i < len(numbers)-1:                   
#         is_odd = num % 2 == 1                
#         is_next_odd = numbers[i+1] % 2 == 1  
#         if is_odd and is_next_odd:           
#             result.append("-")
#         elif not is_odd and not is_next_odd: 
#             result.append("*")

# print("".join(result))
# #14번
# s = 'aabcccaaaaas'

# result = s[0]  # 첫번째 값을 결과에 넣는다
# count  = 0   #

# for st in s:
#     if st == result[-1]:  #
#         count += 1
#     else:
#         result += str(count) + st
#         count = 1
# result += str(count)

# print (result)
# #15번
# n = [''.join(sorted(x)) for x in raw_input().split()]
# for x in n:
#     print ("true" if x=="0123456789" else "false",)
#16번
# code=input().split(' ')

# chart= {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
#         '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
#         '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
#         '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
#         '-.--':'Y','--..':'Z'}

# decoded=''

# for x in code:
#     decodedletter=' '
#     for y in chart:
#         if x==y:
#             decodedletter=chart[y]
#             break

#     decoded+=decodedletter
#18번
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
print(m.start() + m.end())












