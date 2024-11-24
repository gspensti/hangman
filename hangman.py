# Game time! Let’s create a hangman game together 
# The game should look like this. Separate the project into multiple functions, take care of good descriptive names and write comments 
# (for future you). You should also put everything to git after every step. 
# • Computer will randomly choose a word (as a beginning out of 3 options). 
#   Also for simplicity use lower case and only words where a letter is used only once. Eg. Mentoring or Pyladies :)
#   • Default setting of game “status” is a string (or a list) with that many underscores as there are letters in the chosen word. 
#   • Default setting of unsuccessful tries is zero. (as a counter of guesses) • Keep repeating: 
        #  Ask the player for a letter. 
        #  If the letter is in the chosen word, replace corresponding 
        #  underscores with letters in the game status. Write a function for this. 
    
        #  If the letter is not present, add one to unsuccessful tries. 
        #  Print out the game “status” – string with underscores and already revealed letters or still just underscores. 

        #  If in the string are no underscores, congratulate a player and end the game. 
        #  Print out the number of unsuccessful tries and (if you want) print out the corresponding picture of a hangman. 
        #  If the number of unsuccessful tries is 9 or higher, the player loses the game and ends the game.
from random import choice

words = ("pyladies", "thomas", "snack")

def board ():
    chosen_word = choice(words)
    print(chosen_word)
    length_of_word = len(chosen_word)
    board = "-" * length_of_word
    print(board)
board()

def move (board):
        used_letters = []
        user_letter = input("Give me a letter, lowercase only: ")
        if user_letter in chosen_word:
            return board()
            board.index(user_letter) == user_letter
            used_letters.append(user_letter)
            print(board)
            print(used_letters)
        elif user_letter not in chosen_word:
            unsuccessful_tries +=1
            used_letters.append(user_letter)
            print(board)
            print(used_letters)
        else: 
             print("Am I a joke to you?")

# def board_update ():

    # ask player for letter 
    # if correct: update board 
    # if wrong: update unsuccessful tries 



# def move (string, position_number, character):
    # part_a = string[:position_number] 
    # part_b = string[position_number + 1:]
    # board_update = part_a + character + part_b # splits string so that character can be inserted at either player or pc position
    # return board_update



# unsuccsessful_tries = 0 

