# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:15:42 2017
This script is convert a word from verb/adjective to it's base form.
@author: Jaydeep

verb/adjective to it's Base Form

1. reading -> read 
2. interesting -> interest 
3. talking -> talk 
4. acceptable -> accept
5. creditable -> credit
6. madness -> mad
7. firmness -> firm
8. courageous -> courage
9. dangerous -> danger
10. delightful -> delight
11. forceful -> force

"""

#this function is take a word as input and convert into it's base form.
def wordToBase(aWord):
    
    if(aWord.endswith("y")):
        #remove 'y'
        return aWord[0:-1];
    
    elif(aWord.endswith("ed")):
        #remove 'ed'
        return aWord[0:-2];
    
    elif(aWord.endswith("ing") or aWord.endswith("ous") or aWord.endswith("ful")):
        #remove 'ing', 'ous', 'ful'
        return aWord[0:-3];
    
    elif(aWord.endswith("ness") or aWord.endswith("able") or aWord.endswith("ness")):
        #remove 'ness', 'able', 'ness'
        return aWord[0:-4];
    
    else:
        #nothing match found than return original word
        return aWord;
    


print "Please enter a adjective/verb you want to convert into it's base form:"
inputWord = raw_input();
inputWord = inputWord.lower();
print "Input Word: "+inputWord;
print "Base Form : "+wordToBase(inputWord);