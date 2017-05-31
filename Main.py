import codecs
from Components import search_in_page


def main():
    word_base = 'Albanella'
    file = codecs.open('File/Concetto.txt', 'rU', 'utf-8')
    '''
    list = Lettura_file.create_dict(word_base)
    list_urls = []
    for i in range(len(list[0])):
        url = list[0][i]
        url = url.replace('<', '')
        url = url.replace('>', '')
        list_urls.append(url)
    '''
    match = search_in_page.search_in_abstract(file, word_base)
    print(sorted(match, reverse=True))

if __name__ == '__main__':
    main()
