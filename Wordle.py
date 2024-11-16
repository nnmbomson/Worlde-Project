import random
import sys

def main():
    # Get a random word.
    answer = getRandomWord()

    # PUT YOUR CODE HERE.
    # Start by asking the user for their initial guess
    # Ask them to "Enter a 5 letter guess?"
    # Start with section 3 in the starter doc.
    attempts=0
    guess = ""

    while attempts < 6 and guess != answer:
        guess = input("Enter a 5 letter guess?\n")
        printGuessColors(guess, answer)
        attempts += 1
    if answer == guess:
        print(f"You Won! That took {str(attempts)} guess(es).")
    else:
        print(f"You lost. The answer was {answer}.")

# A helper method that prints the guess with the
# correct colors to the console.
# Example usage:
# printGuessColors("broke", "broke") should print the five lines:
#
# b - Green
# r - Green
# o - Green
# k - Green
# e - Green
def printGuessColors(guess, answer):
    for i in range(5):
        color = letterColor(guess, answer, i)
        print(f"{guess[i]} - {color}")
    return


# A helper method that determines the color
# of the letter in the guess. This function
# should return "Green", "Red", or "Yellow"
def letterColor(guess, answer,index):
    if guess[index] == answer[index]:
        return "Green"
    elif guess[index] not in answer:
        return "Red"
    else:
        return "Yellow"

    

# A method that gets a random word from a file.
# You should not change this function.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()
