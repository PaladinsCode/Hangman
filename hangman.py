from nltk.corpus import words
import random
import os

def main():
    # Generate Random Word
    a = words.words()
    word = random.choice(a)
    # print(word) # Sanity check to view word

    # Create a list for the guessed word, a T / F dictionary to keep track of guessed letters, Dictionary for letter count
    Guessed = dict()
    guessWord = list()
    GuessWordDict = dict()
    for letter in word:
        # print(letter) Sanity check to iterate through letters
        guessWord.append(letter)
        GuessWordDict[letter] = GuessWordDict.get(letter, 0) + 1 
        Guessed[letter] = Guessed.get(letter, False)
    # More Sanity Checks
    # print(GuessWordDict)   
    # print(Guessed)
    # print(guessWord)

    # Hangman
    hangmanCount = 6
    printProgress(word, Guessed, hangmanCount)
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
                printProgress(word, Guessed, hangmanCount)
                print("Invalid Input, please input a letter")          
        
        # Checking if letter has been guessed
        if userInput in Guessed:
            if Guessed[userInput] == True:
                print("You already guessed this letter")
                printProgress(word, Guessed, hangmanCount)
                continue
            else:
                Guessed[userInput] = True
                print("Letter in Word! :)")
                printProgress(word, Guessed, hangmanCount)
        else:
            print("Letter not in word :(")
            hangmanCount -= 1
            printProgress(word, Guessed, hangmanCount)

    if hangmanCount == 0:
        print(" You have used up your guessed, the word is: ", word)

def printProgress(word:str, guess:dict(),hangmanCount) -> str:
    # Print Tthe word
    for letter in word:
        if letter in guess:
            if guess[letter] == True:
                print(letter, end=" ")
            else: 
                print("_ ", end="")
    print("\n")
    print("Remiaining attempts:", hangmanCount)

if __name__ == "__main__":
    main()
