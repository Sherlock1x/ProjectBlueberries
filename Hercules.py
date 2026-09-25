

#   SpaCy Natural Language Processing Models in Python

#https://www.geeksforgeeks.org/nlp/spacy-for-natural-language-processing/#google_vignette

#https://realpython.com/natural-language-processing-spacy-python/

#   Frontier Lab

#   spaCy for Natural Language Processing
#    spaCy is a Python library used to process and analyze text efficiently for natural language processing tasks. It provides ready-to-use models and tools for working with linguistic data.
#   Supports tokenization, POS tagging and dependency parsing
#    Designed for speed and production use
#   Works well with large text datasets
#   Commonly used in NLP pipelines
#   Unlike traditional NLP libraries such as NLTK, which are often used for learning and experimentation, spaCy is built with a modern architecture optimized for large-scale text processing and industrial use cases.
#   Core Concepts and Data Structures
#   spaCy processes text using a central Language object and when raw text is passed to this object, it returns a Doc object that stores all linguistic annotations.
#   Key Container Objects:
#   Doc: Stores the processed text and all linguistic annotations
#   Token: Represents an individual word, punctuation mark or symbol
#   Span: A slice or segment of a Doc object
#   Vocab: Stores lexical attributes and word vectors
# Language: Manages the NLP pipeline and processes text 


#import spacy

#nlp = spacy.load("en_core_web_sm")

#doc = nlp("The quick brown fox jumps over the Lazy dog.")

#for token in doc:

#    print (token.text, token.pos_, token.dep_)

#https://www.youtube.com/watch?v=Uh2ebFW8OYM

with open('FrontierLab.txt', 'a') as af:
    af.write('\nDate: 20261001')
    af.write('\n90501847-1725=90500122  wt WellMx Basex Withdrawel Cumalative AcctPayable New current Balance$$ MTD')
    af.write('\n0+3746+1686+1821+1771+1681+1821+4095+1631+1725=19981  wtt WellMx Cumalative AcctPayable Xpense$$ YTD')
    af.write('\n1/3*90500122+90500122-90500122=30166707  q WellMx Apexy Pyrimidzxy Derivative')
    af.write('\n90500122+30166707=120666829 "[bold yellow]j WellMx Pyramidzxy AcctPay Apexy and Basex[/yellow]')
    af.write('\n120666829+30166707=150833536 "[bold green]d WellMx Pyramidzxy and Apexy Deposit AcctRec[/green]')
    af.write('\n300*15083.4=4525020.0,300*20111.14=6033342.0 "[oil, Oz of Gold Times a Barrell of Oil in $ Total oz Gold]')

with open('FrontierLab.txt', 'r+') as rf:
    f_contents = rf.readlines()
    print(f_contents)

#f = open('FrontierLab.txt', 'r','w')


#with open('FrontierLab.txt','r') as rf:
#    with open('FrontierLab.txt', 'w') as wf:
#        for line in rf:
#            wf.write(line)
            #print(line, end ='')


#  The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators 
#  with the same name that can be executed on many objects or classes.



