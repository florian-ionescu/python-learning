#1. Reverse the order of the items in an array.
#Example: a = [1, 2, 3, 4, 5]
#Result: a = [5, 4, 3, 2, 1]

#metoda 1:
>>> a = [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

>>> a[::-1]
[5, 4, 3, 2, 1]

# metoda 2:
>>> a.reverse()
>>> a
[5, 4, 3, 2, 1]


#2. Get the number of occurrences of var b in array a.
#Example:
#a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
#b = 2
#Result: 4

>>> a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
>>> a.count(2)
4

#3. Given a sentence as string, count the number of words in it.
#Example:
#a = 'ana are mere si nu are pere'
#Result: 7

>>> a = 'ana are mere si nu are pere'
>>> len(a.split())
7
