#program is using PySimpleGUI from pip
import PySimpleGUI as sg

def bin_to_dec(number):
    decimal, i, = 0, 0
    while (number != 0):
        dec = number % 10
        decimal = decimal + dec * pow(2, i)
        number = number // 10
        i += 1
    return decimal

def dec_to_hex(number):
    conversion_table = "0123456789ABCDEF"
    hexadecimal = ''
    while(number > 0):
        remainder = number % 16
        hexadecimal = conversion_table [ remainder ] + hexadecimal
        number = number // 16
    return hexadecimal

def dec_to_oct(number):
    conversion_table = "012345678"
    octal = ''
    while(number > 0):
        remainder = number % 8
        octal = conversion_table [ remainder ] + octal
        number = number // 8
    return octal

def hex_to_dec(number):
    conversion_table = "0123456789ABCDEF"
    decimal = 0
    i = len(number) - 1
    while(i >= 0):
        decimal += (pow(16, len(number) - 1 - i) * conversion_table.index(number [ i ]))
        i -= 1
    return decimal

def oct_to_dec(number):
    conversion_table = "01234567"
    decimal = 0
    i = len(number) - 1
    while(i >= 0):
        decimal += (pow(8, len(number) - 1 - i) * conversion_table.index(number [ i ]))
        i -= 1
    return decimal

sg.set_options(font = "Calibri 40")
spin_names = ["dec to bin", "bin to dec", "dec to hex", "hex to dec", "oct to dec", "dec to oct"]
layout = [
    [sg.Input(key = "input", size = (80,0))],
    [
        sg.Spin(spin_names, key = "units", expand_x = True, tooltip = "please, choose convertion method", enable_events = True),
        sg.Button("Convert", key = "convert", button_color = ("#00BFFF", "black"))
    ],
    [sg.Text("output", enable_events = True, key = "output", background_color = "#DCDCDC", text_color = "black")], #top row
]

window = sg.Window("Konwenter", layout, background_color = "#008080", size = (1000, 300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "convert":
        input_value = values["input"];

        if values ["units"] == "dec to bin":
            output = "{0:b}".format(int(input_value))
            output_string = f"decimal: {input_value} in binary: {output}"
        elif values ["units"] == "bin to dec":
            output = bin_to_dec(int(input_value))
            output_string = f"binary: {input_value} in decimal: {output}"
        elif values["units"] == "dec to hex":
            output = dec_to_hex(int(input_value))
            output_string = f"decimal: {input_value} in hexadecimal: {output}"
        elif values["units"] == "hex to dec":
            output = hex_to_dec(input_value)
            output_string = f"hexadecimal: {input_value} in decimal: {output}"
        elif values["units"] == "oct to dec":
            output = oct_to_dec(input_value)
            output_string = f"octal: {input_value} in decimal: {output}"
        elif values["units"] == "dec to oct":
            output = dec_to_oct(int(input_value))
            output_string = f"decimal: {input_value} in octal: {output}"

        window["output"].update(output_string)

window.close()



