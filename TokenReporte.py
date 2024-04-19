import webbrowser

def reportoken(listaToken = []):
  info = " "
  htmlFile = open("Token.html", "w", encoding="utf-8")

  htmlFile.write("""<!DOCTYPE HTML PUBLIC"

    <html>

    <head>
        <title>REPORTE </title>
     <meta http-equiv=”Content-Type” content=”text/html"; unicode=UTF-8″ />
     <meta http-equiv=”Content-Type” content=”text/html; charset=ISO-8859-1″ />
                 
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body>
    <div class="container">
  <h2 style = "background-color:#6c757d"> REPORTE DE TOKENS </h2>
  
      
  <table class="table table-dark table-borderless">
    <thead>
      <tr>
       
        <th>TIPO</th>
        <th>LEXEMA</th>
        <th>LINEA</th>
        <th>COLUMNA</th>
      </tr>
    </thead>

    """)

  for tok in listaToken:
        info += '<tr>'
        info += "<td>"+ tok.tipo + "</td>\n"
        info += "<td>"+ tok.lexema + "</td>\n"
        info += "<td>"+ str(tok.linea) + "</td>\n"
        info += "<td>"+ str(tok.columna) + "</td>\n"
        info += '<tr>'


  htmlFile.write(info)
  htmlFile.write("""
      </table>
    </div>
        </body>
        </html>""")
  webbrowser.open("Token.html")
  htmlFile.close