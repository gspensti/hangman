# Game time! Let’s create a hangman game together 

from random import choice

words = (
    "pyladies", "thomas", "snack", "shoe", "nupi", "car", "house", "pig", "mouse", "tiger", "lion", "wolf", "sock", "panther", "shirt", 
    "flower", "woman", "power", "snow", "star", "crash", "flight", "fight", "game", "python", "coding", "animals", "nightmares", 
    "windstorm"
           )
secret_word =  choice(words)  # chooses a random word from list of words 
lenght_of_secret_word = len(secret_word)
blanks = "-" * lenght_of_secret_word # variable for game board, where each character of the secret word is replaced by a "-"

false_letters = [] # initializes list of false letters 
unsuccessful_tries = 0 # max 7
used_letters = [] # initilizes list of used letters

hangman_stages = [
    """
      +---+
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\  |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\  |
     /    |
         ===
    """,
    """
      +---+
      O   |
     /|\  |
     / \  |
         ===
    """,
]

def player_move():
    global blanks
    global used_letters
    global unsuccessful_tries

    # game runs as long as there are dashes in the `board' and as long as unsiccessful
    # tries are <7 
    # 7 bc this is when the hang man hangs + one additional try
    while "-" in blanks and unsuccessful_tries < 7:  
        print(blanks)
        user_letter = (input("Can you guess the word? Give me a letter! ")).lower() # catches upper- and lowercase letters

        if len(user_letter) != 1: # check for only one letter 
            print("Please enter only one letter at a time.") 
        
        elif not ('a' <= user_letter <= 'z'):  # cchecks if input is a letter 
            print("The heck am I supposed to do with that?! Please enter a letter.")

        elif user_letter in used_letters: # checks if letter has already been used and asks again if so
            print("You've lready used that one!")
        
        else:
            used_letters.append(user_letter)  # if letter is new, letter is added to used letters list 
            print ("Used letters: ", used_letters)
        
            if user_letter in secret_word: # if letter is new and in secret word, dash will be replaced by character 
                index = secret_word.index(user_letter) # this returns the index of that letter in the secret word
                part_a = blanks[:index] # splits blank into part before and part after that letter (using corresponding index)
                part_b = blanks[index + 1:]
                blanks = part_a + user_letter + part_b # joins parts with inserted letter 
                print(hangman_stages[unsuccessful_tries]) # prints current status of hangman game 
        
            elif user_letter not in secret_word:  # if letter is not in secret word, unsuccessful tries increase, list of false letters is updated
                unsuccessful_tries += 1
                false_letters.append(user_letter)
                print ("False letters: ", false_letters)
                print("Unsuccessful tries: ", unsuccessful_tries)

                if unsuccessful_tries < 7:  # Only print if unsuccessful_tries is 6 or less
                    print(hangman_stages[unsuccessful_tries]) # current status of hangman is printed as long as unsuccessful tries is below 7
        
    if unsuccessful_tries == 7:  # if max amount of guesses is reached, game is lost
        print ("Oh no! You lost!")
        print (hangman_stages[-1]) # final hangman stage is printed
        print(secret_word) # secret word is revealed
    
    elif "-" not in blanks: # if there aren't any dashes left, game is won.
        print ("Congrats! You guessed the word correctly!")

    return blanks, used_letters, false_letters


player_move()
