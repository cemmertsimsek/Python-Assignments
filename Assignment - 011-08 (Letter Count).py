sentence = str(input("Please enter a sentence : ")).lower()


def letter_count(sentence):
    result = {}
    for i in sentence:
        result[i] = result.get(i, 0)+1
    return result


letter_count(sentence)
