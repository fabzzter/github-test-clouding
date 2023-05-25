from datetime import datetime

# Crear Curso
# {api.example.com}/api/v1/admin/crear_curso
def crear_curso(profesor, lista_estudiantes, tema):
    return {"profesor" : profesor, "estudiantes" : lista_estudiantes, "tema" : tema}

def nombre_curso(curso):
    return {**curso, "nombre_curso" : curso["profesor"]["nombre"] + "-" + str(datetime.now())} # ** adiciona al objeto curso la llave y valor de "nombre_curso". Si ya existiera una llave con el mismo nombre, lo sobreescribiria.

# Estudiantes
# Definición: {nombre, edad, ubicacion, correo}
e_pablo = {"nombre" : "Pablo Montoya", "edad" : 40, "ubicacion" : "Colombia", "correo" : "pedro.peralta@gmail.com"}
e_pedro = {"nombre" : "Pedro Perez", "edad" : 26, "ubicacion" : "Perú", "correo" : "pedro.peralta@gmail.com"}
e_pepe = {"nombre" : "Pepe Gonzalez", "edad" : 18, "ubicacion" : "Mexico", "correo" : "pepe.gonzale@gmail.com"}


# Profesores
# Definición: {nombre, edad, ubicacion, correo, modulos[]}
p_camilo = {"nombre" : "Camilo Rojas", "edad" : 25, "ubicacion" : "Colombia", "correo" : "camilo.rojas@gmail.com", "modulos" : ["linux", "python", "ansible"]}

curso = crear_curso(p_camilo, [e_pablo, e_pedro, e_pepe], "linux")
curso = nombre_curso(curso)
print(curso)
print(curso.get("profesor").get("nombre"))
