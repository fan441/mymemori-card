#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, choice

App = QApplication([])

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q1 = Question('Какая любимая игра', 'terraria', 'Call of Duty', 'Forza Horizon', 'Skyrim')

Win = QWidget()
Win.resize(600, 400)
Win.setWindowTitle('Memory card')

Win.total = 0
Win.score = 0

Quest = QLabel('Какой национальности не существует ?')
Quest.setStyleSheet('font-size: 35px')
But = QPushButton('Ответить')
But.setStyleSheet('font-size: 35px')

QGB = QGroupBox('Варианты ответов')
QGB.setStyleSheet('font-size: 35px')

btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Смурфы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)



AGB = QGroupBox('Результаты ответа')
AGB.setStyleSheet('font-size: 35px')
result = QLabel('Правильно/Неправильно')
tr_res = QLabel('Правильный ответ')
AGB_L = QVBoxLayout()
AGB_L.addWidget(result, alignment = Qt.AlignLeft)
AGB_L.addWidget(tr_res, alignment = Qt.AlignHCenter)
AGB.setLayout(AGB_L)


ans1 = QHBoxLayout()
ans2 = QVBoxLayout()
ans3 = QVBoxLayout()

ans2.addWidget(btn1)
ans2.addWidget(btn2)
ans3.addWidget(btn3)
ans3.addWidget(btn4)

ans1.addLayout(ans2)
ans1.addLayout(ans3)

QGB.setLayout(ans1)

ML = QVBoxLayout()

ML.addWidget(Quest)
ML.addWidget(QGB)
ML.addWidget(AGB)
AGB.hide()
ML.addWidget(But)
Win.setLayout(ML)

answers = [btn1, btn2, btn3, btn4]

Question_list = list()
Question_list.append(Question('Сколько лет Ван пису ?', '27','30', '20', '19'))
Question_list.append(Question('Сколько лет Бличу ?', '20', '15', '18', '22'))
Question_list.append(Question('Сколько лет Берсерку ?', '35', '30', '29', '28'))

def show_result():
    QGB.hide()
    AGB.show()
    But.setText('Следующий вопрос')

def show_quest():
    AGB.hide()
    QGB.show()
    But.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)



def ask(q1: Question):
    shuffle(answers)
    answers[0].setText(q1.right_answer)
    answers[1].setText(q1.wrong1)
    answers[2].setText(q1.wrong2)
    answers[3].setText(q1.wrong3)
    Quest.setText(q1.question)
    tr_res.setText(q1.right_answer)
    show_quest()



def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    result.setText(res)
    show_result()

def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
        Win.score += 1
        show_result()
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    print('Статистика')
    print('Всего вопросов:', Win.total)
    print('Правильных:', Win.score)
    print('Рейтинг')


def next_question():
    Win.total += 1
    q = choice(Question_list)
    ask(q)

def clic():
    if But.text() == 'Ответить':
        check_answer()
    elif But.text() == 'Следующий вопрос':
        next_question()
next_question()
But.clicked.connect(clic)

Win.show()
App.exec_()


