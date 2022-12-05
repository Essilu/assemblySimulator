import parser #parser.py
import memory #memory.py

#Don't start the program before main is called
if __name__ == '__main__':
    full_code = parser.import_file("asm_samples/example1.txt")
    full_code = parser.unclutter(full_code)

    data, code = parser.split_data_code(full_code)

    print(data)
    print(code)