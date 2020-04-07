import sys


def generateKey(word):
    return ''.join(sorted(word.lower()))


def makeDictionary(array):
    dictionary = {}

    for word in array:
        key = generateKey(word)
        if key in dictionary.keys():
            dictionary[key].append(word.lower())
        else:
            dictionary[key] = []
            dictionary[key].append(word.lower())

    return dictionary


def groupAnagrams(words):
    anagramDictionary = makeDictionary(words)

    return [anagramDictionary[key] for key in anagramDictionary]


print(groupAnagrams(sys.argv[1:]))
