# This challenge is an English twist on the Japanese word game Shiritori. The basic premise is to follow two rules:
#
#     The first character of the next word must match last character of the current word.
#     The word must not have already been said.
#
# For example
#
# ["word", "dowry", "yodel", "leader", "righteous", "serpent"]  #valid!
#
# ["motive", "beach"]  # invalid! - beach should start with "e"
#
# ["hive", "eh", "hive"]  # invalid! - "hive" has already been said
#
# Write a Shiritori class that has two instance variables:
#
#     words: a list of words already said
#     game_over: a boolean that is True if the game is over
#
# and two instance methods:
#
# play: a method that takes in a word as an argument and checks if it is valid (the word should follow rules #1 and
# #2 above).
#   If it is valid, it adds the word to the words list, and returns the words list.
#   If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to True.
# restart: a method that sets the words list to an empty one [] and sets the game_over boolean to False. It should
# return "game restarted".


class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if len(self.words) == 0:
            self.words.append(word)
        else:
            last_letter = self.words[len(self.words)-1][::-1][0]
            first_letter = word[0]
            if last_letter == first_letter and word not in self.words:
                self.words.append(word)
            else:
                self.game_over = True
                return "game over"
        return self.words

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"


my_shiritori = Shiritori()

assert my_shiritori.game_over == False
assert my_shiritori.play("apple") == ["apple"]
assert my_shiritori.words == ["apple"]
assert my_shiritori.play("ear") == ["apple", "ear"]
assert my_shiritori.play("rhino") == ["apple", "ear", "rhino"]
assert my_shiritori.play("ocelot") == ["apple", "ear", "rhino", "ocelot"]
assert my_shiritori.game_over is False
assert my_shiritori.play("oops") == "game over"
assert my_shiritori.game_over is True
assert my_shiritori.words == ["apple", "ear", "rhino", "ocelot"]

assert my_shiritori.restart() == "game restarted"
assert my_shiritori.words == []
assert my_shiritori.game_over is False
assert my_shiritori.play("hostess") == ["hostess"]
assert my_shiritori.game_over is False
assert my_shiritori.play("stash") == ["hostess", "stash"]
assert my_shiritori.play("hostess") == "game over"
assert my_shiritori.words == ["hostess", "stash"]

print("Success!")

# completed 6/9
