class Password:
    def __init__(self, password):
        self.__password = password

    def verify(self, string):
        i = 0
        for char in string:
            if char != self.__password[i]:
                return False
            i += 1
        return True