# Make a function that encrypts a given input with these steps:
#
# Input: "apple"
#
# Step 1: Reverse the input: "elppa"
#
# Step 2: Replace all vowels using the following chart:
#
# a => 0
# e => 1
# o => 2
# u => 3
#
#
# "1lpp0"
#
# Step 3: Add "aca" to the end of the word: "1lpp0aca"
#
# Output: "1lpp0aca"


def encrypt(message):
    vowel_map = {vowel: index for index, vowel in enumerate(["a", "e", "o", "u"])}
    message = reversed(message)
    emessage = ""
    for letter in message:
        if letter in vowel_map:
            letter = str(vowel_map[letter])
        emessage += letter
    emessage += "aca"
    return emessage


assert encrypt("banana") == "0n0n0baca"
assert encrypt("karaca") == "0c0r0kaca"
assert encrypt("burak") == "k0r3baca"
assert encrypt("alpaca") == "0c0pl0aca"
print("Encrypt Success")

# CHALLENGE COMPLETED 5/20


def decrypt(message):
    vowel_map = {vowel: index for index, vowel in enumerate(["a", "e", "o", "u"])}
    # replace the vowel map keys with their values and vice-versa
    vowel_map = {vowel: index for index, vowel in vowel_map.items()}
    emessage = ""
    message = message.rstrip("aca")
    message = message[::-1]

    for letter in message:
        if letter in str(list(vowel_map.keys())):
            letter = vowel_map[int(letter)]
        emessage += letter
    return emessage


assert decrypt("0n0n0baca") == "banana"
assert decrypt("0c0r0kaca") == "karaca"
assert decrypt("k0r3baca") == "burak"
assert decrypt("0c0pl0aca") == "alpaca"
print("Decrypt Success")

# CHALLENGE COMPLETED 5/21
