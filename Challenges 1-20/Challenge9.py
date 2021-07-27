# Create a function that takes a string and censors words over four characters with *.
#
# Notes
#
# Don't censor words with exactly four characters.
# If all words have four characters or less, return the original string.
# The amount of * is the same as the length of the word.


def censor(sentence):
    words = sentence.split(" ")
    censored = ''
    i = 1
    for word in words:
        if len(word) > 4:
            word = "*" * len(word)
        if i == len(words):
            censored += word
            return censored
        else:
            censored += "%s " % word
        i += 1


assert censor("The code is fourty") == "The code is ******"
assert censor("Two plus three is five") == "Two plus ***** is five"
assert censor("aaaa aaaaa 1234 12345") == "aaaa ***** 1234 *****"
assert censor("abcdefghijklmnop") == "****************"
assert censor("a") == "a"
