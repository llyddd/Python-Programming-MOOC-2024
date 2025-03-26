# Write your solution here
from random import randint
from random import shuffle


def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper))
    shuffle(number_pool)
    weekly_draw = number_pool[0:amount]
    sort = sorted(weekly_draw)
    return sort

if __name__ == "__main__":
    for number in lottery_numbers(3,2,22):
        print(number)   
    