from PyQt5 import QtWidgets, QtCore
from random import choice
from languages.languageManager import lang
from stylesheets import gameWindowStyle as style

class gameWindow(QtWidgets.QLabel):
	def __init__(self, parent, team_name, team_score_box, raund):
		super().__init__(parent)

		self.parent_page = parent
		self.name = team_name[3:]
		self.score_box = team_score_box
		self.raund = raund
		self.time = parent.game_rule[0]
		self.initUi()
		self.show()

	def initUi(self):
		self.lang = self.parent_page.lang


		self.setGeometry(0, 0, 300, 500)
		self.setStyleSheet(style.window)

		self.score = int(self.score_box.text().split()[0])
		self.part_score = 0

		self.word_list()

		raund = lang[self.lang]["raund"]
		r = self.raund
		self.header = QtWidgets.QLabel(f"{raund} {r} \n#{self.name}", self)
		self.header.setGeometry(10, 10, 280, 60)
		self.header.setAlignment(QtCore.Qt.AlignCenter)
		self.header.setStyleSheet(style.header)

		coin = lang[self.lang]["coin"]
		self.coin_box = QtWidgets.QLabel(f"{self.score} {coin}", self)
		self.coin_box.setGeometry(200, 10, 90, 30)
		self.coin_box.setAlignment(QtCore.Qt.AlignRight)
		self.coin_box.setStyleSheet(style.coin_box)

		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.finish_raund)
		self.timer.start(1000)

		time = lang[self.lang]["time"]
		sec = lang[self.lang]["s"]
		self.timer_box = QtWidgets.QLabel(f"{time} {self.time}{sec}", self)
		self.timer_box.setGeometry(10, 90, 280, 20)
		self.timer_box.setAlignment(QtCore.Qt.AlignCenter)
		self.timer_box.setStyleSheet(style.timer_box)

		exit_btn = lang[self.lang]["exit"]
		self.exit_btn = QtWidgets.QPushButton(exit_btn, self)
		self.exit_btn.clicked.connect(self.parent_page.deleteLater)
		self.exit_btn.setStyleSheet(style.exit_btn)
		self.exit_btn.setGeometry(10, 10, 70, 30)


		next_btn = lang[self.lang]["next"]
		self.next_btn = QtWidgets.QPushButton(next_btn, self)
		self.next_btn.setGeometry(10, 400, 280, 90)
		self.next_btn.setStyleSheet(style.next_btn)
		self.next_btn.clicked.connect(self.change_words)

	def word_list(self):
		with open(f"base/base_{self.lang}.txt", "r", encoding="utf_8") as base:
			words = base.read().splitlines()
			word_lst = [choice(words) for _ in range(5)]

		self.word_btns = []
		self.word_btns_state = {}

		for i in range(5):
			self.word_btns.append(QtWidgets.QPushButton(word_lst[i], self))
			self.word_btns[i].setGeometry(30, 140+i*50, 240, 40)
			self.word_btns[i].setStyleSheet(style.word)
			self.word_btns_state[f"{i}"] = False

		self.word_btns[0].clicked.connect(lambda:self.inc_score(0))
		self.word_btns[1].clicked.connect(lambda:self.inc_score(1))
		self.word_btns[2].clicked.connect(lambda:self.inc_score(2))
		self.word_btns[3].clicked.connect(lambda:self.inc_score(3))
		self.word_btns[4].clicked.connect(lambda:self.inc_score(4))


	def inc_score(self, i):
		if not self.word_btns_state[f"{i}"]:
			self.part_score += 1
			self.word_btns[i].setStyleSheet(style.word_checked)
			self.word_btns_state[f"{i}"] = True

			coin = lang[self.lang]["coin"]
			self.coin_box.setText(f"{self.score + self.part_score} {coin}")


	def change_words(self):
		with open(f"base/base_{self.lang}.txt", "r", encoding="utf_8") as base:
			words = base.read().splitlines()
			word_lst = [choice(words) for _ in range(5)]

		for i in range(5):
			self.word_btns[i].setText(word_lst[i])
			self.word_btns[i].setStyleSheet(style.word)
			self.word_btns_state[f"{i}"] = False
		
		self.score += (2 * self.part_score) - 5
		self.part_score = 0
		
		if self.score < 0:
			self.score = 0
		coin = lang[self.lang]["coin"]
		self.coin_box.setText(f"{self.score} {coin}")

	def finish_raund(self):
		if self.time == 0:
			coin = lang[self.lang]["coin"]
			score = self.score + self.part_score
			if score < 0:
				score = 0
			self.score_box.setText(f"{score} {coin}")

			self.deleteLater()
			self.parent_page.check_winner()
		else:
			self.time -= 1
			time = lang[self.lang]["time"]
			sec = lang[self.lang]["s"]
			self.timer_box.setText(f"{time} {self.time}{sec}")

			self.timer.startTimer(1000)





