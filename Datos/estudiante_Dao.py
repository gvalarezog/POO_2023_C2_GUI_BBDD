from Datos.conexion import Conexion
from Dominio.estudiante import Estudiante


class EstudianteDao:

    _INSERTAR_ESTUDIANTE = ("INSERT INTO Estudiantes (nombre, cedula, semestre, email, edad) "
                            "VALUES (?, ?, ?, ?, ?)")
    _SELECCIONAR_X_CEDULA = ("SELECT NOMBRE, CEDULA, SEMESTRE, EMAIL, EDAD FROM Estudiantes "
                             "WHERE CEDULA = ?")
    _SELECCIONAR_PERSONAS = "SELECT NOMBRE, CEDULA, SEMESTRE, EMAIL, EDAD FROM Estudiantes"

    @classmethod
    def insertar_estudiante(cls, estudiante):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.nombre, estudiante.cedula, estudiante.semestre, estudiante.email
                         ,estudiante.edad, )
                cursor.execute(cls._INSERTAR_ESTUDIANTE, datos)
        except Exception as e:
            print(e)
    @classmethod
    def seleccionar_x_cedudla(cls, estudiante):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.cedula,)
                resultado = cursor.execute(cls._SELECCIONAR_X_CEDULA, datos)
                estudiante_encontrado = resultado.fetchone()
                estudiante.cedula = estudiante_encontrado[1]
                estudiante.nombre = estudiante_encontrado[0]
                estudiante.email = estudiante_encontrado[3]
                estudiante.semestre = estudiante_encontrado[2]
                estudiante.edad = estudiante_encontrado[4]
                return estudiante
        except Exception as e:
            print(e)
            estudiante = None

    @classmethod
    def seleccionar_personas(cls):
        try:
            estudiantes = list()
            cursor = Conexion.obtenerCursor()
            registros = cursor.execute(cls._SELECCIONAR_PERSONAS).fetchall()
            for registro in registros:
                estudiante = Estudiante(nombre=registro[0], cedula=registro[1]
                                        , email=registro[3], semestre=registro[2], edad=registro[4])
                estudiantes.append(estudiante)
            return estudiantes
        except Exception as e:
            print(e)
            return None

if '__main__' == __name__:
    # EstudianteDao.insertar_estudiante()
    personas = EstudianteDao.seleccionar_personas()
    for persona in personas:
        print(persona)