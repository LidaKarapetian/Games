#!/usr/bin/python

# Field of Dreams game

#The rules of the game:  when we start the program, it asks the question, then gives dashes the size of the answer, 
#when we enter a letter, it puts a letter in the correct place of the answer and finally gives the correct answer.

question =  print("What is the capital of South Korea?")
answer = "seoul"
guessed_letters = ""
guessed_word = ""

#This code block for printing dashes the size of the answer
print("The answer has the following quantity of letters: ")
for i in range(len(answer)):
    print('_')

while True:
    print("Guessed word is: ", guessed_word) 
    letter = input("Guess the letter: (please enetered only lowercase letters): ")

    guessed_letters += letter

    #Case when the entered letter isn't in the word
    if letter not in answer:
        print("The letter you entered does not exist in the answer, please enter another letter.")
    
    #Case when the entered letter is in the word
    if letter in answer:
        guessed_word = "".join(
            j if j == letter or j in guessed_letters else "_"
            for j in answer
        )

    if guessed_word == answer:
        print("You guess the answer, it's a: ", answer)
        break
