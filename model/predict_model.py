import pandas as pd
import pickle


def getKey(dct,value):  # works for unique values; might be better to reverse dict instead
     return [key for key in dct if (dct[key] == value)]


target_mapper = {"Terrible day": 0, "Not great day": 1, "Okay day": 2, "Good day": 3, "Incredible day": 4}

folder = ''

with open(f'{folder}productivity_model', 'rb') as f:
    model = pickle.load(f)

print(getKey(target_mapper, model.predict([[
    8, 5, 2,  # prod, ai, unprod
    0, 1,  # exercise n/y
    0, 1,  # social n/y
    0, 1,  # sleep n/y
    0, 1,  # tech n/y
    1, 0,  # people n/y
]])))