# In music, cadences act as punctuation in musical phrases, and help to mark the end of phrases. Cadences are the two
# chords at the end of a phrase. The different cadences are as follows:
#
# - V followed by I is a Perfect Cadence
# - IV followed by I is a Plagal Cadence
# - V followed by Any chord other than I is an Interrupted Cadence
# - Any chord followed by V is an Imperfect Cadence
#
# Create a function where given a chord progression as a list, return the type of cadence the phrase ends on.


def find_cadence(chords: list) -> str:
    chords = chords[::-1]
    last_chord = chords[0]
    following_chord = chords[1]
    if last_chord == "I":
        if following_chord == "V":
            cadence = "perfect"
        elif following_chord == "IV":
            cadence = "plagal"
        else:
            cadence = "no cadence"
    elif last_chord != "I" and following_chord == "V":
        cadence = "interrupted"
    elif last_chord == "V":
        cadence = "imperfect"
    else:
        cadence = "no cadence"
    return cadence


assert find_cadence(["I", "IV", "V"]) == "imperfect"
assert find_cadence(["ii", "V", "I"]) == "perfect"
assert find_cadence(["I", "IV", "I", "V", "vi"]) == "interrupted"
assert find_cadence(["I", "IV", "I", "V", "IV"]) == "interrupted"
assert find_cadence(["I", "III", "IV", "V"]) == "imperfect"
assert find_cadence(["I", "IV", "I"]) == "plagal"
assert find_cadence(["V", "IV", "I"]) == "plagal"
assert find_cadence(["V", "IV", "V", "I"]) == "perfect"
assert find_cadence(["V", "IV", "V", "I", "vi"]) == "no cadence"
assert find_cadence(["V", "IV", "V", "III", "vi"]) == "no cadence"

# finished 5/24