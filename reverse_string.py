def reverse_string(string):
	"""
	reverses a string and returns it
	"""
	if len(string) < 1:
		return ''
	length = len(string)
	new_str = ''
	for l in range(length):
		new_str += string[length-l-1]

	return new_str

from nose.tools import assert_equal

class testing(object):
	
	def test(self, function):
		assert_equal(function('anomaly'), 'ylamona')
		assert_equal(function('hello world'), 'dlrow olleh')
		assert_equal(function('i'), 'i')
		assert_equal(function(''), '')

def main():
	test = testing()
	test.test(reverse_string)	
	string = raw_input('Enter a non empty string: ')
	print reverse_string(string)

if __name__ == '__main__':
	main()
