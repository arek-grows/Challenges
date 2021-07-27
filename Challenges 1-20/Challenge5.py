# Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True
# otherwise.


def no_duplicate_letters(phrase):
    words = phrase.split(" ")
    for word in words:
        for letter in word[1:]:
            if word.count(letter) > 1:
                return False
    return True


if __name__ == "__main__":
    tests = {
        "Easy does it.": True,
        "So far, so good.": False,
        "Better late than never.": False,
        "Beat around the bush.": True,
        "Give them the benefit of the doubt.": False,
        "Your guess is as good as mine.": False,
        "Make a long story short.": True,
        "Go back to the drawing board.": True,
        "Wrap your head around something.": True,
        "Get your act together.": False,
        "To make matters worse.": False,
        "No pain, no gain.": True,
        "We'll cross that bridge when we come to it.": False,
        "Call it a day.": False,
        "It's not rocket science.": False,
        "A blessing in disguise.": False,
        "Get out of hand.": True,
        "A dime a dozen.": True,
        "Time flies when you're having fun.": True,
        "The best of both worlds.": True,
        "Speak of the devil.": True,
        "You can say that again.": False,
    }

    failed = 0
    for test_phrase, test_result in tests.items():
        result = no_duplicate_letters(test_phrase)
        if result is not test_result:
            failed += 1
            print(f"FAILED: {repr(test_phrase)}")

    print(f"---\n{failed} TESTS FAILED")

# completed 5/28
