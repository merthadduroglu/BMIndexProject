import tkinter

my_screen = tkinter.Tk()
my_screen.title("Body-Mass Index")
my_screen.minsize(width=270,height=250)

#functions
def calculate_clicked():
    height_text = height_entry.get().strip()
    weight_text = weight_entry.get().strip()

    if not height_text and not weight_text:
        result_label.config(text="Please enter both height and weight!")
    elif not weight_text:
        result_label.config(text="Please enter weight (kg)!")
    elif not height_text:
        result_label.config(text="Please enter height (cm)!")
    else:
        try:
            h_input_cm = float(height_text)
            h_input_m = h_input_cm/100
            w_input = float(weight_text)
            bm_value = (w_input/h_input_m**2)
            calculation_result(bm_value)
        except ValueError:
            result_label.config(text="Invalid input! Please use numbers only!")


def calculation_result(bm_value):
    if bm_value <= 18.5:
        result_text = "You are underweight."
    elif 18.5 < bm_value <= 24.9:
        result_text = "Your weight is normal."
    elif 24.9 < bm_value <= 29.9:
        result_text = "You are overweight."
    elif 29.9 < bm_value <= 34.9:
        result_text = "You are class I obese."
    elif 34.9 < bm_value <= 39.9:
        result_text = "You are class II obese."
    else:
        result_text = "You are class III obese."

    result_label.config(text=f"BMI: {bm_value:.1f}\n{result_text}")

#screen objects
weight_label = tkinter.Label(text="Enter your weight (kg):")
weight_label.pack(padx=5,pady=5)

weight_entry = tkinter.Entry()
weight_entry.pack(padx=5,pady=5)

height_label = tkinter.Label(text="Enter your height (cm):")
height_label.pack(padx=5,pady=5)

height_entry = tkinter.Entry()
height_entry.pack(padx=5,pady=5)

calculate_button = tkinter.Button(text="calculate",command=calculate_clicked)
calculate_button.pack(padx=5,pady=5)

#result label
result_label = tkinter.Label(text="")
result_label.pack(padx=5,pady=10)

tkinter.mainloop()