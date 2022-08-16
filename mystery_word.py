import random
from re import M



def re_run(): #ask to play again
    play_again = input("\nDo you think you can handle another round? (Y/N): ").upper()
    if play_again == "Y":
        play_game()
    else:
        print("Well fine, be that way")
        exit()


def play_game():
    file = open("test-word.txt", "r")    #import words file
    open_file = file.read() #read the opened file
    words_list = open_file.upper().split()   # #make all the words upper case
    mystery_word = random.choice(words_list) #choose random word from list
    blanks = (len(mystery_word)*"_") #make blank spaces
    attempts = 8  #set counter for guess attempts
    letters_guessed = [] #set list for letters user has already guessed

    print("\nYour word is", len(mystery_word), "letters long")
    
    while attempts > 0:
        #increase turn number
        #print current letter/blank spaces, letters guessed
        print("You have", attempts, "attempts remaining")
        print("Letters already guessed", letters_guessed)
        print(blanks)
        #user input
        guess = input("Enter a letter A-Z: ").upper()
        #compare user input to mystery word
        if len(guess) > 1: #user entered more than 1 letter
            print("One guess a time bozo\n")
        elif guess in letters_guessed: #user entered duplicate guess
            print("Ummm you already tried that\n")
        elif guess not in letters_guessed: #add user guess to list
            attempts -= 1
            letters_guessed.append(guess)
            if guess in mystery_word: #correct guess
                attempts += 1
                for i in range(0, len(mystery_word)):
                    if guess == mystery_word[i]:
                        print("Correct\n")
                        blanks = blanks[:i] + guess +blanks[i+1:] #replace black spaces w/ correct letters
            else: #user makes incorrect guess
                print("Incorrect\n")
        if "_" not in blanks:  #wincon
            print("You Win...this time....")
            print("The word was", mystery_word)
            re_run()
        if attempts == 0: #user fails to guess the word
            print("HAHAHAHAH YOU LOSE")
            print("The word was", mystery_word)
            re_run()
    #ask user if they would like to play
    
if __name__ == "__main__":
    question = input("Would you like to play a game...? (Y/N): ").upper()
    if question == "Y":
        print("Then try to guess the word, you get 8 incorrect guesses...\n")
        play_game()
    else:
        print("Then why are you bothering me?")
    




