from Components import search_in_page, Lettura_file

def main():
    word_base = 'Link'
    list = Lettura_file.create_dict(word_base)
    list_urls = []
    for i in range(len(list[0])):
        url = list[0][i]
        url = url.replace('<', '')
        url = url.replace('>', '')
        list_urls.append(url)
    match = search_in_page.search_in_abstract(word_base, list_urls)
    print(match)

if __name__ == '__main__':
    main()