# Write your solution here
from string import ascii_letters,ascii_uppercase, ascii_lowercase,punctuation,printable, whitespace, digits


def change_case(orig_string: str):
    result = ""
    for char in orig_string:
        if char in ascii_lowercase:
            result += char.upper()
        elif char in ascii_uppercase:
            result += char.lower()
        elif char in whitespace:
            result += char
    #print(result)
    return result
def split_in_half(orig_string: str):
    length = len(orig_string) // 2

    first = orig_string[:length]
    second = orig_string [length:]

    #print(first)
    #print(second)

    return tuple((first, second))
def remove_special_characters(orig_string: str):
    result = ""
    for char in orig_string:
        
        if char in ascii_letters and char not in punctuation or char in whitespace or char in digits:
            result += char
    
            
        

    #print(result)
    return result
if __name__ == "__main__":
    change_case("two different words")
    remove_special_characters("Thi§ is a test: test?")
    split_in_half("tee")