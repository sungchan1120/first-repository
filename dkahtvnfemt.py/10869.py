class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        sesult = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
       result = self.first / self.second
       return result

a = FourCal()
print(a.setdata(4, 2))
print(a.add())