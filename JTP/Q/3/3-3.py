# i = 0

# while True:
#     i += 1
#     print(i * "*")

#     if i > 4:
#         break

# while True:
#     i -= 1
#     print(i * "*")

#     if i == 0:
#         break

# // while_count >> 3
#  *      // b1 s1
# ***     // b0 s3
#  *      // b1 s1

# // while_count >> 5
#   *     // b2 s1
#  ***    // b1 s3
# *****   // b0 s5
#  ***    // b1 s3
#   *     // b2 s1

# // while_count >> 7
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n = int(input("input : "))  # 2

for i in range(1, n + 1):  # 1, 2
    print(" " * (n - i), "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):  # 1
    print(" " * (n - i), "*" * (2 * i - 1))
