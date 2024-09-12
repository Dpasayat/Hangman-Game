import random as rd
import hangman_words as wrd
from hangman_art import logo,stages,win,lost
#to clear the console after each iteration:
import os
#for windows it is cls for linux it is clear
import platform
#below code checks for the operation sustem
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

print(logo)
lives=6
# word list
word_List=wrd.word_list
#randomly choosing a word
chosen_word= rd.choice(word_List)
#cheatig line, remove to play fairly
print(f"psstt chosen word is {chosen_word}")
display=[]
for ch in chosen_word:
    display.append("_")
for ch in display:
    print(ch,end="")
print()

end_of_game=False

while not end_of_game:
    
    guess=input("Guess a letter: ").lower()
    clear()

    for idx in range(len(chosen_word)):
        if guess == chosen_word[idx]:
            cutLife=False
            display[idx]=chosen_word[idx]
            
        
    if guess not in chosen_word:
        print(f"NOOOOOO!! {guess} is not in there!!!!!")
        lives=lives-1  
    else:
        print(f"Phew! {guess} is in there.")
    for ch in display:
        print(ch,end="")
    print(stages[lives])
    if '_' not in display or lives==0:
        end_of_game=True
        if lives==0:
            print("You Lost!!")
            print(lost)
        else:
            print("You guesses it correctly!!")
            print(win)
    