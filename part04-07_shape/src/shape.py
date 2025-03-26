# Copy here code of line function from previous exercise and use it in your solution
def line(integer, string):
    if len(string) == 0:
        print(f"{integer * "*"}")
    elif len(string) > 0:
        word = string[0]
        print(integer * word )

def shape(width, string1, height, string2):
    i = 0
    o = 1
    while i <= width:
        line(i, string1)
        i += 1
    while o <= height:
         line(width, string2)
         o += 1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")