from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import MySQLdb


ui, _ = loadUiType('MainAdmin.ui')
login,_ = loadUiType('Login.ui')
FirstPage,_ = loadUiType('FirstPage.ui')


class PageInitial(QWidget , FirstPage):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handle_InitialPage)
        
    def Handle_InitialPage(self) : 
        
        self.window2= Login()
        self.close()
        self.window2.show()
        
    
        

class Login(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)
        
        
    

       
    def Handel_Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='apogee')
        #La création de l'objet cursor pour interagir avec la bdd, pour exécuter des requêtes SQL
        self.cur = self.db.cursor()

        CIN = self.lineEdit.text()
        mdpadmin = self.lineEdit_2.text()

        sql = ''' SELECT * FROM admin '''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if CIN == str(row[1]) and mdpadmin == row[2]:
                self.window2= MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Make Sure You Enterd Your Username And Password Correctly')
    

class MainApp(QWidget, ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()


        
    def Handel_Buttons(self):
        
        self.pushButton_4.clicked.connect(self.Confirmer_inscriptions)
        self.pushButton.clicked.connect(self.Ajouter_resultats)
        self.pushButton_2.clicked.connect(self.Liste_des_etudients)
        self.pushButton_3.clicked.connect(self.Resultats_des_etudients)
        self.pushButton_5.clicked.connect(self.Laureats_de_Geoinformation)
        self.pushButton_6.clicked.connect(self.Add_First_semester)

        
        
        
            
    def Handel_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)
        
        """------- Open tabs ------- """

    def Confirmer_inscriptions(self):
        self.tabWidget.setCurrentIndex(0)

    def Ajouter_resultats(self):
        self.tabWidget.setCurrentIndex(1)


    def Liste_des_etudients(self):
        self.tabWidget.setCurrentIndex(2)
        

    def Resultats_des_etudients(self):
        self.tabWidget.setCurrentIndex(3)
        
        
    def Laureats_de_Geoinformation(self):
        self.tabWidget.setCurrentIndex(3)  
        
        
        
         
        """------- Ajouter des notes pour le semestre 1 ------- """
    
    
    
    def Add_First_semester(self):
        
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='apogee')
        self.cur = self.db.cursor()
        
        CNE = self.lineEdit_9.text()
        Algo = self.lineEdit.text()
        AN = self.lineEdit_4.text()
        TS_BPT = self.lineEdit_5.text()
        LC = self.lineEdit_6.text()
        SI = self.lineEdit_7.text()
        Stat_ADD = self.lineEdit_8.text()


        
        
        self.cur.execute('''
            INSERT INTO semestre1(Algo,AN,TS_BPT,LC,SI, Stat_ADD,CNE )
            VALUES (%s , %s , %s , %s  , %s, %s, %s)
        ''' ,( Algo , AN , TS_BPT  , LC, SI, Stat_ADD, CNE ))

        self.db.commit()
        print('done')

        self.lineEdit_9.setText('')
        self.lineEdit.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')  
        self.lineEdit_7.setText('')  
        self.lineEdit_8.setText('')  

        
        
        
def main():
       app = QApplication(sys.argv)
       window = PageInitial()
       window.show()
       sys.exit(app.exec_())
       
if __name__ == '__main__':
     main()

