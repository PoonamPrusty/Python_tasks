import random

Words = ("sword", "armor", "python", "cruel")

word = random.choice(Words) # chooses one element from the tuple randomly

correct = word

jumble = ""

while word:
    position = random.randrange(len(word)) #picks a random letter from the word  
    jumble += word[position] #adds the letter in word[position] to jumble variable 
    word = word[:position] + word[(position + 1):] #word consists of letters before the jumble letter and after the jumble letter

print jumble

guess = raw_input("Guess the word: ")  
guess = guess.lower()

while (guess != correct) and (guess != ""):
    print "Wrong guess, try again!"
    guess = raw_input("Guess the word: ")  
    guess = guess.lower()

if guess == correct:
    print "Correct!You Win."

raw_input("\n\nPress enter to exit")
