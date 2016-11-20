# -*- coding: utf-8 -*-
import sys
import core
from PyQt4 import QtGui,QtCore

class Form(QtGui.QWidget):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        fbox = QtGui.QFormLayout()

        self.inFe = QtGui.QLineEdit()
        self.inFe.setReadOnly(True)
        inButDir = QtGui.QPushButton(u"...")
        inButDir.clicked.connect(self.saveInButDir)
        inLayout = QtGui.QHBoxLayout()
        inLayout.addWidget(self.inFe)
        inLayout.addWidget(inButDir)
        fbox.addRow(QtGui.QLabel(u"Вкажіть назву директорії де шукати картинки"), inLayout)

        self.outFe = QtGui.QLineEdit()
        self.outFe.setReadOnly(True)
        outButDir = QtGui.QPushButton(u"...")
        outButDir.clicked.connect(self.saveOutButDir)
        outLayout = QtGui.QHBoxLayout()
        outLayout.addWidget(self.outFe)
        outLayout.addWidget(outButDir)
        fbox.addRow(QtGui.QLabel(u"Вкажіть назву директорії куди копіювати картинки"), outLayout)

        chDelete = QtGui.QCheckBox(u"Видалити директорії після копіювання із диска")
        chDelete.clicked.connect(self.saveChDelete)
        fbox.addRow(chDelete)
        chRename = QtGui.QCheckBox(u"Перейменовувати картинки у відповідності до дати створення")
        chRename.clicked.connect(self.saveChRename)
        fbox.addRow(chRename)

        prefix = QtGui.QLineEdit()
        prefix.editingFinished.connect(lambda:self.savePrefix(prefix))
        fbox.addRow(QtGui.QLabel(u"Добавити префікс до назви кожної картинки:"), prefix)

        year = QtGui.QLineEdit()
        year.editingFinished.connect(lambda:self.saveYear(year))
        fbox.addRow(QtGui.QLabel(u"Присвоїти всім картинкам рік створення:"), year)

        month = QtGui.QLineEdit()
        month.editingFinished.connect(lambda:self.saveMonth(month))
        fbox.addRow(QtGui.QLabel(u"Присвтоїти всім картинкам місяць створення:"), month)
        
        self.cp = QtGui.QLineEdit()
        self.cp.setReadOnly(True)
        self.rm = QtGui.QLineEdit()
        self.rm.setReadOnly(True)
        countLayout= QtGui.QHBoxLayout()
        countLayout.addWidget(QtGui.QLabel(u"Скопійовано картинок:"))
        countLayout.addWidget(self.cp)
        countLayout.addWidget(QtGui.QLabel(u"Видалено картинок:"))
        countLayout.addWidget(self.rm)
        fbox.addRow(countLayout)

        Ok = QtGui.QPushButton(u"Почати")
        Ok.clicked.connect(self.process)
        fbox.addRow(Ok)

        self.setLayout(fbox)

        self.setGeometry(100,100,1000,300)
        self.setWindowTitle(u"Сортування картинок")

        self.initVars()

    def initVars(self):
        self.inFeText = ""
        self.outFeText = ""
        self.PrefixText = ""
        self.YearText = ""
        self.MonthText = ""
        self.chDeleteIsChecked = False
        self.chRenameIsChecked = False

    def savePrefix(self,Prefix):
        self.PrefixText = str(Prefix.text().toUtf8())

    def saveYear(self,Year):
        self.YearText = str(Year.text().toUtf8())

    def saveMonth(self,Month):
        self.MonthText = str(Month.text().toUtf8())

    def saveChDelete(self,chDeleteIsChecked):
        self.chDeleteIsChecked = chDeleteIsChecked

    def saveChRename(self,chRenameIsChecked):
        self.chRenameIsChecked = chRenameIsChecked

    def saveInButDir(self):
        self.inFeText = QtGui.QFileDialog.getExistingDirectory(self, u'Відкрити папку звідки', 'd:\\', QtGui.QFileDialog.ShowDirsOnly)
        self.inFe.setText(self.inFeText)

    def saveOutButDir(self):
        self.outFeText = QtGui.QFileDialog.getExistingDirectory(self, u'Відкрити папку призначення', 'd:\\', QtGui.QFileDialog.ShowDirsOnly)
        self.outFe.setText(self.outFeText)

    def process(self):
        parameters = {'delete': self.chDeleteIsChecked,
                      'rename': self.chRenameIsChecked,
                      'prefix': str(self.PrefixText),
                      'year': str(self.YearText),
                      'month': str(self.MonthText)
                      }

        (numberCp, numberRm) = core.sortImgs(str(self.inFeText), str(self.outFeText), parameters)

        self.cp.setText(str(numberCp))
        self.rm.setText(str(numberRm))

def interface():
    app = QtGui.QApplication(sys.argv)
    win = Form()

    win.show()
    sys.exit(app.exec_())

