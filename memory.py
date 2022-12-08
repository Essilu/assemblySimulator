#This part of the code is the memory of the program. It contains the variable dictionnary, 
#the register dictionnary, the stack and the label list.

variable_dictionnary = {}
                        
register_dictionnary = {
                        "T0" : 0,
                        "T1" : 0,
                        "T2" : 0,
                        "T3" : 0
                        }

stack = []

#This variable is used to store the labels and their corresponding line number
label_list = {}

"""This function initializes the data section of the memory, by copying every data line into the variable dictionnary"""
def initialize_data(data):
    data = data[1:] #Remove the #data line
    for line in data:
        line = line.split()
        variable_dictionnary[line[0]] = int(line[1])

"""This function initializes the label list, by copying every label line into the label list"""
def initialize_label_list(code):
    global label_list
    print(code)
    for line in code:
        line = line.split()
        if line[0][-1] == ":":
            label_list[line[0][:-1]] = code.index(line[0])
    return label_list