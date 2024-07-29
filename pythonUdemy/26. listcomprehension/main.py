# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd
#TODO 1. Create a dictionary in this format:

file = pd.read_csv("phonetics.csv")
dic = {row.letter:row.code for (ind,row) in file.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("enter any word: ").upper()
x = [dic[w] for w in word ]
print(x)