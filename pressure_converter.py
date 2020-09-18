import tkinter as tk
from functools import partial

# Set initial dropdown value
tempVal = None

def PressureConverter():

    # The values in ratio of the first element in the units
    globP = [1, 1e5, 14.5038, 750.062]

    # The first element here has to be the base
    pUnits = ['bar', 'Pascal', 'psi', 'mmhg']

    p_mapping = {y: x for x, y in zip(globP, pUnits)}


    # Save the new dropdown value
    def store_temp(set_temp):
        global tempVal
        tempVal = set_temp


    # Function for converting the pressure, returns a list of values to display
    def convert_pressure(value: float, unit: str):
        glob_val = 1/p_mapping[unit] * value

        values = ["{} {}".format('%.3g' % (glob_val * p_mapping[x]), x)
                for x in p_mapping if x != unit]
        

        return values

    def call_convert():
        results = convert_pressure(float(numberInput.get()), var.get())
        for label, value in zip(result_labels.values(), results):
            label.config(text=value)
            
        return


    numberInput = tk.StringVar()
    var = tk.StringVar()

    top = tk.Toplevel()
    top.title("Pressure Converter")
    top.configure(background='#09A3BA')
    top.grid_columnconfigure(1, weight=1)
    top.grid_rowconfigure(0, weight=1)

    # label and entry field
    input_label = tk.Label(top, text="Enter pressure",
                        background='#09A3BA', foreground="#FFFFFF")
    input_entry = tk.Entry(top, textvariable=numberInput)
    input_label.grid(row=1)
    input_entry.grid(row=1, column=1)

    result_labels = {unit: tk.Label(
        top, background='#09A3BA', foreground="#FFFFFF") for unit in range(len(pUnits) - 1)}

    for index, label in enumerate(result_labels, start=3):
        result_labels[label].grid(row=index, columnspan=4)

    # drop down initalization and setup
    dropDownList = pUnits.copy()
    dropdown = tk.OptionMenu(top, var, *dropDownList, command=store_temp)
    var.set(dropDownList[0])
    dropdown.grid(row=1, column=3, padx=10)
    dropdown.config(background='#09A3BA', foreground="#FFFFFF")
    dropdown["menu"].config(background='#09A3BA', foreground="#FFFFFF")

    # button click
    result_button = tk.Button(
        top, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")
    result_button.grid(row=2, columnspan=4)
