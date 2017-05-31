import codecs
from Components import search_in_page


def main():
    word_base = 'Albanella'
    file = codecs.open('File/Concetto.txt', 'rU', 'utf-8')
    match = search_in_page.search_in_abstract(file, word_base)
    print(sorted(match, reverse=True))

if __name__ == '__main__':
    main()
