# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:47:13 2020

@author: hongi
"""
import math

def compare_dictionaries(d1, d2):
    """ take two feature dictionaries d1 and d2 as inputs, and it should compute and return their log similarity score
    """
    score = 0
    gef = 0
    for z in d1:
        gef += d1[z]
    total = gef
        
    for x in d2:
        if x in d1:
            score += math.log(d1[x] / total) * d2[x]  
        else:
            score += math.log(0.5/total)  * d2[x]
    return score
def clean_text(txt):
        """takes a string of text txt as a parameter and returns a list 
        containing the words in txt after it has been “cleaned”.
        """
        s = txt
        s = s.replace('.', '')
        s = s.replace(',', '')
        s = s.replace('?', '')
        s = s.replace('!', '')
        s = s.replace(';', '')
        s = s.replace(':', '')
        s = s.replace('"', '')
        jeff = s.lower()
        return jeff.split(' ')
    
def stem(s):
    """accepts a string as a parameter. The function should then return the
    stem of s. The stem of a word is the root part of the word, which excludes
    any prefixes and suffixes.
    """
    if len(s) < 5 :
        return s
    
    if s[-3:] == 'ing':
        if s[-4] == s[-5]:
            if s[-4] == 'l' :
                s = s[:-3]
            s = s[:-4]
        else: 
            s = s[:-3]
    elif s[-2:] == 'er':
        s = s[:-2]
    elif s[-1] == 's' :
        s = s[:-1]
        stem_rest = stem(s)
        return stem_rest
    if len(s) >= 9:
        if s[-3:] == 'ion':
            s = s[:-3]
    
    
    elif s[0:3] == 'mis':
        if s == 'misses' or s == 'missus':
            return s[0:4]
        else:
            s = s[3:]
    elif s[:2] == 'un':
        s = s[2:]
        
    if len(s) >= 7:
        if s[:4] == 'over':
            s = s[4:]
    return s
            

class TextModel:
    """a class that will compare two texts in a variety of ways
    """
    def __init__(self, model_name):
        """constructs a new textmodel object by accepting a string model_name 
        as a parameter and initializing three attributes
        """
        self.name = model_name
        self.words = ({})
        self.word_lengths = ({})
        self.stems = ({})
        self.sentence_lengths = ({})
        self.punctuation = ({})
        
        
    def __repr__(self):
        """returns a string that includes the name of the model as well as the
        sizes of the dictionaries for each feature of the text
        """
        printer = 'text model name: ' + str(self.name) + '\n'
        printer += '  number of words: ' + str(len(self.words)) +'\n'
        printer += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        printer += '  number of stems: ' + str(len(self.stems)) + '\n'
        printer += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        printer += '  number of different punctuations: ' + str(len(self.punctuation)) 
        return printer
    
    def add_string(self, s):
        """adds a string of text s to the model by augmenting the feature 
        dictionaries defined in the constructor
        """
        space = 0
        count = 0
        word_list = clean_text(s)
        for w in word_list:
            # Update self.words to reflect w
             if w not in self.words:
                 self.words[w] = 0
             self.words[w] += 1
        #self.word_lengths
        for w in word_list:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 0
            self.word_lengths[len(w)] += 1
        #self.stem
        for w in word_list:
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 0 
            self.stems[stem(w)] += 1 
        #self.sentence_lengths
        for w in s:
            if w == ' ':
                space += 1
            if w in '.?!' and count == 0:
                if space not in self.sentence_lengths:
                    self.sentence_lengths[space+1] = 1
                space = 0
                count += 1 
            elif w in '.?!' and count > 0:
                if space not in self.sentence_lengths:
                    self.sentence_lengths[space] = 0
                self.sentence_lengths[space] += 1
                space = 0
        #self.punctuation
        for w in s:
            if w == '?':
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == "...":
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == ".":
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == "!":
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == "-":
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == '/':
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == ';':
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == '[':
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == '\"':
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == '(':
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == '—':
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == ':':
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
            if w == '\'':
                if w not in self.punctuation:
                    self.punctuation[w] = 0
                self.punctuation[w] += 1 
                

            
            
            
            
          
            
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)
        f.close()
        
    def save_model(self):
        """saves the TextModel object self by writing its various feature 
        dictionaries to files
        """
        jeff = self.name + '_words'
        f = open(jeff, 'w')
        f.write(str(self.words))
        f.close()
        
        jeph = self.name + '_word_lengths'
        f = open(jeph, 'w')
        f.write(str(self.word_lengths))
        f.close()
        
        geoff = self.name + '_stems'
        f = open(geoff, 'w')
        f.write(str(self.stems))
        f.close()
        
        joeff= self.name + '_sentence_lengths'
        f = open(joeff, 'w')
        f.write(str(self.sentence_lengths))
        f.close()
        
        geoph = self.name + '_punctuation'
        f = open(geoph, 'w')
        f.write(str(self.punctuation))
        f.close()
        
    def read_model(self):
        f = open(self.name + '_words')
        d_str=f.read()
        f.close()
        
        d = dict(eval(d_str))
        self.words = d
       
        
        f = open(self.name + '_word_lengths')
        d_str=f.read()
        f.close()
        
        z = dict(eval(d_str))
        self.word_lengths = z
        
        
        f = open(self.name + '_stems')
        d_str=f.read()
        f.close()
        
        z = dict(eval(d_str))
        self.stems = z
        
        
        f = open(self.name + '_sentence_lengths')
        d_str=f.read()
        f.close()
        
        z = dict(eval(d_str))
        self.sentence_lengths = z

        
        f = open(self.name + '_punctuation')
        d_str=f.read()
        f.close()
        
        z = dict(eval(d_str))
        self.punctuation = z       
        
    def similarity_scores(self, other):
        """computes and returns a list of log similarity scores measuring the 
        similarity of self and other – one score for each type of feature 
        (words, word lengths, stems, sentence lengths, and your additional 
        feature)
        """
        word_score = []
        word_score += [compare_dictionaries(other.words, self.words)]
        word_score += [compare_dictionaries(other.word_lengths, self.word_lengths)]
        word_score += [compare_dictionaries(other.stems, self.stems)]
        word_score += [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]     
        word_score += [compare_dictionaries(other.punctuation, self.punctuation)]
        return word_score
        
    def classify(self, source1, source2):
        """compares the called TextModel object (self) to two other “source” 
        TextModel objects (source1 and source2) and determines which of these 
        other TextModels is the more likely source of the called TextModel
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name +':' + str(scores1))
        print('scores for ' + source2.name +':' + str(scores2))
        weighted_sum1 = 2*scores1[0] + 2*scores1[1] + scores1[2] + 2*scores1[3] + scores1[4] 
        weighted_sum2 = 2*scores2[0] + 2*scores2[1] + scores2[2] + 2*scores2[3] + scores2[4] 
        if max(weighted_sum1, weighted_sum2) == weighted_sum1: 
            print(str(self.name) + ' is more likely to have come from ' + str(source1.name))
        elif max(weighted_sum1, weighted_sum2) == weighted_sum2: 
            print(str(self.name) + ' is more likely to have come from ' + str(source2.name))

def test():
    """ test text model with given strings """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def run_tests():
    """ tests the text model with new text files """
    source1 = TextModel('50 Shades of Gray')
    source1.add_file('50.txt')
    
    print()
    
    source2 = TextModel('King James Version of the Bible')
    source2.add_file('kjv.txt')

    print()

    new1 = TextModel('Shakespeare')
    new1.add_file('shake.txt')
    new1.classify(source1, source2)
    
    print()
    
    new2 = TextModel('JK Rowling')
    new2.add_file('hp.txt')
    new2.classify(source1, source2)
    
    print()
    
    new3 = TextModel('Breitbart News Network')
    new3.add_file('bnn.txt')
    new3.classify(source1, source2)
    
    print()
    
    new4 = TextModel('Chaucer')
    new4.add_file('tct.txt')
    new4.classify(source1, source2)
    