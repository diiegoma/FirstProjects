 #* Crea un programa que invierta el orden de una cadena de texto
 #* sin usar funciones propias del lenguaje que lo hagan de forma automática.
 #* - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 #*/
 
 
#cadena = "Hola Mundo"

#cadenareversa = cadena[::-1] #output odnuM aloH

#cadenareversa2 = cadena [::-2] #output onMao

#ejemplocadena = "Contraseña GITHUB"

#ejemplocadenareversa = ejemplocadena [::2]

#Si en lugar de -1 pongo -2 en el parámetro de slicing, estaré saltando de 2 en 2 caracteres en la cadena original, en lugar de tomar todos los caracteres en orden inverso.
#Por ejemplo, si tengo la cadena "Hola Mundo" y utilizo cadena[::-2], el resultado sería "o aMnd".
#Esto es porque el parámetro -2 indica que quiero empezar desde el final de la cadena y moverme hacia atrás, pero saltando de 2 en 2 caracteres. Así, la cadena resultante solo contiene cada segundo carácter de la cadena original, en orden inverso.
#En resumen, si pones -2 en lugar de -1, estarás obteniendo cada segundo carácter de la cadena original, en lugar de invertir la cadena completa. 

#Ahora voy a crear un programa el cual te pedira que cadena quieres invertir
# y esta misma la invertira, proporcionando la CADENA ORIGINAL y la CADENA INVERTIDA

def cadena_inversa ():
  cadena = input("Introduce la cadena que deseas invertir: ")
  parametrocadenas = input ("¿Quieres invertir (inv), saltar caracteres de 2 en 2 (jumptwo) o invertir la cadena y saltar caracteres de 2 en 2 (invtwo):").lower ()
  if parametrocadenas == "inv": 
    cadenareversa = cadena [::-1]
  elif parametrocadenas == "jumptwo":
    cadenareversa = cadena [::2]
  elif parametrocadenas == "invtwo":
    cadenareversa = cadena [::-2]
  else:
    print ("Error, elige una de las dos opciones proporcionadas. (inv/jumptwo/invtwo)")
    return

  print ("Cadena original:", cadena)
  print ("Cadena inversa/adelantada:", cadenareversa)
  
cadena_inversa ()


  
