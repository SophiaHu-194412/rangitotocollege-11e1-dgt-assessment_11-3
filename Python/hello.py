from tkinter import * 
import tkinter as tk
import random

'''menu'''
root = tk.Tk()
root.title('Game Menu')
root.geometry('500x500')
menuLabel = tk.Label(root, text='Welcome to Game menu', bg='black')
menuLabel.pack()

namevar = tk.StringVar()
name_label = tk.Label(root, text='Username')
name_label.pack()
name_entry = tk.Entry(root, textvariable = namevar)
name_entry.pack(pady=5)

def submit():
    name=namevar.get()
    print('The name is: ' + name)
    namevar.set('')

sub_btn=tk.Button(root, text='Submit', command=submit)
sub_btn.pack(pady=5)

'''hangman'''
def hangmanwindow():
    hangman = tk.Toplevel(root)
    hangman.title('Hangman')
    hangman.geometry('500x500')

    hangmanlabel = tk.Label(hangman, text = 'Welcome to Hangman!', bg='black')
    hangmanlabel.pack(pady=10)

    text = tk.Text(hangman, fg='yellow', bg='black')
    text.pack(pady=10)

    frame = tk.Frame(hangman, bg='white')
    frame.pack(fill='both', expand=True)

    chosenword=random.choice(['apple', 'mango', 'grape', 'watermelon'])
    display_word = ['_'] * len(chosenword)
    text.insert(tk.END, ' '.join(display_word))
    guessvar = tk.StringVar()
    entry = tk.Entry(hangman, textvariable=guessvar)
    entry.pack()
    lives = [7]

    def checkguess():
        guess=guessvar.get().lower()
        guessvar.set('')
        if len(guess) != 1:
            text.insert(tk.END, '\nEnter aa letter')
            return
        if guess in chosenword:
            for i in range(len(chosenword)):
                if chosenword[i] == guess:
                    display_word[i]=guess

        else:
            lives[0] -= 1
            text.insert(tk.END, f"\nThe letter {guess} isn't in the word!")
        text.insert(tk.END, "\n" + " ".join(display_word))

        if '_' not in display_word:
            text.insert(tk.END, f"\nYou win!")
        elif lives[0] == 0:
            text.insert(tk.END, f"\nYou lose! The word was {chosenword}")

    tk.Button(frame, text='Submit', command=checkguess).pack()



'''1A2B'''
def oneatwobwindow():
    oneatwob = Toplevel(root)
    oneatwob.title('1A2B')
    oneatwob.geometry('500x500')
    oneatwoblabel = tk.Label(oneatwob, text = 'Welcome to 1A2B!')
    oneatwoblabel.pack()
    text2=tk.Text(oneatwob, fg='pink')
    text2.pack()

    guessvar = StringVar()
    Entry(oneatwob, textvariable=guessvar).pack()


    def generate_number():
        digits = list('0123456789')
        random.shuffle(digits)
        return ''.join(digits[:4])

    number_to_guess = generate_number()
    attempts = [0]

    def checkguess():
        guess=guessvar.get()
        guessvar.set('')
        if len(guess) != 4 or not guess.isdigit():
            text2.insert(END, '\nPlease enter a valid 4-digit number.')
            return
        attempts[0] += 1
        A = sum(1 for i in range(4) if guess[i] == number_to_guess[i])
        B = sum(1 for digit in guess if digit in number_to_guess) - A
        text2.insert(tk.END, f"\nAttempt {attempts}: {guess}")
        text2.insert(tk.END, f"\n{A}A{B}B")
        if A == 4:
            text2.insert(END, f"\nCongratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

    Button(oneatwob, text='Submit', command=checkguess).pack()


'''sudoku'''
def sudokuwindow():
    sudoku = Toplevel(root)
    sudoku.title("Sudoku")
    sudoku.geometry('500x500')
    sudokulabel = tk.Label(sudoku, text = 'Welcome to Sudoku!')
    sudokulabel.pack()

    # create a 9x9 grid
    sudoku.frame = tk.Frame(sudoku, padx=10, pady=10, borderwidth=2)
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

'''wordle'''
def wordlewindow():
    wordle = Toplevel(root)
    wordle.title("Wordle")
    wordle.geometry('500x500')
    wordlelabel = tk.Label(wordle, text='Welcoem to Wordle!')
    wordlelabel.pack()

    wordleguesses = [6]
    wordlewordlist = ['apple', 'grape', 'peach', 'berry', 'mango']
    wordlechosen = random.choice(wordlewordlist)
 
    text2 = Text(wordle, height = 20, width = 30, fg='hotpink')
    text2.pack()

    guessvar = tk.StringVar()
    entry = tk.Entry(wordle, textvariable=guessvar)
    entry.pack()

    def checkguess():
        guess=guessvar.get().lower()
        guessvar.set("")
        if len(guess)!=5 or not guess.isalpha():
            text2.insert(tk.END, "\nPlease enter a valid 5-letter word.")
            return
        wordleguesses[0]-=1
        feedback = ''
        for i in range(5):
            if guess[i] == wordlechosen[i]:
                feedback += 'G'  # Green
            elif guess[i] in wordlechosen:
                feedback += 'Y'  # Yellow
            else:
                feedback += 'B'  # Black
        text2.insert(tk.END, f"\n{guess} -> {feedback}")

        if guess == wordlechosen:
            text2.insert(tk.END, f"\nCongratulations! You've guessed the word {wordlechosen}.")
        if wordleguesses[0] == 0:
            text2.insert(tk.END, f'You lose! The word was {wordlechosen}')


    tk.Button(wordle, text='Submit', command=checkguess).pack()

'''menu'''

Button(root, text='Hangman game', command=hangmanwindow).pack(pady=5)
Button(root, text='1a2b game', command=oneatwobwindow).pack(pady=5)
Button(root, text='Sudoku game', command=sudokuwindow).pack(pady=5)
Button(root, text='Wordle game', command=wordlewindow).pack(pady=5)


root.mainloop()


