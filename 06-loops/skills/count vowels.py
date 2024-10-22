def count_vowels(text):
    vowel = 0
    for char in text:
        if char.lower() in "aeiouy":
            vowel += 1
    return vowel