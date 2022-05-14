#code form https://www.youtube.com/watch?v=QeMaWQZllhg
import PySimpleGUI as sg

def factorial (number):
    if number < 2:
        return 1
    return number * factorial(number - 1)

def CBtn(button_text):
    return sg.Button(button_text, size=(5, 2), font=("Helvetica", 14))

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = "Franklin 14", button_element_size = (5, 2))
    button_size = (5, 2)
    button_name = ["Clear", "!", "sqrt", "pow", 7, 8, 9, "*", 4, 5, 6, "/", 1, 2, 3, "-", 0, ".", "+", "="]
    layout = [
        [sg.Text(
            "output",
            font = "Franklin 26",
            justification = "right",
            expand_x = True, pad = (10, 20),
            right_click_menu = theme_menu,
            key = "-text-")
        ],
        [CBtn(button_name [ i ]) for i in range (0,4)],
        [CBtn(button_name [ i ]) for i in range(4, 8)],
        [CBtn(button_name [ i ]) for i in range(8, 12)],
        [CBtn(button_name [ i ]) for i in range(12, 16)],
        [CBtn(button_name [ i ]) for i in range(16, 20)],
    ]
    return sg.Window("Calculator", layout)

theme_menu = ["MENU", ["dark", "LightBlue6", "BlueMono", "DarkAmber", "random"]]
window = create_window("LightGrey1")

current_numbers = []
full_operation = []
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu [ 1 ]:
        window.close()
        window = create_window(event)

    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        current_numbers.append(event)
        number_string = "".join(current_numbers)
        window["-text-"].update(number_string)

    if event in ["+", "-", "/", "*"]:
        full_operation.append("".join(current_numbers))
        current_numbers = []
        full_operation.append(event)
        window["-text-"].update("")
    if event in "!": #["!", "sqrt", "pow"]
        size = len (current_numbers) - 1
        full_operation.append("".join(current_numbers))
        result = factorial(int((" ".join(full_operation))))
        full_operation.pop()
        window["-text-"].update(result)
        if size + 1 != 0:
            current_numbers.pop()
        current_numbers.append(str(result))

    if event == "=":
        full_operation.append("".join(current_numbers))
        result = eval(" ".join(full_operation))
        window["-text-"].update(result)
        full_operation = []
    if event == "Clear":
        current_numbers = []
        full_operation = []
        window["-text-"].update("")


window.close()