#!/usr/bin/env python
# coding: utf-8

# # Final Project - Word Cloud

# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')


import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys





# This is the uploader widget
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()



# In[91]:


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'“”"\,’<>./?@#$%^&*—_~'''
    punctuations = set(punctuations)
#     print(punctuations)
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    file_contents = file_contents.lower()
    freqWord = dict()
    wordlist = file_contents.split()

    for word in wordlist:
        for letter in word:
            if letter in punctuations or letter.isnumeric():

                word = word.replace(letter, "")

        if len(word)>0 and word not in uninteresting_words:
            if word in freqWord:
                freqWord[word] += 1
            else:
                freqWord[word] = 1
#     print(freqWord)

            
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freqWord)
    return cloud.to_array()




# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


