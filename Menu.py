#_*_ coding: utf-8 _*_
import os
import sys
from classPlayero import *
from classPromo import *
from classSurtidor import *
from classAdministracion import *
import datetime
from classError import *

adm1=Administracion()
Ahorrado_Clientes = 0
Recaudado_Estacion = 0

def ordenar (lis):     #Funcion de ordenamiento burbuja
	num = len(lis)
	i=0
	while i < num:
		j=i
		while j < num:
			if lis[i] > lis[j]:
				aux = lis[i]
				lis[i] = lis[j]
				lis[j] = aux
			j = j + 1
		i +=1
	return (lis) 		
pla=Playero('Sebastian Gonzalez',26589741,10,18)
pla1=Playero('Pedro Garcia',24807741,18,8)
pla2=Playero('Alberto Perez',35145781,8,16)
pla3=Playero('Bayron Hernandez',40236514,8,16)
pla4=Playero('Sebastian Gonzalez',39841257,10,18)
adm1.AgregarPlayero(pla)
adm1.AgregarPlayero(pla1)
adm1.AgregarPlayero(pla2)
adm1.AgregarPlayero(pla3)
adm1.AgregarPlayero(pla4)
sur=Surtidor(1,'Disel',40,1000)
sur1=Surtidor(2,'Infinia',53,1500)
sur2=Surtidor(3,'Super',45,2000)
sur3=Surtidor(4,'InfiniaDisel',49.25,100)
sur4=Surtidor(5,'Super',40,958)
adm1.AgregarSurtidor(sur)
adm1.AgregarSurtidor(sur1)
adm1.AgregarSurtidor(sur2)
adm1.AgregarSurtidor(sur3)
adm1.AgregarSurtidor(sur4)
pro=Promo('% de Descuento',25,'YPF Serviclub')
pro2=Promo('Puntos',125,'Clarin 365 Plus')
pro3=Promo('% de Descuento',15,'Banco la Nacion')
pro4=Promo('Puntos',500,'Cencosud')
adm1.darAltaPromo(pro)
adm1.darAltaPromo(pro2)
adm1.darAltaPromo(pro3)
adm1.darAltaPromo(pro4)
def BorrarPantalla():
	return os.system('cls')
def controlnombre(i):
	
	try:
		for p in i:
			if ord(p) > 64 and ord(p) < 91 or ord(p) < 123 and ord(p)>95 or ord(p)==32 :
				pass
			else:
				raise ValueError
		return 1		
	
	except (ValueError):
		return ('Error, ingrese datos validos')

#--------------Funciones Recursivas-------------
#def ListarPla(lis,tam):
#	if tam==0:
#		return lis[0]
#	else:
#		return ListarPla(lis,tam-1)
#----------------------------------------------------------

def EstacionServicio():
	while True:
		
		BorrarPantalla()
		print ("================================================================")
		print ("	             Estacion de Servicio								")
		print ("================================================================")
		print ("1- Surtidores\n")
		print ("2- Playeros\n")
		print ("3- Promociones\n")
		print ("4- Administracion\n")
		print ("5- Salir\n")
	
	
	
		try:
			opcionMenu = input("Ingrese una opción: ")
			if opcionMenu == "1":
				BorrarPantalla()
				MenuSurtidor()
			elif opcionMenu == "2":
				BorrarPantalla()
				MenuPlayero()
				
			elif opcionMenu == "3":
				BorrarPantalla()
				MenuPromocion()
			elif opcionMenu == "4":
				BorrarPantalla()
				MenuAdmin()			
			elif opcionMenu == "5":
				sys.exit()
			else:
				raise FueradeIndice(opcionMenu)
				
				 
		except (ValueError):
			raise ValorErroneo(opcionMenu)
		except ValorErroneo as lp:
			print ('Ingrese solo numeros enteros ')
		except FueradeIndice as FI:
			print('Numero fuera de indice. Usted selecciono el numero: ',str(FI.indice))	
		except (TypeError):
			print ('Hubo un inconveniente con el tipo de dato ingresado')
		input()
		BorrarPantalla()	
		EstacionServicio()    

