'''
Create a function that takes a string and returns a string ordered by the length of the words. 
From shortest to longest word. If there are words with the same amount of letters, order them alphabetically.
Punctuation (periods, commas, etc) belongs to the word in front of it.
'''

def sort_by_length(txt):
  list1=txt.split(" ")
  list1=sorted(list1,key=lambda x:(len(x),x.lower()))
  str1=" ".join(list1)
  return str1
