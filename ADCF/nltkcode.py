
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.word_tokenize('text')
text = input('enter bro: ')
arr = word_tokenize(text)

print(arr)

# print(sent_tokenize(text))

# i plan to call in a searching file and allow
#  it to search the array for keyword onces get
#  the keyword the searching file returns the
#  keyword to funtions file and a required funtion is peformend
