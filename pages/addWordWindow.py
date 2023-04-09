from PyQt5 import QtWidgets, QtCore
from languages.languageManager import lang
from stylesheets import addWordWindowStyle as style

class addWordWindow(QtWidgets.QLabel):
	def __init__(self, parent):
		super().__init__(parent)

		self.lang = parent.lang
		self.initUi()
		self.show()

	def initUi(self):
		self.setGeometry(0, 0, 300, 500)
		self.setStyleSheet(style.window)

		exit_btn = lang[self.lang]["exit"]
		self.exit_btn = QtWidgets.QPushButton(exit_btn, self)
		self.exit_btn.setGeometry(10, 10, 70, 30)
		self.exit_btn.setStyleSheet(style.exit_btn)
		self.exit_btn.clicked.connect(self.deleteLater)

		self.input = QtWidgets.QLineEdit(self)
		self.input.setStyleSheet(style.word_input)
		self.input.setGeometry(10, 350, 280, 30)

		add = lang[self.lang]["add"]
		self.add_btn = QtWidgets.QPushButton(add, self)
		self.add_btn.setGeometry(10, 400, 280, 90)
		self.add_btn.setStyleSheet(style.add_btn)
		self.add_btn.clicked.connect(self.add_word)

	def add_word(self):
		word = self.input.text()
		if not word:
			return

		with open(f"base/base_{self.lang}.txt", "r", encoding="utf_8") as base:
			words = base.read().splitlines()


		if word.capitalize() in words:
			msg = lang[self.lang]["existmsg"]
			messege(self, msg)
			return

		for i in word.lower():
			if i not in lang[self.lang]["letters"]:
				msg = lang[self.lang]["wrongmsg"]
				messege(self, msg)
				return

		with open(f"base/base_{self.lang}.txt", "a", encoding="utf_8") as base:
			base.write(f"\n{word.capitalize()}")

		msg = lang[self.lang]["succesmsg"]
		messege(self, msg)



class messege(QtWidgets.QLabel):
	def __init__(self, parent, msg):
		super().__init__(parent)

		self.initUi(msg)
		self.show()

	def initUi(self, msg):
		self.setGeometry(10, 80, 280, 90)
		self.setStyleSheet(style.msg)
		self.setAlignment(QtCore.Qt.AlignCenter)
		self.setText(msg)

		timer = QtCore.QTimer(self)
		timer.start(2000)
		timer.timeout.connect(self.deleteLater)




