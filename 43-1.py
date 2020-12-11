# total = 0
# for n in range(1, 101):
#     if n % 3 == 0:
#         print(n)


# def say(*args):
#     result = ""
#     for a in args:
#         result += a

#     print(result)


# say("text1", "text2", "text3")


# say("가", "위")


# def is_odd(number):
#     if number % 2 == 1:
#         print("홀수")
#     else:
#         print("짝수")


# is_odd(4)


# input1 = input("첫 번째 숫자를 입력하세요:")
# input2 = input("두 번째 숫자를 입력하세요:")

# total = int(input1) + int(input2)
# print("두수의 합은 %s 입니다" % total)

# print("you" "need" "python")
# print("you"+"need"+"python")
# print("you","need","python")
# print("".join(["you","need","python"]))

# f1 = open("test.txt", 'w')
# f1.write("life is too short!!!")
# f1.close() 

# f2 = open("test.txt", 'r')
# print(f2.read())
# f2.close()


def avg_number(*args):
    result = 0
    for i in args:
       result += i
    return result/len(args)

avg_number(1,2)
print(avg_number(1,2,))







