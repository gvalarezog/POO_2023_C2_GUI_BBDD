from Datos.conexion import Conexion


class EstudianteDao:

    _INSERTAR_ESTUDIANTE = ("INSERT INTO Estudiantes (nombre, cedula, semestre, email) "
                            "VALUES (?, ?, ?, ?)")
    _SELECCIONAR_X_CEDULA = ("SELECT NOMBRE, CEDULA, SEMESTRE, EMAIL FROM Estudiantes "
                             "WHERE CEDULA = ?")

    @classmethod
    def insertar_estudiante(cls, estudiante):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.nombre, estudiante.cedula, estudiante.semestre, estudiante.email, )
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
                return estudiante
        except Exception as e:
            print(e)
            estudiante = None

if '__main__' == __name__:
    EstudianteDao.insertar_estudiante()