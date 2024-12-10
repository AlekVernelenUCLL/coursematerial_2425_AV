class GamePlayer:
    def __init__(self, word, lives):
        self.word = word
        self.lives = lives

    @property
    def word(self):
        if self == master:
            return self.__word
        else:
            # return self.secret_word()
            print("secret word")
    @word.setter
    def word(self, word):
        self.__word = word
    
    @property
    def lives(self):
        return self.__lives
    @lives.setter
    def lives(self, lives):
        self.__lives = lives
    
    def guess(self, letter):
        if letter not in self.word:
            self.lives -= 1
        else:
            pass



master = GamePlayer("slang", 10)
player = GamePlayer(master.word, master.lives)
print(player.word)