from classAdministracion import *
from classPlayero import *
class Surtidor:
	def __init__(self,nro,tipo,valor,remanente):
		self.__estado=False
		self.__nro=nro
		self.__tipo=tipo
		self.__valor=valor
		self.__remanente=remanente
		self.__playeroasignado=None
		self.__ltsenventa=0							#Litros en una venta
		self.__montodelaventa=0					#Dinero de una venta
		self.__cant_lts_vendidos=0				#Cantidad de litros totales
		self.__ventatotales=0						#Dinero recaudado por cada surtidor
#-------------- BASICO COMIENZO -------------------------#
	def verventastotales(self):
		return self.__ventatotales
	def verestado(self):
		return self.__estado
	def vernumero(self):
		return self.__nro
	def vertipo(self):
		return self.__tipo
	def vervalor(self):
		return self.__valor
	def verremanente(self):
		return self.__remanente
	def verplayero(self):
		return self.__playeroasignado
	def verltsenventa(self):
		return self.__ltsenventa
	def vermontoventa(self):
		return self.__montodelaventa
	def verltsvendidos(self):
		return self.__cant_lts_vendidos

	def  modnumero(self,otro):
		self.__nro=otro
	#--------------modificadores directos de estado----------#	
	def  modestadohabilitar(self):
		self.__estado=True
	def  modestadodeshabilitar(self):
		self.__estado=False
	#--------------------------------------------------------#	
	def  modtipo(self,otro):
		self.__tipo=otro
	def  modvalor(self,otro):
		self.__valor=otro
	def  modremanente(self,otro):
		self.__remanente-=otro
	def  modplayeroasig(self,pla):
		if isinstance (pla,Playero):
			self.__playeroasignado=pla
	def  modltsenventa(self,otro):
		self.__ltsenventa=otro
	def  modmontoventa(self,otro):
		self.__montoventa=otro
	def  modltsvendidos(self,otro):
		self.__cant_lts_vendidos+=otro
	def modventastotales(self,otro):
		self.__ventatotales+=otro
#---------------------------- BASICO FIN -------------------------------#
	def cargaryocupar(self,playero,litros):
		if isinstance (playero,Playero):
			self.modestado(False)
			self.modltsenventa(litros)
			valor=float(self.__valor()*self.__ltsenventa())
			self.modltsvendidos(litros)
			self.modremanente(-litros)
			self.modventastotales(valor)
			playero.modTotal(valor)
			return ("el valor de la compra es ",valor)
			print ('ingrese el monto recibido: ')
			pago=float(input())
			self.cobraryhabilitar(valor,pago)
	def cobraryhabilitar(self,valor,pago):
		v=(pago-valor)
		print ('el vuelto es de ',v)
		self.modestado(True)
#------    COMPARACION  --------------------------------------------------
	def __cmd__(self,otro):
		dif= self.__ventatotales - otro.__ventatotales
		if dif>0:
			return 1
		elif dif<0:
			return -1
		else:
			return 0			
	def compMonto(self,otro):
		return self.__cmd__(otro)


