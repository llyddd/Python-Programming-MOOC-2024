# write your solution here
def spellchecker():
    word_list = []
    with open("wordlist.txt") as new_file:
        for line in new_file:
            values = line.strip()
            
            word_list.append(values)

    text = input("Write Text: ")
    converted_text = []
    converted_text = text.split()
    i = 0
    
    while i < len(converted_text):
        current_word = converted_text[i].lower()
        
        if current_word not in word_list:
            converted_text[i] = f"*{current_word}*"
                    
        i += 1
    joined_string = " ".join(converted_text)
    print(joined_string)
    
spellchecker()