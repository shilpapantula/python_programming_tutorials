list_of_words = ['yerbu', 'buena', 'cali', 'roar', 'ubrey', 'ilac', 'raor']

def find_anagrams(list):

	words_sorted = {}
	for word in list:
		words_sorted[word] = ('').join(sorted(word))
	
	anagrams = []
	sorted_anagrams = []
	count_sorted = {}
	
	for key, val in words_sorted.items():
		if val in count_sorted:
			count_sorted[val] += 1
		else:
			count_sorted[val] = 1
	
	
	for word, count in count_sorted.items():
		if count > 1:
			sorted_anagrams.append(word)

	for key, value in words_sorted.items():
		if value in sorted_anagrams:
			anagrams.append(key)

	return anagrams

print find_anagrams(list_of_words)
