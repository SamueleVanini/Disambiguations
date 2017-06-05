""" Main.py
codecs = modulo per l'apertura di file unicode
search_in_page = funzione per la ricerca nella pagina (urls, abstarct, count match, ecc.)
"""
import codecs
from Components import search_in_page


def main():
    """
    Modulo di avvio del programma word_base in dica la parola di cui si vuole avere l'url del
    concetto, file indica il file contenete un testo per risalire al concetto adeguato
    """
    word_base = 'Albanella'
    file = codecs.open('File/Concetto.txt', 'rU', 'utf-8')
    match = search_in_page.search_in_abstract(file, word_base)
    print(sorted(match, reverse=True))

if __name__ == '__main__':
    main()