#-------------------------Playero------------------------------------------------------------------------------#
def TituloPlayero():
		print ("================================================================")
		print ("	                    Modulo	Playero					")
		print ("================================================================")
			
def MenuPlayero():
	while True:
		BorrarPantalla()
		TituloPlayero()
		
		
		print ("1- Dar de alta un playero\n")
		print ("2- Dar de baja un playero\n")
		print ("3- Asignar playero a un surtidos\n")
		print ("4- Listar todos los playeros\n")
		print ("5- Volver\n")
	

		opcionMenu = input("Ingrese una opcion: ")
		if opcionMenu == "1":
			
			BorrarPantalla()
			TituloPlayero()
			while True:
				try:
					print("Ingrese nombre y apellido: 	")
					nom = input()
					controlnombre(nom)
					if controlnombre(nom)!= 1:
						print (controlnombre(nom))
						raise ValueError
					print ("\n")
					nm = nom.title()
			
					dni = int(input ("Ingrese numero de dni: "))
					cant = (len(str(dni)))
					if cant < 7:
						raise ValueError
										 
					print ("\n")
					print ("ingrese hora entrada:")
					horaini=datetime.time(int(input()))
					print ("\n")
					print ("ingrese hora salida:")
					horasal=datetime.time(int(input()))
					print ("\n")	
					pla1 = Playero(nm,dni,horaini,horasal)
					rta = adm1.ExistePlayero(pla1.verDni())
					if rta == True:
						print("El PLAYERO que intenta cargar ya se encuentra dado de alta")
					else:
						adm1.AgregarPlayero(pla1)
						print ("El PLAYERO con nombre",pla1.verNom(),"con DNI: ",pla1.verDni(),"y el horario de: ",pla1.verHor(),"a",pla1.verHorSalida(),". Se cargo CON EXITO.")
						input()
						break

				except (ValueError):
					input ("El registro no se llevo a cabo... Intente nuevamente")
					BorrarPantalla()
					TituloPlayero()
				BorrarPantalla()
				TituloPlayero()


			
			
		if opcionMenu == "2":
			while True:
				try:
					BorrarPantalla()
					TituloPlayero()
					x = adm1.MostrarListaPla()
					if len(adm1.MostrarListaPla()) == 0:
						input("No contiene ningun playero dado de alta")
						break
			#total = len(x)
			#print (total)
					c = 1
					for playero in x:
						print (c,") ",playero.verNom(),playero.verDni())
						c+=1
					num = int(input ("Seleccione una opccion: "))
					adm1.EliminarPlayero(x[num-1])
			
					print ("\tNueva Lista\n")
					c = 1
					for playero in x:
						print (c,") ",playero.verNom(),playero.verDni())
						c+=1
					input()
					break
				except ValueError:
					input("Elige una opcion valida.")
					BorrarPantalla()
					MenuPlayero()
				except IndexError:
					input("Valor fuera de rango")
			
			
			
		if opcionMenu == "3":
			BorrarPantalla()
			TituloPlayero()
			y = adm1.MostrarListaSur()				#Tengo una lista de surtidores
			#total = len(x)
			#print (total)
			x = adm1.MostrarListaPla()				#Tengo una lista de OBJETOS de playero
			#total = len(x)
			#print (total)
			if len(x) == 0:
				input("Primero debe dar de alta un playero")
				MenuPlayero()
			
			while True:
				try:
					d = 1
					for playero in x:
						print (d,") ",playero.verNom(),playero.verDni())
						d+=1
					nm=int(input('seleccione un playero: \n'))
					play = x[nm-1]
			#print (play.verNom())
			#input("Esta es la prueba") 
			
			# Estabien hasta aqui--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			
			
					lista_surtidores_habilitados = []
					for s in y:    #Y = conjunto de surtidores
						if s.verestado() == True:
							lista_surtidores_habilitados.append(s)
			
					if len(lista_surtidores_habilitados) == 0:
						input("Para realizar esta operacion habilite un surtidor. Gracias.")
						MenuSurtidor()
					k = 1
					for x in lista_surtidores_habilitados:
						print(k,") numero surtidor: ",x.vernumero()," Combustible: ",x.vertipo())
						k+=1
					num = int(input ("Seleccione un surtidor: "))
			
					for sur in y:
						if lista_surtidores_habilitados[num-1].vernumero() == sur.vernumero():
							sur.modplayeroasig(play)
							print("El playero: ",sur.verplayero().verNom(),"con dni :",sur.verplayero().verDni())
							input("Se cargo con exito")
					
			
			#lista_surtidores_habilitados[num-1].modplayeroasig(x[nm-1])
							
			#modplayeroasig(otro)
			#lis[num-1].modplayeroasig(x[nm-1])
			#print ("El playero",lista_surtidores_habilitados[num-1].verplayero().verNom()," ah sido cargado al Surtidor numero", lista_surtidores_habilitados[num-1].vernumero())
			#input()
					
			
