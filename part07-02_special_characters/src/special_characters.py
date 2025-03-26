# Write your solution here

import string
def separate_characters(my_string: str):
    ascii_letters = ""
    punctuation = ""
    other = ""
    tpl = ()
    for char in my_string:
        if char in string.ascii_letters:
            ascii_letters+= char
      
        elif char in string.punctuation:
            punctuation += char
           
        else:
            other += char
          


    result = []
    result.append(ascii_letters)
    result.append(punctuation)
    result.append(other)
    tpl = tuple(result)

    return tpl

if __name__ == "__main__":
    #separate_characters("Olé!!! Hey, are ümläüts wörking?")
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    #parts = "Olé!!! Hey, are ümläüts wörking?"
    print(parts[0])
    print(parts[1])
    print(parts[2])