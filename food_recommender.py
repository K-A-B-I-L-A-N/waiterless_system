import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

food_df = pd.read_csv(r"indian_food.csv")
food_cleaned_df = food_df.drop(columns=['ingredients', 'prep_time', 'cook_time', 'region'])
food_cleaned_df["adjusted"] = food_cleaned_df["flavor_profile"] + ' ' + food_cleaned_df["course"] + ' ' + \
                              food_cleaned_df["state"]
tfv = TfidfVectorizer()
food_cleaned_df['adjusted'] = food_cleaned_df['adjusted'].fillna(' ')
score_matrix = tfv.fit_transform(food_cleaned_df['adjusted'])
sigs = sigmoid_kernel(score_matrix, score_matrix)
indices = pd.Series(food_cleaned_df.index, index=food_cleaned_df['name']).drop_duplicates()


def give_rec(name, sig=sigs):
    idx = indices[name]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:11]
    food_indices = [i[0] for i in sig_scores]
    return food_indices



