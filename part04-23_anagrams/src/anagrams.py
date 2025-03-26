# Write your solution here
def anagrams(str1, str2):

    string1 = sorted(str1)
    string2 = sorted(str2)
    if string1 == string2:
        return True
    else:
        return False


if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) 