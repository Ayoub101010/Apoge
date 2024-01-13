from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import MySQLdb


ui, _ = loadUiType('MainAdmin.ui')
login,_ = loadUiType('Login.ui')
FirstPage,_ = loadUiType('FirstPage.ui')
studentLogin,_ =loadUiType('StudentLogin.ui')
inscription,_ = loadUiType('Inscription.ui')
studentmain, _=loadUiType('StudentMain.ui')



class PageInscription(QWidget, inscription): 
    
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.Handel_Student_Login)
        
        
    def Handel_Student_Login(self):
        
        self.window2= StudentLogin()
        self.close()
        self.window2.show()    

class Student_Main(QWidget, studentmain): 
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        
    
class PageInitial(QWidget , FirstPage):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_InitialPage)
        self.pushButton_2.clicked.connect(self.Handel_StudentLogin)

        
    def Handel_InitialPage(self) : 
        
        self.window2= Login()
        self.close()
        self.window2.show()
        
        
    def Handel_StudentLogin(self):
        
        self.window2= StudentLogin()
        self.close()
        self.window2.show()
        
class  StudentLogin(QWidget, studentLogin): 
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_student_Login)
        self.pushButton_2.clicked.connect(self.Handel_Inscription)
        self.pushButton_3.clicked.connect(self.Handel_Goback_InitialPage)
        
        
    
        


        
        
        
        
    def Handel_student_Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='apogee')
        #La création de l'objet cursor pour interagir avec la bdd, pour exécuter des requêtes SQL
        self.cur = self.db.cursor()

        CNE = self.lineEdit.text()
        datenaisetu = self.lineEdit_2.text()

        sql = ''' SELECT * FROM etudiant '''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if CNE == str(row[0]) and datenaisetu == str(row[7]):
                self.window2= Student_Main()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Make Sure You Enterd Your Username And Password Correctly')
                
    def Handel_Inscription(self): 
         self.window2= PageInscription()
         self.close()
         self.window2.show() 
         
    def Handel_Goback_InitialPage(self): 
        self.window2=PageInitial()
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
        self.pushButton_11.clicked.connect(self.Go_Back_LoginAdmin)

        
        
        
            
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
        self.tabWidget.setCurrentIndex(4)  
        
        
        
         
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

        self.lineEdit_9.setText('')
        self.lineEdit.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')  
        self.lineEdit_7.setText('')  
        self.lineEdit_8.setText('')  

    def Go_Back_LoginAdmin(self):
        warning = QMessageBox.warning(self , 'se déconnecter' , "T'es sure? " , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            

           self.window2= Login()
           self.close()
           self.window2.show() 
        
        
def main():
       app = QApplication(sys.argv)
       window = PageInitial()
       window.show()
       sys.exit(app.exec_())
       
if __name__ == '__main__':
     main()

