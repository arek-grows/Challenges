from typing import Callable
import unittest


def kelvin_to_fahrenheit(decorating: Callable[[], int]) -> Callable[[], int]:
    return  # Put your code here!!!


class Test(unittest.TestCase):
    def tests_1_to_10_thousand(self):
        failures = 0
        printed = 0
        for k in range(0, 10_000):
            @kelvin_to_fahrenheit
            def source():
                return k

            f = int((k-273.15) * 9/5 + 32)
            ret = source()
            if f != ret:
                if printed < 100:
                    printed += 1
                    print(f"{k}K converted to F is {f}, got {ret}")
                failures += 1
        print(f"Failed {failures} times")


if __name__ == "__main__":
    unittest.main()