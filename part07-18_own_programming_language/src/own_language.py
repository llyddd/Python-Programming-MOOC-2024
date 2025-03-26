# Write your solution here

# PRINT [value]: prints the value
# MOV [variable] [value]: assigns the value to the variable
# ADD [variable] [value]: adds the value to the variable
# SUB [variable] [value]: subtracts the value from the variable
# MUL [variable] [value]: multiplies the variable by the value
# [location]:: names a line of code, so it can be jumped to from elsewhere
# JUMP [location]: jumps to the location specified
# IF [condition] JUMP [location]: if the condition is true, jump to the location specified
# END: finish execution

from string import whitespace, digits, ascii_uppercase

def operations(cmd, variable, value, mov_dict):
    #getting the last value of the varaible
    var_value =  int(mov_dict[variable][-1])

    #checking if the value passed is a digit or a variable, if it is a variable
    #the value will be used as a key to the mov_dict
    if value in digits:
        value = int(value)
    else: 
        value = int(mov_dict[value][-1])

    if cmd == "ADD":
        var_value += value
    elif cmd == "SUB":
        var_value -= value
    elif cmd == "MUL":
        var_value *= value
    return var_value

def if_condition(first_var, operator, second_var, location, mov_dict,program, cur_index):
    #getting the last value of the first variable
    fir_var = str(mov_dict[first_var][-1])

    #condition to check if the second variable that has been passed is a digit or a variable
    #if it is a variable, it will get the value on mov_dict
    if second_var.isdigit():
        sec_var = str(second_var)
    else:
        sec_var = str(mov_dict[second_var][-1])

    #combining the condition
    comb_condition = "".join(fir_var + operator + sec_var)
    #evaluate the string to make it an expression
    cond = eval(comb_condition) 
    
    if cond: #calls the jump func and returns the index
        index = jump_to(location,program)
        return index
    else: #if false, return the current index
        return cur_index 



def run(program:list):
    operators_list = ["ADD", "SUB", "MUL"] #creating a list for operators for easy access
    index = 0
    mov_dict = {}
    print_list = []

    #creating objects for each uppercase letter and add default value of 0
    for char in ascii_uppercase:
        if char not in mov_dict:
            mov_dict[char] = [0]

    #this is the loop to traverse the program
    while index < len(program):
        #splitting each part to access the command passed to the program
        parts = program[index].split(" ")
        #parts[0] is the default position of commands
        cmd = parts[0] 
        
        if cmd == "IF" :
            first_var = parts[1]
            operator = parts[2]
            second_var = parts[3]
            location = parts[5]+":"
            
            #this index will vary depends on the return value of if condition func, if false, it returns the current index
            index = if_condition(first_var,operator, second_var,location, mov_dict,program,index)

        elif cmd == "MOV":
            variable = parts[1]
            check_value = parts[2]

            #checking if the digit is a digit or not, so if the it is a digit, it is asked whether the value of dictionary has a default value of 0
            #if it has a default value, it will be pop so that the first value given by the user, will be the first in the list
            if check_value.isdigit():
                if mov_dict[variable][0] == 0:
                    mov_dict[variable].pop(0)
                mov_dict[variable].append(check_value)

            else:
                #if it is not a digit, we will use the check_value as a key to the dictionary, and gets the last item in the list
                value = mov_dict[check_value][-1]
                mov_dict[variable].append(value)
            

        elif cmd in operators_list:
            variable = parts[1]
            value = parts[2]
            if variable in mov_dict:
                #every time the operators are called, the value will be append to the mov_dict
                mov_dict[variable].append(operations(cmd, variable, value,mov_dict))

        elif cmd == "PRINT":
            variable = parts[1]
            #checking if the variable exist in the dictionary, else it is a digit
            if variable in mov_dict:
                print_list.append(printing(variable, mov_dict))
            elif variable.isdigit():
                print_list.append(int(variable))

        elif cmd == "JUMP":
            #the jump returns an index based on the position of the location in the variable
            location = parts[1]+":"
            index = jump_to(location,program) 

        elif cmd == "END":
            break     
               
        index += 1
    return print_list
    
def printing(variable, mov_dict):
    #getting the last value in the mov_dict using the key(variable)
    if variable in mov_dict:
        var = int(mov_dict[variable][-1])
        return var

def jump_to(location:str, program:list):
    #finding the index using the index func, then returning it
    index = program.index(location)
    return index 

if __name__ == "__main__":
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")

    #program2.append("MOV A 5")
    #program2.append("PRINT A")

    # program2.append("PRINT A")
    # program2.append("END")

    # program2.append("MOV A 10")
    # program2.append("PRINT A")
    # program2.append("MOV B A")
    # program2.append("SUB B 8")
    # program2.append("PRINT B")
    # program2.append("SUB A B")
    # program2.append("PRINT A")

    # program2.append("begin:")
    # program2.append("IF A >= B JUMP quit")

    # program2.append("PRINT B")
    # program2.append("ADD A 1")
    # program2.append("SUB B 1")
    # program2.append("JUMP begin")
    # program2.append("quit:")
    # program2.append("END")

    # program2.append("MOV A 1")
    # program2.append("MOV B 1")
    # program2.append("start:")
    # program2.append("MUL A 2")
    # program2.append("ADD B 1")
    # program2.append("IF B != 101 JUMP start")
    # program2.append("PRINT A")

    # program2.append("MOV A 1")
    # program2.append("PRINT 2")
    # program2.append("MOV B 999")
    # program2.append("start:")
    # program2.append("ADD A 1")
    # program2.append("SUB B 1")
    # program2.append("ADD C 1")
    # program2.append("IF A == B JUMP end")
    # program2.append("JUMP start")
    # program2.append("end:")
    # program2.append("PRINT C")

    
    # program2.append("MOV N 100")
    # program2.append("PRINT 2")
    # program2.append("MOV A 3")
    # program2.append("start:")
    # program2.append("MOV B 2")
    # program2.append("MOV Z 0")
    # program2.append("test:")
    # program2.append("MOV C B")
    # program2.append("new:")
    # program2.append("IF C == A JUMP virhe")
    # program2.append("IF C == A JUMP pass_by")
    # program2.append("ADD C B")
    # program2.append("JUMP new")
    # program2.append("virhe:")
    # program2.append("MOV Z 1")
    # program2.append("JUMP pass_by2")
    # program2.append("pass_by:")
    # program2.append("ADD B 1")
    # program2.append("IF B < A JUMP test")
    # program2.append("pass_by2:")
    # program2.append("IF Z == 1 JUMP pass_by3")
    # program2.append("PRINT A") 
    # program2.append("pass_by3:")
    # program2.append("ADD A 1")
    # program2.append("IF A <= N JUMP start")


    result = run(program2)
    print(result)



