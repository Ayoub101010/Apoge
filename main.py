from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import MySQLdb
from PyQt5.QtCore import QDate




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
        self.pushButton.clicked.connect(self.Inscription)
        self.pushButton_2.clicked.connect(self.Handel_Student_Login)
        
        
    def Handel_Student_Login(self):
        
        self.window2= StudentLogin()
        self.close()
        self.window2.show()  
        
    def Inscription(self):
        
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='apogee')
        self.cur = self.db.cursor()
        
        CNE_t = self.lineEdit_14.text()
        nometu_t = self.lineEdit_13.text()
        prenometu_t = self.lineEdit_12.text()
        CIN_t = self.lineEdit_11.text()
        Emailetu_t = self.lineEdit_15.text()
        adretu_t = self.lineEdit_9.text()
        telephoneetu_t = self.lineEdit_10.text()
        datenaisetu_a= self.dateEdit.date()
        datenaisetu_t = datenaisetu_a.toString("yyyy-MM-dd")

        
        Annee = self.lineEdit_16.text()
        Sexe = None

        if self.checkBox.isChecked():
            Sexe = "Homme"
        elif self.checkBox_2.isChecked():
            Sexe = "Femme"

        


        
        
        self.cur.execute('''
            INSERT INTO inscription(CNE_t,nometu_t,prenometu_t,CIN_t,Emailetu_t, adretu_t,telephoneetu_t,datenaisetu_t, Sexe, Annee  )
            VALUES (%s , %s , %s , %s  , %s, %s, %s, %s, %s, %s)
        ''' ,( CNE_t , nometu_t , prenometu_t  , CIN_t, Emailetu_t, adretu_t, telephoneetu_t, datenaisetu_t, Sexe, Annee ))

        self.db.commit()

        self.lineEdit_14.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_15.setText('')  
        self.lineEdit_9.setText('')  
        self.lineEdit_10.setText('')
        self.dateEdit.setDate(QDate())
        
        self.lineEdit_16.text() 
        if self.checkBox.isChecked():
            self.checkBox.setChecked(False)
        elif self.checkBox_2.isChecked():
            self.checkBox_2.setChecked(False)  
        self.lineEdit_16.settext()

