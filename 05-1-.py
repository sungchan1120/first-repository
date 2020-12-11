# result = 0

# def add(num):
#     global result
#     result += num
#     return result
# print(add(3))
# print(add(4))
# print(add(5))

# result1 = 0
# result2 = 0

# def add1(num):
# global result1
# result += num
# return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))
# tdef sub(self, num):
#     self.result -= num
#     return self.result
# class Cookis:
#     pass
# a = Cookis()
# b = Cookis()
# class FourCal():
#     pass

#  a = FourCal()
#  print(type(a))
# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

# a = FourCal()
# b = FourCal()
# a.setdata(4, 2)
# b.setdata(3, 7)
# print(a)
# class FourCal:
#     def setdata(self, first, second):
#         slef.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
# a = FourCal
# a.setdata(4,2)
# print(a.add())
# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result

# class FourCal: #계산기 틀
#     def __init__(self, first, second): # 초기데이터 설정
#         self.first = first
#         self.second = second
#     def setdata(self, first, second): 
#         self.first = first
#         self.second = second
#     def add(self): 
#         result = self.first + self.second 
#         return result #return result는 result를 반환 한다
#     def mul(self): 
#         result = self.first * self.second
#         return result
#     def sub(self): 
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal(4, 2)  #a라는 객체를 만든다 
# print(a.add()) #return 값을 출력한다

# a.setdata(10, 20) # setdata의 10은 first 20은 second
# print(a.add())
# #self = 생성되는 객체
# #first = 4
# #second = 2
# # a = FourCal(4, 2)
# # print(a.add())
# # class MoreFourCal(FourCal):
# #     pass
# # a = MoreFourCal(4, 2)
# # print(a.add())
# # class MoreFourCal(FourCal):
# #     def pow(self):
# #         result = self.first ** self.second #곱하기 2번
# #         return result
# # a = MoreFourCal(4, 2) #2는 제곱이다
# # print(a.pow())
# # class SafeFourCal(FourCal):
# #     def div(self):
# #         if self.second == 0:
# #             return 0
# #         else:
# #             return self.first / self.second
# # a = SafeFourCal(4, 0)
# # print(a.div())
# # class Family:
# #     lastname = "김"
# # print(Family.lastname)
# # print(id(Family.lastname))
def add(a, b):
    return a + b

def add(a, b):
    return a-b

    