#			for sur in y:
#				if sur.vernumero()==y[num-1].vernumero():
#					sur.modplayeroasig(x[nm-1])
#					input("El payero",x[nm-1].verNom(),x[nm-1].verDni(), "ah sido asignado al  Surtidor numero: ",sur.vernumero())
		
					
			#y[num-1].modplayeroasig(d[nm-1])
			#print ('el Playero', d[nm-1].verNom(),d[nm-1].verDni(),'ah sido asignado a Surtidor',x[num-1].vernumero(),'correctamente')
			
					BorrarPantalla()
					MenuPlayero()
					break
				except IndexError:
					input ("Valor fuera de rango")
					BorrarPantalla()
					TituloPlayero()
				except ValueError:
					input("Los datos ingresados no son consistentes")
					MenuPlayero()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		if opcionMenu == "4":
			BorrarPantalla()
			TituloPlayero()
			x = adm1.MostrarListaPla()
			#tamanio = len(x)-1
			#ListarPla(x,tamanio)
			
			
			
			#print (total)
			c = 1
			for playero in x:
				print (c,") ",playero.verNom(),playero.verDni())
				c+=1
			
		if opcionMenu == "5":
			BorrarPantalla()
			EstacionServicio()
		
			
		else:
			input("Presione un tecla para continuar...")
			BorrarPantalla()

#................................Promocion.......................................................................#
def TituloPromo():
		print ("*************************************************************")
		print ("******                  Modulo	Promocion      **************")
		print ("******                                         **************")
		print ("*************************************************************")
def TituloPromo1():
		print ("*************************************************************")
		print ("******                   Modulo	Promocion              ******")
		print ("******                   Alta de promocion             ******")
		print ("*************************************************************")
def TituloPromo2():
		print ("*************************************************************")
		print ("******                   Modulo	Promocion              ******")
		print ("******                   Baja de promocion             ******")
		print ("*************************************************************")
def TituloPromo3():
	print ("***************************************************************")
	print ("******                   Modulo	Promocion                ******")
	print ("******                 Lista de promociones              ******")
	print ("***************************************************************")
