pyg = 'ay'

original = input('Enter a word:')

word = original.lower()
first = word[0]
new_word = word[1:len(word)] + first + pyg

if len(original) > 0 and original.isalpha():
    print (new_word)
else:
    print ('empty')
