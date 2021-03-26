# piglatin.py


def firstvowelindex(word):
    i = 0
    while word[i] not in "aeiouy":
        i += 1
    return i


def piglatin(word):
    i = firstvowelindex(word)
    # print("value of i is: ", i)
    if i == 0:
        return word[i + 1 :] + word[: i + 1] + "ay"
    return word[i:] + word[:i] + "ay"


def main():
    w = input("Enter a word: ")
    print("In Pig Latin, that word is: ", piglatin(w))


main()
