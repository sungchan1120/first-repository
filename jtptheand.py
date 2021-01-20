# a = "a:b:c:d" 
# b = a.split(":") #a의 : 지운다
# c = "#".join(b) #을 a에다가 집어는다
# print(c)

# a = {'a':90, 'b':80}  #먼저 a =90 b = 80 너준다
# a.gat('c',70) # a에다가 c를 는다
# print (a)

# a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25] 
# result = 0
# while a: # 20,55 등 반복적으로 해야되기 때문에 while을 쓴다
#         mark = a.pop() #pop은 리스트의 마지막 요소를 돌려주고 그요소는 삭제한다
#     if mark >= 50: #50점 이상의 점수만 더한다
#         result += mark
# print(result)


# def fib(n):
#     if n == 0 : return 0          # n이 0일 때는 0을 반환
#     if n == 1 : return 1          # n이 1일 때는 1을 반환
#     return fib(n-2) + fib(n-1)    # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

# for i in range(10):
#     print(fib(i))

# user_input = input("숫자를 입력하세요: ")
# numbers = user_input.split(",")  #input에다가 적는 숫자중 ,있으면,지운다
# total = 0
# for n in numbers:
#     total += int(n)    # 입력은 문자열이므로 숫자로 변환해야 한다.
# print(total)

# print(':: 2단 ::')
# for i in range(1, 10):  # 1부터 9까지
#     print(f'2 x {i} = {2*i}') #2*1,2,3,4...9까지 곱한다

# print((70+60+55+75+95+90+80+80+85+100) / 10)

# class Calculator: #클래스를 만든다
#     def __init__(self, numberList): #함수를 지정한다
#         self.numberList = numberList

#     def sum(self):
#         result = 0
#         for num in self.numberList: 
#             result += num
#         return result

#     def avg(self):
#         total = self.sum()
#         return total + len(self.numberList) 

# cal1 = Calculator([1,2,3,4,5]) 
# print (cal1.sum())
# print (cal1.avg())

# cal2 = Calculator([6,7,8,9,10]) 
# print (cal2.sum())
# print (cal2.avg())

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
#      result += 4

# print(result)

# data = "4546793" 
# numbers = list(map(int, data))  #숫자 문자열을 리스트로 바꿈 
# result = []

# for i, num in enumerate(numbers):
#     result.append(str(num))
#     if i < len(numbers)-1:                  
#         is_odd = num % 2 == 1 #             
#         is_next_odd = numbers[i+1] % 2 == 1  
#         if is_odd and is_next_odd:           
#             result.append("-")
#         elif not is_odd and not is_next_odd: 
#             result.append("*")

# print("".join(result))

# s = 'aabcccaaaaas'

# result = s[0]  # 첫번째 값을 결과에 넣는다
# count  = 0   

# for st in s:
#     if st == result[-1]:  
#         count += 1
#     else:
#         result += str(count) + st
#         count = 1
# result += str(count)

# print (result)

# a = input("0~9 사ㅇ;의 숫자로 이루어진 문자열 입력 : ")
# print('true' if len(a) == lan(set(a)) ==10 else 'false')

alphabet={'':' ','.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
line=input("type morse: ").split(' ')#알파뱃에 지정해넣은 부호를 넣고 ' '는 지운다
for i in line:
    print(alphabet[i], end='')


#2번 a...b
# import re

# p = re.compile("a[.]{3,}b")
# print(p.match)

# import re
# p = re.compile("[a-z]+")
# m = p.search("5 python")
# print(m.start() + m.end())