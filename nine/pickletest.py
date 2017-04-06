import pickle

class Fruits:
	pass


#f = open("1.txt", 'rb')
#for item in f:
#	print item,

#f.close()
banana = Fruits()
banana.color = 'yellow'
banana.value = 30

filehandler = open("1.txt", "wb")
pickle.dump(banana, filehandler)
filehandler.close()
print banana.color, banana.value



