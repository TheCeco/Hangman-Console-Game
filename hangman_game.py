import requests


def get_generated_word():
    """
    Return one stored word randomly. Options can be further specified, see the parameters menu.
    The returned word is in format ["word"].
    """

    response = requests.get("https://random-word-api.herokuapp.com/word")
    return response.text.strip('[""]')


def is_valid_input(letter, guessed_letters):
    if len(letter.strip()) != 1:
        return False

    if letter in guessed_letters:
        return False

    guessed_letters.append(letter)
    return True


def valid_guess(word, encrypted_word, letter):
    temp = list(encrypted_word)
    for i in range(len(word)):
        if word[i] == letter:
            temp[i] = letter

    return ''.join(temp)


def play(mistakes, word, encrypted_word, guessed_letters):
    while mistakes > 0:

        print(f'Allowed mistakes -> {mistakes}')
        print(f'Used letters: {", ".join(guessed_letters)}')
        print(encrypted_word)
        print('Please enter your guess: ')
        letter = input().lower()

        if not is_valid_input(letter, guessed_letters):
            continue

        if letter not in word:
            mistakes -= 1

            if mistakes == 0:
                print(word)
                print('You Lose...')

        else:
            encrypted_word = valid_guess(word, encrypted_word, letter)
            if encrypted_word == word:
                print(word)
                print('You WON!!!')
                break


def main():
    mistakes = 10
    word = get_generated_word()
    encrypted_word = '_' * len(word)
    guessed_letters = []

    play(mistakes, word, encrypted_word, guessed_letters)


if __name__ == '__main__':
    main()
