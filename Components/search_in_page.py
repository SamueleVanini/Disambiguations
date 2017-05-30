import requests
import bs4
from Components import exclude_word

# ritorna il contenitore delle informazioni della pagina web


def search_abstract(url):
    page = requests.get(url).text
    soup = bs4.BeautifulSoup(page, 'lxml')
    try:
        div = soup.findAll("div", {"class": "it"})[0]
    except IndexError:
        print("l'articolo non possiede un abstract: " + url)
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


def search_in_abstract(plist):
    match = 0
    #plist = search_urls(word_base)
    for i in plist:
        parag = search_abstract(i + '/html')
        if parag is not None:
            abstract = parag.text  # richiamo la funzione
        word_to_search = 'di'  # parola da cercare che nel testo può essere prima o dopo della parola chiave

        if word_to_search not in exclude_word.stop_words:
            if word_to_search in abstract:  # se trovo la parola nella descrizione
                match = match + 1  # aumento il contatore di uno

    return match
