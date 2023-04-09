from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from stylesheets import mainWindowStyle as style
from pages.gameRules import gameRuleForm
from pages.gameMode import gameModeForm
from pages.scoreWindow import scoreWindow
from languages.languageManager import lang
from pages.winnerWindow import winnerWindow
from pages.addWordWindow import addWordWindow
from pages.rulesWindow import rulesWindow

class mainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUi()

	def initUi(self):
		self.lang = "en"

		self.setFixedSize(300, 500)
		self.setWindowIcon(QIcon("icons/window.png"))
		self.setStyleSheet(style.window)

		self.initButtons()
		self.set_language()

	def initButtons(self):
		self.team_list = ["Team 1", "Team 2"]
		self.game_rule = (30, 50)

		self.lang_btn = QPushButton(self)
		self.lang_btn.setGeometry(5, 5, 40, 30)
		self.lang_btn.setStyleSheet(style.lang_btn)
		self.lang_btn.clicked.connect(self.change_language)


		self.gamemode_btn = QPushButton(self)
		self.gamemode_btn.setGeometry(205, 10, 85, 30)
		self.gamemode_btn.setStyleSheet(style.gamemode_btn)
		self.gamemode_btn.clicked.connect(lambda:gameModeForm(self))

		self.gamerule_btn = QPushButton(self)
		self.gamerule_btn.setGeometry(205, 50, 85, 30)
		self.gamerule_btn.setStyleSheet(style.gamerule_btn)
		self.gamerule_btn.clicked.connect(lambda:gameRuleForm(self))

		self.play_btn = QPushButton(self)
		self.play_btn.setGeometry(10, 400, 280, 90)
		self.play_btn.setStyleSheet(style.play_btn)
		self.play_btn.clicked.connect(lambda:scoreWindow(self))

		self.rules_btn = QPushButton(self)
		self.rules_btn.setGeometry(10, 360, 135, 30)
		self.rules_btn.setStyleSheet(style.rules_btn)
		self.rules_btn.clicked.connect(lambda:rulesWindow(self))

		self.add_word_btn = QPushButton(self)
		self.add_word_btn.setGeometry(155, 360, 135, 30)
		self.add_word_btn.setStyleSheet(style.add_word_btn)
		self.add_word_btn.clicked.connect(lambda:addWordWindow(self))

	def change_language(self):
		style = self.lang_btn.styleSheet()
		if "en" in style:
			style = style.replace("en", "ru")
			self.lang = "ru"
		elif "ru" in style:
			style = style.replace("ru", "am")
			self.lang = "am"
		elif "am" in style:
			style = style.replace("am", "en")
			self.lang = "en"
		self.lang_btn.setStyleSheet(style)
		self.set_language()


	def set_language(self):
		team = lang[self.lang]["team"]
		self.team_list = [f"{team} 1", f"{team} 2"]

		self.setWindowTitle(lang[self.lang]["window"])
		self.gamemode_btn.setText(lang[self.lang]["gamemode"])
		self.gamerule_btn.setText(lang[self.lang]["gamerule"])
		self.rules_btn.setText(lang[self.lang]["rules"])
		self.play_btn.setText(lang[self.lang]["play"])
		self.add_word_btn.setText(lang[self.lang]["addword"])







