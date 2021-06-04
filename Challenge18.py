##  COMPLETED

# @Challenges  #18 - Stretched Words
#
# Write a function that takes a string, and returns a new string with any duplicate consecutive letters removed.
#
# Examples
# unstretch("ppoeemm") ➞ "poem"
#
# unstretch("wiiiinnnnd") ➞ "wind"
#
# unstretch("ttiiitllleeee") ➞ "title"
#
# unstretch("cccccaaarrrbbonnnnn") ➞ "carbon"
#
# Notes
#
# Final strings won't include words with double letters (e.g. "passing", "lottery").

from typing import AnyStr


def unstretch(word: AnyStr) -> AnyStr:
    lookingLetter = ""
    unstretched = ""
    for letter in word:
        if lookingLetter != letter:
            unstretched = unstretched + letter
            lookingLetter = letter
    return unstretched


assert unstretch('llossttttt') == 'lost'
assert unstretch('cccccaaaaannnnne') == 'cane'
assert unstretch('hhoooneestttt') == 'honest'
assert unstretch('ppppooowwddddeeerrrr') == 'powder'
assert unstretch('eexxpppppeeccctt') == 'expect'
assert unstretch('rrrrepooooorrttt') == 'report'
assert unstretch('pppaaaaattteeeennnntt') == 'patent'
assert unstretch('mmmeeemoooryy') == 'memory'
assert unstretch('vvvvviiiiisssuuaaalll') == 'visual'
assert unstretch('eeeennnnsuuurrre') == 'ensure'
assert unstretch('iiinncclludddddeee') == 'include'
assert unstretch('ttteestiffffyyy') == 'testify'
assert unstretch('ggrrrrraaaaavvvvviiitttyyyy') == 'gravity'
assert unstretch('cccuuuultttttuuuuurreee') == 'culture'
assert unstretch('qquaalliiifffyy') == 'qualify'
assert unstretch('iiinnccoooonnnnnggggrrrrruuuuooouuuuusss') == 'incongruous'
# Find more code tests on GitHub
print("You've successfully unstretched all the words! Challenge 18 Successfully Completed!")