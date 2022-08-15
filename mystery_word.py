import random
from re import M

def play_game():
    

    def play_time():
        #import words file
        file = open("test-word.txt", "r")
        #read the opened file
        open_file = file.read()

        # #make all the words upper case
        words_list = open_file.upper().split()
        
        # #choose a random word from the list
        mystery_word = random.choice(words_list)
        #make blank spaces
        blanks = (len(mystery_word)*"_")
        #set counter for guess attempts
        attempts = 0
        #set list for letters user has already guessed
        letters_guessed = []

        print("Your word is", len(mystery_word), "letters long")
        
        while attempts < 8:
            #increase turn number
            attempts +=1
            #print current letter/blank spaces, letters guessed
            print("Guess", attempts, "of 8")
            print("Letters already guessed", letters_guessed)
            print(blanks)
            #user input
            guess = input("Guess a letter A-Z: ").upper()
            if guess not in letters_guessed:
                letters_guessed.append(guess)
            #compare guess to letters in mystery_word
            if len(guess) > 1:
                print("One guess a time bozo\n")
            if guess in letters_guessed and guess in mystery_word:
                print("Ummm you already tried that\n")
            if guess in mystery_word and guess not in letters_guessed:
                for i in range(0, len(mystery_word)):
                    if guess == mystery_word[i]:
                        print("Correct\n")
                        blanks = blanks[:i] + guess +blanks[i+1:] #replace black spaces w/ correct letters
            if guess not in mystery_word:
                print("Incorrect\n")
            if "_" not in blanks:
                print("You Win...this time....")
                print("The word was", blanks)
                break
            if attempts == 8:
                print("HAHAHAHAH YOU LOSE")
                break

    question = input("Would you like to play a game...? (Y/N): ").upper()
    if question == "Y":
        print("Then try to guess the word, you get 8 chances...")
        play_time()
    else:
        print("Then why are you bothering me?")
    


#no touchy
if __name__ == "__main__":
    play_game()
