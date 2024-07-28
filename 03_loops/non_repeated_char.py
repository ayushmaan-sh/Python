# Given a string, find the first non-repeated character

word = "ayushmaan"

for i in word:
   if word.count(i) == 1:
    print('First non-repeated character is',i)
    break

