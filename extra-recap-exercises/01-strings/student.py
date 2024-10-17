def decode1(word):
    a = word.replace('A','o')
    return a

# print(decode1('SchAAl'))
def decode2(word):
    a = word[::2]
    return a
# print(decode2('hqovtzdpozgm'))

def decode3(sentence):
    index_space = sentence.find(' ')
    a = sentence[index_space-1::-1]
    b = f"{a}{sentence[index_space:]}"
    return b

# print(decode3('sepocseleT are too expensive.'))

def decode4(word):
    a = word[2:(len(word)//2)+2]
    return a

# print(decode4("oddolfijnnjiflK"))

def decode5(sentence):
    # print('sentence:',sentence)
    first = decode1(sentence)
    # print('first:',first)
    words = first.split(' ')
    # print('words:',words)
    b = []
    for word in words:
        a = decode2(word)
        b.append(a)
    # c = ' '.join(b)
    e = []
    for word in b:
        d = decode4(word)
        e.append(d)
    # print('e:',e)
    f = ' '.join(e)
    result = decode3(f)
    return result

    # third = decode4(second)
    # fourth = decode3(third)
    # return fourth

# decode5("MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu")
# print(decode5("rAxNejhfTrns maGwcaifrIcRuEmzsHtxaUnVcSeWsllKnmsYiMiFwQpMZyRhabPu aHhPhyajvfeViSYg xrfAcphhadnqgIeodAAXyDjTcFGT"))