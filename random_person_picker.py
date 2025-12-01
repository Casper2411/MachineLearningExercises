import random

def random_item_from_list(list):
    randomINT = random.randint(0, len(list)-1)
    return list[randomINT]

persons = ["Emilie",
           "Olivia",
           "Albert",
           "Carmen",
           "Jacob",
           "Mads",
           "Alex",
           "Mathilde",
           "Millard",
           "Fich",
           "Felix",
           "Frederik",
           "Max",
           "Natalie",
           "rasmus",
           "Casper"
           ]
#print(len(persons))

print(random_item_from_list(persons))