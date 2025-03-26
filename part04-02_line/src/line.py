# Write your solution here
def line(integer, string):
    if len(string) == 0:
        print(f"{integer * "*"}")
    elif len(string) > 0:
        word = string[0]
        print(integer * word )
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(8, "lol")