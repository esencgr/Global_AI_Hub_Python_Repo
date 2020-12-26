from words_module import words_list
from images_module import images
import random
import os

def get_word():
    selected_word = random.choice(words_list)
    return selected_word.upper()

def status(usr, wrd, ch, g_lets, g_words, n_val):
    os.system("clear")
    
    print("\n ------------- USER ------------ \n")
    print(f"hello {usr} !!")

    print("\n ---------- LETS PLAY ---------- \n")
    print(wrd)
    print(images[7 - ch])

    print(f"\nyour chance : {ch} ")
    print(f"\nguessed letters : {g_lets} ")
    print(f"\nguessed words : {g_words} ")
    print(f"\nnot valid answers : {n_val} ")


def result(st, w):
    if st:
        print(f"\nThe word is {w}.")
        print("\n! Great you win the game !\n")
    else:
        print("\n! Game over !\n")
        print(f"\nThe word was {w}.")


def play(selected_word,user):
    word = '-' * len(selected_word)    
    chance = 7 
    state = False
    guessed_letters = []
    guessed_words = []
    not_valid = []
    
    # PLAY CONTINUES WHEN THE GUESS IS TRUE OR CHANCE IS FINISHED
    while not state and chance > 0:

        status(user, word, chance, guessed_letters, guessed_words, not_valid)
        guess = input("\nguess a letter or word : ").upper()

        # FOR GUESS A LETTER 
        if len(guess) == 1 and guess.isalpha():
        
            if guess not in selected_word:
                guessed_letters.append(guess)
                chance -= 1
    
            else:
                guessed_letters.append(guess)
                
                selected_word_lst = list(selected_word)
                word_lst = list(word)
                
                ind = [ i for i, letter in enumerate(selected_word) if guess == letter ]
                for pos in ind:
                    word_lst[pos] = guess 
    
                word = "".join(word_lst)

                if "-" not in word:
                    state = True
        
        # FOR GUESS A WORD
        elif len(guess) == len(selected_word) and guess.isalpha():
                   
            if guess != selected_word:
                guessed_words.append(guess)
                chance -= 1

            else:
                state = True
                word = guess

        else: 
            not_valid.append(guess)

    status(user, word, chance, guessed_letters, guessed_words, not_valid)
    result(state, word)

def main():
 
    print("\n ---------- USER INFO ---------- \n")
    user = input("please enter your name : ") 
    word = get_word()
    play(word, user)

if __name__ == "__main__":
    main()