import collections
str1=["eat","tea","tan","ate","nat","bat"]
anagram=collections.defaultdict(list)
for a in str1:
    anagram[''.join(sorted(a))].append(a)  
print(anagram.values())

def groupAnagrams(strs:[str])->[[str]]:
    anagrams=collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

print(groupAnagrams(str1))