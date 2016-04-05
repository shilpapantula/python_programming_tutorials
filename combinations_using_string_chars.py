"""
This script prints all combinations of chars in a given string
example: 
input: 'ab'
output: ['', 'a', 'b', 'ab', 'ba']
"""

def combinations(string):

    string_length = len(string)

    if string_length <= 1:
        return set(['', string])

    list_combinations = set()

    for i in range(string_length):
        combs = combinations(string[:i]+string[i+1::])
        for c in combs:
            list_combinations.add(''.join(sorted(c)))
            list_combinations.add(''.join(sorted(c+string[i])))

    return list_combinations

from nose.tools import assert_equal

def test(function):

    assert_equal(function(''), set(['']))
    assert_equal(function('a'), set(['', 'a']))
    assert_equal(function('ab'), set(['', 'a', 'b', 'ab']))

def main():

    test(combinations)
    string = raw_input('Enter a string: ')
    print combinations(string)

if __name__ == '__main__':
    main()

