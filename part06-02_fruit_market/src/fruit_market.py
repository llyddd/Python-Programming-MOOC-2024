# write your solution here
def read_fruits():
    fruits = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
           
            name = parts[0]
            print(parts)
            price = float(parts[1])
            fruits[name] = price
            

        #return fruits
        

if __name__ == "__main__": 
    read_fruits()