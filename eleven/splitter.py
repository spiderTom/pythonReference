
def split(line, types=None, delimiter=None):
	"""Splits a line of text and optionally performs type conversion
		...
	"""
	fields = line.split(delimiter)
	if types:
		fields = [ty(val) for ty, val in zip(types, fields)]
	return fields