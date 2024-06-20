#El objetivo de este ejercicio es crear un programa el cual convierta cualquier tipo de texto que le des a mayuscula o minuscula
def convertir_texto():
    texto = input("Ingrese un texto: ")
    mayus_min = input("¿Quieres convertir el texto a mayúscula o minúscula? (may/min): ").lower()
    
    if mayus_min == "may":
       texto_convertido = texto.upper()
       
    elif mayus_min == "min":
      texto_convertido = texto.lower()
    else:
      print ("Error, elige una de las dos opciones proporcionadas. (may/min)")
  
      return

    print ("Texto Original: ", texto )
    print ("Texto Convertido a mayuscula:",texto_convertido)    


convertir_texto()
