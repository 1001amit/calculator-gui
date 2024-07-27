import tkinter as tk
import random

class MinesweeperGame:
    def __init__(self, master, rows=10, cols=10, mines=20):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines

        self.board = [[0] * cols for _ in range(rows)]
        self.buttons = [[None] * cols for _ in range(rows)]

        self.create_widgets()
        self.place_mines()
        self.calculate_adjacent_mines()

    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root)
        display_frame.pack(expand=True, fill='both')

        input_field = tk.Entry(display_frame, textvariable=self.input_text, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4)
        input_field.grid(row=0, column=0, columnspan=4)

        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill='both')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('←', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('exp', 7, 0), ('π', 7, 1), ('MC', 7, 2), ('MR', 7, 3),
            ('M+', 8, 0), ('M-', 8, 1)
        ]

        for (text, row, col) in buttons:
            tk.Button(buttons_frame, text=text, font=('Arial', 18), command=lambda x=text: self.on_button_click(x)).grid(row=row, column=col, sticky='nsew')

        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(9):
            buttons_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == "=":
            try:
                self.expression = self.expression.replace("π", str(math.pi))  # Replace "π" with math.pi
                result = str(eval(self.expression))
                self.expression = result
                self.input_text.set(result)
            except:
                self.input_text.set("Error")
        elif button == "C":
            self.expression = ""
            self.input_text.set("")
        elif button == "←":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif button in ["sin", "cos", "tan", "log", "exp"]:
            self.expression += f"math.{button}("
        elif button == "π":
            self.expression += "π"
        elif button == "MC":
            self.memory = 0
        elif button == "MR":
            self.expression += str(self.memory)
        elif button == "M+":
            try:
                self.memory += eval(self.expression)
            except:
                self.input_text.set("Error")
        elif button == "M-":
            try:
                self.memory -= eval(self.expression)
            except:
                self.input_text.set("Error")
        else:
            self.expression += button
            self.input_text.set(self.expression)

def main():
    root = tk.Tk()
    root.title("Minesweeper")
    game = MinesweeperGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
