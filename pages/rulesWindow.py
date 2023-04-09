from PyQt5 import QtWidgets, QtCore
from languages.languageManager import lang
from stylesheets import rulesWindowStyle as style

class rulesWindow(QtWidgets.QLabel):
	def __init__(self, parent):
		super().__init__(parent)

		self.lang = parent.lang
		self.initUi()
		self.show()

	def initUi(self):
		self.setGeometry(0, 0, 300, 500)
		self.setAlignment(QtCore.Qt.AlignCenter)
		self.setStyleSheet(style.window)
		text = lang[self.lang]["rulestext"]
		self.setText(text)

		exit_btn = lang[self.lang]["exit"]
		self.exit_btn = QtWidgets.QPushButton(exit_btn, self)
		self.exit_btn.setGeometry(10, 10, 70, 30)
		self.exit_btn.setStyleSheet(style.exit_btn)
		self.exit_btn.clicked.connect(self.deleteLater)