#from obfus import SHEL as sek
# <--- Thanks To zvtyrdt.id / val
import os,time,random,string
dats = ""
class kutil:
	@staticmethod
	def convert(n=None, format='%(value).1f %(symbol)s', symbols='customary'):
		SYMBOLS = {
					'customary': ('B', 'K', 'Mb', 'G', 'T', 'P', 'E', 'Z', 'Y'),
					'customary_ext': ('byte', 'kilo', 'mega', 'giga', 'tera', 'peta', 'exa',
					'zetta', 'iotta'),
					'iec': ('Bi', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi'),
					'iec_ext': ('byte', 'kibi', 'mebi', 'gibi', 'tebi', 'pebi', 'exbi',
					'zebi', 'yobi'),
					}
		n = int(n)
		if n < 0:
			raise ValueError("n < 0")
		symbols = SYMBOLS[symbols]
		prefix = {}
		for i, s in enumerate(symbols[1:]):
			prefix[s] = 1 << (i + 1) * 10
		for symbol in reversed(symbols[1:]):
			if n >= prefix[symbol]:
				value = float(n) / prefix[symbol]
				return format % locals()
			return format % dict(symbol=symbols[0], value=n)
class fucking:
	@staticmethod
	def pantad(list,saving):
		global dats
		Lonte = open(saving,"w")
		meki = os.uname()
		date = time.ctime()
		a = []
		for x in range(5):
			a.append(random.choice(string.ascii_letters).lower())
			a.append(random.choice(string.ascii_letters).upper())
			a.append(str(random.choice(range(1,9))))
		key = "".join(a)
		is_time = time.ctime()
		dat = {
					"garis":"#------------------------------------------------------------------------------------------------------------------------------\n",
					"github":"# github  : https://github.com/Sazxt/comz\n",
					"from":"# from "+meki[0]+"\n",
					"local":"# "+meki[1]+" : "+meki[4]+"\n",
					"key":"# key : saz-"+key+"\n",
					"date":"# date : "+is_time+"\n"
				}
		dats += dat["garis"]+"# Obfuscate By Sazxt Thanks To Black Coder Crush\n"+dat["github"]+dat["from"]+dat["local"]+dat["key"]+dat["date"]+dat["garis"]
		if "#Compile By Sazxt" in list:
			Lonte.write("# Folow github : https://github.com/Sazxt/comz\n"+list)
		else:
			Lonte.write(dat["garis"]+"# Obfuscate By Sazxt Thanks To Black Coder Crush\n"+dat["github"]+dat["from"]+dat["local"]+dat["key"]+dat["date"]+dat["garis"]+list)
		Lonte.close()