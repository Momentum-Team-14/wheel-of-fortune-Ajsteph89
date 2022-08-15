import random
from re import M

def play_game():
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
    
    while attempts < 8:
        #increase turn number
        attempts +=1
        #print current letter/blank spaces
        print(blanks)
        #user input
        guess = input("Guess a letter A-Z: ").upper()
        #compare guess to letters in mystery_word
        if guess in mystery_word:
            for i in range(0, len(mystery_word)):
                if guess == mystery_word[i]:
                    print("Correct")
                    blanks = blanks[:i] + guess +blanks[i+1:]
        if guess not in mystery_word:
            print("Incorrect")
        if "_" not in blanks:
            print("You Win...this time....")
            print("The word is", blanks)
            break
        if attempts == 8:
            print("You LOSE")
            break


    # if guess in mystery_word:
    #     print("correct")
    # else:
    #     print("Incorrect")


#no touchy
if __name__ == "__main__":
    play_game()
