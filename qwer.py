#1번
class UpgradeCalculator(Calculator):#클레스 머시기를 만든다
    def minus(self, val):#def minus함수를 만들고 그안에 self와minus를 너준다
        self.value -= val#마지막으로self와value을뺀거는 val이라는걸 알려준다
#2번        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

#3번 몰라

#4번
li = [-3,5,1,2,-5,-2]#이 리스트 중에서 음수를 제거 하고 싶으면
f = filter(lambda a: a>0,li)
#5번
print(int('0xea', 16))
#6번
print(list(map(lambda x:x*3, [1,2,3,4])))



