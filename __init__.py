import source
import eventer15
import PySimpleGUI as sg

line = {"a": "???", "b": "???", "f": "???", "r": "???"}
if __name__ == "__main__":
    window = sg.Window("Hackathone 15-17 y.o.", source.layout)

    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        print(event, value)

        if event == "-Solve-":
            line = eventer15.eventer(event, value)
            if line == {"a": "???", "b": "???", "f": "???", "r": "???"}:
                sg.popup(title= "Don't understand input", background_color= "#C1C1C1", custom_text= "Error!", icon= "Logo.png")
            window["-A-"].update(line["a"])
            window["-F-"].update(line["f"])
            window["-B-"].update(line["b"])
            window["-R-"].update(line["r"])
