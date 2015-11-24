import urllib
from mylib import *
from bs4 import BeautifulSoup
import json

REQUEST_ERROR = 'request_error'
PARSED_ERROR = 'parsed_error'


def get_tafsir(surat, ayat):
	url = 'http://quran.ksu.edu.sa/interface.php?ui=pc&do=tafsir&author=indonesian&sura='+str(surat)+'&aya='+str(ayat);
	try:
		html = urllib.urlopen(url).read()
	except Exception, e:
		return REQUEST_ERROR

	parsed_html = BeautifulSoup(html, 'lxml')

	try:
		text_tafsir = parsed_html.body.find('div', attrs={'class':'tafheem_comments'}).text
	except Exception, e:
		text_tafsir = PARSED_ERROR

	return text_tafsir

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
		surat_list.append(surat_obj)

	writeJSON(json.dumps(surat_list), "surat.json")

def save_result(surat, ayat, result):
	fileName = "result_{0}_{1}.json"
	writeJSON(json.dumps(result), fileName)

def do_crawl(surats):
	result = []
	for surat in surats:
		for ayat in xrange(1,surat['ayat']+1):
			tafsir = get_tafsir(surat['no'],ayat)
			
			print "*********** QS {0} - Ayat {1} **********".format(surat['nama'], ayat)
			print tafsir
			
			# if request error, save current tafsir result (backup)
			if (tafsir == REQUEST_ERROR):
				save_result(surat=surat['nama'], ayat=ayat, result=tafsir)
				print "****** REQUEST ERROR ******"
			
			result.append({ 'surat' : 1, 'ayat' : ayat, 'tafsir' :  tafsir })

			
	save_result(surat=surat['nama'], ayat=ayat, result=tafsir)
	
def __main__():
	surats = readJSON("surat.json")
	do_crawl(surats[:30])

__main__()