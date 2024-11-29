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

HANGMAN_PICS = ['''
+---+
    |
    |
    |
    ===''', '''
+---+
 O  |
    |
    |
===''', '''
+---+
 O  |
 |  |
    |
===''', '''
+---+
 O  |
/|  |
    |
===''', '''
+---+
 O  |
/|\ |
    |
===''', '''
+---+
 O  |
/|\ |
/   
===''', '''
+---+
 O  |
/|\ |
/ \ |     
===''']



words = ("pyladies", "thomas", "snack")
false_letters = []
unsuccessful_tries = 0
secret_word = get_random_word(words)

from random import randrange 
def get_random_word(words):     # returns random string from the list 
    random_index = randrange (0, len(words)) # returns random integer from 0 to length of list of words
    print (words[random_index])
    return words[random_index]  # returns random string from list of words with index stored in random variable


get_random_word(words)

def display_board(false_letters, unsuccessfull_tries, secret_word):
    print (HANGMAN_PICS(len(false_letters)))
    

    for letter in false_letters: 
        false_letters.append(letter)
        print("False letters: ", false_letters, end = ' ')
    
    length_of_word = len(secret_word)
    board = "-" * length_of_word


   print(board)
    return board

# def game_status ():
     
# def play_again (): 








# def move (board):
      #  user_letter = input("Give me a letter, lowercase only: ")
       # if user_letter in used_letters:
           # print("You already used that one. Try again.")
        #elif user_letter[i] in chosen_word:


          #  board = board[i] + chosen_word [i] + board[i]





           # position_user_letter = chosen_word.index(user_letter)
            #print(position_user_letter)
            #board[position_user_letter] == user_letter
            #used_letters.append(user_letter)
            #print(board)
            #print(used_letters)
        #elif user_letter not in chosen_word:
         #   unsuccessful_tries += 1
          #  used_letters.append(user_letter)
           # print(board)
            #print(used_letters)
        #else: 
           #  print("Am I a joke to you?")



#move(empty_board())

#def game (board, move):
     

# unsuccsessful_tries = 9  

# If in the string are no underscores, congratulate a player and end the game. 
        #  Print out the number of unsuccessful tries and (if you want) print out the corresponding picture of a hangman. 
        #  If the number of unsuccessful tries is 9 or higher, the player loses the game and ends the game.