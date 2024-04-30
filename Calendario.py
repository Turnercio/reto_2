

class Dia:
    def __init__(self, anyo=1970, mes=1, dia=1):
        
        if self.es_entero(anyo):
            self.anyo = anyo       
        else:
            raise ValueError("Año debe de ser un número entero")
        if self.es_entero(mes):
            self.mes = mes  
        else:
            raise ValueError("Mes debe de ser un número entero")
        if self.es_entero(dia):
            self.dia = dia    
        else:
            raise ValueError("Dia debe de ser un número entero")
        

        self.comprobar_fecha() 
    
    def es_entero(self, valor):      
        return isinstance(valor, int)

    def es_bisiesto(self):
        return self.anyo % 4 == 0 and (self.anyo %100 != 0 or self.anyo % 400 == 0)

    def comprobar_fecha(self):
        if self.anyo < 1:
            raise ValueError("Fecha incorrecta. Año Fuera de rango.")

        if self.mes < 1 or self.mes > 12:
            raise ValueError("Fecha incorrecta. Mes fuera de rango.")

        dias_del_mes = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        if self.es_bisiesto():
            dias_del_mes[2] = 29

        if self.dia < 1 or self.dia > dias_del_mes[self.mes]:
            raise ValueError("Fecha incorrecta. Dia fuera de rango.")
        
