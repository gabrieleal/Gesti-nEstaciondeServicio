from classPlayero import *
from classPromo import *
from classSurtidor import *


class Administracion:
	def __init__ (self):
		self.__ListaSurtidor      = []
		self.__ListaPromocion = []
		self.__ListaPlayero       = []

#-----------------SURTIDOR---------------------------------				
	def HabilitarSurtidor(self,sur):	
		for x in self.__ListaSurtidor:
			if x.vernumero() == sur.vernumero():
				sur.modestadohabilitar()
	def DeshabilitarSurtidor(self,sur):
		if isinstance(sur,Surtidor):
			for x in self.__ListaSurtidor:
				if x.vernumero() == sur.vernumero():
					sur.modestadodeshabilitar()
	def AgregarSurtidor(self,sur):
			self.__ListaSurtidor.append(sur)
			
	
	
			
	def MostrarListaSur(self):
		return self.__ListaSurtidor
#..........................................................
#................PLAYERO----------------------------------	
	def ExistePlayero(self,dni): 	#Busca en la lista playero. Si lo encuentra no lo da de alta. sino lo da de alta y lo agrega en la lista
		for x in self.__ListaPlayero:
			if x.verDni() == dni:
				return True
	def AgregarPlayero(self,playero):
		if isinstance(playero,Playero):
			self.__ListaPlayero.append(playero)
	
	def EliminarPlayero(self,playero):
		if isinstance(playero,Playero):
			for x in self.__ListaPlayero:
				if x.verDni() == playero.verDni():
					self.__ListaPlayero.remove(x)
	def MostrarListaPla(self):
		return self.__ListaPlayero		
	
	def MostrarListaPro(self):
		return self.__ListaPromocion
#------------------PROMO--------------------------------------------------------		
	def darAltaPromo(self,promo):
		if isinstance(promo,Promo):
			self.__ListaPromocion.append(promo)
			return ('la promocion ah sido dada de alta exitosamente')
		
	def darBajaPromo(self,promo):
		if isinstance(promo,Promo):
			for x in self.__ListaPromocion:
				if x.VerTipoPromo() == promo.VerTipoPromo() and x.VerCantPunto() == promo.VerCantPunto() and x.VerNomTarjeta() ==promo.VerNomTarjeta():
					self.__ListaPromocion.remove(x)
		else:
			print("Esta promocion no fue dada de alta")
					 
#----------------------ORDENAMIENTO------------------------------------------------------------
	def Ordenar(self,datos):
		n=len(datos)-1
		for i in range(n-1):
			for j in range(i+1,n):
				if(datos[i]<datos[j]):
					swap=datos[i]
					datos[i]=datos[j]
					datos[j]=swap
		return (datos) 
						 


