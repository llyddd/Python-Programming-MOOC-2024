# Write your solution here
def dict_of_numbers():
    dictionary = {}
    numbers = []

    zero = ['zero']
    wordSingle = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    wordTeens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    wordTens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    for initialize in range(100): #counts from 0 to 99
        numbers.append(initialize)
    
    control = []
    
    for i in range(len(wordTens)): #it creates the hyphenated words
        control.append(wordTens[i])
        for j in range(len(wordSingle)):
            control.append(wordTens[i] + "-" + wordSingle[j])
    
    result_word = []
    result_word.append(zero[0]) #starts the list to 0

    for i in wordSingle: #single digit numbers
        result_word.append(i)
    for i in wordTeens: #teens numbers
        result_word.append(i)
    for i in control: #hyphenated words
        result_word.append(i)
    for i in range(len(numbers)): #it builds the words passed to the dictionary
        dictionary[numbers[i]] = result_word[i]
    return dictionary


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])