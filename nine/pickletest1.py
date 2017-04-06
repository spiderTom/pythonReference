import pickle

class Fruits:
	pass


file = open("1.txt", "rb")
object_file = pickle.load(file)
file.close()

print object_file.color, object_file.value



