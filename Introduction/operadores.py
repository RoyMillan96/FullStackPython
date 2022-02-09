## Operadores lógicos
    # and 
        # Devuelve Verdadero si las todas las variables que estoy comparando son Verdaderas
print("ejemplo de AND")
es_estudiante = True
trabaja = False
if es_estudiante and trabaja:
    print("se cumple ya que ambos son true")    
else:
    print("debe ser trabaja = True para que sucedad")
    # or
        # Devuelve verdadero si al menos una de las variables que estoy comparando es verdadera.
print("ejemplo de OR")
es_estudiante = True
trabaja = False
if es_estudiante or trabaja:
    print("se cumple ya que al menos uno es true")   
else:
    print("no se cumple por que ninguno es true")
    # not 
        # Invertir el valor boleano.
not es_estudiante
# Operadores de comparación
    # == 
        # Compara dos variables/valores, y devuelve verdadero si son iguales y falso si no lo son
    # !=
        # Compara dos variables/valores, devuelve verdadero si son diferentes o falso de lo contrario
    # > 
        #Compara dos variables/valores, devuelve verdadero si el primero es mayor que el segundo.
    # < 
        #Compara dos variables/valores, devuelve verdadero si el primero es menor que el segundo.
    # >=
        # Compara dos variables/valores, devuelve verdadero si el primero es mayor o igual que el segundo.
    # <=
        # Compara dos variables/valores, devuelve verdadero si el primero es menor o igual que el segundo.