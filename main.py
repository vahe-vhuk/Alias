import sys
from PyQt5.QtWidgets import QApplication
from mainWindow import mainWindow

if "__main__" == __name__:
	app = QApplication(sys.argv)

	ex = mainWindow()
	ex.show()

	sys.exit(app.exec_())

