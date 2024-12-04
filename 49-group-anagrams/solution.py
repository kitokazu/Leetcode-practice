def groupAnagrams(input):
  # a word is a anagram if there exists the same number of characters in the string

  output = []
  anagrams = {}
  for word in input:
      temp = tuple(sorted(word))
      if temp in anagrams:
          anagrams[temp].append(word)
      else:
          anagrams[temp] = [word]
  
  return list(anagrams.values())

test_input = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(test_input)) # [["eat","tea","ate"],["tan","nat"],["bat"]]