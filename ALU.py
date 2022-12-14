import errors #errors.py
import memory #memory.py
import CPU #execution.py

# All the 20 instructions required are implemented in this file.

"""JMP function : Jump to a label"""
def jump(label):
    print("Jumping to label " + label)
    CPU.current_line_number = memory.label_list[label]

"""LDA function : Load the value of a variable/register/const into the register given
    Format: LDA(register, value)"""
def LDA(register, value):
    if register in memory.register_dictionnary:                                 #check if the register is valid
        if type(value) == int:                                                  #check if the value is a constant
            memory.variable_dictionnary[register] = value
        elif value in memory.variable_dictionnary:
            memory.register_dictionnary[register] = memory.variable_dictionnary[value]
        else: 
            raise errors.InvalidValue
    else:
        raise errors.InvalidRegister

"""STR function: Store the value of a register/variable into a variable """
def STR(variable, value):
    if variable in memory.variable_dictionnary:
        if type(value) == int:
            memory.variable_dictionnary[variable] = value
        elif value in memory.register_dictionnary:
            memory.variable_dictionnary[variable] = memory.register_dictionnary[value]
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidValue
"""PUSH function : Push the value of a register/variable/const onto the stack"""
def PUSH(register):
    if register in memory.register_dictionnary:
        memory.stack.append(memory.register_dictionnary[register])
    elif register in memory.variable_dictionnary:
        memory.stack.append(memory.variable_dictionnary[register])
    elif type(register) == int:
        memory.stack.append(register)
    else:
        raise errors.InvalidRegister

"""POP function : Pop the value of the top of the stack into a register"""
def POP(register):
    if register in memory.register_dictionnary:
        memory.register_dictionnary[register] = memory.stack.pop()
    else:
        raise errors.InvalidRegister

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
            raise errors.InvalidValue
    else:
        raise errors.InvalidRegister

"""OR function Performs a logical OR operation between reg1 and a register reg2, a variable var or a constant and store the result in a register"""
def OR(register, variable):
    if register in memory.register_dictionnary:
        if variable in memory.register_dictionnary:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] | memory.register_dictionnary[variable]
        elif variable in memory.variable_dictionnary:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] | memory.variable_dictionnary[variable]
        elif type(variable) == int:
            memory.register_dictionnary[register] = memory.register_dictionnary[register] | variable
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidRegister

"""NOT function Performs a logical NOT operation on a register reg and store the result in a register"""
def NOT(register):
    if register in memory.register_dictionnary:
        memory.register_dictionnary[register] = ~memory.register_dictionnary[register]
    else:
        raise errors.InvalidRegister

"""ADD function : Add the value of a register/variable/const to the value of a register"""
def ADD(register, variable):
    if register in memory.register_dictionnary:
        if variable in memory.register_dictionnary:
            memory.register_dictionnary[register] = int(memory.register_dictionnary[register]) + int(memory.register_dictionnary[variable])
        elif variable in memory.variable_dictionnary:
            memory.register_dictionnary[register] = int(memory.register_dictionnary[register]) + int(memory.variable_dictionnary[variable])
        elif type(variable) == int:
            memory.register_dictionnary[register] = int(memory.register_dictionnary[register]) + int(variable)
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidRegister

"""SUB function : Substract the value of a register/variable/const to the value of a register"""
def SUB(register, variable):
    if register in memory.register_dictionnary:
        if variable in memory.register_dictionnary:
            memory.register_dictionnary[register] = int(memory.register_dictionnary[register]) - int(memory.register_dictionnary[variable])
        elif variable in memory.variable_dictionnary:
            memory.register_dictionnary[register] = int(memory.register_dictionnary[register]) - int(memory.variable_dictionnary[variable])
        elif type(variable) == int:
            memory.register_dictionnary[register] = int(memory.register_dictionnary[register]) - int(variable)
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidRegister

"""DIV function : Divide the value of a register/variable/const to the value of a register"""
def DIV(register, variable):
    if register in memory.register_dictionnary:
        if variable in memory.register_dictionnary:
            memory.register_dictionnary[register] = int(int(memory.register_dictionnary[variable]) / int(memory.register_dictionnary[register]))
        elif variable in memory.variable_dictionnary:
            memory.register_dictionnary[register] = int(int(memory.variable_dictionnary[variable]) / int(memory.register_dictionnary[register]))
        elif type(variable) == int and variable != 0:
            memory.register_dictionnary[register] = int(int(variable) / int(memory.register_dictionnary[register]))
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidRegister

"""MUL function : Multiply the value of a register/variable/const to the value of a register"""
def MUL(register, variable):
    if register in memory.register_dictionnary:
        if variable in memory.register_dictionnary:
            memory.register_dictionnary[register] = int(memory.register_dictionnary[register]) * int(memory.register_dictionnary[variable])
        elif variable in memory.variable_dictionnary:
            memory.register_dictionnary[register] = int(memory.register_dictionnary[register]) * int(memory.variable_dictionnary[variable])
        elif type(variable) == int:
            memory.register_dictionnary[register] = int(memory.register_dictionnary[register]) * int(variable)
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidRegister

"""MOD function : Modulo the value of a register/variable/const to the value of a register"""
def MOD(register, variable):
    if register in memory.register_dictionnary:
        if variable in memory.register_dictionnary:
            memory.register_dictionnary[register] =  int(memory.register_dictionnary[variable]) % int(memory.register_dictionnary[register])
        elif variable in memory.variable_dictionnary:
            memory.register_dictionnary[register] =  int(memory.variable_dictionnary[variable]) % int(memory.register_dictionnary[register])
        elif type(variable) == int:
            memory.register_dictionnary[register] = int(variable) % int(memory.register_dictionnary[register])
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidRegister

