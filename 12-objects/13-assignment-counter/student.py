class Counter:
    def __init__(self):
        self.__count = 0

    @property
    def count(self):
        return self.__count

    def increment(self):
        self.__count += 1

    def reset(self):
        self.__count = 0


counter = Counter()
counter.increment()
counter.increment()
counter.reset()
print(counter.count)