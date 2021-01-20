user_input = input("숫자를 입력하세요")
numbers = user_input.split(",")#input에 ,가 있으면 ,를 지운다
total = 0
for n in numbers:
    total += int(n)
print(total)