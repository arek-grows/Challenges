# class implementation of an array-based set

# Use your favorite object-oriented programming language to create a class that represents an array-based set. It
# should include functions/methods that serve as the key operations: Read, search, insert, and delete. Ensure that
# the insert operation will not insert duplicate values.


class ABset:
    def __init__(self):
        self.array_set = ["pikachu", "squirtle", "infernape", "houndoom", "rayquaza"]

    def read(self, index):
        return self.array_set[index]

    def search(self, item):
        i = 0
        for x in self.array_set:
            if x == item:
                return i
            i += 1
        return False

    def insert(self, item, index):
        i = len(self.array_set)
        self.array_set.append("dummy")
        for x in self.array_set[i-1:index-1:-1]:
            self.array_set[i] = x
            i -= 1
        self.array_set[index] = item

    def delete(self, index):
        return


test = ABset()
print(test.array_set)
print(str(test.search("infernape")))
print(str(test.search("arceus")))
test.insert("dhelmise", 1)
print(test.array_set)