'''
A word is alphabetically sorted if all of the letters in it are in consecutive alphabetical order. 
Some examples of alphabetically sorted words: abhors (a is before b, b is before h, h is before o, etc.), ghost, accent, hoop.

Create a function that takes in a sentence as input and returns True if there is at least one alphabetically sorted word inside that has a minimum length of 3.

'''

def is_alphabetically_sorted(sentence):
    list1=sentence.split(" ")
    for element in list1:
        if len(element)>=3:
            strsorted="".join(sorted(element,key=lambda x:x.lower()))
            if element==strsorted:
                return True
    return False
