DICT = {
    "mother": "мама",
    "father": "папа",
    "sun": "солнце",
    "son": "сын",
    "cat": "кот",
    "dog": "собака",
    "car": "машиниа",
    "door": "дверь",
    "note": "заметка",
}
REVERSED_DICT = {}
for key, value in DICT.items():
    REVERSED_DICT[value] = key


def get_parameters():
    word = input("Введите слово для перевода: ")

    print("Выберите направление перевода")
    print("1. с английского на русский (по умолчанию)")
    print("2. с русского на английский")
    direction = input()
    if not direction:
        direction = 1
    direction = int(direction)
    return word, direction

def get_translation(word, dictionary):
    if word in dictionary:
        translation = dictionary[word]
        return dictionary[word]
    else:
        return None


def print_translation(word, translation):
    if translation:
        print(f"Перевод слова {word} - {translation}")
    else:
        print(f"Нет перевода для слова {word}")

def prepare_word(word):
    return word.lower().strip()

while True:
    word, direction = get_parameters()

    word = prepare_word(word)

    if direction == 1:
        translation = get_translation(word, DICT)
    else:
        translation = get_translation(word, REVERSED_DICT)
    print_translation(word, translation)


