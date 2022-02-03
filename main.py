from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDate
Form, Window = uic.loadUiType("tracker.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def on_click():
    print(form.plainTextEdit.toPlainText())
    print(form.dateEdit.dateTime().toString('dd-MM-yy'))
    #print('clicked')
    #print(form.calendarWidget.selectedDate().toString('dd-MM-yy'))
    #date = QDate(2022, 9, 30)
    #form.calendarWidget.setSelectedDate(date)
    
def on_click_calendar():
    print(form.calendarWidget.selectedDate().toString('dd-MM-yy'))
    form.dateEdit.setDate(form.calendarWidget.selectedDate())
    
def on_dateedit_change():
    print(form.dateEdit.dateTime().toString('dd-MM-yy'))
    form.calendarWidget.setSelectedDate(form.dateEdit.date())

form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateedit_change)

#form.label.setText('asdasdsa')


app.exec_()