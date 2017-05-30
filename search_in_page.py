import re
import requests
from urllib import *
import string
import bs4

#ritorna il contenitore delle informazioni della pagina web
def search_abstract(url): 
	page = requests.get(url).text
	soup = bs4.BeautifulSoup(page, 'lxml')
	try:
		div = soup.findAll("div", { "class" : "it" })[0]
	except IndexError:
		print ("l'articolo non possiede un abstract")
		div = None
	return div

def main():
	word = 'base' #parola da cercare con dbpedia
	word = word[0].upper() + word[1:] #metto la prima lettera maiuscola perchè l'url vuole così
	plist = [] #creo una lista vuota 
	software = 0 #contatore impostato a zero
	url = 'http://it.dbpedia.org/resource/' + word + '/html' #url della pagina web
	# trovo l'html della pagina web
	page = requests.get(url).text 
	soup = bs4.BeautifulSoup(page, 'lxml')
	div = soup.findAll("a", { "class" : "isLocal" }) # trovo il contenitore dei link
	for i in div: # per ogni link tiro fuori l'url pulito e lo metto nella lista
		new_url = i.get('title')
		new_url = new_url.replace('<','')
		new_url = new_url.replace('>','')
		plist.append(new_url)
	plist = plist[1:]
	print(plist)
	#first_link = plist[4] # prendo il primo elemento della lista
	#print(first_link + '/html')
	for i in plist:
		parag = search_abstract(i + '/html')
		if parag != None:
			abstract = parag.text #richiamo la funzione
		print (abstract)
		parola = 'base' # parola da cercare che nel testo può essere prima o dopo della parola chiave
		 
		if parola in abstract: # se trovo la parola nella descrizione 
			software = software + 1 # aumento il contatore di uno

	print(software) # stampo software
if __name__ == '__main__':
	main()       