from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from Datos.estudiante import Estudiante
from GUI.vtn_principal import Ui_vtn_principal


class EstudianteServicio(QMainWindow):
    def __init__(self):
        super(EstudianteServicio, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.estudiante = None
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.txt_cedula.setValidator(QIntValidator())
        regex = QRegularExpression("^\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b$")
        validator = QRegularExpressionValidator(regex)
        self.ui.txt_email.setValidator(validator)


    def grabar(self):
        if self.validar_datos():
            nombre = self.ui.txt_nombre.text().capitalize()
            email = self.ui.txt_email.text().lower()
            semestre = self.ui.cb_semestre.currentText()
            self.estudiante = Estudiante(nombre=nombre, email=email, semestre=semestre)

            try:
                with open('estudiante.txt', 'a') as archivo:
                    archivo.write(self.estudiante.__str__())
                    archivo.write('\n')
                self.ui.sb_estado.showMessage('Ingreso exitoso.',3000)
                self.ui.txt_email.setText('')
                self.ui.txt_nombre.setText('')
                self.ui.txt_cedula.setText('')
                self.ui.cb_semestre.setCurrentText('Seleccionar')
            except Exception as e:
                QMessageBox.critical(self, 'Error', 'No se pudo grabar.')
                print(e)
        else:
                QMessageBox.warning(self, 'Advertencia', 'Falta ingresar datos.')

    def validar_datos(self):
        return (len(self.ui.txt_nombre.text()) > 0
                and len(self.ui.txt_email.text()) > 0
                and self.ui.cb_semestre.currentText()!='Seleccionar'
                and len(self.ui.txt_cedula.text())==10)

