# Write your solution here
from random import choice

def access_words():
    list_words = []
    with open("words.txt") as read_file:
        for words in read_file:
            values = words.strip()
            list_words.append(values)
    return list_words

def words(n: int, beginning: str):
    result = []
    db_words = access_words()
    temp = []
   
 
    while len(result) < n:
        
        words = choice(db_words)
        temp.append(words)
        if words.startswith(beginning) and words not in result and len(result) < n:
            result.append(words)
        if len(temp) == len(db_words):
                if len(result) != n:
                    raise ValueError        

    return result
   
if __name__ == "__main__":
    word_list = words(2, "car")
    for word in word_list:
        print(word)