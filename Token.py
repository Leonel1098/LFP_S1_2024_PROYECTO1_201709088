#Clase que maneja los token 
class Token:
    
    def __init__(self,tipo,lexema,linea,columna):
        self.tipo = tipo
        self.lexema = lexema
        self.linea = linea
        self.columna = columna

    #Función que permite obtener la información del Token
    def getInfo(self):
        print("\n =========================")
        print("Tipo: ", self.tipo)
        print("Lexema: ", self.lexema)
        print("Linea: ", self.linea)
        print("Columna: ", self.columna)
    
    def getTipo(self):
        return self.tipo
    def getLexema(self):
        return self.lexema
    def getLinea (self):
        return self.linea
    def getColumna (self):
        return self.columna