"""INC function : increment the value of a register"""
def INC(register):
    if register in memory.register_dictionnary:
        memory.register_dictionnary[register] += 1
    else:
        raise errors.InvalidRegister

"""DEC function : decrement the value of a register"""
def DEC(register):
    if register in memory.register_dictionnary:
        memory.register_dictionnary[register] -= 1
    else:
        raise errors.InvalidRegister

"""BEQ function : Performs a comparison between two values, given by registers, variables or constants. Any
combination is permitted. If they are equal, jump to the address defined by the label LABEL"""
def BEQ(value1, value2, label):
    if value1 in memory.register_dictionnary:      #If the value1 is a register : cover all the cases with value2
        if value2 in memory.register_dictionnary:
            if memory.register_dictionnary[value1] == memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if memory.register_dictionnary[value1] == memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if memory.register_dictionnary[value1] == value2:
                jump(label)
        else:
            raise errors.InvalidValue
    elif value1 in memory.variable_dictionnary:     #If the value1 is a variable : cover all the cases with value2
        if value2 in memory.register_dictionnary:
            if memory.variable_dictionnary[value1] == memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if memory.variable_dictionnary[value1] == memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if memory.variable_dictionnary[value1] == value2:
                jump(label)
        else:
            raise errors.InvalidValue
    elif type(value1) == int:
        if value2 in memory.register_dictionnary:
            if value1 == memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if value1 == memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if value1 == value2:
                jump(label)
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidValue

"""BNE function : Performs a comparison between two values, given by registers, variables or constants. Any
combination is permitted. If they are different, jump to the address defined by the label LABEL"""
def BNE(value1, value2, label):
    if value1 in memory.register_dictionnary:      #If the value1 is a register : cover all the cases with value2
        if value2 in memory.register_dictionnary:
            if memory.register_dictionnary[value1] != memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if memory.register_dictionnary[value1] != memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if memory.register_dictionnary[value1] != value2:
                jump(label)
        else:
            raise errors.InvalidValue
    elif value1 in memory.variable_dictionnary:     #If the value1 is a variable : cover all the cases with value2
        if value2 in memory.register_dictionnary:
            if memory.variable_dictionnary[value1] != memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if memory.variable_dictionnary[value1] != memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if memory.variable_dictionnary[value1] != value2:
                jump(label)
        else:
            raise errors.InvalidValue
    elif type(value1) == int:
        if value2 in memory.register_dictionnary:
            if value1 != memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if value1 != memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if value1 != value2:
                jump(label)
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidValue

"""BBG function : Performs a comparison between two values, given by registers, variables or constants. Any
combination is permitted. If the first parameter is bigger than the second parameter, jump to the
address defined by the label LABEL"""
def BBG(value1, value2, label):
    if value1 in memory.register_dictionnary:      #If the value1 is a register : cover all the cases with value2
        if value2 in memory.register_dictionnary:
            if memory.register_dictionnary[value1] > memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if memory.register_dictionnary[value1] > memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if memory.register_dictionnary[value1] > value2:
                jump(label)
        else:
            raise errors.InvalidValue
    elif value1 in memory.variable_dictionnary:     #If the value1 is a variable : cover all the cases with value2
        if value2 in memory.register_dictionnary:
            if memory.variable_dictionnary[value1] > memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if memory.variable_dictionnary[value1] > memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if memory.variable_dictionnary[value1] > value2:
                jump(label)
        else:
            raise errors.InvalidValue
    elif type(value1) == int:
        if value2 in memory.register_dictionnary:
            if value1 > memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if value1 > memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if value1 > value2:
                jump(label)
        else:
           raise errors.InvalidValue
    else:
        raise errors.InvalidValue

"""BSM function : Performs a comparison between two values, given by registers, variables or constants. Any
combination is permitted. If the first parameter is smaller than the second parameter, jump to the
address defined by the label LABEL"""
def BSM(value1, value2, label):
    if value1 in memory.register_dictionnary:      #If the value1 is a register : cover all the cases with value2
        if value2 in memory.register_dictionnary:
            if memory.register_dictionnary[value1] < memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if memory.register_dictionnary[value1] < memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if memory.register_dictionnary[value1] < value2:
                jump(label)
        else:
            raise errors.InvalidValue
    elif value1 in memory.variable_dictionnary:     #If the value1 is a variable : cover all the cases with value2
        if value2 in memory.register_dictionnary:
            if memory.variable_dictionnary[value1] < memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if memory.variable_dictionnary[value1] < memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if memory.variable_dictionnary[value1] < value2:
                jump(label)
        else:
            raise errors.InvalidValue
    elif type(value1) == int:
        if value2 in memory.register_dictionnary:
            if value1 < memory.register_dictionnary[value2]:
                jump(label)
        elif value2 in memory.variable_dictionnary:
            if value1 < memory.variable_dictionnary[value2]:
                jump(label)
        elif type(value2) == int:
            if value1 < value2:
                jump(label)
        else:
            raise errors.InvalidValue
    else:
        raise errors.InvalidValue

"""JMP function : Jump to the address defined by the label LABEL"""
def JMP(label):
    jump(label)

def HLT():
    print("End of program")
    CPU.current_line_number = -1