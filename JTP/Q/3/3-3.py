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

n = int(input("input : "))
for i in range(1, n + 1):  # range(1, 6) => 1, 2, 3, 4, 5
    print(" " * (n - i), "*" * (2 * i - 1))

# 공백 => 5-1, 5-2, 5-3, 5-4, 5-5
# 별 => 2*1-1, 2*2-1, 2*3-1, 2*4-1, 2*5-1
