epsilon = 0.01
y = 54.0
guess = y/2.0
numGuesses = 0

while abs(guess ** 2 - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess ** 2) - y)/(2*guess))
print(f"The number of guesses it took was {numGuesses}")
print(f"The square root of {y} is approx. {guess}")
