# All the 20 instructions required are implemented in this file

#TODO: implement the errors ! (in LDA, )

import memory #memory.py

"""LDA function : Load the value of a variable/register/const into the register given
    Format: LDA(register, value)"""

def LDA(register, value):
    if register in ["T0", "T1", "T2", "T3"]:                                #check if the register is valid
        if type(value) == int:                                              #check if the value is a constant
            memory.variable_dictionnary[register] = value
        elif value in memory.variable_dictionnary:
            memory.variable_dictionnary[register] = memory.variable_dictionnary[value]
        else: 
            print("Error: invalid value")
    else:
        print("Error: Invalid register")                                    #TODO: implement the errors !





memory.variable_dictionnary = {'T0': 0, 'T1': 0, 'T2': 0, 'T3': 0, "A": 5}

LDA("A", "B")
print(memory.variable_dictionnary)