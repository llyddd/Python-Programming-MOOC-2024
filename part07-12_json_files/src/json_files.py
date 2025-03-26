# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as read_file:
        
        data = read_file.read()

        extracted = json.loads(data)
        

        for items in extracted:
            name = items["name"]
            age = items["age"]
            hb = ""
            hobbies = str(items["hobbies"])
        
            i = 0
            parts = hobbies.replace("[", "").replace("]", "").replace("'", "")
            while i < len(parts):
                hb += parts[i]
                i += 1
            print(f"{name} {age} years ({hb})")


if __name__ == "__main__":
    print_persons("file4.json")
    