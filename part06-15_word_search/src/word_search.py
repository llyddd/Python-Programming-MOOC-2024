# Write your solution here
def access_dictionary():
    dictionary = []
    with open("words.txt") as read_file:
        for words in read_file:
            values = words.strip()
            dictionary.append(values)
    return dictionary

def find_words(search_term: str):
    dictionary = []
    dictionary = access_dictionary()
    result = []

    #Process
    pos = char_pos(search_term)
    left_wc = search_term[0:len(search_term)-1] #Getting the value for left asterisk wildcard
    right_wc = search_term[1:len(search_term)] #Getting the value for right asterisk wildcard

   

    for words in dictionary:
        if  "*" not in search_term and "." not in search_term:
            if words == search_term: #For no wildcards, return the original term
                result.append(pos[0])
                return result
        if "." in search_term:
            if search_term.endswith("."): #For one dot in end, and one inside
                if words.startswith(search_term[pos[0]], pos[0]) and words.startswith(search_term[pos[1]], pos[1])  and len(words) == len(search_term):
                    result.append(words)   
            elif search_term.endswith(".") == False: #For inside dots ex. a...e
                if words.startswith(search_term[pos[0]]) and words.endswith(search_term[pos[1]]) and len(words) == len(search_term):
                    result.append(words)
            else: #Had wildcards but no result
                return result
            
        elif "*" in search_term: 
            if pos[0] > 0: #For left asterisk wildcard
                if words.startswith(left_wc):
                    result.append(words)
            elif pos[0] == 0:
                if words.endswith(right_wc): #For right asterisk wildcard
                    result.append(words)
            else: #Had wildcard but no result
                return result
            
    return result

def char_pos(search_term): #getting the position for each character that has wildcards
   
    positions = []
    i = 0

    while i < len(search_term):
        
        if "." in search_term:
            if search_term[i] != ".":
                positions.append(i)
            i += 1
        elif "*" in search_term:
            wc = search_term.find("*")
            positions.append(wc)  
            i += 1
        else: 
            positions.append(search_term)
            i+=1
    return positions

if __name__ == "__main__":
    print(find_words("ca."))
    print(find_words("c.b."))
    print(find_words("a...e"))
    print(find_words("ca*"))
    print(find_words("cat"))
    
