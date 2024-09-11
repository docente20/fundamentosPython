#Funcion personalizada para formatear los numero con separadores
#de miles y decimales (Estilo Colombiano)

def formatearNum(numero):
    numFormateado = f"{numero:,.2f}" #7,654,789.88
    return numFormateado.replace(",","_").replace(".",",").replace("_",".")


numero = 7654789.887
print(formatearNum(numero))

