from Components import search_in_page, Lettura_file

def main():
    word_to_search = 'Basic'
    Lettura_file.create_dict(word_to_search)
    print(dict)


if __name__ == '__main__':
    main()