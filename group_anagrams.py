def group_anagrams(input):
    d = {}
    result = []
    for word in input:
        sorted_word = tuple(sorted(word))
        if d.get(sorted_word) is None:
            d[sorted_word] = [word]
        else:
            d[sorted_word].append(word)
    for l in d.values():
        result.append(l)
    return result

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input))