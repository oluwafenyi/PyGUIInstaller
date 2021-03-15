
import PySimpleGUI as sg


layout = [
    [sg.Text("Install Location:"), sg.InputText(), sg.FolderBrowse()]
]

window = sg.Window("Installer", layout=layout, margins=(320, 224))

if __name__ == "__main__":

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break

    window.close()
