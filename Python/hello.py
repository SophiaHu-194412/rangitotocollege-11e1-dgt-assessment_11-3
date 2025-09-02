'''hangman'''
from tkinter import * 
import tkinter as tk
import random

root = tk.Tk()
btn = tk.Button(root, text='Play Hangman', command=root.quit)
btn.pack(pady=20)

window = tk.Tk()
window.title("Hangman")

for i in range(3):
    for j in range(9):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")

btn2 = tk.Button(window, text='A', command=window.quit)
btn3 = tk.Button(window, text='B', command=window.quit)
btn4 = tk.Button(window, text='C', command=window.quit)
btn5 = tk.Button(window, text='D', command=window.quit)
btn6 = tk.Button(window, text='E', command=window.quit)
btn7 = tk.Button(window, text='F', command=window.quit)
btn8 = tk.Button(window, text='G', command=window.quit)
btn9 = tk.Button(window, text='H', command=window.quit)
btn10 = tk.Button(window, text='I', command=window.quit)
btn11 = tk.Button(window, text='J', command=window.quit)
btn12 = tk.Button(window, text='K', command=window.quit)
btn13 = tk.Button(window, text='L', command=window.quit)
btn14 = tk.Button(window, text='M', command=window.quit)
btn15 = tk.Button(window, text='N', command=window.quit)
btn16 = tk.Button(window, text='O', command=window.quit)
btn17 = tk.Button(window, text='P', command=window.quit)
btn18 = tk.Button(window, text='Q', command=window.quit)
btn19 = tk.Button(window, text='R', command=window.quit)
btn20 = tk.Button(window, text='S', command=window.quit)
btn21 = tk.Button(window, text='T', command=window.quit)
btn22 = tk.Button(window, text='U', command=window.quit)
btn23 = tk.Button(window, text='V', command=window.quit)
btn24 = tk.Button(window, text='W', command=window.quit)
btn25 = tk.Button(window, text='X', command=window.quit)
btn26 = tk.Button(window, text='Y', command=window.quit)
btn27 = tk.Button(window, text='Z', command=window.quit)
root.mainloop()

word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)
display_word = '_' * len(chosen_word)
print("H A N G M A N")
lives = 7
while lives > 0:
    print()
    print(display_word)
    guess = input("Input a letter: ").lower()
    if len(guess) != 1:
        print("You should input a single letter")
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
        print(f"You guessed the word {chosen_word}!\nYou win")
        break


if lives == 0:
    print('You lose!')

root.mainloop()
