#escrito por: Leonardo Otero
#09/07/2025

print ("Bienvenido")
print ("Este es un modelo sencillo de un asistente de sugerencias para soluciones de vulnerabilidades")
print ("Escriba la vulnerabilidad para la que necesita soluciones")


respuestas_vulnerabilidad_control_acceso = ["Implementar sistema de autenticación", "Implementar sistema de privilegios segun nivel de usuario", "Implementar validación de funcionalidades del lado del servidor solamente"]
respuestas_vulnerabilidad_ataque = ["Descargar e instalar los parches necesarios para los SO y las aplicaciones", "Actualizar software anti-virus", "Actualizar SO", "Concientizar sobre el pishing y enlaces maliciosos", "Activar el firewall"]
explicacion_detallada_parches_so = """Dirijase a la pagina oficial del sistema operativo del dispositivo vulnerable, y busque en esta la sección de parches de seguridad.
A continuación, descarguelos e instalelos en el dispositivo"""
respuestas_vulnerabilidad_ransomware = ["Crear respaldos de los archivos en servidores basados en la nube", "Adaptar los servidores fisicos a la nube", "Crear e implementar un plan de respuestana incidentes", ]
respuestas_vulnerabilidad_fisica = ["Contratar personal de seguridad", "Implementar sistema de acceso fisico a las instalaciones mediante tarjetas de acceso", "Mejorar e instalar barreras de seguridad (muros, cercas, etc.)"]

def respuesta_vulnerabilidad(vulnerabilidad):
    vulnerabilidad_1 = vulnerabilidad.lower()
    if "acceso" in vulnerabilidad_1 or "control" in vulnerabilidad_1:
        print ("Soluciones:")
        for solucion in respuestas_vulnerabilidad_control_acceso:
            print ("-", solucion)
   
    elif "malware" in vulnerabilidad_1:
          print ("Soluciones:")
          for solucion in respuestas_vulnerabilidad_ataque:
              print ("-", solucion)
         
          print ("Quiere recibir una explicación detallada de alguna solución?")
          respuesta = str(input("si/no"))
          if respuesta == "si":
             print ("De cual solución quiere ezplicación?")
             respuesta = str(input("1/2/3/4/5?"))
             if respuesta == "1":
                print (explicacion_detallada_parches_so)
             else:
                 print ("No hay explicaciones detalladas disponibles")
          else:
              print ("Ok")
      
    elif "cifrado" in vulnerabilidad_1:
         print ("Soluciones:")
         for solucion in respuestas_vulnerabilidad_ransomware:
             print ("-", solucion)
    elif "atacaron" in vulnerabilidad_1 or "entraron" in vulnerabilidad_1:
         print ("Soluciones:")
         for solucion in respuestas_vulnerabilidad_fisica:
             print ("-", solucion)
             
             

while True:
    vulnerabilidad1 = str(input("Vulnerabilidad:"))
    respuesta_vulnerabilidad(vulnerabilidad1)
    
    while True:
        print ("Quiere ver soluciones para otra vulnerabilidad?")
        respuesta = str(input("si/no"))
        if respuesta == "si":
            break
        elif respuesta == "no":
            print ("Esta bien")
            exit()
        else:
            print ("?")         