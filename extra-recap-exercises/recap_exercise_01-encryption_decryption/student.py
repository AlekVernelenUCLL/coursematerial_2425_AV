def decode1(word):
    # change A's into o's
    result = ""
    for char in word:
        if char == "A":
            result += "o"
        else:
            result += char
    return result

def decode2(word):
    # get every 2nd letter in word
    result = ""
    for i in range(0,len(word),2):
        result += word[i]
    return result

def decode3(sentence):
    # reverse first word in sentence
    list = sentence.split(" ")

    reverse = list[0]
    word = ""
    for i in range(len(reverse)-1,-1,-1):
        word += reverse[i]
    result = ""
    first = True
    for element in list:
        if first:
            result += word
            first = False
        else:
            result += f" {element}"
    return result

def decode4(word):
    # get word in string
    end_range = int(len(word)/2 + 2)
    return word[2:end_range]

def decode5(sentence):
    # decryption order:
    # decode1 every word of sentence
    list = sentence.split(" ")
    words = ""
    last = False
    for word in list:
        decoded1 = decode1(word)
        # decode2 of word
        decoded2 = decode2(decoded1)
        # decode4 of word
        decoded4 = decode4(decoded2)
        if last:
            words += decoded4
        else:
            words += f"{decoded4} "
    # decode3 of sentence
    return decode3(words)
            
sentence = "rAxNejhfTrns maGwcaifrIcRuEmzsHtxaUnVcSeWsllKnmsYiMiFwQpMZyRhabPu aHhPhyajvfeViSYg xrfAcphhadnqgIeodAAXyDjTcFGT"
print(decode5(sentence))