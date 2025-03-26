# Write your solution here
def main():
    sign = input("Whom should I sign this to: ")
    save = input("Where shall I save it: ")
    
    with open(save, "w") as new_file:
        new_file.write(f"Hi {sign}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
        
    with open(save) as open_file:  
        for line in open_file:
            #line.split()
            print(line)
        
main()