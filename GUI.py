import PySimpleGUI as sg
import memory #memory.py

sg.theme('DarkAmber')   # Add a touch of color

#Layout
layout = [[sg.Text("Assembly Simulator",font=("Helvetica", 25))],
        [sg.FolderBrowse("LOAD"), sg.Button("RUN"), sg.Button("NEXT")],
        [sg.Text("Source: ")],
        [sg.Text("Code:")],
        [sg.Multiline(size=(50, 20))],
        [sg.Text("Register", pad=(20,20)), sg.Text("Variables", pad=(20,20)), sg.Text("Stack", pad=(20,20))],
        [sg.Text("T0", pad=(20,20)), sg.Multiline(""), sg.Multiline("", pad=(20,20))]]

# Create the Window
window = sg.Window('Assembly Simulator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()  