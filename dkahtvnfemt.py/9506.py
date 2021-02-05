perfect_num = {6 : "6 = 1 + 2 + 3",
               28 : "28 = 1 + 2 + 4 + 7 + 14",
               496: "496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248",
               8128 : "8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064"}

num = int(input())
while num != -1:
    if num in perfect_num:#짝수인지 구분
        print(perfect_num[num])
    else:
        print("%s is NOT perfect." % (num))#짝수가아니거나perfect num안에 들어가있는게 아니면 is not perfact출력
    num = int(input())