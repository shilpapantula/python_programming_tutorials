def fibonacci(n):
	
	a = 0
	b = 1
	if n == 1:
		return a
	elif n == 2:
		return b
	
	return fibonacci(n-1) + fibonacci(n-2)
	

if __name__ == '__main__':
	import sys
	n = int(sys.argv[1])
	print fibonacci(n)
