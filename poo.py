# C:\Users\arkad\PycharmProjects
import os

parent_dir = "C:\\Users\\arkad\\PycharmProjects\\"

for x in range(1, 301, 20):
    directory = "Challenges %s-%s" % (x, x + 19)
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory %s created" % directory)