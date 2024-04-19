from Token import Token
from Errores import Error
from ErrorReporte import reporterror
from TokenReporte import reportoken
from Crear_HTML import traduccion_Html
import re



class Analizador_lexico:


    def __init__(self):
        self.listTokens = []
        self.listError = []
        self.listReservadas = []
        self.listValores = []
        self.elementos = {}
    def analizador(self,entry):
        #Reiniciar listas para que en cada análisis se reinicie y poder analizar sin reiniciar el programa
        self.listTokens = []
        self.listError = []
        self.listReservadas = []
        valor = ""
        clave = ""
        buffer = ""
        Titulo = ""
        centinela = "$"
        entry += centinela
        self.elementos = {} 
        self.argsDeElementos ={}
        linea = 1
        columna = 1

        estado = 0

        index = 0
        
        while index < len(entry):
            caracter = entry[index]

            if estado == 0:
                #Reconociendo los signos 
                if caracter == ":":
                    #Se suma uno a la columna
                    columna += 1
                    #Se agrega el caracter al buffer 
                    buffer += caracter
                    #Se crea y agrega el token a la lista de tokens
                    token = Token("DOS PUNTOS", buffer,linea, columna)
                    self.listTokens.append(token)
                    #Se limpia el buffer
                    buffer = ""
                    #Se cambia de estado 
                    estado = 0
                
                elif caracter == "{":
                    columna +=1
                    buffer += caracter
                    token = Token("LLAVE QUE ABRE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0
                    

                elif caracter == "}":
                    columna +=1
                    buffer += caracter
                    token = Token("LLAVE QUE CIERRA", buffer, linea, columna)
                    self.listTokens.append(token)
                    self.elementos[Titulo] = self.argsDeElementos
                    self.argsDeElementos = {}
                    print("=================Elemento ==================")
                    print(self.elementos)
                    print("================= ==================")
                  
                    Titulo =""
                    buffer = ""
                    estado = 0
                
                elif caracter == "\"":
                    columna +=1
                    buffer += caracter
                    token = Token("COMILLA DOBLE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0
                
                elif caracter == ">":
                    columna +=1
                    buffer += caracter
                    token = Token("MAYOR QUE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "<":
                    columna +=1
                    buffer += caracter
                    token = Token("MENOR QUE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "/":
                    columna +=1
                    buffer += caracter
                    token = Token("BARRA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "-":
                    columna +=1
                    buffer += caracter
                    token = Token("GUION", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "!":
                    columna +=1
                    buffer += caracter
                    token = Token("ADMIRACION CIERRA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "+":
                    columna +=1
                    buffer += caracter
                    token = Token("SUMA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == ";":
                    columna +=1
                    buffer += caracter
                    token = Token("PUNTO Y COMA", buffer, linea, columna)
                    self.listTokens.append(token)
                    self.argsDeElementos[clave] = valor
                    
                    valor = ""
                    clave = ""

                    buffer = ""
                    estado = 0

                elif caracter == ",":
                    columna +=1
                    buffer += caracter
                    token = Token("COMA", buffer, linea, columna)
                    self.listTokens.append(token)
                    

                    buffer = ""
                    estado = 0
                
                elif caracter == "[":
                    columna +=1
                    buffer += caracter
                    token = Token("CORCHETE ABRE", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0
                    
                elif caracter == "]":
                    columna +=1
                    buffer += caracter
                    token = Token("CORCHETE CIERRA", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "=":
                    columna +=1
                    buffer += caracter
                    token = Token("IGUAL", buffer, linea, columna)
                    self.listTokens.append(token)
                    

                    buffer = ""
                    estado = 0
                
                elif caracter == ".":
                    columna +=1
                    buffer += caracter
                    token = Token("PUNTO", buffer, linea, columna)
                    self.listTokens.append(token)
                    buffer = ""
                    estado = 0

                elif caracter == "\n":
                    columna = 1
                    linea += 1
                    estado = 0 

                elif caracter == " ":
                    columna +=1
                    buffer += caracter
                elif caracter == "\t":
                    columna += 1
                
                elif re.search(r"[a-zA-Z0-9]", caracter):
                    columna +=1
                    buffer += caracter
                    estado = 1
                
                else: 
                    estado = 3
                    buffer += caracter
            
            #Palabras Reservadas
            elif estado == 1:
                if re.search(r"[a-zA-ZÁ\u00f1\u00d1\u00E0-\u00FC]",caracter) or caracter == "":
                    if caracter == " ":
                        columna += 1
                        estado = 1
                    elif caracter == "\ñ":
                        columna += 1
                        estado = 1
                    elif caracter == "\t":
                        columna +=1

                    elif caracter == "\n":
                        linea +=1
                        columna = 1

                    else: 
                        buffer += caracter
                        estado = 1
                else:
                    Tokentipo = ""

                    if buffer == "Inicio":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                    
                    elif buffer == "Encabezado":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                    
                    elif buffer == "TituloPagina":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer
                    
                    elif buffer == "Cuerpo":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                    
                    elif buffer =="Titulo":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer

                    elif buffer == "texto":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer
                    
                    elif buffer == "posicion":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer
                    
                    elif buffer == "tamaño":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer
                    
                    elif buffer == "color":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer

                    elif buffer == "Fondo":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer

                    elif buffer == "Parrafo":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                    
                    elif buffer == "Texto":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                    
                    elif buffer == "fuente":
                        Tokentipo = "PAlABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer

                    elif buffer == "Codigo":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer

                    elif buffer == "Negrita":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer

                    elif buffer == "Subrayado":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer

                    elif buffer == "Tachado":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer

                    elif buffer == "Cursiva":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer

                    elif buffer == "Salto":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                    
                    elif buffer == "cantidad":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer

                    elif buffer == "Tabla":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                    
                    elif buffer == "filas":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer
                        


                    elif buffer == "columnas":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        clave = buffer

                    elif buffer == "elemento":
                        Tokentipo = "PALABRA RESERVADA"
                        self.listReservadas.append(buffer)
                        Titulo = buffer
                         
                    
                    else:
                        Tokentipo = "IDENTIFICADOR"
                        valor +=  buffer

                    token = Token(Tokentipo,buffer,linea,columna)
                    self.listTokens.append(token)
                    
                    buffer = ""
                    index -= 1
                    estado = 0

            elif estado == 2:
                if re.search(r"[a-zA-Z]",caracter) or re.search(r"[\"]",caracter) or caracter == ' ' or caracter == '-' or caracter == '\t' or caracter  == '\n' or re.search(r"[\:]",caracter):

                    if caracter == "\t":
                        columna += 1

                    elif caracter == "\n":
                        linea += 1
                        columna = 1

                    elif re.search(r"[\:]",caracter):
                        columna += 1
                        buffer += caracter
                        estado = 2
                    
                    elif caracter == '"':
                        token = Token("IDENTIFICADOR", buffer,linea,columna)
                        self.listTokens.append(token)
                        self.listValores.append(buffer)

                        token2 = Token("COMILLA DOBLE",caracter,linea,columna)
                        self.listTokens.append(token2)
                        estado = 2
                        buffer = ""
                    
                    else: 
                        columna += 1
                        estado = 2
                        buffer += caracter
                else:
                    estado = 0 
                    index -= 1

            elif estado == 3:
                errores = Error("ERROR LEXICO", buffer,linea,columna)
                self.listError.append(errores)
                buffer = ""
                estado = 0
                columna += 1
                index -= 1
            index += 1
       
        
        return entry
    
    def ErrorToken(self):
        reportoken(self.listTokens)

    def ErrorReporte(self):
        reporterror(self.listError)

    def html_Creado(self):
        return traduccion_Html(self.elementos)


        
    def imprimirInfo(self):
        print("\n\n\n")
        print("======= Lista de Tokens =======")
        
        for token in self.listTokens:
            token.getInfo()

    def imprimirErrores(self):
        print("\n\n\n")
        print("======= Lista de Errores =======")
        
        i = 0
        for errores in self.listError:
            print(i+1)
            errores.getError()
            i += 1




                    
                    









                
                    
                
                



