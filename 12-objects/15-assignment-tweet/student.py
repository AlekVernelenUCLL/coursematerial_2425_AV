class Tweet:
    def __init__(self, message, max_length):
        self.message = message
        self.max_length = max_length

    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, message):
        self.__message = message

    def valid(self, message, max_length):
        max_length_minimum = max_length >= 1
        if max_length_minimum:
            return len(message) <= max_length