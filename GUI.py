import PySimpleGUI as sg
import execution as exec
import os
import memory as mem

sg.theme('Reddit')   # Add a touch of color
working_directory = os.getcwd()
layout_1 = [[
    sg.Frame('Assembly Simulator',[[
          sg.Text('Input:'),      
        sg.FileBrowse("Import",key="-IN-",initial_folder=working_directory,file_types=(("Text Files", "*.txt"),)),sg.Button("LOAD"),sg.Button('RUN'),sg.Button('STEP'), sg.Exit(),
    ]]),]]
layout_2 =[[
     sg.Frame('Source:',
     [[sg.Text('Code: ')],
     [sg.Multiline(size=(50, 20))],
     [sg.Frame('Register:',[[sg.Text('T0', pad=(20,20)), sg.Text("0",key="-T0-")]]),
     sg.Frame('Var:',[[ sg.Multiline(size=(25, 5)),]]),
     sg.Frame('Stack:',[[ sg.Multiline(size=(25, 5)),]])
     ]])
]]
layout = [
    [layout_1,
    layout_2,]
]

window = sg.Window('App', layout)

while True:             # Event Loop
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "LOAD":
        file_address = values["-IN-"]
        exec.load_file(file_address)
    if event == "RUN":
        exec.full_execution()
    if event == "STEP":
        exec.execute_line()
    window.refresh()
window.close()