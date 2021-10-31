from nltk.corpus import words
import random
import os

def main():
    # Generate Random Word
    a = words.words()
    word = random.choice(a)
    # print(word) # Sanity check to view word

    # Create a list for the guessed word, a T / F dictionary to keep track of guessed letters, Dictionary for letter count
    Guessed = dict()     # Dictionaryto check if letter has been guessed
    GuessedLetters = set() # Set to prevent guessing the wrong letter twice

    for letter in word:
        # print(letter) # Sanity check to iterate through letters
        Guessed[letter] = Guessed.get(letter, False)

    # Hangman
    hangmanCount = 6
    printProgress(word, Guessed, hangmanCount, GuessedLetters)
    while (hangmanCount != 0):
        # Prompting User for Correct Input
        userInput = None
        while True:
            userInput = input("Insert your letter: ")
            print(len(userInput))
            if len(userInput) == 1 and userInput.isalpha():
                print("Valid Input")
                break
            else:
                printProgress(word, Guessed, hangmanCount, GuessedLetters)
                print("Invalid Input, please input a letter")          
        
        # Checking if letter has been guessed
        if userInput in Guessed:
            if Guessed[userInput] == True:
                print("You already guessed this letter")
                printProgress(word, Guessed, hangmanCount, GuessedLetters)
                continue
            else:
                GuessedLetters.add(userInput)
                Guessed[userInput] = True
                print("Letter in Word! :)")
                printProgress(word, Guessed, hangmanCount, GuessedLetters)
        else:
            if userInput in GuessedLetters:
                print("You already guessed this letter. It is incorrect.")
                printProgress(word, Guessed, hangmanCount, GuessedLetters)
            else:
                hangmanCount -= 1
                GuessedLetters.add(userInput)
                print("Letter not in word :(")
                printProgress(word, Guessed, hangmanCount, GuessedLetters)

    if hangmanCount == 0:
        print(" You have used up your guessed, the word is: ", word)

def printProgress(word:str, guess:dict(),hangmanCount, GuessedLetters:set) -> str:
    print("#########################################################")
    for letter in word:
        if letter in guess:
            if guess[letter] == True:
                print(letter, end=" ")
            else: 
                print("_ ", end="")
    print("\n")
    print("Guessed Letters", GuessedLetters)
    print("Remiaining attempts:", hangmanCount)

if __name__ == "__main__":
    main()
