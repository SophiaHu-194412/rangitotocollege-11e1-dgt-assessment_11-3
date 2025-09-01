'''hangman'''
from tkinter import * 
import random

root = Tk()
btn = Button(root, text='Play Hangman', command=root.quit)
btn.pack(pady=20)
btn2 = Button(root, text='A', command=root.quit)
btn2.pack(pady=5)
btn3 = Button(root, text='B', command=root.quit)
btn3.pack(pady=5)
btn4 = Button(root, text='C', command=root.quit)
btn4.pack(pady=5)
btn5 = Button(root, text='D', command=root.quit)
btn5.pack(pady=5)
btn6 = Button(root, text='E', command=root.quit)
btn6.pack(pady=5)
btn7 = Button(root, text='F', command=root.quit)
btn7.pack(pady=5)
btn8 = Button(root, text='G', command=root.quit)
btn8.pack(pady=5)
btn9 = Button(root, text='H', command=root.quit)
btn9.pack(pady=5)
btn10 = Button(root, text='I', command=root.quit)
btn10.pack(pady=5)
btn11 = Button(root, text='J', command=root.quit)
btn11.pack(pady=5)
btn12 = Button(root, text='K', command=root.quit)
btn12.pack(pady=5)
btn13 = Button(root, text='L', command=root.quit)
btn13.pack(pady=5)
btn14 = Button(root, text='M', command=root.quit)
btn14.pack(pady=5)
btn15 = Button(root, text='N', command=root.quit)
btn15.pack(pady=5)
btn16 = Button(root, text='O', command=root.quit)
btn16.pack(pady=5)
btn17 = Button(root, text='P', command=root.quit)
btn17.pack(pady=5)
btn18 = Button(root, text='Q', command=root.quit)
btn18.pack(pady=5)
btn19 = Button(root, text='R', command=root.quit)
btn19.pack(pady=5)
btn20 = Button(root, text='S', command=root.quit)
btn20.pack(pady=5)
btn21 = Button(root, text='T', command=root.quit)
btn21.pack(pady=5)
btn22 = Button(root, text='U', command=root.quit)
btn22.pack(pady=5)
btn23 = Button(root, text='V', command=root.quit)
btn23.pack(pady=5)
btn24 = Button(root, text='W', command=root.quit)
btn24.pack(pady=5)
btn25 = Button(root, text='X', command=root.quit)
btn25.pack(pady=5)
btn26 = Button(root, text='Y', command=root.quit)
btn26.pack(pady=5)
btn27 = Button(root, text='Z', command=root.quit)
btn27.pack(pady=5)
root.mainloop()

word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)
display_word = '_' * len(chosen_word)
print("H A N G M A N")
lives = 7
while lives > 0:
    print()
    print(display_word)
    guess = input("Input a letter: ")
    if len(guess) != 1:
        print("You should input a single letter")
        continue
    if not guess.islower():
        print("Please enter a lowercase English letter")
        continue
    if guess in display_word:
        print("You've already guessed this letter")
        continue
    if guess in chosen_word:
        new_display = ''
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                new_display += guess
            else:
                new_display += display_word[i]
        display_word = new_display
    else:
        print("That letter doesn't appear in the word")
        lives -= 1
    if display_word == chosen_word:
        print(f"You guessed the word {chosen_word}!\nYou survived!")
        break

root.mainloop()