class Student_Main(QWidget, studentmain): 
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_deconnect_student)

    def Handel_deconnect_student(self):
        warning = QMessageBox.warning(self , 'se déconnecter' , "T'es sure? " , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            

           self.window2=StudentLogin()
           self.close()
           self.window2.show()   
    
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
        
        
    
        


        
        
        
        
    """def Handel_student_Login(self):
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
        
    """
    def Handel_student_Login(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='apogee')
        self.cur = self.db.cursor()

        CNE_etu = self.lineEdit.text()
        datenaisetu = self.lineEdit_2.text()
    
    # Selecting all students, assuming you want to check if a student exists
        sql = f"SELECT * FROM etudiant WHERE CNE = '{CNE_etu}' AND datenaisetu = '{datenaisetu}'"
        self.cur.execute(sql)
        student_data = self.cur.fetchone()

        if student_data :
        # The student exists, now fetch semester data
           self.cur.execute(f"SELECT Algo, AN, TS_BPT, LC, SI, Stat_ADD FROM semestre1 WHERE CNE = '{CNE_etu}'")
           semester_data1 = self.cur.fetchone()

           if semester_data1:
            # The semester data exists, update the labels
            self.tabWidget.setCurrentIndex(0)
            self.label_69.setText(str(semester_data1[0]))
            self.label_75.setText(str(semester_data1[1]))
            self.label_76.setText(str(semester_data1[2]))
            self.label_81.setText(str(semester_data1[3]))
            self.label_86.setText(str(semester_data1[4]))
            self.label_87.setText(str(semester_data1[5]))
            moyenne = (semester_data1[0] + semester_data1[1] + semester_data1[2] + semester_data1[3]+ semester_data1[4] + semester_data1[5]) / 6 
            self.label_74.setText(str(moyenne))


            self.cur.execute(f"SELECT CN_DAO, Prog_MO, IG, GAA, Anglais, OAS FROM semestre1 WHERE CNE = '{CNE_etu}'")
            semester_data2 = self.cur.fetchone()

            if semester_data2:
                self.tabWidget.setCurrentIndex(1)
                self.label_94.setText(str(semester_data2[0]))
                self.label_97.setText(str(semester_data2[1]))
                self.label_99.setText(str(semester_data2[2]))
                self.label_109.setText(str(semester_data2[3]))
                self.label_98.setText(str(semester_data2[4]))
                self.label_101.setText(str(semester_data2[5]))
                moyenne = (semester_data2[0] + semester_data2[1] + semester_data2[2] + semester_data2[3]+ semester_data2[4] + semester_data2[5]) / 6 
                self.label_96.setText(str(moyenne))

            self.cur.execute(f"SELECT Topographie, BDS, CP, MAS, SIG, G_LS FROM semestre1 WHERE CNE = '{CNE_etu}'")
            semester_data3 = self.cur.fetchone()

            if semester_data3:
                self.tabWidget.setCurrentIndex(2)
                self.label_108.setText(str(semester_data3[0]))
                self.label_111.setText(str(semester_data3[1]))
                self.label_112.setText(str(semester_data3[2]))
                self.label_113.setText(str(semester_data3[3]))
                self.label_114.setText(str(semester_data3[4]))
                self.label_115.setText(str(semester_data3[5]))
                moyenne = (semester_data3[0] + semester_data3[1] + semester_data3[2] + semester_data3[3]+ semester_data3[4] + semester_data3[5]) / 6 
                self.label_110.setText(str(moyenne))

            self.cur.execute(f"SELECT TRL, TTI, PHOTOGRA,PROG_SIG, Anglais2, WBM FROM semestre1 WHERE CNE = '{CNE_etu}'")
            semester_data4 = self.cur.fetchone()

            if semester_data4:
                self.tabWidget.setCurrentIndex(3)
                self.label_122.setText(str(semester_data4[0]))
                self.label_123.setText(str(semester_data4[1]))
                self.label_124.setText(str(semester_data4[2]))
                self.label_125.setText(str(semester_data4[3]))
                self.label_126.setText(str(semester_data4[4]))
                self.label_127.setText(str(semester_data4[5]))
                moyenne = (semester_data4[0] + semester_data4[1] + semester_data4[2] + semester_data4[3]+ semester_data4[4] + semester_data4[5]) / 6 
                self.label_129.setText(str(moyenne))

            self.cur.execute(f"SELECT GES, GET, SIG_PD, GMP, GR, ADS FROM semestre1 WHERE CNE = '{CNE_etu}'")
            semester_data5 = self.cur.fetchone()
 
            if semester_data5:
                self.tabWidget.setCurrentIndex(4)
                self.label_136.setText(str(semester_data5[0]))
                self.label_139.setText(str(semester_data5[1]))
                self.label_140.setText(str(semester_data5[2]))
                self.label_141.setText(str(semester_data5[3]))
                self.label_142.setText(str(semester_data5[4]))
                self.label_143.setText(str(semester_data5[5]))
                moyenne = (semester_data5[0] + semester_data5[1] + semester_data5[2] + semester_data5[3]+ semester_data5[4] + semester_data5[5]) / 6 
                self.label_138.setText(str(moyenne))


            else:
             print("No semester data found for the student.")
        else:
          print("Student not found.")
    
        self.db.close()

                   


                   

                

            

        
           
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
        self.pushButton_2.clicked.connect(self.Handel_Goback_InitialPage)

        
        
    

       
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
    def Handel_Goback_InitialPage(self): 
        self.window2=PageInitial()
        self.close()
        self.window2.show() 

class MainApp(QWidget, ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        self.Show_All_Results_S1()
        self.Show_All_Results_S2()
        self.show_Inscriptions()


        
    def Handel_Buttons(self):
        
        self.pushButton_4.clicked.connect(self.Confirmer_inscriptions)
        self.pushButton.clicked.connect(self.Ajouter_resultats)
        self.pushButton_2.clicked.connect(self.Liste_des_etudients)
        self.pushButton_3.clicked.connect(self.Resultats_des_etudients)
        self.pushButton_5.clicked.connect(self.Laureats_de_Geoinformation)
        self.pushButton_6.clicked.connect(self. Add_First_semester)
        self.pushButton_7.clicked.connect(self.Add_Second_semester)

        self.pushButton_11.clicked.connect(self.Go_Back_LoginAdmin)

        
        
    """ Hide Tabs """  
            
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
        
        self.Show_All_Results_S1()
        
        
    def Add_Second_semester(self):
        
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='jenousJe@123' , db='apogee')
        self.cur = self.db.cursor()
        
        CNE = self.lineEdit_12.text()
        CN_DAO = self.lineEdit_2.text()
        Prog_MO= self.lineEdit_13.text()
        IG = self.lineEdit_11.text()
        GAA = self.lineEdit_14.text()
        Anglais = self.lineEdit_15.text()
        OAS = self.lineEdit_10.text()


        
        
        self.cur.execute('''
            INSERT INTO semestre2(CN_DAO,Prog_MO,IG,GAA,Anglais, OAS,CNE )
            VALUES (%s , %s , %s , %s  , %s, %s, %s)
        ''' ,( CN_DAO , Prog_MO , IG  , GAA, Anglais, OAS, CNE ))

        self.db.commit()

        self.lineEdit_12.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_14.setText('')  
        self.lineEdit_15.setText('')  
        self.lineEdit_10.setText('')  
        
        self.Show_All_Results_S2()    

    def Go_Back_LoginAdmin(self):
        warning = QMessageBox.warning(self , 'se déconnecter' , "T'es sure? " , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            

           self.window2= Login()
           self.close()
           self.window2.show() 
    '''------List the results-----'''
    
           
    def Show_All_Results_S1(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='apogee')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT semestre1.CNE, etudiant.nometu, etudiant.prenometu, semestre1.Algo, semestre1.AN, semestre1.TS_BPT, semestre1.LC,semestre1.SI, semestre1.Stat_ADD FROM semestre1 INNER JOIN etudiant ON etudiant.CNE = semestre1.CNE ''')
        data = self.cur.fetchall()
        print(data)
        self.tabWidget_4.setCurrentIndex(0)  

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)

        for row, form in enumerate(data ) :
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

        self.db.close()   
        
    def Show_All_Results_S2(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='apogee')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT semestre2.CNE, etudiant.nometu, etudiant.prenometu, semestre2.CN_DAO, semestre2.Prog_MO, semestre2.IG, semestre2.GAA,semestre2.Anglais, semestre2.OAS FROM semestre2 INNER JOIN etudiant ON etudiant.CNE = semestre2.CNE ''')
        data = self.cur.fetchall()
        print(data)
        self.tabWidget_4.setCurrentIndex(1)  

        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)

        for row, form in enumerate(data ) :
            for column, item in enumerate(form):
                self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)

        self.db.close() 
        
    def show_Inscriptions(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='jenousJe@123', db='apogee')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT CNE_t, nometu_t, prenometu_t, CIN_t, Emailetu_t, adretu_t, telephoneetu_t, datenaisetu_t, Sexe, Annee FROM inscription ''')
        data = self.cur.fetchall()
        print(data)

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        for row, form in enumerate(data ) :
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

        self.db.close()
        
        
def main():
       app = QApplication(sys.argv)
       window = PageInitial()
       window.show()
       sys.exit(app.exec_())
       
if __name__ == '__main__':
     main()

