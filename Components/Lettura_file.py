import codecs

def create_dict(word_to_search):
    dict = {}
    file = codecs.open('File_dbpedia/itwiki-20150121-disambiguations.ttl', 'rU', 'utf-8')
    # file = codecs.open('prova', 'rU', 'utf-8')
    list_help = []
    dict_stop = False
    for raw in file:
        if raw != '# started 2015-01-29T09:18:58Z\r\n' or raw != '# completed 2015-01-29T09:54:37Z\r\n':
            key = raw.split()[0]
            value = raw.split()[2]
            if key.upper() == '<HTTP://IT.DBPEDIA.ORG/RESOURCE/'+word_to_search.upper()+'>':
                dict_stop = True
                list_help.append(value)
                dict[key] = tuple(list_help)
            if dict_stop == True and key.upper() > '<HTTP://IT.DBPEDIA.ORG/RESOURCE/'+word_to_search.upper()+'>':
                break
    file.close()
    return list(dict.values())