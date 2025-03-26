# Write your solution here
def longest(strings :list):

    length_storage = []
    longest_storage = []
    i = 0
    o = 0
    
    while i < len(strings):
        length_storage.append (len(strings[i]))
        i+=1
    
    maximum = max(length_storage)
        
    while  o < len(strings):    
        if len(strings[o]) == maximum:
            longest_storage.append (strings[o])
        o +=1
    return (', '.join(longest_storage))
        


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))