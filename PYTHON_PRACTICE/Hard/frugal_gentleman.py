'''
Atticus has been invited to a dinner party, and he decides to purchase a bottle of wine. However, he has little knowledge of how to choose a good bottle. Being a very frugal gentleman (yet disliking looking like a cheapskate), he decides to use a very simple rule. In any selection of two or more wines, he will always buy the second-cheapest.

Given a list of wine dictionaries, write a function that returns the name of the wine he will buy for the party. If given an empty list, return None. If given a list of only one, Atticus will buy that wine.

Examples
chosen_wine([
  { "name": "Wine A", "price": 8.99 },
  { "name": "Wine 32", "price": 13.99 },
  { "name": "Wine 9", "price": 10.99 }
]) ➞ "Wine 9"

chosen_wine([{ "name": "Wine A", "price": 8.99 }]) ➞ "Wine A"

chosen_wine([]) ➞ None
Notes
All wines will be different prices, so there is no confusion in the ordering.
'''

def chosen_wine(wines):

    if len(wines)==0:
        return None

    elif len(wines)==1:
        listnewnew=list(wines[0].values())
        return listnewnew[0]

    dictnew={}
    for dicts in wines:
        dictnew[dicts['name']]=dicts['price']

    newlist=list(dictnew.keys())
    newlist=sorted(newlist, key= lambda x : dictnew[x])
    return newlist[1]

print(chosen_wine([{"name": "Wine A", "price": 8.99}]))
print(chosen_wine([{"name": "Wine A", "price": 8.99}, {"name": "Wine 389", "price": 109.99}, {"name": "Wine 44", "price": 38.44}, {"name": "Wine 72", "price": 22.77}]), "Wine 72")))
