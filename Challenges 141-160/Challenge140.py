from __future__ import annotations
import unittest


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def compare_age(self, other_person: Person) -> str:
        compared = "the same age as"
        if other_person.age > self.age:
            compared = "older than"
        elif other_person.age < self.age:
            compared = "younger than"
        return "%s is %s me." % (other_person.name, compared)


p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("Joel is older than me.", p1.compare_age(p2))

    def test_2(self):
        self.assertEqual("Lily is the same age as me.", p1.compare_age(p3))

    def test_3(self):
        self.assertEqual("Samuel is younger than me.", p2.compare_age(p1))

    def test_4(self):
        self.assertEqual("Lily is younger than me.", p2.compare_age(p3))

    def test_5(self):
        self.assertEqual("Samuel is the same age as me.", p3.compare_age(p1))

    def test_6(self):
        self.assertEqual("Joel is older than me.", p3.compare_age(p2))


if __name__ == "__main__":
    unittest.main()