class tipodato(Exception):
	def __init__(self,dato):
		self.dato=dato
	def __str__(self) :
		return str (self.dato)
class noexiste(Exception):
	def __init__(self,parametro):
		self.parametro=parametro
	def __str__(self) :
		return str (self.parametro)
class campoVacio(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self) :
		return str (self.value)
class ValorErroneo(Exception):
	def __init__(self,valor):
		delf.valor=valor
	def __str__(self):
		return str(self.valor)
class FueradeIndice(Exception):
	def __init__(self,indice):
		self.indice=indice
	def __str__(self):
		return str ( self.indice )
