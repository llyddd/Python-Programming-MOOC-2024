# write your solution here

import difflib
import string 

def spellchecker():
    word_list = []
    with open("wordlist.txt") as new_file:
        for line in new_file:
            values = line.strip()
            
            word_list.append(values)

    text = input("Write Text: ")
    converted_text = []
    temp = []
    converted_text = text.split()
    i = 0
    
    while i < len(converted_text):
        current_word = converted_text[i].lower()
        
        if current_word not in word_list:
            converted_text[i] = f"*{current_word}*"
            temp.append(converted_text[i].strip("*"))
                    
        i += 1
    joined_string = " ".join(converted_text)

    print(f"{joined_string}")
    print("suggestions:")

    result_dict = {}
    matched_res = []
    for words in temp:

        result = difflib.get_close_matches(words,word_list)
        if words not in result_dict:
            result_dict[words] = []
     

        result_dict[words].append(result)

    

    for key, value in result_dict.items():
       
        result = f"{key}: {', '.join(value[0])}"
        
        print(result)

spellchecker()