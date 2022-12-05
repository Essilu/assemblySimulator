import parsing #parsing.py
import memory #memory.py

#Don't start the program before main is called
if __name__ == '__main__':

    #Basic operation before starting execution of the ASM files
    full_code = parsing.import_file("asm_samples/example1.txt")
    full_code = parsing.unclutter(full_code)
    data, code = parsing.split_data_code(full_code)
    memory.initialize_data(data)

    #Start execution of the ASM files

    print(memory.register_dictionnary)
    print(memory.variable_dictionnary)

    print(code)
    
    