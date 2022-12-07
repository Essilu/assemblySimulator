import PySimpleGUI as sg
import execution as exec
import os
import memory as mem

def run():
    sg.theme('Reddit')   # Add a touch of color
    working_directory = os.getcwd()

    status = "Status :\n\nFile : Loaded \n\nProgram counter :  "




    layout_1 = [[
        sg.Frame('Assembly Simulator',[[
            sg.Text('Input:'),      
            sg.FileBrowse("Import",key="-IN-",initial_folder=working_directory,file_types=(("Text Files", "*.txt"),)),
            sg.Button("LOAD"),
            sg.Button('RUN'),
            sg.Button('STEP'),
            sg.Exit(),
        ]]),]]
    layout_2 =[[
        sg.Frame('Source:',
        [[sg.Text('Code: ')],
        [sg.Multiline(key="-CODE-",size=(50, 20)),sg.Text("Status :\n\nFile :Not Loaded \n\nProgram counter : ",key="-S-",size=(13,20)),sg.Text("0",key="-CNT-",size=(20,12))],
        [sg.Frame('Registers:',[[sg.Text('T0', pad=(20,2)), sg.Text("0",key="-T0-")],
        [sg.Text("T1",pad=(20,2)),sg.Text("0",key="-T1-")],
        [sg.Text("T2",pad=(20,2)),sg.Text("0",key="-T2-")],
        [sg.Text("T3",pad=(20,2)),sg.Text("0",key="-T3-")],]),
        sg.Frame('Var:',[[ sg.Multiline(key="-VAR-",size=(25, 5)),]]),
        sg.Frame('Stack:',[[ sg.Multiline(key="-STACK-",size=(25, 5)),]])
        ]])
    ]]
    layout = [
        [layout_1,
        layout_2,],  
    ]
    def formatter(data):
        data = str(data)
        data = data.replace(',', '\n')
        data = data.replace("'", '')
        data = data.replace("[", ' ')
        data = data.replace("]", '')
        data = data.replace("{", ' ')
        data = data.replace("}", '')
        return data

    window = sg.Window('Assembly simulator 3000', layout)

    while True:             # Event Loop
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "LOAD":
            try :
                file_address = values["-IN-"]
                exec.load_file(file_address)
                window["-S-"].update(status)
                exec.current_line_number = 0
                window["-T0-"].update(0)
                window["-T1-"].update(0)
                window["-T2-"].update(0)
                window["-T3-"].update(0)
                window["-CODE-"].update(formatter(exec.code))
                window["-VAR-"].update(formatter(mem.variable_dictionnary))
                mem.stack = []
                window["-STACK-"].update(formatter(mem.stack))
                window["-CNT-"].update(0)
            except:
                sg.popup("No file selected")
           
        if event == "RUN":
            try:
                if exec.current_line_number != -1:
                    exec.full_execution()
                    window["-T0-"].update(mem.register_dictionnary["T0"])
                    window["-T1-"].update(mem.register_dictionnary["T1"])
                    window["-T2-"].update(mem.register_dictionnary["T2"])
                    window["-T3-"].update(mem.register_dictionnary["T3"])
                    window["-VAR-"].update(formatter(mem.variable_dictionnary))
                    window["-STACK-"].update(formatter(mem.stack))
                    window["-CNT-"].update("End of program")
                else : 
                    sg.popup("You need to reload the file to run it again")
            except:
                sg.popup("You need to load the file first")
        if event == "STEP":
            try:
                exec.execute_line()
                if exec.current_line_number != -1:
                    exec.next_line()
                    pg_counter = exec.current_line_number
                    print(pg_counter)
                    window["-CNT-"].update(pg_counter)
                    window["-T0-"].update(mem.register_dictionnary["T0"])
                    window["-T1-"].update(mem.register_dictionnary["T1"])
                    window["-T2-"].update(mem.register_dictionnary["T2"])
                    window["-T3-"].update(mem.register_dictionnary["T3"])
                    window["-VAR-"].update(formatter(mem.variable_dictionnary))
                    window["-STACK-"].update(formatter(mem.stack))
                else: 
                    window["-CNT-"].update("End of program")
                    mem.stack = []    
                    sg.popup("You need to reload the file to run it again")
            except:
                sg.popup("You need to load the file first")
    
        window.refresh()
    window.close()