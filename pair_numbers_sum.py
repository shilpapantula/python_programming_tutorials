# find pairs of numbers adding up to 0 from given list of unique numbers
def find_pairs(list):

	if len(list) < 2:
		return []
	pairs = []
	for i in list:
		if -1*i in list and list.index(i) < list.index(-1*i):
			pairs.append((i, -1*i))

	return pairs


if __name__ == '__main__':
	list = [-7, 9, 4, 5, -4, 2, 3, 0, 7]
	print find_pairs(list)
