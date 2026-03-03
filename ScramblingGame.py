import random

words = ["apple", "mango", "grapes", "banana"]

word = random.choice(words)
scrambled = ''.join(random.sample(word, len(word)))

print("Guess the word:", scrambled)

guess = input("Enter your guess: ")

if guess == word:
    print("Correct! You win.")
else:
    print("Wrong! The correct word was:", word)