from __future__ import annotations
import unittest


def fiscal_code(person: dict[str, str]) -> str:
    f_code = ''
    name, surname, gender, dob = person["name"].upper(), person["surname"].upper(), person["gender"], person["dob"].split('/')
    dob_day, dob_month, dob_year = dob[0], dob[1], dob[2]
    month_conversion = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
                        "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T"}

    vowels = ['A', 'E', 'I', 'O', 'U']

    if len(surname) < 3:
        f_code += surname + ('X' * (3 - len(surname)))
    else:
        unvoweled = ''
        ordered_vowels = ''
        for x in surname:
            if x in vowels:
                ordered_vowels += x
            else:
                unvoweled += x
        if len(unvoweled) >= 3:
            f_code += unvoweled[:3]
        else:
            f_code += unvoweled + ordered_vowels[:len(unvoweled) * -1 + 3]

    n_consonants = ''
    n_vowels = ''
    for x in name:
        if x in vowels:
            n_vowels += x
        else:
            n_consonants += x
    if len(name) < 3:
        f_code += n_consonants + n_vowels + ('X' * (3 - len(n_consonants) - len(n_vowels)))
    elif len(n_consonants) == 3:
        f_code += n_consonants
    elif len(n_consonants) > 3:
        f_code += n_consonants[0] + n_consonants[2:4]
    else:
        f_code += n_consonants + n_vowels[:len(n_consonants) * -1 + 3]

    if gender == 'M' and len(dob_day) == 1:
        dob_day = '0' + dob_day
    elif gender == 'F':
        dob_day = str(int(dob_day) + 40)
    f_code += dob_year[2:] + month_conversion[dob_month] + dob_day
    return f_code  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            fiscal_code(
                {
                    "name": "Brendan",
                    "surname": "Eich",
                    "gender": "M",
                    "dob": "1/12/1961",
                }
            ),
            "CHEBND61T01",
        )

    def test_2(self):
        self.assertEqual(
            fiscal_code(
                {"name": "Helen", "surname": "Yu", "gender": "F", "dob": "1/12/1950"}
            ),
            "YUXHLN50T41",
        )

    def test_3(self):
        self.assertEqual(
            fiscal_code(
                {"name": "Al", "surname": "Capone", "gender": "M", "dob": "17/1/1899"}
            ),
            "CPNLAX99A17",
        )

    def test_4(self):
        self.assertEqual(
            fiscal_code(
                {
                    "name": "Mickey",
                    "surname": "Mouse",
                    "gender": "M",
                    "dob": "16/1/1928",
                }
            ),
            "MSOMKY28A16",
        )

    def test_5(self):
        self.assertEqual(
            fiscal_code(
                {"name": "Marie", "surname": "Curie", "gender": "F", "dob": "7/11/1867"}
            ),
            "CRUMRA67S47",
        )


if __name__ == "__main__":
    unittest.main()