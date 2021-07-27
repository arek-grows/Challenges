# Create a function that takes a series of dice rolls from 1-6. Return the sum of the rolls with the following
# conditions:
#
# If it's a 1 the next counts as 0.
# If it's a 6 the next is multiplied by 2.


def calculate_score(*rolls):
    total_score = 0
    previous_roll = 0
    for roll in rolls:
        if previous_roll == 1:
            total_score += 0
        elif previous_roll == 6:
            total_score += roll * 2
        else:
            total_score += roll
        previous_roll = roll
    return total_score


if __name__ == "__main__":
    test_games = {
        (1, 2, 3): 4,
        (2, 6, 2, 5): 17,
        (6, 1, 1): 8,
        (5, 1, 6, 1, 6): 8,
        (1, 1, 1): 1,
        (1, 1, 3, 1, 1): 2,
        (1, 1, 1, 1, 1): 1,
        (6, 6, 6): 30
    }

    failed = 0
    for game, test_score in test_games.items():
        score = calculate_score(*game)
        if score != test_score:
            failed += 1
            print(f"FAILED: {game} should give score {test_score}, got {score}")

    print(f"---\nRan {len(test_games)} test games\nFailed {failed} games")

# CHALLENGE FINISHED 5/23
