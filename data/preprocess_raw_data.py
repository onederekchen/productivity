import pandas as pd
import os

path = "../base data (dnc)/Daily Recap (Responses) - RAW form responses.csv"

df = pd.read_csv(path).dropna(subset=['How would you rate your overall satisfaction for the day?'])  # drop missing target values

# remove irrelevant features
irrelevant_features = [
    'Week Start', 'Combined Date/Weekday', 'Last 7 days?', 'Last 30 days?',
    'Weekday',  # may remove later
    'Timestamp', 
    'What day is this for?',  # may remove later
    'Anything else you want to share?',
    'Do you want to take this form today?',  # may remove later
    'Was today a free day?', 'Notes'
]
df.drop(irrelevant_features, axis=1, inplace=True, errors='raise')  # can i not raise but print something?

# rename columns
column_mapper = {
    'Productive Hours': 'productive',
    'Productive AI Hours': 'productive_ai', 
    'Unproductive Hours': 'unproductive',
    'How would you rate your overall satisfaction for the day?': 'satisfaction',
    'Did you exercise today?': 'exercise', 
    'Did you post on social media today?': 'media',
    'Was your sleep schedule healthy today?': 'sleep',
    'Was your relationship with technology was healthy today?': 'tech',
    'Did you spend time with someone you wanted to today?': 'people',
}
df.rename(columns=column_mapper, inplace=True)

# ordinally encode target
target_mapper = {"Terrible day": 0, "Not great day": 1, "Okay day": 2, "Good day": 3, "Incredible day": 4}
df['satisfaction_score'] = df['satisfaction'].replace(target_mapper)  # this is after renaming satisfaction

# reorder satisfaction to first and second?
cols = ['satisfaction', 'satisfaction_score']  + [col for col in df if col != 'satisfaction' and col != 'satisfaction_score']
df = df[cols]

# # limit numerical features to 8
hours_features = ['productive', 'productive_ai', 'unproductive']  # 121 prod is 11, 140 unprod is 10
for f in hours_features:
    df[f] = df[f].apply(lambda x: x if x < 8 else 8)

# save
df.to_csv("data.csv", index=False)
