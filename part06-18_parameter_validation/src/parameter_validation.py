# Write your solution here
def new_person(name: str, age: int):
    storage = ()
    if name == "" or  " " not in name or len(name) > 40 or age < 0 or age > 150:
        raise ValueError
    else:
        storage = name, age
        
    return storage

if __name__ == "__main__":
    result = new_person("kuya kuya", 25)
    print(result)