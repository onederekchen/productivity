import pandas as pd
import pickle

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.ensemble import RandomForestClassifier

# get data
df = pd.read_csv('../data/data.csv')
X = df.drop(['satisfaction', 'satisfaction_score'], axis=1).copy()
y = df['satisfaction_score'].copy()

# numerical preprocessing
numerical_features = [f for f in X.columns if X[f].dtype in ['int64', 'float64']]
numerical_transformer = SimpleImputer(strategy='constant')

# categorical preprocessing
categorical_features = [f for f in X.columns if X[f].nunique() < 10 and X[f].dtype == "object"]
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# bundle preprocessing pipelines
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

model = RandomForestClassifier(n_estimators=100, random_state=0)  # very basic model

# bundle preprocessor and model
clf = Pipeline(steps=[('preprocessor', preprocessor), 
                      ('model', model)
                     ])

# fit model
clf.fit(X, y)

# export pickled model
folder = ''
with open(f'{folder}productivity_model', 'wb') as f:  # this is trained on X
    pickle.dump(model, f)
