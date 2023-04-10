from PyQt5.QtWidgets import QLabel, QPushButton, QLabel
from PyQt5 import QtWidgets
from languages.languageManager import lang
from stylesheets import gamemodeWindowStyle as style

class gameModeForm(QtWidgets.QLabel):
	def __init__(self, parent):
		super().__init__(parent)

		self.parent_page = parent
		self.initUi()
		self.show()

	def initUi(self):
		self.lang = self.parent_page.lang

		self.setStyleSheet(style.window)
		self.setGeometry(0, 0, 300, 500)

		self.team_list = []

		self.team_input = QLabel(self)
		self.team_input.setGeometry(0, 0, 300, 360)

		cancel_btn = lang[self.lang]["cancel"]
		self.cancel_btn = QtWidgets.QPushButton(cancel_btn, self)
		self.cancel_btn.setGeometry(10, 10, 70, 30)
		self.cancel_btn.setStyleSheet(style.cancel_btn)
		self.cancel_btn.clicked.connect(self.deleteLater)

		add_team = lang[self.lang]["addteam"]
		self.add_team_btn = QPushButton(add_team, self)
		self.add_team_btn.setGeometry(10, 360, 135, 30)
		self.add_team_btn.setStyleSheet(style.add_team_btn)
		self.add_team_btn.clicked.connect(self.add_team)

		remove_team = lang[self.lang]["removeteam"]
		self.remove_team_btn = QPushButton(remove_team, self)
		self.remove_team_btn.setGeometry(155, 360, 135, 30)
		self.remove_team_btn.setStyleSheet(style.remove_team_btn)
		self.remove_team_btn.clicked.connect(self.remove_team)

		save_btn = lang[self.lang]["save"]
		self.save_btn = QtWidgets.QPushButton(save_btn, self)
		self.save_btn.setGeometry(10, 400, 280, 90)
		self.save_btn.setStyleSheet(style.save_btn)
		self.save_btn.clicked.connect(self.save)

		self.form = QtWidgets.QVBoxLayout(self.team_input)
		
		for i in self.parent_page.team_list:
			self.add_team(i)


	def add_team(self, team_name=None):
		if self.form.count() >= 4:
			return
		team = lang[self.lang]["team"]
		team_header = f"{team} {self.form.count()+1}"
		if not team_name:
			team_name = team_header

		line_edit = QtWidgets.QLineEdit(team_name)
		line_edit.setStyleSheet(style.team_input)
		line_edit.setMaxLength(15)

		label = QtWidgets.QLabel(team_header)
		label.setStyleSheet(style.team_header)
		layout = QtWidgets.QHBoxLayout()
		layout.addWidget(label)
		layout.addWidget(line_edit)

		self.team_list.append(layout)

		self.form.addLayout(layout)

	def remove_team(self):
		if self.form.count() <= 2:
			return
		self.team_list.pop()
		count = self.form.count()
		item = self.form.itemAt(count - 1).layout()
		item.itemAt(0).widget().deleteLater()
		item.itemAt(1).widget().deleteLater()
		item.layout().deleteLater()

	def save(self, parent):
		self.parent_page.team_list = []
		k = 1
		for i in self.team_list:
			team = i.itemAt(1).widget().text()
			if team == "":
				team = lang[self.lang]["team"] + f" {k}"
			self.parent_page.team_list.append(team)
			k += 1

		self.deleteLater()

