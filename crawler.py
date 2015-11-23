import urllib
from mylib import *
from bs4 import BeautifulSoup
import json

def get_tafsir(surat, ayat):
	url = 'http://quran.ksu.edu.sa/interface.php?ui=pc&do=tafsir&author=indonesian&sura='+str(surat)+'&aya='+str(ayat);
	html = urllib.urlopen(url).read()
	parsed_html = BeautifulSoup(html, 'lxml')
	try:
		text_tafsir = parsed_html.body.find('div', attrs={'class':'tafheem_comments'}).text
	except Exception, e:
		text = "error"
	return text_tafsir

def do_crawl(surats):
	result = []
	for surat in surats:
		for ayat in xrange(1,surat['ayat']+1):
			print "*********** QS {0} - Ayat {1}".format(surat['nama'], ayat)
			t = { 'surat' : 1, 'ayat' : ayat, 'tafsir' : get_tafsir(surat['no'],ayat) }
			print t['tafsir']
			result.append(t)

	writeJSON(json.dumps(result), "result.json")

def reformat_data_surat():
	surats = CSV2List("surat.csv")
	surat_list = []
	for surat in surats:
		surat_obj = {
			"no" : int(surat[0]),
			"nama" : surat[1],
			"arti" : surat[2],
			"ayat" : int(surat[3]),
			"tempat_turun" : surat[4],
			"urutan_turun" : int(surat[5])
		}
		print surat_obj
		surat_list.append(surat_obj)

	writeJSON(json.dumps(surat_list), "surat.json")

def __main__():
	surats = readJSON("surat.json")
	do_crawl(surats)

__main__()