class Tweet:
    def __init__(self, message, max_length):
        self.message = message #property
        self.max_length = max_length #property

    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, string):
        if not hasattr(self, "max_length"):
            self.__max_length = len(string)
            self.__message = string
        elif len(string) > self.max_length:
            truncated_string = self.__truncate(string)
            self.__message = truncated_string
        else:
            self.__message = string

    @property
    def max_length(self):
        return self.__max_length
    
    @max_length.setter
    def max_length(self, value):
        self.__max_length = value
        if value < 1:
            raise ValueError("Max length must be atleast 1")
        elif len(self.message) > value:
            truncated_message = self.__truncate(self.message)
            self.__message = truncated_message

    def __truncate(self, string):
        return string[:self.max_length]
    

tweet = Tweet("1234567", 5)
tweet.max_length = 0
a = tweet.message
print(a)