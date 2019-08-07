from sys import (exit, argv)
from PyQt5.QtCore import *#(Qt, QRegExp)
from PyQt5.QtWidgets import *#(QToolTip, QPushButton, QApplication, QWidget, QLabel, QLineEdit)
from PyQt5.QtGui import *#(QIcon, QPixmap, QFont, QRegExpValidator)
from random import *#choice
from time import sleep

WORDS = ['Captivity']
''', 'America', 'Europe', 'Federal', 'Gluten', 'Ridiculous', 'Automatic', 'Television', 'Difficult', 'Severe', 'Interesting','Indonesia',
'Industrial', 'Automotive', 'President', 'Terrestrial', 'Academic', 'Comedic', 'Comical', 'Genuine',
'Suitcase', 'Vietnam', 'Achievement', 'Careless', 'Monarchy', 'Monetary',  'Quarantine', 'Supernatural',
'Illuminate', 'Optimal', 'Application', 'Scientist', 'Software', 'Hardware', 'Program', 'Colonial', 'Algorithm',
'Intelligent', 'Electricity', 'Verification', 'Broadband', 'Quality', 'Validation', 'Online', 'Telephone',
'Dictionary', 'Keyboard', 'China', 'London', 'Jamaica', 'Biology', 'Chemistry', 'History', 'Historian', 
'Africa', 'Mathematics', 'Computer', 'Literature', 'Gravity', 'Guitar', 'Violin', 'Illuminate', 'England', 
'China', 'Japan', 'Canada', 'Suitcase', 'Wireless', 'Internet']
'''
HANGMAN_PARMS = 100, 200, Qt.KeepAspectRatio, Qt.FastTransformation

class hangman(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):

        #Window Features
        self.setWindowTitle('Hangman')
        self.setWindowIcon(QIcon('Hangman7'))
        self.setGeometry(500, 50, 600, 1300)
        #self.setFixedSize(600, 1300)

        #Game Title
        self.GameTitle = QLabel('HANGMAN', self)
        self.GameTitle.setFont(QFont('Chiller', 60))
        self.GameTitle.move(130, 10)
        
        self.number = 1
        #The first  picture that shows up
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('Hangman{}.png'.format(self.number)))
        self.image.move(0, 150)

        self.word = choice(WORDS)#Random choice from the list of words        
        blank_word = '_ ' * len(self.word)
        blank_word.rstrip()  

        #Adding the blank lines to the window
        self.blank_word_label = QLabel(blank_word, self)
        font1 = self.blank_word_label.font()
        font1.setPointSize(24)
        self.blank_word_label.setFont(font1)
        self.blank_word_label.move(180, 180)
        
        self.guessed_letters = ''

        #Defining the submit button
        self.btn = QPushButton('Check', self)
        self.btn.setFont(QFont('SansSerif', 20))
        self.btn.clicked.connect(self.check_letter)
        self.btn.resize(102, 43)
        self.btn.move(250, 820)

        #Defining the line edit
        self.entered_letter = QLineEdit(self)
        
        #Validating what happens in the line edit (Only letters and only one word)
        regex = QRegExp("[a-z-A-Z_]+")
        validator = QRegExpValidator(regex)
        self.entered_letter.setValidator(validator)
        self.entered_letter.setFont(QFont('Sanserif',24))
        self.entered_letter.setMaxLength(1)
        self.entered_letter.setFocus(True)
        self.entered_letter.returnPressed.connect(self.check_letter)
        self.entered_letter.resize(100, 43)
        self.entered_letter.move(150, 820)   

        #This is where either the correct or incorrect.png will show on the window
        self.correct_or_incorrect = QLabel(self)
        self.correct_or_incorrect.move(0, 150)
        self.correct_or_incorrect.setVisible(False)

        #The image after the person misses seven times
        self.you_lose = QLabel(self)
        self.you_lose.setPixmap(QPixmap('Game Over.png'))
        self.you_lose.move(0, 150)
        self.you_lose.setVisible(False)

        
        #After the person fails seven times, the correct word shows
        self.correct_word = QLabel('The word was: {}'.format(self.word), self)
        #self.correct_word.setText(self.word)
        self.correct_word.setFont(QFont('Times New Roman', 18))
        self.correct_word.move(0,190)
        self.correct_word.setAlignment(Qt.AlignCenter)
        self.correct_word.setVisible(False)

        #The replay button without instruction
        self.replay_btn = QPushButton('Play Again', self)
        self.replay_btn.setFont(QFont('SansSerif', 15))
        self.replay_btn.clicked.connect(self.replay)
        self.replay_btn.resize(200, 50)
        self.replay_btn.move(200, 820)
        self.replay_btn.setVisible(False)

        self.show()

    def check_letter(self):
        
            if self.entered_letter.text().lower() in self.word.lower():#If **a** letter is guessed correctly
                self.guessed_letters += self.entered_letter.text().lower()
                self.correct_or_incorrect.setPixmap(QPixmap('Correct.png').scaled(40, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation))
                self.correct_or_incorrect.setVisible(True)
                QApplication.processEvents()
                sleep(0.1)
                self.correct_or_incorrect.setVisible(False)
                QApplication.processEvents()

            else:#If a letter is guessed incorrectly
                
                self.number += 1
                self.image.setPixmap(QPixmap('Hangman{}.png'.format(self.number)))#.scaled(*HANGMAN_PARMS))
                self.correct_or_incorrect.setPixmap(QPixmap('Incorrect.png'))
                self.correct_or_incorrect.setVisible(True)
                QApplication.processEvents()
                sleep(0.1)
                self.correct_or_incorrect.setVisible(False)
                QApplication.processEvents()    

                #the_list = append(entered_letter.text().lower())             

            blank_word = ''
            for i in self.word:
                if i.lower() in self.guessed_letters:
                    blank_word += i   

                else:
                    blank_word += '_ '


            blank_word.rstrip()

            self.blank_word_label.setText(blank_word)
            self.entered_letter.setText('')
            #self.entered_letter.setFocus(True)

            
            if self.number == 7:#When the person misses 7 times (0 to 6 times)
                self.blank_word_label.setText(self.word)
                self.image.setVisible(False)
                self.entered_letter.setVisible(False)
                self.btn.setVisible(False)
                self.you_lose.setVisible(True)
                self.correct_word.setVisible(True)
                self.replay_btn.setVisible(True)

            
            if blank_word == self.word:#When the person guesses all the letters correctly
                self.image.setPixmap(QPixmap('You Win.png'))
                self.image.setVisible(True)
                self.entered_letter.setVisible(False)
                self.btn.setVisible(False)
                self.correct_word.setVisible(True)
                self.replay_btn.setVisible(True)
                #self.blank_word.setVisible(False)

    def replay(self):
        self.number = 1
        self.image.setPixmap(QPixmap('Hangman{}.png'.format(self.number)))
        self.word = choice(WORDS)
        blank_word = '_ ' * len(self.word)
        blank_word.rstrip()
        self.blank_word_label.setText(blank_word)
        self.guessed_letters = ''
        #Hiding the pictures that show at the end of the game
        self.you_lose.setVisible(False)
        #self.you_win.setVisible(False)
        self.correct_word.setVisible(False)
        self.replay_btn.setVisible(False)
        self.image.setVisible(True)#The initial image is set visible again
        self.entered_letter.setVisible(True)
        self.btn.setVisible(True)
        self.entered_letter.setFocus(True)

if __name__ == '__main__':

    app = QApplication(argv)
    ex = hangman()
    ex.show()
    exit(app.exec_())
