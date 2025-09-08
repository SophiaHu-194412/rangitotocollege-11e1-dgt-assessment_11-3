from tkinter import * 
import tkinter as tk
import random

'''hangman'''
window = tk.Tk()
window.title("Hangman")
btn = tk.Button(window, text='Play Hangman', command=window.quit)
btn.pack(pady=20)
T = Text(window, height = 10, width = 30)
T.pack()
T.insert(tk.END, "Welcome to Hangman! Type 'exit' to quit anytime.\n")

'''hangman game logic'''
word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)
display_word = '_' * len(chosen_word)
lives = 7
while lives > 0:
    T.insert(tk.END, "\n" + display_word)
    guess = input("Input a letter: ").lower()
    if guess == 'exit':
        T.insert(tk.END, f'\nThe word was {chosen_word}. Thanks for playing!')
        break
    if len(guess) != 1:
        T.insert(tk.END, "\nYou should input a single letter")
        continue
    if guess in display_word:
        T.insert(tk.END, "\nYou've already guessed this letter")
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
        T.insert(tk.END, "\nThat letter doesn't appear in the word")
        lives -= 1
    if display_word == chosen_word:
        T.insert(tk.END, "\n" + display_word)
        T.insert(tk.END, f"\nYou guessed the word {display_word}!\nYou win")
        break


if lives == 0:
    T.insert(tk.END, 'You lose!')

window.mainloop()

'''1A2B'''

root = tk.Tk()
root.title("1A2B")
btn = tk.Button(root, text='Play 1A2B', command=root.quit)
btn.pack(pady=20)


'''1A2B game logic'''

for i in range(5):
    w = Canvas(root, width=40, height=20)
    w.pack()
    canvas_height=20
    canvas_width=75
    y = int(canvas_height / 2)
    w.create_line(0, y, canvas_width, y, fill="#FF0000")

text1 = Text(root, height = 50, width = 30)
text1.pack()

def generate_number():
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:4])

number_to_guess = generate_number()
attempts = 0
while True:
    attempts += 1
    guess = input("Enter your guess: ")
    if guess.lower() == 'exit':
        text1.insert(tk.END, f'\nThe number was {number_to_guess}. Thanks for playing!')
        break
    if len(guess) != 4 or not guess.isdigit():
        text1.insert(tk.END, "\nPlease enter a valid 4-digit number.")
        continue
    text1.insert(tk.END, f"\nAttempt {attempts}: {guess}")
    A = sum(1 for i in range(4) if guess[i] == number_to_guess[i])
    B = sum(1 for digit in guess if digit in number_to_guess) - A
    text1.insert(tk.END, f"\n{A}A{B}B")
    if A == 4:
        text1.insert(tk.END, f"\nCongratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break

root.mainloop()

'''sudoku'''
sudoku = tk.Tk()
sudoku.title("Sudoku")
btn = tk.Button(sudoku, text='Play Sudoku', command=sudoku.quit)
btn.pack(pady=20)

'''sudoku'''
# create a 9x9 grid
sudoku.frame = Frame(sudoku, padx=10, pady=10, borderwidth=2)
sudoku.frame.pack()
for row in range(9):
    for col in range(9):
        sudoku_widget = tk.Entry(sudoku.frame, width=2, font=('Arial', 24), justify='center')
        sudoku_widget.grid(row=row, column=col, padx=5, pady=5)

for i in range(9):
    sudoku.frame.grid_rowconfigure(i, weight=1)
    sudoku.frame.grid_columnconfigure(i, weight=1)

# create 10 buttons in a grid
button1 = tk.Button(sudoku, text='1')
button2 = tk.Button(sudoku, text='2')
button3 = tk.Button(sudoku, text='3')
button4 = tk.Button(sudoku, text='4')
button5 = tk.Button(sudoku, text='5') 
button6 = tk.Button(sudoku, text='6')
button7 = tk.Button(sudoku, text='7')
button8 = tk.Button(sudoku, text='8')
button9 = tk.Button(sudoku, text='9')
button10 = tk.Button(sudoku, text='0')

# grid buttons vertically
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()

sudoku.mainloop()

'''wordle'''
wordle = tk.Tk()
wordle.title("Wordle")
btn = tk.Button(wordle, text='Play Wordle', command=wordle.quit)
btn.pack(pady=20)

'''wordle game logic'''
import random
wordleguesses = 6
wordlewordlist = ['apple', 'grape', 'peach', 'berry', 'mango']
wordlechosen = random.choice(wordlewordlist)
text2 = Text(wordle, height = 50, width = 30, fg='hotpink')
text2.pack()
text3 = Text(wordle, height= 50, width = 30, fg='black')
text3.pack()
while wordleguesses > 0:
    guess = input("Enter your 5-letter guess: ").lower()
    if guess == 'exit':
        text2.insert(tk.END, f'\nThe word was {wordlechosen}. Thanks for playing!')
        break
    if len(guess) != 5 or not guess.isalpha():
        text2.insert(tk.END, "\nPlease enter a valid 5-letter word.")
        continue
    feedback = ''
    for i in range(5):
        if guess[i] == wordlechosen[i]:
            feedback += 'G'  # Green
        elif guess[i] in wordlechosen:
            feedback += 'Y'  # Yellow
        else:
            feedback += 'B'  # Black
    text2.insert(tk.END, f"\n{guess} -> {feedback}")
    wordleguesses -= 1
    if guess == wordlechosen:
        text2.insert(tk.END, f"\nCongratulations! You've guessed the word {wordlechosen}.")
        break
wordle_window.mainloop()

menu.mainloop()

