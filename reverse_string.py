string = 'anomaly'

def reverse_string(string):
	"""
	reverses a string and returns it
	"""
	if len(string) < 1:
		return []
	length = len(string)
	new_str = ''
	for l in range(length):
		new_str += string[length-l-1]

	return new_str

print reverse_string(string)
