# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Exception Handling and Pickling demo
# Natalie, September 8, 2023, Modified code to complete assignment 07
# ---------------------------------------------------------------------------- #

import pickle #import the pickle module

# create a dictionary
pickle_example = {
    'task': 'sweep',
    'time (minutes)': 30,
    'priority': 'medium'
}

# Pickling
# write the object to a file
with open('pickle_example.p', 'wb') as file: #open a file named 'dict_pickle.p' in write and binary mode ('wb')
    pickle.dump(pickle_example, file) #use pickle.dump() to dump the dictionary to the opened file

print("Dictionary has been pickled!")

# Unpickling
# read the object from the file
with open('pickle_example.p', 'rb') as file:
    unpickled_example = pickle.load(file) #check if the dictionary has been properly pickled

print("Unpickled dictionary:", unpickled_example)

# if the pickle_example dictionary was instead stored as a string of text files:
with open('not_pickled_file.p', 'w') as file:
    not_pickled = str(pickle_example)
        # write the dictionary to the file
    file.write(not_pickled)
print("Not pickled file:", not_pickled)

# try to unpickle the file
try:
    with open('not_pickled_file.p', 'rb') as file:
        unpickled_example = pickle.load(file)
    print("Unpickled example:", unpickled_example)
except pickle.UnpicklingError as ue:
    print("UnpicklingError:", str(ue)) #will show an UnpicklingError 
    #we are trying to unpickle a file that isn't actually a pickled object

