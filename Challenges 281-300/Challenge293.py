import unittest


def countdown(start_at: int, say: str) -> str:
    say = say.upper() + "!"
    c_down = [str(x) for x in range(start_at, 0, -1)]
    c_down.append(say)
    return ". ".join(c_down)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            countdown(10, "Blast Off"), "10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BLAST OFF!"
        )

    def test_2(self):
        self.assertEqual(countdown(3, "go"), "3. 2. 1. GO!")

    def test_3(self):
        self.assertEqual(countdown(5, "FIRE"), "5. 4. 3. 2. 1. FIRE!")

    def test_4(self):
        self.assertEqual(
            countdown(12, "watch out"),
            "12. 11. 10. 9. 8. 7. 6. 5. 4. 3. 2. 1. WATCH OUT!",
        )

    def test_5(self):
        self.assertEqual(countdown(7, "fire"), "7. 6. 5. 4. 3. 2. 1. FIRE!")

    def test_6(self):
        self.assertEqual(
            countdown(16, "shoot"),
            "16. 15. 14. 13. 12. 11. 10. 9. 8. 7. 6. 5. 4. 3. 2. 1. SHOOT!",
        )

    def test_7(self):
        self.assertEqual(
            countdown(28, "fire"),
            "28. 27. 26. 25. 24. 23. 22. 21. 20. 19. 18. 17. 16. 15. 14. 13. 12. 11. 10. 9. 8. 7. 6. 5. 4. 3. 2. 1. FIRE!",
        )

    def test_8(self):
        self.assertEqual(
            countdown(14, "watch out"),
            "14. 13. 12. 11. 10. 9. 8. 7. 6. 5. 4. 3. 2. 1. WATCH OUT!",
        )

    def test_9(self):
        self.assertEqual(
            countdown(29, "take down"),
            "29. 28. 27. 26. 25. 24. 23. 22. 21. 20. 19. 18. 17. 16. 15. 14. 13. 12. 11. 10. 9. 8. 7. 6. 5. 4. 3. 2. 1. TAKE DOWN!",
        )

    def test_10(self):
        self.assertEqual(countdown(8, "boom"), "8. 7. 6. 5. 4. 3. 2. 1. BOOM!")


if __name__ == "__main__":
    unittest.main()