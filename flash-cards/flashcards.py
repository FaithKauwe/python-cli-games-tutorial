# import the json module from python3
import json
import random
from random import randint
# streatch goal- randomize cards
# dicts don't have indexes, they have keys and I couldn't find a way to shuffle the keys
# I can take the keys, add those to a list, randomize those and then take the random index generated and find it's matching key in the dict


# open the file and parse the JSON, pass 2 args: name of file and "r" for read
# as f means contents of file were passed as the variable "f"
# load variable f (the json dict) into a new python dict called "data"
with open('me-capitals.json', 'r') as f: 
    data = json.load(f) 

# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0    

# fun story: I thought data[cards] was a dict and spent a stupid amount of time trying to ficure out
# how to randomize a dict (convert to list of items, shuffle, convert back to dict). Didn't work until I 
# realized data[cards] is a list which makes it very easy (random.shuffle). Thankfully, I got wise and 
# printed a bunch of things so I could see the shape of the data
random.shuffle(data["cards"])

# i is the iterator and data[cards] is accessing the 'cards' key of the 'data' dict:
# 'cards' is filled with other nested dicts with key = 'q' holding the 'a' portion
# {'cards': [{'q': 'What is the capital of Syria', 'a': 'Damascus'}{'q': 'What is the capital of Lebanon?', 'a': 'Beirut'}]}
for i in data["cards"]:
# intialize variable guess which holds the user input. input will be in response to the 'q' key
# which is accessed by i["q"] then concatonated with a string ">"    
    guess = input(i["q"] + " > ")
# access the value of the "a" key in the i-th position in the dict
# compare to user input and perform conditional logic
# use .lower() built in function in case user misses a capital letter
    if guess.lower() == i["a"].lower():
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
    else:
# combining 2 comma separated print statements        
        print("Incorrect!The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")