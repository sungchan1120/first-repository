# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

# print("hi")
# try:
#     f = open('none', 'r')
# except FileNotFoundError as e:
#     print(str(e))
# else: #open이오류가없을떼 else실행해라
#     data = f.read()
#     print(data)
#     f.close
# f = open('foo.txt', 'w')
# try:
#     # 무언가를 수행한다
#     data = f.read()
#     print(data)
# except Exception as e:
#     print(e)
# finally:
#     f.close()
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 할 수 없습니다.")
# 라try:
#     f = open("나없는파일", 'r')
# except FileNotFoundError:
#     pass #오류가 발생했을때 그냥 지나가
# class Bird:
#     def fiy(self):
#         raise NotImplementedError

# class Eagle(Bird):
#     def fiy(self):
#         print("very fast")

# eagle = Eagle()
# eagle.fiy()
# class MyError(Exception):
#     pass
# def say_nick(nick):
#     if nick == '바보':
#         raise MyErro