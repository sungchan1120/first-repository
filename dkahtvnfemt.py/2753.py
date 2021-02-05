year = int(input())

if((year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)):#연도가 4의 배수이면1 아님 0
    print('1')
else:
    print('0')