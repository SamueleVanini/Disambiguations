import codecs

dict = {}

def create_dict(file, word_to_search):
    list_help = []
    i = 0
    dict_stop = False
    for raw in file:
        print (i)
        if raw != '# started 2015-01-29T09:18:58Z\r\n' or raw != '# completed 2015-01-29T09:54:37Z\r\n':
            key = raw.split()[0]
            value = raw.split()[2]
            if key.upper() == '<HTTP://IT.DBPEDIA.ORG/RESOURCE/'+word_to_search.upper()+'>':
                dict_stop = True
                list_help.append(value)
                dict[key] = tuple(list_help)
            if dict_stop == True and key.upper() > '<HTTP://IT.DBPEDIA.ORG/RESOURCE/'+word_to_search.upper()+'>':
                break
        i += 1

def main():
    file = codecs.open('itwiki-20150121-disambiguations.ttl', 'rU', 'utf-8')
    #file = codecs.open('prova', 'rU', 'utf-8')
    word_to_search = 'Basic'
    create_dict(file, word_to_search)
    print (dict)

if __name__ == '__main__':
    main()