from wordnik import *
import json
from docx.shared import Pt
import os

"""
(Required packages)
pip install wordNik
pip install python-docx

from wordnik import *
import json
from docx.shared import Pt
import os
"""

print("STARTING PROGRAM\n")

outputFileName = input("Word Document Name: ")
title = input("Title For Document: ")
limitDefNumber = input("Definitions Limit: ")
#teacher = input("Teacher Name: ")
#block = input("Class Block Number: ")
#name = input("Your Name: ")
#outputFileName = "VocabularySet1"
#title = "Vocabulary Set 1"
teacher = "Smiley"
block = "2"
name = "Jonathan Le"

#Authenticates wordNik
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'ed7da28872250fb9c000c082c1305d06e3e1ea0334e4665ab'
client = swagger.ApiClient(apiKey, apiUrl)

#Used for counting and writing definition numbers
num = 1

#Asks for word
#wordSearch = input("Word:")
#print("\n")
wordApi = WordApi.WordApi(client)

print("===OPENING WORDS LIST===\n")
inputFile = open("VocabWords.txt", "r")

print("===OPENING WORD DOCUMENT===\n")
outputFile = open(outputFileName + ".doc", "w")

outputFile.write("-PLEASE CHECK OVER THE WORD DOCUMENT-\n\n")

outputFile.write(title + "\n")
outputFile.write("Teacher: " + teacher + "\n")
outputFile.write("Block " + block + "\n")
outputFile.write("By: " + name + "\n\n\n")

print("===WRITING TO FILE===\n")
for line in inputFile:

    wordSearch = line.replace('\n', '')

    word = wordApi.getWord(wordSearch)
    wordDisplay = str(word.word.upper())
    print("=" + wordDisplay + "=\n")
    outputFile.write("===" + wordDisplay + "===\n\n")


    #Requests definition of wordSearch
    #definitions = wordApi.getDefinitions(wordSearch, limit=1, partOfSpeech = "noun")
    definitionsCheck = wordApi.getDefinitions(wordSearch, sourceDictionaries = "ahd")

    #Asks for 2 synonyms and antonyms
    synonyms = wordApi.getRelatedWords(word = wordSearch, relationshipTypes = "synonym", useCanonical = True, limitPerRelationshipType = 2)
    antonyms = wordApi.getRelatedWords(word = wordSearch, relationshipTypes = "antonym", useCanonical = True, limitPerRelationshipType = 2)

    if not definitionsCheck:
        print("WORD NOT FOUND - "  + wordSearch + " - (CHECK SYNTAX)\n")
        outputFile.write("ERROR - WORD NOT FOUND - " + wordSearch + " - (CHECK SYNTAX)\n")
    else:

        print("===DEFINITIONS===")
        if not definitionsCheck:
            print("No Definitions Found - (Search for online)")
            outputFile.write("No Definitions Found - (Search for online)\n")
        else:
            num = 1
            definitions = wordApi.getDefinitions(wordSearch, partOfSpeech = "noun", limit = limitDefNumber, sourceDictionaries = "ahd")
            if definitions:
                for x in range(0, len(definitions)):
                    print(str(num) + ": (NOUN) - " + definitions[x].text + "\n")
                    outputFile.write(str(num) + ": (NOUN) - " + definitions[x].text + "\n\n")
                    num = num + 1
            definitions = wordApi.getDefinitions(wordSearch, partOfSpeech = "pronoun", limit = limitDefNumber, sourceDictionaries = "ahd")
            if definitions:
                for x in range(0, len(definitions)):
                    print(str(num) + ": (PRONOUN) - " + definitions[x].text + "\n")
                    outputFile.write(str(num) + ": (PRONOUN) - " + definitions[x].text + "\n\n")
                    num = num + 1
            definitions = wordApi.getDefinitions(wordSearch, partOfSpeech = "verb", limit = limitDefNumber, sourceDictionaries = "ahd")
            if definitions:
                for x in range(0, len(definitions)):
                    print(str(num) + ": (VERB) - " + definitions[x].text + "\n")
                    outputFile.write(str(num) + ": (VERB) - " + definitions[x].text + "\n\n")
                    num = num + 1
            definitions = wordApi.getDefinitions(wordSearch, partOfSpeech = "adjective", limit = limitDefNumber, sourceDictionaries = "ahd")
            if definitions:
                for x in range(0, len(definitions)):
                    print(str(num) + ": (ADJECTIVE) - " + definitions[x].text + "\n")
                    outputFile.write(str(num) + ": (ADJECTIVE) - " + definitions[x].text + "\n\n")
                    num = num + 1
            definitions = wordApi.getDefinitions(wordSearch, partOfSpeech = "adverb", limit = limitDefNumber, sourceDictionaries = "ahd")
            if definitions:
                for x in range(0, len(definitions)):
                    print(str(num) + ": (ADVERB) - " + definitions[x].text + "\n")
                    outputFile.write(str(num) + ": (ADVERB) - " + definitions[x].text + "\n\n")
                    num = num + 1
            definitions = wordApi.getDefinitions(wordSearch, partOfSpeech = "preposition", limit = limitDefNumber, sourceDictionaries = "ahd")
            if definitions:
                for x in range(0, len(definitions)):
                    print(str(num) + ": (PREPOSITION) - " + definitions[x].text + "\n")
                    outputFile.write(str(num) + ": (PREPOSITION) - " + definitions[x].text + "\n\n")
                    num = num + 1
            definitions = wordApi.getDefinitions(wordSearch, partOfSpeech = "conjunction", limit = limitDefNumber, sourceDictionaries = "ahd")
            if definitions:
                for x in range(0, len(definitions)):
                    print(str(num) + ": (CONJUNCTION) - " + definitions[x].text + "\n")
                    outputFile.write(str(num) + ": (CONJUNCTION) - " + definitions[x].text + "\n\n")
                    num = num + 1
            definitions = wordApi.getDefinitions(wordSearch, partOfSpeech = "interjection", limit = limitDefNumber, sourceDictionaries = "ahd")
            if definitions:
                for x in range(0, len(definitions)):
                    print(str(num) + ": (INTERJECTION) - " + definitions[x].text + "\n")
                    outputFile.write(str(num) + ": (INTERJECTION) - " + definitions[x].text + "\n\n")
                    num = num + 1

        print("===SYNOMYMS===")
        outputFile.write("Synonyms - ")
        if not synonyms:
            print("No Synonyms Found (Search for online)\n")
            outputFile.write("No Synonyms Found - (Search for online)\n")
        else:
            for x in range(0, 1):
                print(synonyms[x].words)
                outputFile.write(str(synonyms[x].words) + "\n")
        print("\n")
        outputFile.write("\n")


        print("===ANTONYMS===")
        outputFile.write("Antonyms - ")
        if not antonyms:
            print("No Antonyms Found (Search for online)\n")
            outputFile.write("No Antonyms Found - (Search for online)\n")
        else:
            for x in range(0, 1):
                print(antonyms[x].words)
                outputFile.write(str(antonyms[x].words) + "\n")
        print("\n")
        outputFile.write("\n")

print("===FINISHED WRITING TO FILE===\n")

print("===CLOSING WORD DOCUMENT===\n")
outputFile.close()
print("===CLOSING WORD LIST===\n")
inputFile.close()

print("===PROGRAM FINISHED===\n\n-PLEASE CHECK OVER THE WORD DOCUMENT-\n\n-If there are any mistakes in the word document, there is a mistake in the word list-\n\nEnjoy! ^_^\n")
os.system("pause")
