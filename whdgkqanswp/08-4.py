a = [20,55,67,67,82,45,33,90]

result = 0
while a:#반복적으로 구해야 돼기 때문에 while을 쓴다
    mark = a.pop()

    if mark >= 50:#50점 이상만 더한다
        result += mark

print(result)