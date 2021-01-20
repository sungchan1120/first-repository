# https://wikidocs.net/17114

# Q9 평균값 구하기
# 다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.

# 70
# 60
# 55
# 75
# 95
# 90
# 80
# 80
# 85
# 100

# T Code

f = open("sample.txt")
numbers = f.readlines()
f.close()

total = 0
for num in numbers:
  score = int(num)
  total += score

average = total / len(numbers)

f = open("result.txt", "w")
f.write(str(average))
f.close()