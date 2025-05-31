import tkinter

my_screen = tkinter.Tk()
my_screen.title("Body-Mass Index")
my_screen.minsize(width=230,height=230)

#functions
def calculate_clicked():

    try:
        h_input_cm = float(height_entry.get())
        h_input_m = h_input_cm/100
        w_input = float(weight_entry.get())
        bm_value = (w_input/h_input_m**2)
        calculation_result(bm_value)
    except:
        result_label.config(text="enter a valid number")


def calculation_result(bm_value):
    if bm_value <= 18.5:
        result_label.config(text="You are underweight.")
    elif 18.5 < bm_value <= 24.9:
        result_label.config(text="Your weight is normal.")
    elif 24.9 < bm_value <= 29.9:
        result_label.config(text="You are overweight.")
    elif 29.9 < bm_value <= 34.9:
        result_label.config(text="You are class I obese.")
    elif 34.9 < bm_value <= 39.9:
        result_label.config(text="You are class II obese.")
    elif bm_value > 39.9:
        result_label.config(text="You are class III obese.")


#screen objects
weight_label = tkinter.Label(text="Enter your weight")
weight_label.pack(padx=5,pady=5)

weight_entry = tkinter.Entry()
weight_entry.pack(padx=5,pady=5)

height_label = tkinter.Label(text="Enter your height")
height_label.pack(padx=5,pady=5)

height_entry = tkinter.Entry()
height_entry.pack(padx=5,pady=5)

calculate_button = tkinter.Button(text="calculate",command=calculate_clicked)
calculate_button.pack(padx=5,pady=5)

#result label
result_label = tkinter.Label(text="")
result_label.pack(padx=5,pady=10)

tkinter.mainloop()