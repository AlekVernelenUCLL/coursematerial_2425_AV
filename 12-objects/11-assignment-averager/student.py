class Averager:
    def __init__(self):
        self.values = []
        
    def add(self, value):
        self.values.append(value)
        return self.values

    def average(self):
        average = sum(self.values)/len(self.values)
        return average
    
    def reset(self):
        self.values = []

a = Averager()
a.add(10)
a.add(20)

k = a.average()
print(k)

q = a.reset()
print(q)