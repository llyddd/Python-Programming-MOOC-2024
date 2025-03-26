# Write your solution here

def no_shouting(list):
    storage = []
    for  i in list:
        is_it_upper = i.isupper()
        
        if is_it_upper:
            continue
        else:
            storage.append(i)
    return storage


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)