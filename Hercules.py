

#SpaCy Natural Language Processing Models in Python

#https://www.geeksforgeeks.org/nlp/spacy-for-natural-language-processing/#google_vignette

#https://realpython.com/natural-language-processing-spacy-python/

#spaCy for Natural Language Processing
#spaCy is a Python library used to process and analyze text efficiently for natural language processing tasks. It provides ready-to-use models and tools for working with linguistic data.
#Supports tokenization, POS tagging and dependency parsing
#Designed for speed and production use
#Works well with large text datasets
#Commonly used in NLP pipelines
#Unlike traditional NLP libraries such as NLTK, which are often used for learning and experimentation, spaCy is built with a modern architecture optimized for large-scale text processing and industrial use cases.
#Core Concepts and Data Structures
#spaCy processes text using a central Language object and when raw text is passed to this object, it returns a Doc object that stores all linguistic annotations.
#Key Container Objects:
#Doc: Stores the processed text and all linguistic annotations
#Token: Represents an individual word, punctuation mark or symbol
#Span: A slice or segment of a Doc object
#Vocab: Stores lexical attributes and word vectors
#Language: Manages the NLP pipeline and processes text


import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("The quick brown fox jumps over the Lazy dog.")

for token in doc:

    print (token.text, token.pos_, token.dep_)