def MenuPromocion():
	while True:
		BorrarPantalla()
		TituloPromo()
		print ("1- Dar de alta una promocion \n")
		print ("2- Dar de baja una Promocion \n")
		print ("3- Listar todas las promociones \n")
		print ("4- Volver \n")
		escoger=input()
		
		if escoger=="1":
			
			while True:
				try:
					BorrarPantalla()
					TituloPromo1()
					lis=[('% de Descuento'),('Puntos')]
					c=1
					for x in lis:
						print (c,')',x)
						c+=1
					es=int(input('elije Tipo de promo \n'))
					tipo=lis[es-1]
					ptos=int(input('ingrese cantidad: \n'))
					if tipo == lis[0] and ptos >100:
						raise ValueError
						#print ('el valor ingresado no es correcto, por favor ingrese en el rango [0:100]')	
						#ptos=int(input('ingrese cantidad: \n'))			
					tarj=str(input('ingrese nombre de la tarjeta: \n'))
					prom=(Promo(tipo,ptos,tarj))
					adm1.darAltaPromo(prom)
					input('La Promocion fue cargada con exito: \n')
					BorrarPantalla()
					break
				except ValueError:
					input("El valor ingresado no es correcto")
				except IndexError:
					input("Opcion invalida")
			
			
		elif escoger=="2":
			BorrarPantalla()
			TituloPromo2()
			x = adm1.MostrarListaPro()
			#total = len(x)
			#print (total)
			c = 1
			for promo in x:
				print (c,") ",promo.VerCantPunto(),promo.VerTipoPromo(),promo.VerNomTarjeta())
				c+=1
			num = int(input ("Seleccione una opccion: "))
			adm1.darBajaPromo(x[num-1])
			input('la promocion ha sido dada de baja exitosamente')
			BorrarPantalla()
			
		elif escoger=="3":
			BorrarPantalla()
			TituloPromo3()
			x = adm1.MostrarListaPro()
			#total = len(x)
			#print (total)
			c = 1
			for promo in x:
				print (c,") ",promo.VerCantPunto(),promo.VerTipoPromo(),promo.VerNomTarjeta())
				c+=1
			input()
			BorrarPantalla()
			
			
		elif escoger=="4":
			BorrarPantalla()
			EstacionServicio()
			
		else:
			print ('No escogio ninguna opcion correcta. \n Vuelva a intentarlo ')
			escoger=input()
				
#-----------------------------------------Surtidor---------------------------------------------------------------#
def TituloSurtidores():
		print ("================================================================")
		print ("	                    MODULO SURTIDORES						")
		print ("================================================================")
def TituloSurtidor1():
		print ("================================================================")
		print ("	                    MODULO SURTIDORES						")
		print ("	                   	Agregar Surtidor						")
		print ("================================================================")
def TituloSurtidor2():
		print ("================================================================")
		print ("	                    MODULO SURTIDORES						")
		print ("	                    Habilitar Surtidor 					")
		print ("================================================================")
def TituloSurtidor3():
		print ("================================================================")
		print ("	                    MODULO SURTIDORES						")
		print ("	                   Deshabilitar Surtidor   					")
		print ("================================================================")
def TituloSurtidor4():
		print ("================================================================")
		print ("	                    MODULO SURTIDORES						")
		print ("	              Ver la cantidad de litros vendidos     		")
		print ("================================================================")
def TituloSurtidor5():
		print ("================================================================")
		print ("	                    MODULO SURTIDORES						")
		print ("	                   	Cargar Combustible						")
		print ("================================================================")
def TituloSurtidor6():
		print ("================================================================")
		print ("	                    MODULO SURTIDORES						")
		print ("	                 Listar todos los surtidores  							")
		print ("================================================================")
