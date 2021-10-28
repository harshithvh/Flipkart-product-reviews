import spacy
nlp = spacy.load('en_core_web_sm')

import gensim

import pandas as pd
from gensim import corpora

import re

nlp.vocab['star'].is_stop = True
nlp.vocab['stars'].is_stop = True
nlp.vocab['good'].is_stop = True

#pandas
reviews = pd.read_csv('Flipkart_ratings.csv')
print(reviews.shape)

#pandas
reviews['star_rating'] = reviews['star_rating'].apply(lambda x:1 if x > 4 else 0)

#pandas
negative_sentiments = reviews[reviews['star_rating'] == 0]
print(negative_sentiments.shape[0])

# New Section
#pandas
negative_sentiments['Final review'] = negative_sentiments['review_headline'] + ' ' + negative_sentiments['review_body']
negative_sentiments['Final review'] = negative_sentiments['Final review'].str.replace("[^a-zA-Z#]", " ")

#pandas
negative_sentiments = negative_sentiments.dropna()

#tokenization, stop words removal
negative_sentiments['Final Text'] = ''
for i in range(negative_sentiments.shape[0]):
    temp = []
    document = nlp(negative_sentiments['Final review'].iloc[i].lower())
    for j in document:
        if j.is_stop!=True and j.is_punct!=True:
            temp.append(j.lemma_)
    negative_sentiments['Final Text'].iloc[i] = temp

#vectoriazation and topic modeling 
def topic_modelling(text):
    dictionary = corpora.Dictionary(text)
    doc_term_matrix = [dictionary.doc2bow(rev) for rev in text]
    LDA = gensim.models.ldamodel.LdaModel
    lda_model = LDA(corpus = doc_term_matrix, id2word = dictionary, 
                    num_topics = 1, random_state = 19, passes = 50)
    temp = re.findall('[a-z]*',lda_model.print_topics()[0][1])
    tags = [x for x in temp if x]
    return tags

#pandas
negative_sentiments['Final Text'] = negative_sentiments['Final Text'].apply(lambda x:' '.join(x))
print(negative_sentiments.head(2))

#pandas
negative_sentiments['Review Tags'] = negative_sentiments['Final Text'].apply(lambda x: topic_modelling([x.split(' ')]))
print(negative_sentiments.head(2))

from functools import reduce

final_list = reduce(lambda x,y :x+y ,negative_sentiments['Review Tags'].dropna().values.tolist())
final_list
dic = {}
for i in final_list:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1

#pandas
df = pd.Series(dic)
df = df.drop(['t','s'])
df = df.sort_values(ascending = False)
df.head(20)

#data visualization, matplotlib & seaborn
import matplotlib.pyplot as plt
import seaborn as sns

#data visualization, matplotlib & seaborn
fig = plt.figure(figsize = (10,8))
sns.barplot(df.head(20).index.values.tolist(), df.head(20).values.tolist())
plt.xticks(rotation = 90)
print(plt.show())