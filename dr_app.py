# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:28:06 2022

@author: Drashya
"""

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st

#header
st.header("Generate your word clude")
#title
#st.title('Copy or Write your text')
# take the User input Here
text = st.text_input("")
#subtitle
st.subheader("Copy or Write your taxt here")
# button
#st.button("Let's GO!'")




token = word_tokenize(text) 
fdist = FreqDist(token)
fdist1 = fdist.most_common(30)
text = " ".join(cat.split()[0] for cat in token)
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
plt.imshow(word_cloud, interpolation = 'bilinear')
plt.axis("off")
output = plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(output)
