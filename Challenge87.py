from typing import List
import unittest


def last_name_lensort(names: List[str]) -> List[str]:
    last_lengths = []  # [ [length of last name, first name, last name], [...] ]
    for name in names:
        name = name.split()
        last_lengths.append([len(name[1])] + name)
    last_lengths.sort()

    end_list = []
    c_length = last_lengths[0][0]
    c_names = []
    for n in last_lengths:
        if n[0] != c_length:
            c_names.sort(key=lambda x: x[1])
            for name in c_names:
                end_list.append(" ".join(name))

            c_names = []
            c_length = n[0]
        c_names.append([n[1], n[2]])

    c_names.sort(key=lambda x: x[1])  # last loop that above written loop can't(?) process
    for name in c_names:
        end_list.append(" ".join(name))

    return end_list  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEquals(
            [
                "Heather Mcgee",
                "Nicole Yoder",
                "Melissa Hoffman",
                "Jennifer Figueroa",
                "Amanda Schwartz",
            ],
            last_name_lensort(
                [
                    "Jennifer Figueroa",
                    "Heather Mcgee",
                    "Amanda Schwartz",
                    "Nicole Yoder",
                    "Melissa Hoffman",
                ]
            ),
        )

    def test_2(self):
        self.assertEquals(
            [
                "Edward Elric",
                "Rintaro Okabe",
                "Kurisu Makise",
                "Light Yagami",
                "Hitagi Senjougahara",
            ],
            last_name_lensort(
                [
                    "Hitagi Senjougahara",
                    "Edward Elric",
                    "Light Yagami",
                    "Rintaro Okabe",
                    "Kurisu Makise",
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()