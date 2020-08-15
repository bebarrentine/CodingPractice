import random

HANGMAN_ASCII = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

play_again = True
while play_again:
    print('HANGMAN:')

    word_bank = ['dragon', 'wagon', 'yacht', 'revolver', 'scandal', 'elephant', 'ferocious', 'airways', 'sickly', 'supernova', 'decision', 'xylophone', 'nectarine', 'wallop', 'ringbearer', 'avocado', 'zephyr', 'wretched', 'slumber', 'parachute']
    hangman_word = word_bank[random.randint(0, len(word_bank))]

    n = 0
    hangman_output = ['_']*len(hangman_word)
    missed_letters = []
    print(HANGMAN_ASCII[0])
    guessed_letter = 1
    while n < 6:
        print(f'Missed Letters: {missed_letters}')
        print(hangman_output)
        if '_' not in hangman_output:
            break
        guessed_letter = input('Guess a letter in the Hangman word: ').lower()
        if guessed_letter in list(hangman_word):
            indices = [i for i, x in enumerate(list(hangman_word)) if x == guessed_letter]
            for k in indices:
                hangman_output[k] = guessed_letter
            print(HANGMAN_ASCII[n])
        else:
            if guessed_letter not in missed_letters:
                n += 1
                missed_letters.append(guessed_letter)
                print(HANGMAN_ASCII[n])
            else:
                print(' ')
                print(HANGMAN_ASCII[n])
                print('You already guessed that letter.')


    def replay():
        x = 1
        global play_again
        while x not in ['y', 'n']:
            x = input('Would you like to play again? (y/n): ').lower()
            if x not in ['y', 'n']:
                print(' ')
                print('Please enter either y or n.')
            elif x == 'y':
                play_again = True
                return play_again
            else:
                play_again = False
                return play_again
    if n == 6:
        print(' ')
        print('You lost.')
        replay()
    else:
        print(' ')
        print('You won!')
        replay()

print('Thanks for playing.')










