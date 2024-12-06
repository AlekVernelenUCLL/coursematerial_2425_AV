class GamePlayer:
    def __init__(self, word, lives):
        self.word = word
        self.lives = lives

    @property
    def word(self):
        if self == master:
            return self.__word
        else:
            print("you cannot acces word")
    @word.setter
    def word(self, word):
        self.__word = word
    
    @property
    def lives(self):
        return self.__lives
    @lives.setter
    def lives(self, lives):
        self.__lives = lives
    
    # def guess(self, letter):
    #     if letter in self.word:


master = GamePlayer("slang", 10)
player = GamePlayer("slang", 10)
# print(master.word)