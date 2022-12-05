# All the 20 instructions required are implemented in this file

#TODO: implement the errors ! (in LDA, )
#TODO: AND, OR, NOT

import memory #memory.py

"""LDA function : Load the value of a variable/register/const into the register given
    Format: LDA(register, value)"""
def LDA(register, value):
    if register in memory.register_dictionnary:                                #check if the register is valid
        if type(value) == int:                                              #check if the value is a constant
            memory.variable_dictionnary[register] = value
        elif value in memory.variable_dictionnary:
            memory.variable_dictionnary[register] = memory.variable_dictionnary[value]
        else: 
            print("Error: invalid value")
    else:
        print("Error: Invalid register")                                    #TODO: implement the errors !

"""STR function: Store the value of a register/variable into a variable """
def STR(variable, value):
    if variable in memory.variable_dictionnary:
        if type(value) == int:
            memory.variable_dictionnary[variable] = value
        elif value in memory.register_dictionnary:
            memory.variable_dictionnary[variable] = memory.register_dictionnary[value]
        else:
            print("Error: invalid value")  #TODO: implement the errors !
    else:
        print("Error: invalid variable")   #Todo: implement the errors !

"""PUSH function : Push the value of a register/variable/const onto the stack"""
def PUSH(register):
    if register in memory.register_dictionnary:
        memory.stack.append(memory.register_dictionnary[register])
    elif register in memory.variable_dictionnary:
        memory.stack.append(memory.variable_dictionnary[register])
    elif type(register) == int:
        memory.stack.append(register)
    else:
        print("Error: invalid input") #TODO: implement the errors !

"""POP function : Pop the value of the top of the stack into a register"""
def POP(register):
    if register in memory.register_dictionnary:
        memory.register_dictionnary[register] = memory.stack.pop()
    else:
        print("Error: invalid register") #TODO: implement the errors !

"""AND function Performs a logical AND operation between reg1 and a register reg2, a variable var or a constant
const, and store the result in a register."""
def AND(register, variable):
    if register in memory.register_dictionnary:
        if variable in memory.register_dictionnary:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] & memory.register_dictionnary[variable]
        elif variable in memory.variable_dictionnary:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] & memory.variable_dictionnary[variable]
        elif type(variable) == int:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] & variable
        else:
            print("Error: invalid variable") #TODO: implement the errors !
    else:
        print("Error: invalid register") #TODO: implement the errors !

"""OR function Performs a logical OR operation between reg1 and a register reg2, a variable var or a constant and store the result in a register"""
def OR(register, variable):
    pass

"""NOT function Performs a logical NOT operation on a register reg and store the result in a register"""
def NOT(register):
    pass

"""ADD function : Add the value of a register/variable/const to the value of a register"""
def ADD(register, variable):
    if register in memory.register_dictionnary:
        if variable in memory.register_dictionnary:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] + memory.register_dictionnary[variable]
        elif variable in memory.variable_dictionnary:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] + memory.variable_dictionnary[variable]
        elif type(variable) == int:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] + variable
        else:
            print("Error: invalid variable") #TODO: implement the errors !
    else:
        print("Error: invalid register") #TODO: implement the errors !

"""SUB function : Substract the value of a register/variable/const to the value of a register"""
def SUB(register, variable):
    if register in memory.register_dictionnary:
        if variable in memory.register_dictionnary:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] - memory.register_dictionnary[variable]
        elif variable in memory.variable_dictionnary:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] - memory.variable_dictionnary[variable]
        elif type(variable) == int:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] - variable
        else:
            print("Error: invalid variable") #TODO: implement the errors !
    else:
        print("Error: invalid register") #TODO: implement the errors !

memory.stack = [1,2,3,4,5]
memory.register_dictionnary = {'T0': 7, 'T1': 3, 'T2': 0, 'T3': 0}
memory.variable_dictionnary = {"A": 5}

print("memory : " + str(memory.stack))
print("variable : " + str(memory.variable_dictionnary))
print("register : " + str(memory.register_dictionnary)) 

