word = 'abc'
word_list = ['a', 'b', 'c']
word = ''.join(word)
print(word)
word = [('a',), ('b',), ('c',)]
list_of_list = [list(elem) for elem in word]
print(list_of_list)

'''
string = ''.join(list_of_list)
print(string)

transformar:
[('a',), ('b',), ('c',)]


['a', 'b', 'c']
'''
palavra = ('a', 'a')
print(''.join(palavra))
