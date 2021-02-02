class Playero:
        def __init__(self,nomyape,dni,h_trabajoinicio,h_trabajofin):
                self.__nomyape = nomyape
                self.__dni = dni
                self.__h_trabajoinicio = h_trabajoinicio
                self.__h_trabajofin=h_trabajofin
                self.__monto_total = 0
        def verNom(self):
                return self.__nomyape
        def verDni(self):
                return self.__dni
        def verHor(self):
                return self.__h_trabajoinicio
        def verHorSalida(self):
                return self.__h_trabajofin
        def verTotal(self):
                return self.__monto_total
        def modNom(self,otro):
                self.__nomyape = otro
        def modDni(self,otro):
                self.__dni = otro

        def modHor(self,otro):
                self.__h_trabajoinicio = otro
        def modHorSale(self,otro):
                self.__h_trabajofin = otro
        def modTotal(self,otro):
                self.__monto_total += otro
#.....................COMPARACION.............................
        def __cmd__(self,otro):
                dif= self.__monto_total - otro.__monto_total
                if dif>0:
                        return 1
                elif dif<0:
                        return -1
                else:
                        return 0
        def compMonto(self,otro):
                return self.__cmd__(otro)
