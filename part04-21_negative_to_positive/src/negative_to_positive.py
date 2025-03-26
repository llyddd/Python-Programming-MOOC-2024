# Write your solution here
num = int(input("Please type in a postiive integer: "))

for i in range(-num, num+1):
    if i == 0:
        continue
    else:
        print(i)