def MenuSurtidor():
	while True:
		BorrarPantalla()
		TituloSurtidores()
		
		
		print ("1- Agregar Surtidor\n")
		print ("2- Habilitar Surtidor\n")
		print ("3- Deshabilitar Surtidor\n")
		print ("4- Ver la cantidad de litros vendidos \n")
		print ("5- Cargar Combustible\n")
		print ("6- Listar todos los surtidores\n") 
		print ("7- Volver\n")
	

		opcionMenu = input("Ingrese una opcion: ")
		if opcionMenu == "1":
			BorrarPantalla()
			TituloSurtidor1()
			while True:
					try:
						BorrarPantalla()
						TituloSurtidor1()
						h=adm1.MostrarListaSur()
						nro=int(input('ingrese Nro de Surtidor: \n'))
						for x in h:
							if nro == x.vernumero():
							#input('Nro de Surtidor existente...Presione una tecla para intentar nuevamente')
								raise ValorErroneo()
						lis=[('Super'),('Infinia'),('Disel'),('InfiniaDisel')]
						c=1
						for x in lis:
							print(c,'-',x)
							c+=1
						p=int(input('elija un tipo de combustible: \n'))
						tipo=lis[p-1]
						valor=float(input('ingrese valor por litro: \n'))
						remanente=float(input('ingrese litros remanentes: \n'))
						s=Surtidor(nro,tipo,valor,remanente)
						adm1.AgregarSurtidor(s)
						input ('Ha sido agregado correctamente')
					#input('presione una tecla para continuar...')
						MenuSurtidor()
					except (IndexError):
						input("Valor Incorrecto intente nuevamente...")
					except(ValueError):
						raise ValorErroneo()
					except ValorErroneo as lp:
						input("Valor Incorrecto intente nuevamente...")
					
		elif opcionMenu == "2":					#OK
			while True:
				try:
					BorrarPantalla()
					TituloSurtidor2()

					x = adm1.MostrarListaSur()
					c = 1
					lista_sur_desa = []
					for s in x:
						if s.verestado()== False:
							print (c,") ",s.vernumero(),s.vertipo())
							c+=1
							lista_sur_desa.append(s)
					num = int(input ("Seleccione una opccion: "))
					if num >= c:
						raise FueradeIndice()
					if type(num)==str:
						raise ValueError
					if len(lista_sur_desa)==0:
						raise ValueError
					for sur in x:
						if lista_sur_desa[num-1].vernumero() == sur.vernumero():
							sur.modplayeroasig(None)
							sur.modestadohabilitar() 
							print ('El surtidor', sur.vernumero(),'ah sido habilitado correctamente')
					
							input()
							MenuSurtidor()
				except (IndexError):
					raise FueradeIndice()
				except (ValueError):
					raise ValorErroneo()			
				except ValorErroneo as xr:
					print("Todos los surtidores estan habilitados")
					input()
					MenuSurtidor()
				except FueradeIndice as fi:
					print("Todos los surtidores estan habilitados")
					input()
					MenuSurtidor()
											
		elif opcionMenu == "3":    				#OK
			while True:
				try:
					BorrarPantalla()
					TituloSurtidor3()
					x = adm1.MostrarListaSur()
					lista_sur_habi = []
					c = 1
					for s in x:
						if s.verestado()== True:
							print (c,") ",s.vernumero(),s.vertipo())   #Te muestra todos los surtidores
							c+=1
							lista_sur_habi.append(s)
					num = int(input ("Seleccione una opccion: "))
			
					for sur in x:
						if lista_sur_habi[num-1].vernumero() == sur.vernumero():
							sur.modestadodeshabilitar()
			#adm1.DeshabilitarSurtidor(x[num-1])
							print ('El surtidor', sur.vernumero(),'ha sido deshabilitado correctamente')
							input()
					if num > c:
						raise FueradeIndice(num)
					#BorrarPantalla()
					MenuSurtidor()
				except  (ValueError):
					print("Todos los surtidores estan deshabilitados")
					input()
					MenuSurtidor()
				except FueradeIndice as FI:
					print ('el vslor que ingreso (',FI.indice(),') esta Fuera de indice, intentar nuevamente...')
					input()
					MenuSurtidor()
				except (IndexError):
					print("Todos los surtidores estan deshabilitados")
					input()
					MenuSurtidor()
		elif opcionMenu == "4":
			while True:
				try:
					BorrarPantalla()
					TituloSurtidor4()
					x = adm1.MostrarListaSur()
					if len(x)>0:
						for surtidor in x:
							if surtidor.verestado() == True:
								print ("Surtidor numero:",surtidor.vernumero()," -  Tipo Comb:",surtidor.vertipo(),' Estado- Habilitado')
							elif surtidor.verestado() == False:
								print ("Surtidor numero:",surtidor.vernumero()," -  Tipo Comb:",surtidor.vertipo(),' Estado- Deshabilitado')
							else:
								print ("Surtidor numero:",surtidor.vernumero()," -  Tipo Comb:",surtidor.vertipo())
						num = int(input("Selecciona con el numero de surtidor: "))
						for k in x:
							if k.vernumero() == num:
								print("La cantidad de litros vendidos es: ",k.verltsvendidos())
								input()
								BorrarPantalla()
								MenuSurtidor()
								
							else:
								raise IndexError
					else:
						raise ValueError	
				except ValueError:
					input("El codigo de surtidor no es valido, no se encuentran Surtidores Cargados")
					MenuSurtidor()
				except IndexError:
					input("Error ,Fuera de indice ")
					MenuSurtidor()
				
		elif opcionMenu == "5":	
			global Ahorrado_Clientes
			global Recaudado_Estacion
			while True:
				try:
					BorrarPantalla()
					TituloSurtidor5()
					SurEnCond = []
					x = adm1.MostrarListaSur()
					if len(x) == 0:
						input("Debe dar de alta un surtidor")
						MenuSurtidor()
					k = 1
					
					for i in x:
						if i.verestado()==True and  i.verplayero() == None:
							print ('debe asignar un playero para realizar la carga')
							input()
							MenuPlayero()
						if i.verestado()==True and  i.verplayero() != None:				
							#Compruebo que el estado del surtidor este habilitado y tenga asignado un surtidor
							#Para luego agregar el monto de la venta al playero sino da error
							print (k,")","\tSurtidor numero: ",i.vernumero())
							k +=1
							SurEnCond.append(i)
						
					indice = int(input('Ingrese nro de surtidor: \n'))
					#lista_surtidores = adm1.MostrarListaSur()
					#for y in SurEnCond:
					print("Elegiste el surtidor numero: ",SurEnCond[indice-1].vernumero()) #if numsur == sur.vernumero():
					can=float(input('ingrese cantidad de litros cargados: \n'))
					SurEnCond[indice-1].modltsenventa(can)
					SurEnCond[indice-1].modltsvendidos(can)
					if 	SurEnCond[indice-1].verremanente() - can <0:			#Si al comprar el stock no puede cargar entonces no se puede
						input("No se puede realizar la compra porque no hay stock suficiente")
						raise ValueError
					else:
						SurEnCond[indice-1].modremanente(can)
					a=str(input('paga con alguna promocion? S o N'))
					if a.lower()=='s':
						x = adm1.MostrarListaPro()
						if len(x) == 0:
							input("No hay Promosiones en este momento")
							MenuSurtidor()
						else:
							c = 1
							for promo in x:
								print (c,") ",promo.VerCantPunto(),promo.VerTipoPromo(),promo.VerNomTarjeta())
								c+=1
							
							ad=int(input('Seleccione una promocion: '))
							if 	x[ad-1].VerTipoPromo() =="% de Descuento":
								descuento_con_promo = (SurEnCond[indice-1].verltsenventa()*SurEnCond[indice-1].vervalor()*x[ad-1].VerCantPunto())/100
								total_a_pagar = SurEnCond[indice-1].verltsenventa()*SurEnCond[indice-1].vervalor()-descuento_con_promo
								print("El monto total de la venta con descuento es: ",total_a_pagar)
							#Agrego el monto a Playero
								SurEnCond[indice-1].verplayero().modTotal(total_a_pagar)
							#Agrego monto al Surtidor
								SurEnCond[indice-1].modventastotales(total_a_pagar)
							#Agrego lo ahorrado por el cliente
								Ahorrado_Clientes += descuento_con_promo
							#Agrego total Estacion Servicio
								Recaudado_Estacion += total_a_pagar
							
								input()
								BorrarPantalla()
								MenuSurtidor()
							
					else:
						total_a_pagar = SurEnCond[indice-1].verltsenventa()*SurEnCond[indice-1].vervalor()
						print("El monto total de la venta es: ",total_a_pagar)
						#Agrego el monto a Playero
						SurEnCond[indice-1].verplayero().modTotal(total_a_pagar)
						#Agrego monto al Surtidor
						SurEnCond[indice-1].modventastotales(total_a_pagar)
						#Agrego Total a Estacion Servicio
						Recaudado_Estacion += total_a_pagar
								
						input()
						BorrarPantalla()
						MenuSurtidor()
								
					#else:
						#raise IndexError		
				except ValueError:
					input("Error inesperado... Intente nuevamente")
					MenuSurtidor()
				except IndexError:
					input("Error. Intentalo mas tarde")		
						
								
		elif opcionMenu == "6":   #ok
			while True:
				try:
					BorrarPantalla()
					TituloSurtidor6()
					surtidor = adm1.MostrarListaSur()
					print ("\t Lista de Todos los Surtidores ")
					for x in surtidor:
						if len(surtidor)== 0:
							raise ValueError
						if x.verestado()==True:
							print('Surtidor numero:',x.vernumero()," - ",'Tipo Comb:',x.vertipo(),'Estado- Habilitado')
						if x.verestado()==False:
							print('Surtidor numero:',x.vernumero()," - ",'Tipo Comb:',x.vertipo(),'Estado- Deshabilitado')
					input()
					BorrarPantalla()
					MenuSurtidor()
				except ValueError:
					print ("Aun no hay datos cargados")
															
		elif opcionMenu == "7": #ok
			BorrarPantalla()
			EstacionServicio()		
		else:
			input("Presione un tecla para continuar...")
			BorrarPantalla()



