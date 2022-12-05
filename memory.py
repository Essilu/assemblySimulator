#Memory 

import parsing #parsing.py

variable_dictionnary = {
                        "T0" : 0,
                        "T1" : 0,
                        "T2" : 0,
                        "T3" : 0
                        }

"""This function initializes the data section of the memory, by copying every data line into the variable dictionnary"""
def initialize_data(data):
    data = data[1:] #Remove the #data line
    for line in data:
        line = line.split()
        variable_dictionnary[line[0]] = line[1]