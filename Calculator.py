#Import
import tkinter as tk

#Define
def inputnumber(number):
    global expression
    expression = expression + str(number)
    inputtext.set(expression)
def result():
    global expression
    result = str(eval(expression))
    inputtext.set(result)
    expression = result
def button_clear():
    global expression
    expression = ""
    inputtext.set("")

#Window
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x400")

#Variable
inputtext = tk.StringVar()

#Entry
entry = tk.Entry(window, width = 400, borderwidth = 100, font = ("Arial", 18), justify = "right", textvariable = inputtext)

#Numerical Buttons
button0 = tk.Button(window, bg = "black", text = "0", padx = 20, pady = 20, command = lambda: inputnumber(0))
button1 = tk.Button(window, bg = "black", text = "1", padx = 20, pady = 20, command = lambda: inputnumber(1))
button2 = tk.Button(window, bg = "black", text = "2", padx = 20, pady = 20, command = lambda: inputnumber(2))
button3 = tk.Button(window, bg = "black", text = "3", padx = 20, pady = 20, command = lambda: inputnumber(3))
button4 = tk.Button(window, bg = "black", text = "4", padx = 20, pady = 20, command = lambda: inputnumber(4))
button5 = tk.Button(window, bg = "black", text = "5", padx = 20, pady = 20, command = lambda: inputnumber(5))
button6 = tk.Button(window, bg = "black", text = "6", padx = 20, pady = 20, command = lambda: inputnumber(6))
button7 = tk.Button(window, bg = "black", text = "7", padx = 20, pady = 20, command = lambda: inputnumber(7))
button8 = tk.Button(window, bg = "black", text = "8", padx = 20, pady = 20, command = lambda: inputnumber(8))
button9 = tk.Button(window, bg = "black", text = "9", padx = 20, pady = 20, command = lambda: inputnumber(9))

#Operational Buttons
addition = tk.Button(window, bg = "black", text = "+", padx = 20, pady = 40, command = lambda: inputnumber("+"))
subtraction = tk.Button(window, bg = "black", text = "-", padx = 20, pady = 20, command = lambda: inputnumber("-"))
multiplication = tk.Button(window, bg = "black", text = "*", padx = 20, pady = 20, command = lambda: inputnumber("*"))
division = tk.Button(window, bg = "black", text = "/", padx = 20, pady = 20, command = lambda: inputnumber("/"))
modulus = tk.Button(window, bg = "black", text = "mod", padx = 20, pady = 20, command = lambda: inputnumber("mod"))
percentage = tk.Button(window, bg = "black", text = "%", padx = 20, pady = 20, command = lambda: inputnumber("%"))
equal = tk.Button(window, bg = "black", text = "=", padx = 20, pady = 20, command = lambda: inputnumber(result()))
clear = tk.Button(window, bg = "orange", text = "Clear", padx = 40, pady = 20, command = lambda: inputnumber(button_clear()))

#Entry Grids
entry.grid(row = 0, column = 0, columnspan = 5)

#Numerical Button Grids
button0.grid(row = 4, column = 1)
button1.grid(row = 3, column = 1)
button2.grid(row = 3, column = 2)
button3.grid(row = 3, column = 3)
button4.grid(row = 2, column = 1)
button5.grid(row = 2, column = 2)
button6.grid(row = 2, column = 3)
button7.grid(row = 1, column = 1)
button8.grid(row = 1, column = 2)
button9.grid(row = 1, column = 3)

#Operational Button Grids
addition.grid(row = 3, column = 4)
subtraction.grid(row = 1, column = 4)
multiplication.grid(row = 2, column = 4)
division.grid(row = 1, column = 5)
percentage.grid(row = 2 , column = 5)
modulus.grid(row = 3, column = 5)
equal.grid(row = 4, column = 5)
clear.grid(row = 4, column = 2)

#Loop
window.mainloop()


