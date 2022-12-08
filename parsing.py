#Parsing functions for the interpreter

"""This functions imports the file and returns a list of the lines"""""
def import_file(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data.split('\n')

"""Remove comments and empty lines"""
def unclutter(data):
    # Iterate over the elements of the input list in reverse order
    for i in range(len(data)-1, -1, -1):
        # Check if the element starts with "!" or is an empty string
        if data[i].startswith("!") or data[i] == "":
            # If the element does start with "!" or is an empty string, remove it from the list
            del data[i]

    # Return the modified list
    return data

"""Function to find the line number in an array where #CODE starts"""
def find_code(data):
    for i in range(len(data)):
        if data[i] == "#CODE":
            return i

"""Function to split the data and the code to allow for better parsing"""
def split_data_code(data):
    code_line = find_code(data)
    code = data[code_line+1:]
    data = data[:code_line]
    return data, code

