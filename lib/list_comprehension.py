#!/usr/bin/env python3

def return_evens(num_list):
    if len(num_list) == 0:
        print([])
        return []
    else:
        new_list = [item for item in num_list if item % 2 == 0]
        print(new_list)
        return new_list
    
return_evens([0, 1, 3, 5, 7, 8, 9])
# [0, 8]

def make_exclamation(sentence_list):
    new_setntence_list = [item + "!" for item in sentence_list]
    print(new_setntence_list)
    return new_setntence_list

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
# ["Hello!", "I'm doing great!", "Python is fun!"]
