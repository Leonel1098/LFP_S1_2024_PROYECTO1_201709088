import webbrowser

def traduccion_Html(elementos = {}):
    #print("case TRaduccion HTML ") 
    html_final = "<!DOCTYPE html>\n<html>\n     <head>\n        <title>\n"

    name_page = ""
    for clave_titulo in elementos:
        """print("Title")
        print(clave_titulo)
        print("Values")
        print(elementos[clave_titulo])"""
        valor_argumento = elementos[clave_titulo] 
        
       
        for argumento in  valor_argumento :
            print("Argumentos enviar html ")
            print(argumento , "---", valor_argumento [argumento] )

            'para titulo '
            if clave_titulo == "Encabezado":
                if argumento ==  "TituloPagina"  :
                    html_final += "             "+valor_argumento [argumento] + "\n         </title>\n      </head>\n      <body>\n   "
                    name_page = valor_argumento [argumento]

            if clave_titulo == "Titulo":
                if argumento == "texto":
                   texto_titulo = valor_argumento[argumento]
                if argumento ==  "posicion":
                    posicion_titulo = valor_argumento [argumento]
                    if posicion_titulo == "izquierda":
                        posicion_titulo = "left"
                    if posicion_titulo == "centro":
                        posicion_titulo = "center"
                    if posicion_titulo == "derecha":
                        posicion_titulo = "right"

                if argumento == "tamaño":
                    tamaño_titulo = valor_argumento[argumento]
                    if tamaño_titulo == "t1":
                        tamaño_titulo = "h1"
                    elif tamaño_titulo == "t2":
                        tamaño_titulo = "h2"                    
                    elif tamaño_titulo == "t3":
                        tamaño_titulo = "h3"                    
                    elif tamaño_titulo == "t4":
                        tamaño_titulo = "h4"                    
                    elif tamaño_titulo == "t5":
                        tamaño_titulo = "h5" 
                    elif tamaño_titulo == "t6":
                        tamaño_titulo = "h6"      

                if argumento == "color":
                    color_titulo = valor_argumento [argumento]
                    if color_titulo == "rojo":
                        color_titulo = "red"
                    elif color_titulo == "amarillo":
                        color_titulo = "yellow"                    
                    elif color_titulo == "azul":
                        color_titulo = "blue"   
                    elif color_texto == "blanco":
                        color_texto = "white"     

                    html_final += "         <"+tamaño_titulo+" style= 'text-align: "+ posicion_titulo+";" " color: "+color_titulo+";'>\n            "+texto_titulo+"\n         </"+tamaño_titulo+">\n"

            if clave_titulo == "Fondo":
                if argumento == "color":
                    color_fondo = valor_argumento [argumento]
                    if color_fondo== "rojo":
                        color_fondo = "red"
                    elif color_fondo == "amarillo":
                        color_fondo = "yellow"                    
                    elif color_fondo == "azul":
                        color_fondo = "blue" 
                    elif color_fondo == "blanco":
                        color_fondo = "white"

                html_final += '''         <style> body {background-color: '''+color_fondo+''';}</style>\n'''

            if clave_titulo == "Parrafo":
                if argumento == "texto":
                    texto_parrafo = valor_argumento[argumento]
                if argumento == "posicion":
                    posicion_parrafo = valor_argumento[argumento]
                    if posicion_parrafo == "izquierda":
                        posicion_parrafo = "left"
                    if posicion_parrafo == "centro":
                        posicion_parrafo = "center"
                    if posicion_parrafo == "derecha":
                        posicion_parrafo = "right"

                    html_final += "         <p style='text-align:" +posicion_parrafo+";'>"+texto_parrafo+"</p>\n"

            if clave_titulo == "Texto":
                if argumento == "fuente":
                    fuente_texto = valor_argumento[argumento]

                if argumento == "color":
                    color_texto = valor_argumento[argumento]
                    if color_texto== "rojo":
                        color_texto = "red"
                    elif color_texto == "amarillo":
                        color_texto = "yellow"                    
                    elif color_texto == "azul":
                        color_texto = "blue"
                    elif color_texto == "blanco":
                        color_texto = "white"

                if argumento == "tamaño":
                    tamaño_texto = valor_argumento[argumento]

                if argumento == "texto":
                    texto_del_texto = valor_argumento[argumento]
                
                    html_final += "         <span style='font-family:"+fuente_texto+ "; color:" +color_texto+ "; font-size:" +tamaño_texto+"px;'>\n             "+texto_del_texto+"!!\n         </span>\n"

            if clave_titulo == "Codigo":
                if argumento == "texto":
                    texto_codigo = valor_argumento[argumento]
                if argumento =="posicion":
                    posicion_codigo = valor_argumento[argumento]
                    if posicion_codigo == "izquierda":
                        posicion_codigo = "left"
                    if posicion_codigo == "centro":
                        posicion_codigo = "center"
                    if posicion_codigo == "derecha":
                        posicion_codigo = "right"

                    html_final += "           <pre style= 'text-align:" +posicion_codigo+"; font-family: monospace;'>\n                 "+texto_codigo+"\n          </pre>\n"
            
            if clave_titulo == "Negrita":
                if argumento == "texto":
                    texto_negrita = valor_argumento[argumento]
                    
                    html_final += "          <strong>"+texto_negrita+"</strong><br>\n"

            if clave_titulo == "Subrayado":
                if argumento == "texto":
                    texto_subrayado = valor_argumento[argumento]
                    
                    html_final += "         <u>"+texto_subrayado+"</u><br>\n"

            if clave_titulo == "Tachado":
                if argumento == "texto":
                    texto_tachado = valor_argumento[argumento]
                    
                    html_final += "         <del>"+texto_tachado+"</del><br>\n"

            if clave_titulo == "Cursiva":
                if argumento == "texto":
                    texto_cursiva = valor_argumento[argumento]
                    
                    html_final += "         <em>"+texto_cursiva+"</em><br>\n"
            
            if clave_titulo == "Salto":
                if argumento == "cantidad":
                    cantidad_salto = valor_argumento[argumento]
                    for i in range(int(cantidad_salto)):
                        salto ="         <br>\n"
                        html_final += salto

            if clave_titulo == "Tabla":
                if argumento == "fila":
                    fila_tabla = valor_argumento[argumento]
                if argumento == "columna":
                    columna_tabla = valor_argumento[argumento]

                html_final += "<table><tr><td>" "</td><td>" "</td><td>" "</td></tr></table>"

    htmlFile = open(name_page + ".html", "w", encoding="utf-8")
    html_final += "         </div>\n        </body>\n</html>\n"       
    
    print(html_final)
    htmlFile.write(html_final)
    webbrowser.open(name_page+".html")
    return html_final
















































































