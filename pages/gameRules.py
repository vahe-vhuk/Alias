from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5 import QtWidgets, QtCore
from languages.languageManager import lang
from stylesheets import gameRuleWindowStyle as style

class gameRuleForm(QLabel):
	def __init__(self, parent):
		super().__init__(parent)

		self.parent_page = parent
		self.initUi()
		self.show()

	def initUi(self):
		self.lang = self.parent_page.lang

		self.setStyleSheet(style.window)
		self.setGeometry(0, 0, 300, 500)

		self.time_form()
		self.score_form()

		cancel_btn = lang[self.lang]["cancel"]
		self.cancel_btn = QtWidgets.QPushButton(cancel_btn, self)
		self.cancel_btn.setGeometry(10, 10, 50, 30)
		self.cancel_btn.setStyleSheet(style.cancel_btn)
		self.cancel_btn.clicked.connect(self.deleteLater)

		save_btn = lang[self.lang]["save"]
		self.save_btn = QtWidgets.QPushButton(save_btn, self)
		self.save_btn.setGeometry(10, 400, 280, 90)
		self.save_btn.setStyleSheet(style.save_btn)
		self.save_btn.clicked.connect(self.save)

		

		

	def time_form(self):
		time_value = self.parent_page.game_rule[0]
		game_time = lang[self.lang]["selecttime"]
		self.time_check_header = QtWidgets.QLabel(game_time, self)
		self.time_check_header.setGeometry(10, 70, 140, 20)
		self.time_check_header.setAlignment(QtCore.Qt.AlignCenter)
		self.time_check_header.setStyleSheet(style.header)

		self.time_check_spin_box = QtWidgets.QSpinBox(self)
		self.time_check_spin_box.setGeometry(30, 110, 90, 20)
		self.time_check_spin_box.setSuffix(lang[self.lang]["s"])
		self.time_check_spin_box.setMinimum(20)
		self.time_check_spin_box.setMaximum(180)
		self.time_check_spin_box.setValue(time_value)
		self.time_check_spin_box.setStyleSheet(style.spin_box)
		self.time_check_spin_box.textChanged.connect(self.change_slider_time)

		self.time_check = QtWidgets.QSlider(self)
		self.time_check.setMinimum(20)
		self.time_check.setMaximum(180)
		self.time_check.setValue(time_value)
		self.time_check.setSingleStep(2)
		self.time_check.setGeometry(30, 140, 90, 240)
		self.time_check.valueChanged.connect(self.change_spinbox_time)

	def score_form(self):
		score_value = self.parent_page.game_rule[1]
		game_score = lang[self.lang]["selectscore"]
		self.score_check_header = QtWidgets.QLabel(game_score, self)
		self.score_check_header.setGeometry(160, 70, 140, 20)
		self.score_check_header.setAlignment(QtCore.Qt.AlignCenter)
		self.score_check_header.setStyleSheet(style.header)

		self.score_check_spin_box = QtWidgets.QSpinBox(self)
		self.score_check_spin_box.setGeometry(180, 110, 90, 20)
		self.score_check_spin_box.setSuffix(lang[self.lang]["coin"])
		self.score_check_spin_box.setMinimum(20)
		self.score_check_spin_box.setMaximum(400)
		self.score_check_spin_box.setValue(score_value)
		self.score_check_spin_box.setStyleSheet(style.spin_box)
		self.score_check_spin_box.textChanged.connect(self.change_slider_score)

		self.score_check = QtWidgets.QSlider(self)
		self.score_check.setMinimum(20)
		self.score_check.setMaximum(400)
		self.score_check.setValue(score_value)
		self.score_check.setSingleStep(5)
		self.score_check.setGeometry(180, 140, 90, 240)
		self.score_check.valueChanged.connect(self.change_spinbox_score)

	def change_spinbox_time(self):
		time = self.time_check.value()
		self.time_check_spin_box.setValue(time)

	def change_slider_time(self):
		time = self.time_check_spin_box.value()
		self.time_check.setValue(time)

	def change_spinbox_score(self):
		score = self.score_check.value()
		self.score_check_spin_box.setValue(score)

	def change_slider_score(self):
		score = self.score_check_spin_box.value()
		self.score_check.setValue(score)

	def save(self):
		time = self.time_check.value()
		score = self.score_check.value()

		self.parent_page.game_rule = time, score
		self.deleteLater()
