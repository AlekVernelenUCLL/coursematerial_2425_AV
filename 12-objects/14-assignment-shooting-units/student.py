class Unit:
    def __init__(self, health, firepower, armor):
        self.health = health
        self.firepower = firepower
        self.armor = armor

    @property
    def health(self):
        return self.__health
    
    @property
    def firepower(self):
        return self.__firepower
    
    @property
    def armor(self):
        return self.__armor
    
    @health.setter
    def health(self, health):
        if not self.valid_stat(health):
            raise ValueError()
        else:
            self.__health = health

    @firepower.setter
    def firepower(self, firepower):
        if not self.valid_stat(firepower):
            raise ValueError()
        else:
            self.__firepower = firepower

    @armor.setter
    def armor(self, armor):
        if not self.valid_stat(armor):
            raise ValueError()
        else:
            self.__armor = armor

    @health.setter
    def health(self, health):
        if not self.valid_stat(health):
            raise ValueError()
        else:
            self.__health = health
    
    def valid_stat(self, stat):
        check_int = isinstance(stat, int)
        check_pos = stat >= 0
        return check_int and check_pos
    
    def shot_by(self, other):
        damage = self.damage(other)
        no_health_gaining = damage >= 0
        if no_health_gaining:
            self.health = self.health_after_shot(damage)
    
    def health_after_shot(self, damage):
        health = self.health - damage
        if health < 0:
            return 0
        return health
    
    def damage(self, other):
        return other.firepower - self.armor

A = Unit(10, 10, 2)
B = Unit(5, 0, 2)
B.shot_by(A)
print(B.health)
# A.shot_by(B)
# print(A.health)