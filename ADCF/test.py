# from nltk.chat.util import Chat, reflections

# pairs = [
#     ['my name is (.*)', ['Hello ! % 1']],
#     ['(hi|hello|hey|holla|hola)', ['Hey !', 'hi', 'hello']],
#     ['(name?|your name ?|(.*) your name ?)', ['My name is mini']],
#     ['(.*) do you do ?',
#      ['We provide a platform for tech enthusiasts, a wide range of options !']],
#     ['(.*) created you ?', ['Geeksforgeeks created me using python and NLTK']]
# ]

# chat = Chat(pairs, reflections)
# chat.converse()


# from nltk.chat.util import Chat, reflections

# pairs =[
# 	['my name is (.*)', ['Hello ! % 1']],
# 	['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !', 'Hey !']],
# 	['(.*) your name ?', ['My name is Geeky']],
# 	['(.*) do you do ?', ['We provide a platform for tech enthusiasts, a wide range of options !']],
# 	['(.*) created you ?', ['Geeksforgeeks created me using python and NLTK']]
# ]

# chat = Chat(pairs, reflections)
# chat.converse()


# import the existing word and sentence tokenizing
# libraries
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Natural language processing (NLP) is a field " + \
    "of computer science, artificial intelligence " + \
    "and computational linguistics concerned with " + \
    "the interactions between computers and human " + \
    "(natural) languages, and, in particular, " + \
    "concerned with programming computers to " + \
    "fruitfully process large natural language " + \
    "corpora. Challenges in natural language " + \
    "processing frequently involve natural " + \
    "language understanding, natural language" + \
    "generation frequently from formal, machine" + \
    "-readable logical forms), connecting language " + \
    "and machine perception, managing human-" + \
    "computer dialog systems, or some combination " + \
    "thereof."

print(sent_tokenize(text))
print(word_tokenize(text))
