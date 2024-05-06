from itertools import product
from random import randint

def allwords(chars, length):
    wordlist = []
    for letters in product(chars, repeat=length):
        word = ''.join(letters)
        wordlist.append(word)
    
    return wordlist

def generate_wordList(letters):
    
    for wordlen in range(2, 5):
        wordList = allwords(letters, wordlen)
    # wordList = allwords(letters, 2)
    return wordList

def display_word(char, randomWord, display_word_list):
    for position in range(len(randomWord)):
        if char == randomWord[position]:
            display_word_list[position] = char
    
    print(display_word_list)

def guess_game(randomWord, display_word_list):
    input_char = (input("Guess a letter: ")).lower()
    display_word(input_char, randomWord, display_word_list)

def main():
    print("Welcom to HangMan!")

    letters = "abcdefghijklmnopqrstuvwxyz"
    wordList = generate_wordList(letters)
    wordListLen = len(wordList)
    print("word list length is", wordListLen)
    index = randint(0, wordListLen - 1) 
    randomWord = wordList[index]
    print("The random word is:", randomWord)

    display_word_list = []
    for letter in randomWord:
        display_word_list += "_"

    game_over = False
    num = 0
    print("You have 5 guesses!")

    while not game_over:
        guess_game(randomWord, display_word_list)
        num += 1

        if num < 5 :
            if "_" not in display_word_list:
                print("You win!")
                game_over = True
            
            else:
                print(f"You have {5 - num} guess left.")

        else:
            print("You loser!")
            game_over = True
            
        

if __name__=="__main__":
    main()