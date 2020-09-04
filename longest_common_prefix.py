'''
1. Capture smallest string and longest string
2. Iterate over smallest string:
  2.a. return the sub-string till there is a match with longest string
3. By default smallest string is longest common prefix so return that
'''

def longestCommonPrefix(strs) -> str:
  if not strs: return ''
  # since list of string will be sorted and retrieved min max by alphebetic order
  s1 = min(strs) # e.g. 'b' v/s 'abc' => 'abc' 
  s2 = max(strs)
  
  """
  Alternatively we could (to make it faster) use sort which is O(nlog(n)) time complexity
  strs.sort()
  s1, s2= strs[0], strs[-1]
  """
  
  for i, c in enumerate(s1):
    print(f'[i]: {i}, [c]: {c}')
    if c != s2[i]:
      print(f'c => {c} != s2[i] => {s2[i]}')
      return s1[:i] # stop until hit the split index i.e. s1[0]...s[i-1]
  return s1

print(longestCommonPrefix(["flower","flow","flight"]))


'''
[i]: 0, [c]: f
[i]: 1, [c]: l
[i]: 2, [c]: i
c => i != s2[i] => o
fl
'''