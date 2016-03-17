a = [2, 5, 8]
b = [-10, -1,  5]

def merge_by_sorting(a,b):
	
	if len(a) < 1:
		return b
	elif len(b) < 1:
		return a
	elif len(a) < 1 and len(b) <1:
		return []


	sorted = []
	
	i = 0
	j = 0
	
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			sorted.append(a[i])
			i += 1
		else:
			sorted.append(b[j])
			j += 1

	if i < len(a):
		sorted += a[i:]
	elif j < len(b):
		sorted += b[j:]

	return sorted

print 'a:'
print a
print 'b:'
print b
print(merge_by_sorting(a,b))
