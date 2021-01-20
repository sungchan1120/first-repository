a = input("0~9 사이의 숫자로 이루어진 문자열 입력 : ")
print('true' if len(a) == len(set(a)) == 10  else 'false')
