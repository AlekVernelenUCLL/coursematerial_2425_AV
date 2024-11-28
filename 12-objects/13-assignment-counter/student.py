class Counter:
    def __init__(self, count):
        self.__count = count

    @property
    def count(self):
        return self.__count

    def increment(self):
        self.count += 1

    def reset(self):
        self.__count
