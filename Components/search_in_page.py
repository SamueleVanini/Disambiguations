"""search_in_page.py
requests = modulo utilizzato per le richieste agli url
bs4 = modulo per interrogazione web
re = modulo usato per ricerca di espressioni regolari
search_in_page = funzione per la ricerca nella pagina (urls, abstarct, count match, ecc.)
"""
import re
import requests
import bs4
from Components import exclude_word


def search_abstract(url):
    """
    Funzione che ricerca testo utile nella web page
    :param url: url della pagina su cui si cerca l'abstract
    :return div: testo della pagina
    """
    page = requests.get(url).text
    soup = bs4.BeautifulSoup(page, 'lxml')
    try:
        div = soup.findAll("div", {"class": "fixed"})
    except IndexError:
        print("La pagina non contiene informazioni: " + url)
        div = None
    return div


def search_urls(word_base):
    """
    Funzione che ricerca data una parola la relativa pagina dbpedia di disambiguazione
    :param word_base: parola di cui si vuole avere il concetto
    :return plist: lista di url derivanti dalla pagina di disambiguazione
    """
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


def clean_string(item):
    """
    Funzione che rimuove dalla stringa da caretteri indesiderati
    :param item: stringa su cui effettuare la rulizia
    :return item: stringa dopo la rimozione
    """
    return item.text.replace('\t', '').replace('\xa0', '').replace('\n', '').replace('\r', '')


def search_in_abstract(file, word_base):
    """
    :param file: file contente il concetto del termine da cercare
    :param word_base: indica la parola su cui si basa il concetto che si vuole cercare
    :return result: lista contenete match + url per ogni url
    """
    plist = search_urls(word_base)
    words_to_search = file.read()
    words_to_search = re.sub(r'[^\w\s]', '', words_to_search)
    words_to_search = words_to_search.split()
    result = []
    tuple_result = ()
    for url in plist:
        total_match = 0
        for word in words_to_search:
            match = 0
            conten = []
            parag = search_abstract(url + '/html')
            if parag is not None:
                for item in parag:
                    conten.append(clean_string(item))
            boolean = True
            for i in conten:
                if match == 1:
                    boolean = False
                if boolean and word in i and word not in exclude_word.USELES_WORDS and word not in \
                   word_base:
                    match = match + 1
            total_match += match
            tuple_result = (total_match, url)
        result.append(tuple_result)

    return result
