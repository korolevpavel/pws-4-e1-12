import random
import string

WORDS = ['skillfactory', 'testing', 'blackbox',
         'pytest', 'unittest', 'coverage']
WORD = random.choice(WORDS)
HEALTH = 4


def game():
    list_letters = set(string.ascii_lowercase)
    word_chars = set(WORD)
    word_list = list(" ".join("_" * len(w) for w in WORD.split()))
    error_point = 0

    while error_point < HEALTH:
        print(''.join(word_list))
        if WORD == ''.join(word_list):
            return True

        letter = input("Введите букву на латинице: ")
        if len(letter) > 1:
            print("Введи только одну букву!")
        elif len(letter) < 1:
            return letter == WORD
        elif letter not in list_letters:
            if letter in word_chars:
                print("Буква %s была угадана ранее" % letter)
            else:
                print("Некорректный ввод!")
        elif letter in word_chars:
            print("Буква %s угадана!" % letter)
            list_letters.remove(letter)
            for i in replace_letter(WORD, letter):
                word_list[i] = letter
        else:
            print("Буквы %s нет в загаданном слове! :(" % letter)
            list_letters.remove(letter)
            error_point += 1
        print()
    return False


def replace_letter(game_word, letter):
    return [i for i, l in enumerate(game_word) if l == letter]


def main():

    if game():
        print('Поздравляем! Вы угадали слово!')
        return True
    else:
        print('Вы проиграли! :( Загаданное слово: %s' % WORD)
        return False


if __name__ == "__main__":
    main()
