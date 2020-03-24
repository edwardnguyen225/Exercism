spec_char = "!@#$%^&*()-=[]\;,./_+\{\}|:\"<>?\n"

def process_sentence(sentence: str) -> str:
    for c in spec_char:
        sentence = sentence.replace(c, " ")
    length = len(sentence)
    while sentence[0] == '\'':
        sentence = sentence[1:]
        length -= 1
    while sentence[length-1] == '\'':
        sentence = sentence[:length-1]
        length -= 1
    for i in range(length):
        char = sentence[i]
        if sentence[i] == "'" and (not sentence[i-1].isalpha() or not sentence[i+1].isalpha()):
            sentence = sentence[:i] + ' ' + sentence[i + 1:]
    sentence = sentence.lower()
    return sentence

def count_words(sentence):
    wordcount = {}
    tmp = process_sentence(sentence).split()
    for word in tmp:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount

sen = "''',\n,one,\n ,two \n 'three'"
# print(sen)
# print(process_sentence(sen))
print(count_words(sen))
