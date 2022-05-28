
def find_anagram(word, anagram):
    # [assignment] Add your code here
   if sorted(word) == sorted(anagram):
     return True
   else:
     return False
anagramChecker = find_anagram(
  input('FirstWord; '),
  input('SecondWord; ')
)
print(anagramChecker)
