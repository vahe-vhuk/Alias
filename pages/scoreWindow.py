from PyQt5 import QtWidgets
from .gameWindow import gameWindow
from .winnerWindow import winnerWindow
from languages.languageManager import lang
from stylesheets import scoreWindowStyle as style

class scoreWindow(QtWidgets.QLabel):
	def __init__(self, parent):
		super().__init__(parent)

		self.parent_page = parent
		self.game_rule = parent.game_rule
		self.raund = 1
		self.initUi()
		self.show()

	def initUi(self):
		self.lang = self.parent_page.lang

		self.setGeometry(0, 0, 300, 500)
		self.setStyleSheet(style.window)

		self.score_list()
		self.queue = -1

		exit_btn = lang[self.lang]["exit"]
		self.exit_btn = QtWidgets.QPushButton(exit_btn, self)
		self.exit_btn.setGeometry(10, 10, 70, 30)
		self.exit_btn.setStyleSheet(style.exit_btn)
		self.exit_btn.clicked.connect(self.deleteLater)

		start_btn = lang[self.lang]["start"]
		self.start_btn = QtWidgets.QPushButton(start_btn, self)
		self.start_btn.setGeometry(10, 400, 280, 90)
		self.start_btn.setStyleSheet(style.start_btn)
		self.start_btn.clicked.connect(self.start_game)


	def score_list(self):
		lst = self.parent_page.team_list
		self.team_lst = []
		self.score_lst = []

		for i in range(len(lst)):
			self.team_lst.append(QtWidgets.QLabel(f"{i+1}) {lst[i]}", self))
			self.team_lst[i].setGeometry(10, 70+i*50, 180, 40)
			self.team_lst[i].setStyleSheet(style.team_lst)

			coin = lang[self.lang]["coin"]
			self.score_lst.append(QtWidgets.QLabel(f"0 {coin}", self))
			self.score_lst[i].setGeometry(200, 70+i*50, 90, 40)
			self.score_lst[i].setStyleSheet(style.score_lst)

	def start_game(self):
		if self.queue == len(self.team_lst) - 1:
			self.queue = 0
			self.raund += 1
		else:
			self.queue += 1

		team = self.team_lst[self.queue].text()
		score = self.score_lst[self.queue]
		gameWindow(self, team, score, self.raund)


	def check_winner(self):
		if self.queue == len(self.team_lst) - 1:
			max_coin = 0
			winner = 0
			for i in range(len(self.score_lst)):
				coin = int(self.score_lst[i].text().split()[0])
				if coin > max_coin:
					max_coin = coin
					winner = i
			
			if max_coin > self.game_rule[1]:
				team = self.team_lst[winner]
				score = self.score_lst[winner]
				winnerWindow(self, team, score)
		






