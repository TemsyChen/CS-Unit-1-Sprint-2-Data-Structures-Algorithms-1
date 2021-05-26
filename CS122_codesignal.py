'''
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another 
character while preserving the order of characters. 
No two characters may map to the same character but a 
character may map to itself.

Understand:
a = "odd", b = "egg" --> true
a = "foo", b = "bar" --> false
a = "abca", b = "zbxz" --> true
a = "abc", b = "" --> false

Plan:
Create a dictionary. Map the corresponding characters to each other. If a key is already assigned to a value, and there is a new key value pair, return false.

Runtime: O(n)
Space: O(n)
'''

def csIsomorphicStrings(a, b):
    if len(a) == len(b):
        pass
    else:
        return False
        
    dict_ = {}
    for i in range(len(a)):
        if a[i] not in dict_:
            dict_[a[i]] = b[i]
        else:
            if dict_[a[i]] == b[i]:
                pass
            else:
                return False
    return True

'''
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one 
correspondence between a letter in pattern and a non-empty word in a.

Understand:
"abba", "lambda school school lambda" --> true
"abba", "lambda school school coding" --> false
"aaaa", "lambda school school lambda" --> false
"abba", "lambda lambda lambda lambda" --> false

Plan:
Split a into a list of words. Hash and store each letter of the pattern to the word in the string. If it exists already and the values don't match, return false.

Runtime: O(n)
Space: O(n)
'''

def csWordPattern(pattern, a):
    a_tokens = a.split()
    
    if len(a_tokens) != len(pattern):
        return False
    else:
        pass
    
    dict_ = {}
    for i in range(len(pattern)):
        if pattern[i] not in dict_ and a_tokens[i] not in dict_.values():
            dict_[pattern[i]] = a_tokens[i]
        elif pattern[i] in dict_ and dict_[pattern[i]] != a_tokens[i]:
            return False
        elif pattern[i] not in dict_ and a_tokens[i] in dict_.values():
            return False 
    return True

'''
Given an array of strings strs, write a function 
that can group the anagrams. The groups should be
ordered such that the larger groups come first, 
with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging 
the letters of a different word or phrase, typically 
using all the original letters exactly once.

Understand:
["apt","pat","ear","tap","are","arm"] --> 
[["apt","pat","tap"],["ear","are"],["arm"]]
[""] --> [[""]]
["a"] --> [["a"]]

Plan:
Create a new dictionary. Iterate through each word in the list. 
In the for loop, sort the word alphabetically. 
If the sorted word is not in the dictionary key, 
put it in a new key value pair. If it is in the dictionary, 
append it to the key value pair. Return a list of the lists of values, 
in descending order.

Runtime: O(n)
Space: O(n)
'''

def csGroupAnagrams(strs):
    dict_ = {}
    for word in strs:
        sorted_chars = sorted(word)
        sorted_word = "".join(sorted_chars)
        if sorted_word not in dict_:
            dict_[sorted_word] = [word]
        else:
            dict_[sorted_word].append(word)
    result = []
    for key, value in dict_.items():
        result.append(value)
    return result

