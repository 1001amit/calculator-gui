import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")

        self.expression = ""
        self.input_text = tk.StringVar()
        self.memory = 0  # Initialize memory variable

        self.create_widgets()

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
        try:
            if button == "=":
                self.expression = self.expression.replace("π", str(math.pi))  # Replace "π" with math.pi
                # Evaluate the expression and round the result to prevent floating-point issues
                result = str(round(eval(self.expression), 10))
                self.expression = result
                self.input_text.set(result)
            elif button == "C":
                self.expression = ""
                self.input_text.set("")
            elif button == "←":
                self.expression = self.expression[:-1]
                self.input_text.set(self.expression)
            elif button == "sin":
                self.expression = str(math.sin(math.radians(eval(self.expression))))
                self.input_text.set(self.expression)
            elif button == "cos":
                self.expression = str(math.cos(math.radians(eval(self.expression))))
                self.input_text.set(self.expression)
            elif button == "tan":
                self.expression = str(math.tan(math.radians(eval(self.expression))))
                self.input_text.set(self.expression)
            elif button == "log":
                self.expression = str(math.log10(eval(self.expression)))
                self.input_text.set(self.expression)
            elif button == "exp":
                self.expression = str(math.exp(eval(self.expression)))
                self.input_text.set(self.expression)
            elif button == "π":
                self.expression += "π"
            elif button == "MC":
                self.memory = 0
            elif button == "MR":
                self.expression += str(self.memory)
            elif button == "M+":
                self.memory += eval(self.expression)
            elif button == "M-":
                self.memory -= eval(self.expression)
            else:
                self.expression += button
                self.input_text.set(self.expression)
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
