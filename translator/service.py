def get_translation(word, dictionary):
    if word in dictionary:
        translation = dictionary[word]
        return dictionary[word]
    else:
        return None


def prepare_word(word):
    return word.lower().strip()
