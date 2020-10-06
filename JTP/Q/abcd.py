# 1
# a = "life is too short, you need python"

# if "wife" in a:
#     print("wife")
# elif "python" in a and "you" not in a:
#     print("python")
# elif "shirt" not in a:
#     print("shirt")
# elif "need" in a:
#     print("need")
# else:
#     print("none")

# 2


# 3
# n = int(input("input : "))

# for i in range(1, n + 1):
#     print("*" * i)

# 4
# for i in range(1, 101):
#     print(i)

# 5
# date = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# result = 0

# for a in date:
#     result += a

# print(result / len(date))



num = 0
sum = 0
while num < 1000:
    num += 1
    if (num % 3) != 0: continue
    sum = sum + num
print(sum)