#------------------------------------------administracion-----------------------------------------------------------------#
def TituloAdmin():
		print ("================================================================")
		print ("	                    Modulo	Administracion					")
		print ("================================================================")
		
def TituloAdminPla():
		print ("================================================================")
		print ("	                    Modulo	Administracion					")
		print ("	                    Recaudacion	Playero    					")		
		print ("================================================================")
		
def TituloAdminSur():
		print ("================================================================")
		print ("	                    Modulo	Administracion					")
		print ("	                    Recaudacion	Surtidor   					")		
		print ("================================================================")
		
def TituloAdminDes():
		print ("================================================================")
		print ("	                    Modulo	Administracion					")
		print ("	                    Monto Por Descuento     					")		
		print ("================================================================")



		
def MenuAdmin():
	while True:
		BorrarPantalla()
		TituloAdmin()
		print ("1- Recaudacion final de la estacion\n")
		print ("2- Recaudacion de un surtidor\n")
		print ("3- Recaudacion de un playero\n")
		print ("4- Monto total correspondiente a ventas con promociones\n")
		print ("5- Volver\n")
	
	
	

		opcionMenu = input("Ingrese una opción: ")
		if opcionMenu == "1":
			BorrarPantalla()
			TituloAdmin()
			print("\n\n\n La recaudacion final de la Estacion: $", Recaudado_Estacion)
			
			
		if opcionMenu == "2":
			BorrarPantalla()
			TituloAdminSur()
			print ("\t\tListado de Surtidores Habilitados")
			surtidor = adm1.MostrarListaSur()
			
			sds=0
			LisRecaudacion = []
			for x in surtidor:
				if x.verestado() == True:
					sds+=x.verventastotales()
					LisRecaudacion.append(x.verventastotales())
					
			y = ordenar(LisRecaudacion)				#Funcion Ordenamiento
			y.reverse()					#De mayor a menor
			for lista in y:
				for n in surtidor:
					if n.verventastotales() == lista:
						print("Surtidor numero",n.vernumero()," - Tipo Comb:", n.vertipo()," -  Recaudacion: $",n.verventastotales())
								
			print ('La recaudacion total es de $',sds)
			input()
			MenuAdmin()

		
			
		if opcionMenu == "3":
			BorrarPantalla()
			TituloAdminPla()
			lista = adm1.MostrarListaPla()
			tam = len(lista)-1
#-------------------------Recursion--------------------------------------------	
			def listar (lis,tam):
				if tam == 0:
					print ("\t",lis[tam].verNom(),"Recaudo: $",lis[tam].verTotal())
				else:
					print ("\t",lis[tam].verNom(),"Recaudo: $",lis[tam].verTotal())
					listar(lis,tam-1)
#---------------------------------------------------------------------------------------			
			listar(lista,tam)
			input()
			MenuAdmin()
			
			
		if opcionMenu == "4":
			BorrarPantalla()
			TituloAdminDes()
			print("Monto total con descuentos en ventas con promociones: $",Ahorrado_Clientes)
			input()
			MenuAdmin()
		if opcionMenu == "5":
			BorrarPantalla()
			EstacionServicio()
		else:
			
			input("Presione un tecla para continuar...")
			BorrarPantalla()
			
