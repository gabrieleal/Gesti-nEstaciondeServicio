class Promo:
	def __init__(self,tipo_promo,cant_punto,nombre_tarjeta):
		self.__tipo_promo       =   tipo_promo
		self.__cant_punto        =   cant_punto
		self.__nombre_tarjeta =   nombre_tarjeta

	def VerTipoPromo(self):
		return self.__tipo_promo
	
	def VerCantPunto(self):
		return self.__cant_punto
		
	def VerNomTarjeta(self):
		return self.__nombre_tarjeta
		
	def ModTipoPromo(self,otro):
		self.__tipo_promo = otro
	
	def ModCantPunto(self,otro):
		self.__cant_punto = otro

	def ModNomTarjeta(self,otro):
		self.__nombre_tarjeta = otro



