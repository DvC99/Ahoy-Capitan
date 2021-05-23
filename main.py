""" Programa para apoyar al marinero Seijo
    Daniel Valencia Cordero
    Mayo 3-2021 """

import utilidades as util

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# Ejecuta el programa varias veces para ver su funcionamiento
criatura= util.aparecer_criatura()
direccion=util.aparecer_direccion()

if(criatura == 'Kraken'):
  if(direccion == 'babor' or direccion == 'estribor'):
    print("Ahoy! capitán, un Kraken a "+direccion)
  elif(direccion == 'proa' or direccion == 'popa'):
    print("Ahoy! capitán, un Kraken por la "+direccion)
elif(criatura == 'Sirenas'):
  if(direccion == 'babor' or direccion == 'estribor'):
    print("Ahoy! capitán, unas Sirenas a "+direccion)
  elif(direccion == 'proa' or direccion == 'popa'):
    print("Ahoy! capitán, unas Sirenas por la "+direccion)
elif(criatura == 'Ballena'):
  if(direccion == 'babor' or direccion == 'estribor'):
    print("Ahoy! capitán, una Ballena a "+direccion)
  elif(direccion == 'proa' or direccion == 'popa'):
    print("Ahoy! capitán, una Ballena por la "+direccion)
elif(criatura == 'Hipocampo'):
  if(direccion == 'babor' or direccion == 'estribor'):
    print("Ahoy! capitán, un Hipocampo a "+direccion)
  elif(direccion == 'proa' or direccion == 'popa'):
    print("Ahoy! capitán, un Hipocampo por la "+direccion)
elif(criatura == 'Macaraprono'):
  if(direccion == 'babor' or direccion == 'estribor'):
    print("Ahoy! capitán, una Macaraprono a "+direccion)
  elif(direccion == 'proa' or direccion == 'popa'):
    print("Ahoy! capitán, una Macaraprono por la "+direccion)
elif(criatura == 'Pulpo'):
  if(direccion == 'babor' or direccion == 'estribor'):
    print("Ahoy! capitán, un Pulpo a "+direccion)
  elif(direccion == 'proa' or direccion == 'popa'):
    print("Ahoy! capitán, un Pulpo por la "+direccion)
elif(criatura == 'Leviatanes'):
  if(direccion == 'babor' or direccion == 'estribor'):
    print("Ahoy! capitán, unos Leviatanes a "+direccion)
  elif(direccion == 'proa' or direccion == 'popa'):
    print("Ahoy! capitán, unos Leviatanes por la "+direccion)
elif(criatura == 'Hidras'):
  if(direccion == 'babor' or direccion == 'estribor'):
    print("Ahoy! capitán, unas Hidras a "+direccion)
  elif(direccion == 'proa' or direccion == 'popa'):
    print("Ahoy! capitán, unas Hidras por la "+direccion)