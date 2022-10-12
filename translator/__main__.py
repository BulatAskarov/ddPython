from console import get_parameters, print_translation
from data import DICT, REVERSED_DICT
from service import get_translation, prepare_word

while True:
    word, direction = get_parameters()

    word = prepare_word(word)

    if direction == 1:
        translation = get_translation(word, DICT)
    else:
        translation = get_translation(word, REVERSED_DICT)
    print_translation(word, translation)
