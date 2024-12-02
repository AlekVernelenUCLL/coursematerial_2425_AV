class Tweet:
    def __init__(self, message, max_length):
        self.max_length = max_length
        self.message = message

    @property
    def message(self):
        return self.__message
    
    @property
    def max_length(self):
        return self.__max_length
    
    message.setter
    def message(self, message):
        pass

    max_length.setter
    def max_length(self, max_length):
        if max_length >= 1 and len(self.message) <= max_length:
            self.__max_length = max_length
        if len(self.message) <=