'''
 
   
    if "Inicio" in elementos:
        if "Cuerpo" in elementos["Inicio"]:
            for instruccion in elementos["Inicio"]["Cuerpo"]:
                for clave, valor in instruccion.items():
                    if clave == "Titulo":
                        html_final += f"<h1 style= 'text-align: {valor["posicion"]}; color: {valor["color"]}; font-size: {valor["tamaño"]};'>{valor["texto"]}</h1>>\n"
                    
                    elif clave == "Fondo":
                        html_final += f"<div style = 'background-color: {valor["color"]};'>\n"
                    
                    elif clave == "Parrafo":
                        html_final += f"<p style = 'text-align: {valor["posicion"]};'>{valor["texto"]}</p>\n"
                    
                    elif clave == "Texto":
                        html_final += f"<p style = 'font-family: {valor["fuente"]}; color: {valor["color"]}; font-size: {valor["tamaño"]}px;'>Texto Normal</p>\n"
                    
                    elif clave == "Codigo":
                        html_final += f"<pre style = 'text-align: {valor["posicion"]};'>{valor["texto"]}</pre>\n"

                    elif clave == "Negrita":
                        html_final += f"<strong>{valor["texto"]}</strong>\n"

                    elif clave == "Subrayado":
                        html_final += f"<u>{valor["texto"]}</u>\n"

                    elif clave == "Tachado":
                        html_final += f"<strike>{valor["texto"]}</strike>\n" 

                    elif clave == "Cursiva":
                        html_final += f"<em>{valor["texto"]}</em>\n"

                    elif clave == "Salto":
                        html_final += "<br>\n" * int(valor["cantidad"])
        html_final += "</div>\n</body>\n</html>\n"'''