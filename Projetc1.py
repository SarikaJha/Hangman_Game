import random

HANGMAN=['''
    +----+
    |    |
         |
         |
         |
         |
         |
         |
         |
==============''','''

    +----+
    |    |
    0    |
         |
         |
         |
         |
         |
         |
==============''','''

    +----+
    |    |
    0    |
    |    |
         |
         |
         |
         |
         |
==============''','''

    +----+
    |    |
    0    |
   /|    |
         |
         |
         |
         |
         |
==============''','''

    +----+
    |    |
    0    |
   /|\   |
         |
         |
         |
         |
         |
==============''','''

    +----+
    |    |
    0    |
   /|\   |
   /      |
         |
         |
         |
         |
==============''','''

    +----+
    |    |
    0    |
   /|\   |
   / \     |
         |
         |
         |
         |
==============''']

WORDS=["LOVE","SMILE","SKY","CAMERA","GAME","FRIEND"]

MAX_WRONG=len(HANGMAN)-1

word=random.choice(WORDS)
   

current_guess="_" * len(word)

wrong_guesses=0

used_letters=[]

print("Welcome to Hangman!!!")
print("Try to guess the word")

while wrong_guesses<MAX_WRONG and current_guess!=word:
    print(HANGMAN[wrong_guesses])
    print("So far,the word is : ",current_guess)
    
    guess=input("Enter your letter guess:")
    guess=guess.upper()
    
    while guess in used_letters:
        print("You have already guessed that letter",guess)
        guess=input("Enter your letter guess:")
        guess=guess.upper()
    used_letters.append(guess)
    
    if guess in word:
        print("You have guessed correctly!!!")
        
        
        new_current_guess=""
        for letter in range(len(word)):
            if guess==word[letter]:
                new_current_guess+=guess
            else:
                new_current_guess+=current_guess[letter]
        current_guess=new_current_guess
    else:
        print("Sorry that was incorrect")
        wrong_guesses+=1
    if wrong_guesses==MAX_WRONG:
        print(HANGMAN[wrong_guesses])
        print("You have been hanged!")
        print("The correct word is",word)
    else:
        print("You have won!!")

