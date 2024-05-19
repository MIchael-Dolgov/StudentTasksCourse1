import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application_ui import Ui_MainWindow
from etrigger import E_Trigger

#Global object
e_trigger = E_Trigger()

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label = qtw.QLabel(self)
        pixmap = qtg.QPixmap("Resources/Images/STATE1010.svg")  # Замените на путь к вашему начальному изображению
        self.label.setPixmap(pixmap)

        self.pushButton.pressed.connect(self.on_button_click)
        self.pushButton.released.connect(self.out_button_unclick)
        self.pushButton_2.pressed.connect(self.on_button_click)
        self.pushButton_2.released.connect(self.out_button_unclick)
        self.pushButton_3.pressed.connect(self.on_button_click)
        self.pushButton_3.released.connect(self.out_button_unclick)
        
    @qtc.Slot()
    def on_button_click(self):
        print("Button clicked!")
        sender = self.sender()
        if sender == self.pushButton:
            e_trigger.update(1, 0)
            self.update_image(1, 0)
        elif sender == self.pushButton_2:
            e_trigger.update(0, 1)
            self.update_image(0, 1)
        elif sender == self.pushButton_3:
            e_trigger.update(1, 1)
            self.update_image(1, 1)

    @qtc.Slot()
    def out_button_unclick(self):
        print("unclicked")
        e_trigger.update(0, 0)
        self.update_image(0, 0)

    def update_image(self, stat1, stat2):
        #{stat1}{stat2}{e_trigger.Q}{e_trigger.Q_bar}
        print(f"{stat1}{stat2}{e_trigger.Q}{e_trigger.Q_not}")
        self.BackImg.setText(qtc.QCoreApplication.translate("MainWindow", f"<html><head/><body><p><img src=\":/states/STATE{stat1}{stat2}{e_trigger.Q}{e_trigger.Q_not}.svg\"/></p></body></html>".format(), None))
    



def run():
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__=="__main__":
    run()
else:
    raise "Is not a module!"