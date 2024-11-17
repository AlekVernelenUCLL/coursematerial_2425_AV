def spellcheck(document, valid_words):
    str_doc = document.replace("\n", " ")
    str_doc = str_doc.lower()
    lst_doc = str_doc.split(" ")
    set_words = set(valid_words)
    result = set()
    for word in lst_doc:
        if word and word not in set_words:
            result.add(word)
    return result

# valid_words = [ 'cat', 'mat', 'sat', 'the' ]
# document = """
# The cat
# sat on
# the mat
# """

# a = spellcheck(document, valid_words)
# print(a)