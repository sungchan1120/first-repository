# 3의 배수 총합
# a = 0
# result = 0
# while True:
#     a += 3
#     if a > 1000:
#         break
#     result += a

# print(result)

# 3과 5의 배수 총합
a = 1
result = 0

while True:
    if a % 3 == 0 or a % 5 == 0:
        result += a

    if a >= 100:
        break

    a += 1

print(result)