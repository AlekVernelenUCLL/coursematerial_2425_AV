# write your code here
def coins(amount):
    fives = amount//5
    twos = (amount-(fives*5))//2
    ones = ((amount-(fives*5))-(twos*2))//1
    a = (fives,twos,ones)
    return sum(a)

