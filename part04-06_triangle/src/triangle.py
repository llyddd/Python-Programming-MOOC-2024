# Copy here code of line function from previous exercise
def line(integer, string):
    if len(string) == 0:
        print(f"{integer * "*"}")
    elif len(string) > 0:
        word = string[0]
        print(integer * word )

def triangle(size):
    # You should call function line here with proper parameters
    i = 0
    while i <= size: 
        line(i, "#")
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
