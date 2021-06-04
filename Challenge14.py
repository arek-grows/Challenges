# INCOMPLETE

# Write a function that divides a phrase into word buckets, with each bucket containing n or fewer characters. Only
# include full words inside each bucket. Examples
#
# split_into_buckets("she sells sea shells by the sea", 10)
# ➞ ["she sells", "sea shells", "by the sea"]
#
# split_into_buckets("the mouse jumped over the cheese", 7)
# ➞ ["the", "mouse", "jumped", "over", "the", "cheese"]
#
# split_into_buckets("fairy dust coated the air", 20)
# ➞ ["fairy dust coated", "the air"]
#
# split_into_buckets("a b c d e", 2)
# ➞ ["a", "b", "c", "d", "e"]
#
# Notes
#
# Spaces count as one character
# Trim beginning and ending spaces for each word bucket
# If buckets are too small to hold a single word, return an empty list: []
# The final goal isn't to return just the words with a length equal (or lower) to the given n, but to return the entire
# given phrase bucketized (if possible)
from typing import AnyStr, List


def split_into_buckets(phrase: AnyStr, bucket_size: int) -> List[AnyStr]:
    List = []
    # step is the end index plus one
    step = bucket_size
    # make these update every loop
    aword = ""
    current_end = step - 1
    current_beg = current_end - (bucket_size - 1)
    #
    if phrase[step] == " " or phrase[current_end] == " ":
        for character in phrase[current_beg:current_end]:
            aword += str(character)
        print(aword)
        List.append(aword.strip())
        if phrase[step] == " ":
            step += 1
        step += bucket_size
    else:
        i =

    return List


assert split_into_buckets("she sells sea shells by the sea", 2) == []
assert split_into_buckets("ab bc cd", 1) == []
assert split_into_buckets("she sells sea shells by the sea", 10) == ["she sells", "sea shells", "by the sea"]
assert split_into_buckets("the mouse jumped over the cheese", 7) == ["the", "mouse", "jumped", "over", "the", "cheese"]
assert split_into_buckets("fairy dust coated the air", 20) == ["fairy dust coated", "the air"]
assert split_into_buckets("do the hokey pokey", 6) == ["do the", "hokey", "pokey"]
assert split_into_buckets("do the hokey pokey", 12) == ["do the hokey", "pokey"]
assert split_into_buckets("rich magnificent trees dotted the landscape", 12) == ["rich", "magnificent", "trees dotted", "the", "landscape"]
assert split_into_buckets("rich magnificent trees dotted the landscape", 15) == ["rich", "magnificent", "trees dotted", "the landscape"]
assert split_into_buckets("rich magnificent trees dotted the landscape", 18) == ["rich magnificent", "trees dotted the", "landscape"]
assert split_into_buckets("rich magnificent trees dotted the landscape", 22) == ["rich magnificent trees", "dotted the landscape"]
assert split_into_buckets("rich magnificent trees dotted the landscape", 40) == ["rich magnificent trees dotted the", "landscape"]
assert split_into_buckets("rich magnificent trees dotted the landscape", 43) == ["rich magnificent trees dotted the landscape"]
assert split_into_buckets("beep bo bee bop bee bo bo bop", 6) == ["beep", "bo bee", "bop", "bee bo", "bo bop"]
assert split_into_buckets("beep bo bee bop bee bo bo bop", 10) == ["beep bo", "bee bop", "bee bo bo", "bop"]
assert split_into_buckets("a b c d e", 3) == ["a b", "c d", "e"]
assert split_into_buckets("a b c d e", 2) == ["a", "b", "c", "d", "e"]
assert split_into_buckets("a b c d e", 1) == ["a", "b", "c", "d", "e"]
print("Successfully Passed All Tests For Challenge #14 - Word Buckets")