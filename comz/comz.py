# -*- coding: UTF-8 -*-.
# Author Sazxt
# My Team : Black Coder crush
# Apa lo Mau Liat ? Mau Recode ? Silahkan Stah :v
# Style Coding Setiap Orang Berbeda
# <!-- Napom : # cp037 , cp424 , cp1026 , cp875 , cp424
import command
import obfus as kntod
import sys as _sys
from obfus import *
import datasav as _dat
import os as _osz
import flucyboxy as _box
import py_compile as _compis
import logging
from time import sleep
from os import system as _syst
reload(_sys)
_sys.setdefaultencoding('utf-8')
class comz(object):
	def __init__(self):
		self.cli = command.PARZE.CLI_PARSE()
		self.ARGS = self.cli.parse_args()
		self.INfile = self.ARGS.infiles
		self.Menu = self.ARGS.menu
		self.comp = self.ARGS.compile
		self.encode = self.ARGS.encode
		self._Repeat_ = self.ARGS.repeat
		self.OUTFil = self.ARGS.out
		self.TAMPILL = self.ARGS.tampilkan
		self.AnoNe()
	def lpgger(self,getLog=None,LevelName=None,message=None):
		if getLog:
			self.LOG = logging.getLogger(getLog)
		else:
			self.LOG = logging.getLogger("Obfuscator")
		self.LOG.setLevel(logging.DEBUG)
		self.cHanDler = logging.StreamHandler()
		self.cHanDler.setLevel(logging.DEBUG)
		self.foMatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s : %(message)s")
		self.cHanDler.setFormatter(self.foMatter)
		self.LOG.addHandler(self.cHanDler)
		if LevelName == "debug":
			self.LOG.debug(message);
		if LevelName == "info":
			self.LOG.info(message);
		if LevelName == "warning":
			self.LOG.warning(message);
		if LevelName == "error":
			self.LOG.error(message);
		if LevelName == "critical":
			self.LOG.critical(message);
	def MENU_SHOW(self):
		"""
		Menu
		"""
		_syst("clear")
		print (command.banners)
		ONS["ONC"] = "on"
		print command._MESSAGE
		print (
"""
──────────────────────────────────
<---- Auto Compile Marshal --->
{ 01 } Compile Marshal (repeat : max 400)
{ 02 } Compile Marshal > Base64 (repeat : max 400)
{ 03 } Compile Zlib (repeat : max 400)
{ 04 } Compile Base64 (repeat : max 400)
{ 05 } Compile base32 (repeat : max 400)
{ 06 } Compile Base16 (repeat : max 400)
{ 07 } Compile Binary (repeat : max 10)
{ 08 } Compile Marshal&Base64 (repeat : max 400)
{ 09 } Random Compile { No 1 - 8 } (repeat : max 400)
{ 10 } Encode Random {M,Z,B} (repeat : max 400)
{ 11 } Obfuscate By Sazxt 1
{ 12 } Obfuscate By Sazxt 2
{ 13 } Obfuscate By Sazxt 3 [ Fix ]
{ 14 } Obfuscate By Sazxt 4 [ Fix ]
{ 15 } Encode rot_13
{ 16 } Encode cp424
{ 17 } Encode bz2_codec
{ 18 } Encode utf_32_le
{ 19 } Encode cp500
{ 20 } Encode cp875
{ 21 } Encode cp1026
{ 22 } Encode utf_16
{ 23 } Encode utf_32
{ 24 } Encode utf_16_be
{ 25 } Encode uu_codec
{ 26 } Random Encode [ 15 - 25 ] Max { 100 }
{ 27 } Obfuscate By Sazxt 5
{ 28 } Pyc Inject Not
──────────────────────────────────
{ L } Lapor Bug ? WA
{ E } Exit
{ A } About
{ N } Nick Black Coder Crush
"""
	)
		try:
			self.CHOSEE()
		except KeyboardInterrupt:
			exit("Aborted !")
			#comz() #Reload <--
		except EOFError:
			exit();
	def CHOSEE(self):
		self.CHOSE = raw_input(command._CHOSE)
		if self.CHOSE == "1" or self.CHOSE == "01":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						kntod._mArshal(self.FIL,self.contc)
						_dat.fucking.pantad(SHEL[0],self.saving)
						ONS["File"] = self.saving
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "2" or self.CHOSE == "02":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						kntod._MarbAS(self.FIL,self.contc)
						_dat.fucking.pantad(SHEL[0],self.saving)
						ONS["File"] = self.saving
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "3" or self.CHOSE == "03":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						kntod.uno(self.FIL,self.contc).zlib()
						_dat.fucking.pantad(SHEL[0],self.saving)
						ONS["File"] = self.saving
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "4" or self.CHOSE == "04":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						kntod.uno(self.FIL,self.contc).base64()
						_dat.fucking.pantad(SHEL[0],self.saving)
						ONS["File"] = self.saving
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "5" or self.CHOSE == "05":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						kntod.uno(self.FIL,self.contc).base32()
						_dat.fucking.pantad(SHEL[0],self.saving)
						ONS["File"] = self.saving
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "6" or self.CHOSE == "06":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						kntod.uno(self.FIL,self.contc).base16()
						_dat.fucking.pantad(SHEL[0],self.saving)
						ONS["File"] = self.saving
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "7" or self.CHOSE == "07":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						kntod.uno(self.FIL,self.contc).bin()
						_dat.fucking.pantad(SHEL[0],self.saving)
						ONS["File"] = self.saving
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "8" or self.CHOSE == "08":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						kntod.uno(self.FIL,self.contc).base64_and_marshal()
						_dat.fucking.pantad(SHEL[0],self.saving)
						ONS["File"] = self.saving
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "9" or self.CHOSE == "09":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						ONS["File"] = self.saving
						#print self.saving
						acakaee(self.FIL,self.contc)
						#print SHEL
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
					except:
						exit("<--- Space Device Full -->")
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "10":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						ONS["File"] = self.saving
						varndvond(self.FIL,self.contc).compress()
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "11":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
					did_you_again(open(self.FIL).read())
					_dat.fucking.pantad(SHEL[0],ONS["File"])
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "12":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
					introduces(open(self.FIL).read())
					_dat.fucking.pantad(SHEL[0],ONS["File"])
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "13":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
					special_Compile_By_Sazxt_gans(self.FIL).somethink_puki()
					_dat.fucking.pantad(SHEL[0],ONS["File"])
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "14":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
					special_Compile_By_Sazxt_gans(self.FIL).anymore_flask()
					_dat.fucking.pantad(SHEL[0],ONS["File"])
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "15":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).rot_13()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
					except UnicodeDecodeError:
						print "ascii No Enoding"
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "16":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).cp424()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "17":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).bz2_codec()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "18":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).utf_32_le()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "19":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).cp500()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "20":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).cp875()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "21":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).cp1026()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "22":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).utf_16()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "23":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).utf_32()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "24":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).utf_16_be()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "25":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					try:
						_box.cek_ascii(self.FIL).run()
						self.count = raw_input("[!] Count : ")
						if self.count:
							self.contc = int(self.count)
							if 50  > abs(self.contc):
								pass
							else:
								exit("<--- Count Max 50 ---> ")
						else:
							self.contc = None
						ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						encode(self.FIL,self.contc).uu_codec()
						_dat.fucking.pantad(SHEL[0],ONS["File"])
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "26":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					_box.cek_ascii(self.FIL).run()
					self.count = raw_input("[!] Count : ")
					try:
						self.contc = int(self.count)
						self.saving = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
						ONS["File"] = self.saving
						pvp(self.FIL,self.contc).compress()
						print "──────────────────────────────────"
						print open(ONS["File"]).read()
						print "──────────────────────────────────"
						self.lpgger("finished","info","Succesfuly Obfuscate File at %s | %s"%(ONS["File"],_dat.kutil.convert(len(open(ONS["File"]).read()) + 124)))
					except ValueError:
						print >>_sys.stdout,"<-- Invalid ---> Count %s"%(str(self.count))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "27":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					_box.cek_ascii(self.FIL).run()
					ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
					enc_new(self.FIL).cisage()
					_dat.fucking.pantad(SHEL[0],ONS["File"])
					_box.bytecode(_dat.dats,ONS["File"]).writing_in_bytecode()
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "28":
			self.FIL = raw_input("[!] Insert File : ")
			if _box.flocbox(self.FIL,"cek").ceks() == "ok":
				if _box.flocbox(self.FIL,"syntax").cekSysntax() == "ok":
					print "[?] Using '\\t' tabs and '\\n' newline :v"
					self.messag = raw_input("[+] Pesan : ")
					ONS["File"] = self.FIL.replace(".py","_enc.py") if ".py" in self.FIL else self.FIL+".py"
					self.ni = open(ONS["File"],"w")
					self.ni.write(open(self.FIL).read())
					self.ni.close()
					_box.bytecode(self.messag,ONS["File"]).writing_in_bytecode()
					self.lpgger("Saving","info","Succesfuly Saving As %s | %s"%(ONS["File"],_dat.kutil.convert(len(open(ONS["File"]).read()) + 124)))
				else:
					print >>_sys.stdout,"<-- Invalid Syntax---> "
			else:
				print >>_sys.stderr,"IOError: [Errno 2] No such file or directory: %s"%(self.FIL)
		elif self.CHOSE == "a" or self.CHOSE == "A":
			print _box.about("kontol")
			lap = raw_input("[+] Back Menu : ")
			comz()
		elif self.CHOSE == "L" or self.CHOSE == "l":
			_osz.system("xdg-open "+_box.about("contact"))
		elif self.CHOSE == "n" or self.CHOSE == "N":
			print _box.daftar_nick()
			raw_input("Back >> ")
			comz()
		elif self.CHOSE == "e" or self.CHOSE == "E":
			exit("[+] Exit")
		else:
			print 'Invalid Menu ! %s'%(self.CHOSE)
			sleep(0.5)
			comz();
	# <----- argparsings --->
	def AnoNe(self):
		ONS["ONC"] = "off"
		if self.INfile:
			self.lpgger(None,"debug","Obfuscate File at %s"%(self.INfile))
			self.cekSyntak(self.INfile)
			if _osz.path.isfile(self.INfile):
				if self.comp == 1:
					if self._Repeat_:
						if self.OUTFil:
							kntod._mArshal(self.INfile,self._Repeat_)
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod._mArshal(self.INfile,self._Repeat_)
					else:
						if self.OUTFil:
							kntod._mArshal(self.INfile)
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod._mArshal(self.INfile)
				elif self.comp == 2:
					if self._Repeat_:
						if self.OUTFil:
							kntod._MarbAS(self.INfile,self._Repeat_)
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod._MarbAS(self.INfile,self._Repeat_)
					else:
						if self.OUTFil:
							kntod._MarbAS(self.INfile,self._Repeat_)
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod._MarbAS(self.INfile)
				elif self.comp == 3:
					if self._Repeat_:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).zlib()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).zlib()
					else:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).zlib()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).zlib()
				elif self.comp == 4:
					if self._Repeat_:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).base64()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).base64()
					else:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).base64()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).base64()
				elif self.comp == 5:
					if self._Repeat_:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).base32()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).base32()
					else:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).base32()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).base32()
				elif self.comp == 6:
					if self._Repeat_:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).base16()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).base16()
					else:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).base16()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).base16()
				elif self.comp == 7:
					if self._Repeat_:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).bin()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).bin()
					else:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).bin()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).bin()
				elif self.comp == 8:
					if self._Repeat_:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).base64_and_marshal()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).base64_and_marshal()
					else:
						if self.OUTFil:
							kntod.uno(self.INfile,self._Repeat_).base64_and_marshal()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							kntod.uno(self.INfile,self._Repeat_).base64_and_marshal()
				elif self.comp == 9:
					if self._Repeat_:
						if self.OUTFil:
							try:
								ONS["File"] = self.OUTFil
								acakaee(self.INfile,self._Repeat_)
								print "Saving As - %s "%(self.OUTFil)
							except:
								exit("<--- Space Device Full -->")
						else:
							exit("# Sulution : comz -i FILE -c 9 -r INT -o OutFile")
					else:
						if self.OUTFil:
							try:
								ONS["File"] = self.OUTFil
								acakaee(self.INfile,2)
								print "Saving As - %s "%(self.OUTFil)
							except:
								exit("<--- Space Device Full -->")
						else:
							exit("# Sulution : comz -i FILE -c 9 -r INT -o OutFile")
				elif self.comp == 10:
					if self._Repeat_:
						if self.OUTFil:
							ONS["File"] = self.OUTFil
							varndvond(self.INfile,self._Repeat_).compress()
							print "Saving As - %s "%(self.OUTFil)
						else:
							exit("# Sulution : comz -i FILE -c 10 -r INT -o OutFile")
					else:
						if self.OUTFil:
							ONS["File"] = self.OUTFil
							varndvond(self.INfile,2).compress()
							print "Saving As - %s "%(self.OUTFil)
						else:
							exit("# Sulution : comz -i FILE -c 10 -r INT -o OutFile")
				elif self.comp == 11:
					if self.OUTFil:
						did_you_again(open(self.INfile).read())
						print "Saving As - %s "%(self.OUTFil)
						_dat.fucking.pantad(SHEL[0],self.OUTFil)
					else:
						exit("# Sulution : comz -i FILE -c 11 -o OutFile")
				elif self.comp == 12:
					if self.OUTFil:
						introduces(open(self.INfile).read())
						print "Saving As - %s "%(self.OUTFil)
						_dat.fucking.pantad(SHEL[0],self.OUTFil)
					else:
						exit("# Sulution : comz -i FILE -c 12 -o OutFile")
				elif self.comp == 13:
					if self.OUTFil:
						special_Compile_By_Sazxt_gans(self.INfile).somethink_puki()
						print "Saving As - %s "%(self.OUTFil)
						_dat.fucking.pantad(SHEL[0],self.OUTFil)
					else:
						exit("# Sulution : comz -i FILE -c 13 -o OutFile")
				elif self.comp == 14:
					if self.OUTFil:
						special_Compile_By_Sazxt_gans(self.INfile).anymore_flask()
						print "Saving As - %s "%(self.OUTFil)
						_dat.fucking.pantad(SHEL[0],self.OUTFil)
					else:
						exit("# Sulution : comz -i FILE -c 14 -o OutFile")
				elif self.comp == 15:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).rot_13()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).rot_13()
					else:
						if self.OUTFil:
							encode(self.INfile,1).rot_13()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).rot_13()
				elif self.comp == 16:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).cp424()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).cp424()
					else:
						if self.OUTFil:
							encode(self.INfile,1).cp424()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).cp424()
				elif self.comp == 17:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).bz2_codec()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).bz2_codec()
					else:
						if self.OUTFil:
							encode(self.INfile,1).bz2_codec()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).bz2_codec()
				elif self.comp == 18:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).utf_32_le()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).utf_32_le()
					else:
						if self.OUTFil:
							encode(self.INfile,1).utf_32_le()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).utf_32_le()
				elif self.comp == 19:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).cp500()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).cp500()
					else:
						if self.OUTFil:
							encode(self.INfile,1).cp500()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).cp500()
				elif self.comp == 20:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).cp875()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).cp875()
					else:
						if self.OUTFil:
							encode(self.INfile,1).cp875()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).cp875()
				elif self.comp == 21:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).cp1026()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).cp1026()
					else:
						if self.OUTFil:
							encode(self.INfile,1).cp1026()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).cp1026()
				elif self.comp == 22:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).utf_16()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).utf_16()
					else:
						if self.OUTFil:
							encode(self.INfile,1).utf_16()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).utf_16()
				elif self.comp == 23:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).utf_32()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).utf_32()
					else:
						if self.OUTFil:
							encode(self.INfile,1).utf_32()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).utf_32()
				elif self.comp == 24:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).utf_16_be()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).utf_16_be()
					else:
						if self.OUTFil:
							encode(self.INfile,1).utf_16_be()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).utf_16_be()
				elif self.comp == 25:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).uu_codec()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							self._count_cek(self._Repeat_)
							encode(self.INfile,self._Repeat_).uu_codec()
					else:
						if self.OUTFil:
							encode(self.INfile,1).uu_codec()
							_dat.fucking.pantad(SHEL[0],self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
						else:
							encode(self.INfile,1).uu_codec()
				elif self.comp == 26:
					_box.cek_ascii(self.INfile).run()
					if self._Repeat_:
						if self.OUTFil:
							self._count_cek(self._Repeat_)
							ONS["File"] = self.OUTFil
							pvp(self.INfile,self._Repeat_).compress()
							print "Saving As - %s "%(self.OUTFil)
							print "──────────────────────────────────"
							print open(ONS["File"]).read()
							print "──────────────────────────────────"
							self.lpgger("finished","info","Succesfuly Obfuscate File at %s | %s"%(ONS["File"],_dat.kutil.convert(len(open(ONS["File"]).read()) + 124)))
						else:
							exit("# Sulution : comz -i FILE -c 26 -r [ repeat ] -o OutFile")
					else:
						if self.OUTFil:
							ONS["File"] = self.OUTFil
							pvp(self.INfile,0).compress()
							print "Saving As - %s "%(self.OUTFil)
							print "Saving As - %s "%(self.OUTFil)
							print "──────────────────────────────────"
							print open(ONS["File"]).read()
							print "──────────────────────────────────"
							self.lpgger("finished","info","Succesfuly Obfuscate File at %s | %s"%(ONS["File"],_dat.kutil.convert(len(open(ONS["File"]).read()) + 124)))
						else:
							exit("# Sulution : comz -i FILE -c 26 -o OutFile")
				elif self.comp == 27:
					if self.OUTFil:
						enc_new(self.INfile).cisage()
						print "Saving As - %s "%(self.OUTFil)
						_dat.fucking.pantad(SHEL[0],self.OUTFil)
					else:
						exit("# Sulution : comz -i FILE -c 27 -o OutFile")
				else:
					if self.OUTFil:
						kntod._mArshal(self.INfile)
						_dat.fucking.pantad(SHEL[0],self.OUTFil)
						self.lpgger("Saving","info","Saving As File { %s }"%(self.OUTFil))
					else:
						self.lpgger("System","warning","Not Selection Progress Please --help")
						kntod._mArshal(self.INfile)
			else:
				print "< -- No fileName --> at %s"%(self.INfile)
		if self.TAMPILL:
			if SHEL:
				print "──────────────────────────────────"
				print SHEL[0]
				print "──────────────────────────────────"
				self.lpgger("finished","info","Succesfuly Obfuscate File at %s | %s"%(self.INfile,_dat.kutil.convert(len(SHEL[0]) + 124)))
			else:
				print "──────────────────────────────────"
				print open(self.OUTFil).read()
				print "──────────────────────────────────"
				self.lpgger("finished","info","Succesfuly Obfuscate File at %s | %s"%(self.INfile,_dat.kutil.convert(len(open(self.OUTFil).read()) + 124)))
		elif self.Menu:
			self.MENU_SHOW()
		if SHEL:
			if not self.TAMPILL:
				print "──────────────────────────────────"
				print open(self.OUTFil if self.OUTFil else ONS["File"]).read() if ONS["ONC"] == "on" else SHEL[0]
				print "──────────────────────────────────"
				self.lpgger("finished","info","Succesfuly Obfuscate File at %s | %s"%(self.OUTFil if self.OUTFil else self.INfile if ONS["ONC"] == "off" else ONS["File"],_dat.kutil.convert(len(SHEL[0]) + 124)))
			else:
				pass
		if self.encode:
			comp(self.encode)
			self.lpgger("compile","debug","Succesfuly Compile as %s"%(self.encode))
		else:
			if not self.Menu and not self.INfile and not self.encode:
				command.inu().baf();
			else:
				pass

	def cek(self):
		pass

	def _count_cek(self,count = 0):
		if 50 > abs(count):
			pass
		else:
			exit("<---Count max 50--->")

	def cekSyntak(self,file):
		if _box.flocbox(file,"syntax").cekSysntax() == "ok":
			pass
		else:
			self.lpgger("Error","warning","<--Syntax Error -->")
			exit()

class HandleInterupt(Exception):
	"""
	# handle ctrl-C
	"""
	pass
