from PyQt5 import QtWidgets, QtCore
from languages.languageManager import lang
from stylesheets import winnerWindowStyle as style

class winnerWindow(QtWidgets.QLabel):
	def __init__(self, parent, winner, score):
		super().__init__(parent)

		self.lang = parent.lang
		self.initUi(parent, winner, score)
		self.show()

	def initUi(self, parent, winner, score):
		self.setGeometry(0, 0, 300, 500)
		self.setStyleSheet(style.window)

		header = lang[self.lang]["victory"]
		self.header = QtWidgets.QLabel(header, self)
		self.header.setGeometry(10, 30, 280, 40)
		self.header.setAlignment(QtCore.Qt.AlignCenter)
		self.header.setStyleSheet(style.header)

		self.winner = QtWidgets.QLabel(winner.text(), self)
		self.winner.setGeometry(10, 80, 280, 40)
		self.winner.setAlignment(QtCore.Qt.AlignCenter)
		self.winner.setStyleSheet(style.winner)

		scores = lang[self.lang]["score"]
		self.score = QtWidgets.QLabel(scores, self)
		self.score.setGeometry(10, 130, 280, 40)
		self.score.setAlignment(QtCore.Qt.AlignCenter)
		self.score.setStyleSheet(style.score)

		coin = score.text().split()[0]
		self.coin = QtWidgets.QLabel(coin, self)
		self.coin.setGeometry(10, 180, 280, 40)
		self.coin.setAlignment(QtCore.Qt.AlignCenter)
		self.coin.setStyleSheet(style.coin)

		congrat = lang[self.lang]["congrat"]
		self.congrat = QtWidgets.QLabel(congrat, self)
		self.congrat.setGeometry(10, 230, 280, 40)
		self.congrat.setAlignment(QtCore.Qt.AlignCenter)
		self.congrat.setStyleSheet(style.congrat)

		exit = lang[self.lang]["exit"]
		self.exit_btn = QtWidgets.QPushButton(exit, self)
		self.exit_btn.setGeometry(10, 400, 280, 90)
		self.exit_btn.setStyleSheet(style.exit_btn)
		self.exit_btn.clicked.connect(parent.deleteLater)