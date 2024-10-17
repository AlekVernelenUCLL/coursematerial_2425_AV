def decode1(word):
    a = word.replace('A','o')
    return a

# print(decode1('SchAAl'))
def decode2(word):
    index_space = word.find(' ')
    a = word[:index_space:2]
    return a
# print(decode2('hqovtzdpozgm'))

def decode3(sentence):
    index_space = sentence.find(' ')
    a = sentence[index_space-1::-1]
    b = f"{a}{sentence[index_space:]}"
    return b

# print(decode3('sepocseleT are too expensive.'))

def decode4(word):
    firstletter = word[2]
    a = word[2:(len(word)//2)+2]
    return a

# print(decode4("oddolfijnnjiflK"))

def decode5(sentence):
    print(sentence)
    first = decode1(sentence)
    print(first)
    words = sentence.split(' ')
    for word in words:
        a = decode2(word)
        b = ' '.join(a)
    second = decode2(first)
    print(b)
    print(second)
    third = decode4(second)
    fourth = decode3(third)
    return fourth

decode5("MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu")
# print(decode5("MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu"))