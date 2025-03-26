# Write your solution here
def greatest_number(a,b,c):
    if a > b > c or a > b < c:
        return a  
    elif a < b > c or a > c < b:
        return b
    elif c > b > a or c > a < b:
        return c
    elif a == b == c:
        return a
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(4, 5, 8)
    print(greatest)