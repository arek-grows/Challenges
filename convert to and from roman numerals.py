class RomanNumerals:

    def __init__(self):
        self.roman_number_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                                  10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        self.roman_symbol_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.subtract_number_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    def to_roman(self, val):
        """Converts and integer to a Roman numeral."""
        end_string = ""
        for num in self.roman_number_dict:

            if val < num:
                pass
            else:
                floored = val // num
                end_string += self.roman_number_dict[num] * floored
                val = val % num

            if val == 0:
                return end_string
        return "error"

    def from_roman(self, roman_num):
        """Converts a Roman numeral into an integer."""
        total = 0
        for sub_letter_combo in self.subtract_number_dict:
            if sub_letter_combo in roman_num:
                total += self.subtract_number_dict[sub_letter_combo]
                roman_num = roman_num.replace(sub_letter_combo, "")
        for letter in roman_num:
            total += self.roman_symbol_dict[letter]
        return total


if __name__ == "__main__":
    # tests
    rn = RomanNumerals()
    from_roman_test_dict = {"XLIII": 43, "CLXI": 161, "CCVI": 206, "CXXXII": 132, "CCCLII": 352, "CXIX": 119,
                            "CCCXCVII": 397, "VII": 7, "XXI": 21}

    to_roman_test_dict = {v: k for k, v in from_roman_test_dict.items()}

    print("from roman:")
    for test in from_roman_test_dict:
        print(rn.from_roman(test) == from_roman_test_dict[test])

    print("to roman:")
    for test in to_roman_test_dict:
        return_val = rn.to_roman(test)
        print(return_val == to_roman_test_dict[test])
