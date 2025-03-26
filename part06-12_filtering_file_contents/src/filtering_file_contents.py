# Write your solution here
def read():
    list = []
    with open("solutions.csv") as read_file:
        for line in read_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            solution = parts[1]
            result = parts[2]
            list.append([name, solution, result]) 
    return list

def correct(solution: list):
   
    with open("correct.csv", "w") as write_file:
         for item in solution:
            line = ""
            for value in item:
                line += f"{value};"
                
            line = line[:-1]
            
            write_file.write(line+"\n")


def incorrect(solution: list):
    with open("incorrect.csv", "w") as write_file:
         for item in solution:
            line = ""
            for value in item:
                line += f"{value};"
            line = line[:-1]
            
            write_file.write(line+"\n")
    
def filter_solutions():
    solution_list = read()
    correct_list = []
    incorrect_list = []
    for item in range(len(solution_list)):
        name, solution, result = solution_list[item]
        #temp = 
        for item in range(len(solution)):
            check = solution[item]
            if check == "-":
                first = int(solution[:item])
                second = int(solution[item+1:])
                solve = first - second
                if solve == int(result):
                    correct_list.append([name,solution,solve])
                    
                else:
                    incorrect_list.append([name,solution,result])

            elif check == "+":
                first = solution[:item]
                second = solution[item+1:]
                first = int(solution[:item])
                second = int(solution[item+1:])
                solve = first + second
                if solve == int(result):
                    correct_list.append([name,solution,solve])
                else:
                    incorrect_list.append([name,solution,result])
                    
    correct(correct_list)
    incorrect(incorrect_list)  



if __name__ == "__main__":
    filter_solutions()
    # filter_solutions()
    # filter_solutions()