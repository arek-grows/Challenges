from __future__ import annotations
import unittest


def find_it(stolen_items: dict[str, int], pets_name: str) -> str:
    if pets_name in stolen_items:
        return "%s is gone..." % pets_name.capitalize()
    return "%s is here!" % pets_name.capitalize()  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_it({}, "rambo"), "Rambo is here!")

    def test_2(self):
        self.assertEqual(find_it({}, "heman"), "Heman is here!")

    def test_3(self):
        self.assertEqual(
            find_it(
                {
                    "tv": 30,
                    "stereo": 50,
                },
                "rocky",
            ),
            "Rocky is here!",
        )

    def test_4(self):
        self.assertEqual(
            find_it(
                {
                    "tv": 30,
                    "stereo": 50,
                },
                "spiderman",
            ),
            "Spiderman is here!",
        )

    def test_5(self):
        self.assertEqual(
            find_it(
                {
                    "tv": 30,
                    "stereo": 50,
                    "julius": 100,
                },
                "julius",
            ),
            "Julius is gone...",
        )

    def test_6(self):
        self.assertEqual(
            find_it(
                {
                    "tv": 30,
                    "stereo": 50,
                    "batman": 200,
                },
                "batman",
            ),
            "Batman is gone...",
        )


if __name__ == "__main__":
    unittest.main()