class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def is_empty(self):
        return self.lower > self.upper
    
    def contains(self, value):
        return self.lower <= value <= self.upper
    
    def overlaps_with(self, other):
        num = self.lower
        sett = set()
        while num <= self.upper:
            sett.add(num)
            num += 1
        for num in range(other.lower, other.upper+1):
            if num in sett:
                print("tweede")
                return True
        print("einde")
        return False
    
self = Interval(-5,-5)
other = Interval(-5,-5)
res = self.overlaps_with(other)
print(res)