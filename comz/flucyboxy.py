# -*- coding: UTF-8 -*-.
# Author Sazxt
# My Team : Black Coder crush
import os as _osx
from py_compile import compile as comp
INC = {
		"onc":["cek","syntax"],
		"nca":["ok","not"]
			}
class flocbox(object):
	def __init__(self,file=None,systax=''):
		self.file = file
		if systax == INC['onc'][0]:
			self.ceks()
		if systax == INC["onc"][1]:
			self.cekSysntax()
		else:
			pass
	def ceks(self):
		if _osx.path.exists(self.file):
			return INC['nca'][0]
		else:
			return INC['nca'][1]
	def cekSysntax(self):
		"""
	Cek Systak Error Kalo Error Progres akan di hentikan !
		"""
		try:
			self.COMPLE = compile(open(self.file).read(),"<Test>","exec")
		except SyntaxError as ex:
			return INC["nca"][1]
		else:
			return INC["nca"][0]

class envroments:
	def __init__(self,powd='',filename=None,lisc=None,tems=1):
		self.fline = filename
		self.nmax = tems
		self.listed = [intel_converter(x) for x in lisc]
		# < ---- readfile --->
		self.reader = open(filename).read()
		if powd == 'random_zero':
			self.onesaan()

	def onesaan(self):
		self.count = 1

class bytecode:
	"""
	Memaparkan Pesan ke dalam bytcode
	"""
	def __init__(self,mesec,file):
		if "\\n" in mesec or "\\t" in mesec:
			self.message = mesec.replace("\\n","\n").replace("\\t","\t")
		else:
			self.message = mesec
		self.file = file
		self.compile = comp(self.file)
		self.fopned = open(self.file + "c").read()

	def writing_in_bytecode(self):
		self.filed = open(self.file,"w")
		self.filed.write(self.fopned+"\n"+self.message)
		self.filed.close()
		return _osx.remove(self.file + "c")

class cek_ascii:
	"""
	Cek Systax ascii mungkin saja tidak bisa di encode oleh beberapa fungsi
	"""
	def __init__(self,file=None):
		self.file = open(file).read()

	def run(self):
		try:
			self.file.encode("cp500")
		except Exception as e:
			exit("<---Unicode Error ---> \n%s"%(e))
		else:
			pass

daftar_nick = (lambda : """
	  { Black Coder Crush }
			~ since 2020/2021 ~
	──────────────────────────────────
	[+] - 4K17
	[+] - Dfv47
	[+] - Mr.Tr3v!0n
	[+] - Holilul Anwar
	[+] - R.I.P XerXez7
	[+] - Mr.Đ`HACK
	[+] - kiiroi senko
	[+] - Mr.g0y4n9
	[+] - mie gelas
	[+] - Tampansky ID
	[+] - Mr. Karwek
	[+] - Zhu Bai Lee
	[+] - BL4CK DR460N
	[+] - Mr. XsZ
	[+] - EvCf1703
	[+] - z34
	[+] - Phantomblizt
	[+] - Tn. Crash
	[+] - CapthaCode404_
	[+] - Gboy
	──────────────────────────────────""")

about = (lambda x : \
	"https://wa.me/+6283892081021" if x == "contact" else """
[+] Author : Sazxt
[+] Banner : Tr3v!0n
[-] Available Version Update 1.6
[+] Support only python2
		{ Black Coder Crush }
	──────────────────────────────────
	< python source code obfuscator. only obfuscator >
	< My Whatsapp : 0838-9208-1021 >
	
""")
#cek_ascii("uc.py").run()