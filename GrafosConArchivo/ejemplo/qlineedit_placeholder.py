# coding=utf-8

import sys  # provee la interacción con el intérprete de Python

from PyQt4 import QtGui  # provee los elementos gráficos


# crea la aplicación y toma argumentos de la línea de comandos
aplicacion = QtGui.QApplication(sys.argv)

# correo
edt_correo = QtGui.QLineEdit()
edt_correo.setPlaceholderText('Correo')  # placeholder

# contraseña
edt_password = QtGui.QLineEdit()
edt_password.setPlaceholderText(u'Contraseña')  # placeholder

# los caracteres ingresados son reemplazados por un sólo caracter no alfanumérico
edt_password.setEchoMode(QtGui.QLineEdit.Password)

# botón 'iniciar sesión'
btn_iniciar = QtGui.QPushButton(u'Iniciar sesión')

# crea un vertical box layout para la ventana
vlayout = QtGui.QVBoxLayout()

# añade los widget al layout
vlayout.addWidget(edt_correo)
vlayout.addWidget(edt_password)
vlayout.addWidget(btn_iniciar)
vlayout.addStretch()

# crea la ventana y establece sus propiedades
ventana = QtGui.QWidget()
ventana.setWindowTitle('QLineEdit placeholder')
ventana.resize(300, 100)
ventana.setLayout(vlayout)  # establece el layout de la ventana
ventana.setFocus()  # la ventana adquiere el foco
ventana.show()

# ejecuta la aplicación y espera su valor de retorno al finalizar
sys.exit(aplicacion.exec_())
