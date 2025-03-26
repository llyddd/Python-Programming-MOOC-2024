# Write your solution here

while True:
    string = input("Editor: ")
    if "visual studio code" == string.lower():
        print("an excellent choice!")
        break
    elif "notepad" == string.lower() or "word" == string.lower():
        print("awful")
    else:
        print("not good")