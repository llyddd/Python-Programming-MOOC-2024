# Write your solution here
from random import choice

def roll(die: str):

    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]

    if die == "A":
        result_A = choice(A)
        return result_A
    elif die == "B":
        result_B = choice(B)
        return result_B
    elif die == "C":
        result_C = choice(C)
        return result_C
        
    

def play(die1: str, die2: str, times: int):

    die1_result = 0
    die2_result = 0
    tie = 0
   
    for i in range(times):

        first_dice = roll(die1)
        second_dice = roll(die2)
        if first_dice > second_dice:
            die1_result += 1
        elif first_dice < second_dice:
            die2_result += 1
        elif first_dice == second_dice:
            tie += 1
    
    temp_list = []
    temp_list.append(die1_result)
    temp_list.append(die2_result)
    temp_list.append(tie)
    result = tuple(temp_list)

    return result
if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()

    result = play("A", "B", 100)
    print(result)
    result = play("B", "B", 10)
    print(result)
