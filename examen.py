# Examen práctico - Terminal de Expedición Espacial
# Nombre y apellido:francisco toledo
# Curso:2:1
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.
#
# No borrar estos comentarios.


# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
# Crear las listas de destinos y costos.
# Pedir el nombre del piloto.
nombre= "francisco"
print ("bienbenido francisco")
print ("tu combustible es 100")
combustible= 100
viajes= 3
viajesluna= 1
viajesmarte= 1
viajessaturno= 1
destinos= ["luna", "marte", "saturno"]
costos= [20, 35, 50]
# =========================
# ETAPA 2 - NAVEGACIÓN
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener destino y costo.
destinouno = input ("selecciona un destino entre la luna, marte o saturno: ")
if destinouno == "luna":
    print ("costo= 20")
elif destinouno == "marte":
    print("costo= 35")
else: 
    print ("costo= 50")
luna= 20
marte= 35
saturno= 50
if destinouno == "luna":
    print ("cobustible restante:")
    print ( combustible - luna) 
elif destinouno == "marte":
    print ("cobustible restante:")
    print(combustible - marte)
else: 
    print ("cobustible restante:")
    print (combustible - saturno)
# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la expedición.


# =========================
# ETAPA 4 - ESTADO Y RESUMEN
# =========================

# Mostrar el estado de la nave.
# Recorrer las listas con un for para mostrar destinos y costos.
