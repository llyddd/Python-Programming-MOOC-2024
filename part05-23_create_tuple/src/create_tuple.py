# Write your solution here
def create_tuple(x: int, y: int, z: int):

    
    smallest = min(x,y,z)
    greatest = max(x,y,z)
    total = x + y + z
    tpl = (smallest, greatest, total)
    return tpl



if __name__ == "__main__":
    print(create_tuple(5, 3, -1))