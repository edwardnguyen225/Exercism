def is_isogram(string):
    str = string.lower()
    tmp_char = []
    for c in str:
        if c.isalpha():
            if c in tmp_char:
                return False
            tmp_char.append(c)
    return True
