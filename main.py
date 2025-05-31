import tkinter

my_screen = tkinter.Tk()
my_screen.title("Body-Mass Index")
my_screen.minsize(width=200,height=200)

#screen objects
weight_label = tkinter.Label(text="Enter your weight")
weight_label.pack()

weight_entry = tkinter.Entry()
weight_entry.pack()

height_label = tkinter.Label(text="Enter your height")
height_label.pack()

height_entry = tkinter.Entry()
height_entry.pack()

calculate_button = tkinter.Button(text="calculate")
calculate_button.pack()

tkinter.mainloop()