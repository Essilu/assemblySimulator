import parsing #parsing.py
import memory #memory.py
import ALU #ALU.py
import execution #execution.py

#Don't start the program before main is called
execution.load_file("asm_samples/example1.txt")

execution.execute_line()
execution.next_line()
execution.execute_line()
execution.next_line()
execution.execute_line()
execution.next_line()
execution.execute_line()
execution.next_line()
execution.execute_line()