

def countdown(n):
	while n > 0:
		yield "T-minus %d\n" % n
		n -= 1
	yield "Kaboom!\n"

count = countdown(5)

#out = "@".join(count)
#print out

for item in count:
	print item,

	