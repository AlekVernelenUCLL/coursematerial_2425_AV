def guess_number(number):
    guess = int(input("type number: "))
    guessed = guess == number
    while not guessed:
        if guess > number:
            print("too high")
        else:
            print("too low")
        guess = int(input("type number: "))
        guessed = guess == number
    print("correct")

guess_number(10)