import memory #memory.py
import parsing #parsing.py
import ALU #ALU.py

# This part of the program will contain each execution instruction, and will be called by the main.py file

code = []
data = []

current_line_number = 0

"""This function loads the file"""
def load_file(source_file):
    global code
    #Basic operation before starting execution of the ASM files
    full_code = parsing.import_file(source_file)
    full_code = parsing.unclutter(full_code)
    data, code = parsing.split_data_code(full_code)
    memory.initialize_data(data)   

"""This function executes the current line dictated by the current_line_number variable"""
def execute_line():

    global code
    global current_line_number
    
    #Get the current line of code
    line = code[current_line_number]
    line = line.split()
    

    if current_line_number != -1:
        try:
            if line[0] == "LDA":
                ALU.LDA(line[1], line[2])
            elif line[0] == "STR":
                ALU.STR(line[1], line[2])
            elif line[0] == "PUSH":
                ALU.PUSH(line[1])
            elif line[0] == "POP":
                ALU.POP(line[1])
            elif line[0] == "AND":
                ALU.AND(line[1], line[2])
            elif line[0] == "OR":
                ALU.OR(line[1], line[2])
            elif line[0] == "NOT":
                ALU.NOT(line[1])
            elif line[0] == "ADD":
                ALU.ADD(line[1], line[2])
            elif line[0] == "SUB":
                ALU.SUB(line[1], line[2])
            elif line[0] == "DIV":
                ALU.DIV(line[1], line[2])
            elif line[0] == "MUL":
                ALU.MUL(line[1], line[2])
            elif line[0] == "MOD":
                ALU.MOD(line[1], line[2])
            elif line[0] == "INC":
                ALU.INC(line[1])
            elif line[0] == "DEC":
                ALU.DEC(line[1])
            elif line[0] == "BEQ":
                ALU.BEQ(line[1], line[2], line[3])
            elif line[0] == "BNE":
                ALU.BNE(line[1], line[2], line[3])
            elif line[0] == "BBG":
                ALU.BBG(line[1], line[2], line[3])
            elif line[0] == "BSM":
                ALU.BSM(line[1], line[2], line[3])
            elif line[0] == "JMP":
                ALU.JMP(line[1])
            elif line[0] == "HLT":
                ALU.HLT()
        except:
            print("Error: " + line[0] + " is not a valid instruction")
        debug_print()

"""This function helps to debug the program by printing the current state of the program"""
def debug_print():
    print("Current line number: " + str(current_line_number) + "\n" +
          "Register: " + str(memory.register_dictionnary) + "\n" +
          "Variables : " + str(memory.variable_dictionnary) + "\n" +
          "Stack : " + str(memory.stack) + "\n")    