#Crea un programa el cual le pida al usuario un texto, para despues poner la primera letra de cada palabra en mayuscula

def convertir_texto ():
  texto = input("Ingrese el texto que quiera convertir: ")
  cambiar_capitalizar = input ("¿Deseas cambiar las may y min (swap) o deseas capitalizar (cap) la frase?:").lower()
  
  if cambiar_capitalizar == "swap":
   texto = texto.swapcase()
  
  elif cambiar_capitalizar == "cap":
   texto = texto.title()
   
  else:
    print ("Error, elige una de las dos opciones proporcionadas. (swap/cap)")
    return

  print ("Frase/Texto original:", texto)
  print ("Frase/Texto convertido:", texto)
  
convertir_texto()