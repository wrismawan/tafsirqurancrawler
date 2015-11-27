import crawler.py 

def fix():
	error = [
		[15, 25],
		[26, 106],
		[26, 107],
		[26, 108],
		[26, 109],
		[26, 110],
		[26, 111],
		[26, 112],
		[26, 113],
		[26, 114],
		[26, 115],
		[26, 116],
		[26, 117],
		[26, 118],
		[26, 119],
		[26, 120],
		[26, 121],
		[26, 122],
		[26, 123],
		[26, 124],
		[26, 125],
		[26, 126],
		[26, 127],
		[26, 128],
		[26, 144],
		[26, 145],
		[26, 146],
		[26, 147],
		[26, 148],
		[26, 149]
	]


	for e in error:
		tafsir = get_tafsir(e[0],e[1])
		text = "{0}|{1}|{2}".format(e[0], e[1], str(tafsir))
		print text


def reformat():
	quran_list = []
	quran = readJSON("result/result_tafsir.json")
	for item in quran:
		quran_list.append([item['surat'], item['ayat'], item['tafsir']])

	writeToCSV(quran_list, "result/tafsir.csv")