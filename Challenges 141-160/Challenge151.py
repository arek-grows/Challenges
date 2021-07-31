from __future__ import annotations
import unittest


Products = dict[str, float]
SalesDetails = dict[str, Products]
SalesCommissions = dict[str, float]


def calculate_commissions(revenue: SalesDetails, expenses: SalesDetails) -> SalesCommissions:
    commissions = {}
    for person in revenue:
        commissions[person] = 0
        for rev in revenue[person]:
            if revenue[person][rev] - expenses[person][rev] > 0:
                commissions[person] += (revenue[person][rev] - expenses[person][rev]) * 0.062
    for person in commissions:
        commissions[person] = round(commissions[person], 2)
    return commissions  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            {
                "Frank": 6.2,
                "Jane": 9.49
            },
            calculate_commissions(
                {  # Revenue
                    "Frank": {
                        "Tea": 120,
                        "Coffee": 243,
                    },
                    "Jane": {
                        "Tea": 145,
                        "Coffee": 265,
                    }
                },
                {  # Expenses
                    "Frank": {
                        "Tea": 130,
                        "Coffee": 143,
                    },
                    "Jane": {
                        "Tea": 59,
                        "Coffee": 198
                    }
                }
            )
        )

    def test_2(self):
        self.assertEqual(
            {
                "Johnver": 92.32,
                "Vanston": 5.21,
                "Danbree": 113.21,
                "Vansey": 45.45,
                "Mundyke": 32.55,
            },
            calculate_commissions(
                {
                    "Johnver": {
                        "Tea": 190,
                        "Coffee": 325,
                        "Water": 682,
                        "Milk": 829,
                    },
                    "Vanston": {
                        "Tea": 140,
                        "Coffee": 19,
                        "Water": 14,
                        "Milk": 140,
                    },
                    "Danbree": {
                        "Tea": 1926,
                        "Coffee": 293,
                        "Water": 852,
                        "Milk": 609,
                    },
                    "Vansey": {
                        "Tea": 14,
                        "Coffee": 1491,
                        "Water": 56,
                        "Milk": 120,
                    },
                    "Mundyke": {
                        "Tea": 143,
                        "Coffee": 162,
                        "Water": 659,
                        "Milk": 87,
                    }
                },
                {
                    "Johnver": {
                        "Tea": 120,
                        "Coffee": 300,
                        "Water": 50,
                        "Milk": 67,
                    },
                    "Vanston": {
                        "Tea": 65,
                        "Coffee": 10,
                        "Water": 299,
                        "Milk": 254,
                    },
                    "Danbree": {
                        "Tea": 890,
                        "Coffee": 23,
                        "Water": 1290,
                        "Milk": 89,
                    },
                    "Vansey": {
                        "Tea": 54,
                        "Coffee": 802,
                        "Water": 12,
                        "Milk": 129,
                    },
                    "Mundyke": {
                        "Tea": 430,
                        "Coffee": 235,
                        "Water": 145,
                        "Milk": 76,
                    }
                }
            )
        )


if __name__ == "__main__":
    unittest.main()