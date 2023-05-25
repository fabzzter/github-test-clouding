from datetime import datetime

class Curso:
    campus = "CloudCamp"
    
    # Clase constructor, siempre debe crearse en una clase
    def __init__(self, profesor, estudiantes, tema):
        self.profesor = profesor
        self.estudiantes = estudiantes
        self.tema = tema
        
    def dar_nombre_curso(self):
        self.nombre_curso = self.profesor["nombre"] + "-" + str(datetime.now())

e_pablo = {"nombre" : "Pablo Montoya", "edad" : 40, "ubicacion" : "Colombia", "correo" : "pedro.peralta@gmail.com"}
e_pedro = {"nombre" : "Pedro Perez", "edad" : 26, "ubicacion" : "Perú", "correo" : "pedro.peralta@gmail.com"}
e_pepe = {"nombre" : "Pepe Gonzalez", "edad" : 18, "ubicacion" : "Mexico", "correo" : "pepe.gonzale@gmail.com"}
p_camilo = {"nombre" : "Camilo Rojas", "edad" : 25, "ubicacion" : "Colombia", "correo" : "camilo.rojas@gmail.com", "modulos" : ["linux", "python", "ansible"]}
p_andres = {"nombre" : "Andres Garcia", "edad" : 33, "ubicacion" : "Perú", "correo" : "andres.garcia@gmail.com", "modulos" : ["ansible"]}

clase_1 = Curso(p_camilo, [e_pablo, e_pedro, e_pepe], "Linux")
clase_1.dar_nombre_curso()

clase_2 = Curso(p_camilo, [e_pedro], "Python")
clase_2.dar_nombre_curso()

clase_3 = Curso(p_andres, [e_pablo, e_pedro, e_pepe], "Ansible")
clase_3.dar_nombre_curso()

print(clase_1.profesor)
print(clase_2.tema)
print(clase_3.profesor["nombre"])
print(clase_1.nombre_curso)