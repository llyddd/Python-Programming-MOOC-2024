# Write your solution here
def list_sum(l1,l2):
    i = 0
    result = []
    while i < len(l1):
        result.append ( l1[i] + l2[i])
        i+=1
    return result

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))