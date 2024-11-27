'''
Create a function that, given a phrase and a number of letters guessed, returns a string with hyphens - for every letter of the phrase not guessed, and each letter guessed in place.

Examples
hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"

hangman("tree", ["r", "t", "e"]) ➞ "tree"

hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"

hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"
Notes
The letters are always given in lowercase, but they should be returned in the same case as in the original phrase (see example #3).
All characters other than letters should always be returned
'''

def hangman(phrase, lst):

    def new(lst):
        newlist=[]
        for i in lst:
              a=i.upper()
              newlist.append(a)
        return newlist
    newreturn=new(lst)
    for i in phrase:
        if (i not in lst) and (i not in newreturn):
            if i.isalpha():
            #if (ord(i) in range(ord('a'),ord('z')+1)) or (ord(i) in range(ord('A'),ord('Z')+1)):
                phrase=phrase.replace(i,'-')

    return phrase

#print(hangman("Looney Tunes", ["a", "e", "i", "o", "u"]))
