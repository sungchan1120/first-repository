class UpgradeCalculator(Calculator):#클레스 머시기를 만든다
    def minus(self, val):#def minus함수를 만들고 그안에 self와minus를 너준다
        self.value -= val#마지막으로self와value을뺀거는 val이라는걸 알려준다
        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))
