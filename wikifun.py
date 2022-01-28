import requests
from bs4 import BeautifulSoup
import random
from random_word import RandomWords
rw = RandomWords()

while True:
    while True:
        # generate single english word string
        word = rw.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)
        #url = requests.get("https://en.wikipedia.org/wiki/Special:Random"
        try:
            url = requests.get("https://en.wikipedia.org/wiki/" + word)
            # print("https://en.wikipedia.org/wiki/" + word)
            soup = BeautifulSoup(url.content, "html.parser")
            title = soup.find(class_="firstHeading").text
            content = soup.find(class_="mw-parser-output")
            p_vals = content.findAll('p')
            if (len(p_vals) > 10):
                break
        except:
            pass
        

    while True:
        ind = random.randint(5, len(p_vals))
        if len(p_vals[ind].text.split('.')) > 0:
            if len(p_vals[ind].text.split('.')[0].split(' ')) > 5:
                break
    # print("Number of P's: " + str(len(p_vals)) +"\n")
    # print("Index chosen: " + str(ind) + "\n")
    print(p_vals[ind].text.split('.')[0])
    print('\n')
    
    answer = input('Answer?')
    if answer.lower() == word.lower():
        print("Correct! Answer was " + word + "\n")
    else:
        print("Wrong! Answer was " + word + "\n")
    print('\n')
    
    input('Another Round?')
    print('\n\n')
    

