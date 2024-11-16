# Wordle-Project

This is a simple word guessing game inspired by popular word-based puzzle games like Wordle. The game selects a random 5-letter word, and your task is to guess it in six attempts or fewer.

## How it works

1. The program selects a random word from a word list stored in a text file (`words.txt`).
2. You will be prompted to enter a 5-letter guess.
3. After each guess, feedback is provided in the form of colors:
   - **Green**: The letter is correct and in the correct position.
   - **Yellow**: The letter is in the word, but in the wrong position.
   - **Red**: The letter is not in the word at all.
4. The game ends when either:
   - You guess the word correctly within 6 attempts.
   - You run out of attempts, in which case the correct word is revealed.

## How to play

1. Clone the repository or download the files.
2. Ensure you have a file named `words.txt` in the same directory, containing a list of 5-letter words (one word per line).
3. Run the Python script.

### Example Output

```
Enter a 5 letter guess?
broke
b - Green
r - Green
o - Green
k - Green
e - Green
You Won! That took 1 guess(es).
```

## Requirements

- Python 3.x
- A text file `words.txt` with a list of 5-letter words.

## How it works internally

- The game selects a word randomly from the `words.txt` file (or a word passed as a command-line argument).
- The user's guesses are checked against the correct word, and feedback is printed for each letter.
- The color feedback is implemented using a helper function `printGuessColors` and checks the correctness of each letter using the `letterColor` function.

## Contributing

Feel free to fork the repository, make improvements, and create pull requests.
