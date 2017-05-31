import requests
import bs4
import re
from Components import exclude_word

# ritorna il contenitore delle informazioni della pagina web


def search_abstract(url):
    page = requests.get(url).text
    soup = bs4.BeautifulSoup(page, 'lxml')
    try:
        div = soup.findAll("div", {"class": "fixed"})
    except IndexError:
        print("La pagina non contiene informazioni: " + url)
        div = None
    return div

'''
word_base -> indica la parola su cui si basa il concetto che si vuole cercare
word_to_search -> indica una delle parole situate prima o dopo la parola 'concetto' usate per capire 
a quale concetto la parola base faccia riferimento
'''


def search_urls(word_base):
    plist = []  # creo una lista vuota
    url = 'http://it.dbpedia.org/resource/' + word_base + '/html'  # url della pagina web
    # trovo l'html della pagina web
    page = requests.get(url).text
    soup = bs4.BeautifulSoup(page, 'lxml')
    div = soup.findAll("a", {"class": "isLocal"})  # trovo il contenitore dei link
    for i in div:  # per ogni link tiro fuori l'url pulito e lo metto nella lista
        new_url = i.get('title')
        new_url = new_url.replace('<', '')
        new_url = new_url.replace('>', '')
        plist.append(new_url)
    return plist


def search_in_abstract(file, word_base):
    plist = search_urls(word_base)
    words_to_search = file.read()  # parola da cercare che nel testo può essere prima o dopo della parola chiave
    words_to_search = re.sub(r'[^\w\s]','',words_to_search)
    words_to_search = words_to_search.split()
    result = []
    for url in plist:
        total_match = 0
        for word in words_to_search:
            match = 0
            conten =[]
            parag = search_abstract(url + '/html') # richiamo la funzione
            if parag != None: # se la lista non è nulla
                for item in parag: # per ogni elemento della lista
                    conten.append(item.text.replace('\t','').replace('\xa0','').replace('\n','').replace('\r',''))# tolgo le schifezze dalle stringhe contenute nella lista
            boolean = True
            for i in conten:
                if match == 1 :
                    boolean = False
                if boolean and word in i and word not in  exclude_word.stop_words and word != word_base:  # se trovo la parola nella descrizione
                    match = match + 1  # aumento il contatore di uno
            total_match += match
            tuple_result = (total_match, url)
        result.append(tuple_result)

    return result

