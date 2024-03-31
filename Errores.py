#clase para manejar los errores
class Error: 

    def __init__(self,tipo,lexema,linea,columna): 
        self.tipo = tipo
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
    #función que permite obtener la información de los errores
    def getError(self):
        print("\n =========================")
        print("Tipo: ", self.tipo)
        print("Lexema: ", self.lexema)
        print("Linea: ", self.linea)
        print("Columna: ", self.columna)