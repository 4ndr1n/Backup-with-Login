import glob
import os
import os.path
import pathlib
import shutil
import sys
import time
from datetime import datetime
from os import path
from tkinter import *
from tkinter.messagebox import *
import mysql.connector


class Login():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("450x300")
        self.root.title("Login")
        self.create_elements()
        self.root.mainloop()
        
    def create_elements(self):

        self.databasepass = Label(self.root, text="Basepassword:", font=('Verdana', 14, 'bold'))
        self.databasepass.place(x=5, y=25)

        self.entry_databasepass= Entry(self.root, font=('Verdana', 14))
        self.entry_databasepass.place(x=167, y=25)
        
        self.username = Label(self.root, text="Username:", font=('Verdana', 14, 'bold'))
        self.username.place(x=50, y=60)
 
        self.entry_username = Entry(self.root, font=('Verdana', 14))
        self.entry_username.place(x=167, y=60)
 
        self.password = Label(self.root, text="Password:", font=('Verdana', 14, 'bold'))
        self.password.place(x=55, y=95)
 
        self.entry_password = Entry(self.root, font=('Verdana', 14))
        self.entry_password.place(x=167, y=95)
 
        self.login_button = Button(self.root, text="Login", height=2, width=10, command=self.login_user)
        self.login_button.place(x=180, y=160)

        self.register_button = Button(self.root, text="registrieren", height=2, width=10, command=self.destroy_login)
        self.register_button.place(x=180, y=220)

    def destroy_login(self):
        self.root.destroy()
        register = Register()

    def login_user(self):
        username = self.entry_username.get()
        userpassword = self.entry_password.get()
        databasepass = self.entry_databasepass.get()
 
        if(username == "" or userpassword == "" or databasepass == ""):
            showinfo("Oops!","Die Felder dürfen nicht leer sein!")
            return
<<<<<<< HEAD
        
        try:
            mydb = mysql.connector.connect(
                                host='localhost',
                                database='Schulprojekt',
                                user='root',
                                password=databasepass)
            cs = mydb.cursor(buffered= True)
            mycursor = mydb.cursor()
            sql = "select user, pass from user where user=%s and pass=%s"
            val = (username, userpassword)
            mycursor.execute(sql, val)
            resultLogin = mycursor.fetchone()
            self.entry_username.delete(0, END)
            self.entry_password.delete(0, END)
            self.entry_databasepass.delete(0, END)
            if resultLogin:
                self.root.destroy()
                #die varibaleln mit den einzelenen Buchstaben wurden für die Schleifen gemacht
                #hier fängt das Backup-Szenario an
                d = 1
                while d == 1:
                    print("Möchtest du ein Backup machen, durchsuchen oder exit?")
                    #uip bis uip3 Variabeln sind Userinput zu Fragen mit mehr als 2 Antworten
                    uip = input("Bestätige mit [B]ackup oder [d]urchsuchen oder [E]xit: ")
                    if uip == "B":
                        if path.exists("/media/vmadmin/BACKUP"):
                            fulldir = "/media/vmadmin/BACKUP/Backup"
                            disk = os.statvfs(fulldir)
                            totalAvailSpace = float(disk.f_bsize*disk.f_bfree)
                            print("Verügbarer Speicherplatz:. %.2f GB" % (totalAvailSpace/1024/1024/1024))
                            if totalAvailSpace < 5:
                                shutil.rmtree(min(pathlib.Path(fulldir).glob('*/'), key=os.path.getctime))
                            e = 1
                            while e == 1:
                                print("Willst du ein Backup von Alles machen?")
                                #uipA, uipD, uipDL sind Userinput für Ja und nein Fragen
                                uipA = input("Bestätige mit [J]a oder [N]ein: ")
                                if uipA == "J":
                                    shutil.copytree("/home/vmadmin/Videos", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-AL/Videos')
                                    shutil.copytree("/home/vmadmin/Bilder", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-AL/Bilder')
                                    shutil.copytree("/home/vmadmin/Dokumente", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-AL/Dokumente')
                                    shutil.copytree("/home/vmadmin/Downloads", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-AL/Downloads')
                                    backup_dir= "/media/vmadmin/BACKUP/Backup/"
                                    newest_dir = max(pathlib.Path(backup_dir).glob('*/'), key=os.path.getctime)
                                    for root, dir, files in os.walk(newest_dir ):
                                        for list in files:
                                            list=os.path.join(root,list) #root und filename gejoint für full path damit alle Files vom Ordner und dessen Unterordner gezeigt werden 
                                            listSql = "\""+ list +"\""
                                            float_size = os.path.getsize(list)/float(1<<10)
                                            file_size = str(float_size)
                                            file_sizeSql = "\""+ file_size +"\""
                                            createDate = time.ctime(os.path.getctime(list))
                                            createDateSql = "\""+ createDate +"\""
                                            savequeryA = "INSERT into Backup (filepath, filesize, copydate) values ({}, {}, {});".format(listSql, file_sizeSql, createDateSql)
                                            cs.execute(savequeryA)
                                            mydb.commit()
                                    print("Backup abgeschlossen")
                                    e = 0
                                    d = 1
                                elif uipA == "N":
                                    f = 1
                                    while f == 1:
                                        print("Willst du ein Backup von Dokumente machen?")
                                        uipD = input("Bestätige mit [J]a oder [N]ein ")
                                        if uipD == "J":
                                            shutil.copytree("/home/vmadmin/Dokumente", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-DK')
                                            backup_dir= "/media/vmadmin/BACKUP/Backup/"
                                            newest_dir = max(pathlib.Path(backup_dir).glob('*/'), key=os.path.getctime)
                                            for root, dir, files in os.walk(newest_dir ):
                                                for list in files:
                                                    list=os.path.join(root,list) 
                                                    listSql = "\""+ list +"\""
                                                    float_size = os.path.getsize(list)/float(1<<10)
                                                    file_size = str(float_size)
                                                    file_sizeSql = "\""+ file_size +"\""
                                                    createDate = time.ctime(os.path.getctime(list))
                                                    createDateSql = "\""+ createDate +"\""
                                                    savequeryD = "INSERT into Backup (filepath, filesize, copydate) values ({}, {}, {});".format(listSql, file_sizeSql, createDateSql)
                                                    cs.execute(savequeryD)
                                                    mydb.commit()
                                            print("Backup abgeschlossen")
                                            f = 0
                                            e = 0
                                            d = 1
                                        elif uipD == "N":
                                            g = 1
                                            while g == 1:
                                                print("Willst du ein Backup von Downloads machen")
                                                uipDL = input("Bestätige mit [J]a oder [N]ein ")
                                                if uipDL == "J":
                                                    shutil.copytree("/home/vmadmin/Downloads", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-DL')
                                                    backup_dir= "/media/vmadmin/BACKUP/Backup/"
                                                    newest_dir = max(pathlib.Path(backup_dir).glob('*/'), key=os.path.getctime)
                                                    for root, dir, files in os.walk(newest_dir ):
                                                        for list in files:
                                                            list=os.path.join(root,list)  
                                                            listSql = "\""+ list +"\""
                                                            float_size = os.path.getsize(list)/float(1<<10)
                                                            file_size = str(float_size)
                                                            file_sizeSql = "\""+ file_size +"\""
                                                            createDate = time.ctime(os.path.getctime(list))
                                                            createDateSql = "\""+ createDate +"\""
                                                            savequeryDL = "INSERT into Backup (filepath, filesize, copydate) values ({}, {}, {});".format(listSql, file_sizeSql, createDateSql)
                                                            cs.execute(savequeryDL)
                                                            mydb.commit()
                                                    print("Backup abgeschlossen")
                                                    g = 0
                                                    f = 0
                                                    e = 0
                                                    d = 1
                                                elif uipDL == "N":
                                                    print("bye")
                                                    g = 0
                                                    f = 0
                                                    e = 0
                                                    d = 0
                        else:
                            print("USB stick nicht richtig eingesteckt oder das Backup Ordner ist nicht vorhanden!")
                            d = 0
                    elif uip == "d":
                        print("willst du nach Datum oder Filepfad durchsuchen oder die Anzahl files von bestimmten Backup Ordner anzeigen")
                        uip2 = input("Bestätige mit [D]atum, [F]ilepfad oder [B]ackup Ordner durchsuchen: ")
                        y = 1
                        while y == 1:
                            if uip2 == "D":
                                usrdate = input("Gebe ein Datum ein: ")
                                usrdateSql = "\"%"+ usrdate +"%\""
                                savequeryDate = "Select * from Backup where copydate like {}".format(usrdateSql)
                                cs.execute(savequeryDate)
                                mydb.commit()
                                for x in cs:
                                    print(x)
                                y = 0
                                d = 1

                            
                            elif uip2 == "F":
                                usrfile_name = input("Gebe ein Filename oder Pfad ein: ")
                                usrfile_nameSql = "\"%"+ usrfile_name +"%\""
                                savequeryFile = "Select * from Backup where filepath like {}".format(usrfile_nameSql)
                                cs.execute(savequeryFile)
                                mydb.commit()
                                for x1 in cs:
                                    print(x1)
                                y = 0
                                d = 1
                            
                            elif uip2 == "B":
                                print("Welches der Drei Backup möchtest du Durchsuchen?")
                                uip3 = input("Bestätige mit [A]lles, [D]okumente oder [Do]wnloads: ")    
                                j = 1
                                while j == 1:
                                    if uip3 == "A":
                                        if glob.glob("/media/vmadmin/BACKUP/Backup/*-AL"):
                                            for nameA in glob.glob("/media/vmadmin/BACKUP/Backup/*-AL"):
                                                count = 0
                                                for files in os.walk(nameA):
                                                    count += len(files)
                                                print(nameA, "Anzahl Files", count,)
                                                j = 0
                                                y = 0
                                                d = 1
                                        else:
                                            print("Keine Backups von Alles vorhanden!")
                                            j = 0
                                            y = 0
                                            d = 0
                                    elif uip3 == "D":
                                        if glob.glob("/media/vmadmin/BACKUP/Backup/*-DK"):
                                            
                                            for nameDK in glob.glob("/media/vmadmin/BACKUP/Backup/*-DK"): 
                                                count = 0
                                                for files in os.walk(nameDK):
                                                    count += len(files)
                                                print(nameDK, "Anzahl Files", count,)
                                                j = 0
                                                y = 0
                                                d = 1
                                        else:
                                            print("Keine Backups von Dokumente vorhanden!")
=======
 
        mydb = mysql.connector.connect(
                            host='localhost',
                            database='Schulprojekt',
							user='root',
							password='sml12345')
        cs = mydb.cursor(buffered= True)
        mycursor = mydb.cursor()
        sql = "select user, pass from user where user=%s and pass=%s"
        val = (username, userpassword)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        if result:
            self.root.destroy()
            d = 1
            while d == 1:
                print("Möchtest du ein Backup machen, durchsuchen oder exit?")
                uip = input("Bestätige mit [B]ackup oder [d]urchsuchen oder [E]xit: ")
                if uip == "B":
                    if path.exists("/media/vmadmin/BACKUP"):
                        fulldir = "/media/vmadmin/BACKUP/Backup"
                        disk = os.statvfs(fulldir)
                        totalAvailSpace = float(disk.f_bsize*disk.f_bfree)
                        print("Verügbarer Speicherplatz:. %.2f GB" % (totalAvailSpace/1024/1024/1024))
                        if totalAvailSpace < 5:
                            shutil.rmtree(min(pathlib.Path(fulldir).glob('*/'), key=os.path.getctime))
                        e = 1
                        while e == 1:
                            print("Willst du ein Backup von Alles machen?")
                            uip2 = input("Bestätige mit [J]a oder [N]ein: ")
                            if uip2 == "J":
                                shutil.copytree("/home/vmadmin/Videos", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-AL')
                                shutil.copytree("/home/vmadmin/Bilder", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-AL/Bilder')
                                shutil.copytree("/home/vmadmin/Dokumente", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-AL/Dokumente')
                                shutil.copytree("/home/vmadmin/Downloads", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-AL/Downloads')
                                backup_dir= "/media/vmadmin/BACKUP/Backup/"
                                newest_dir = max(pathlib.Path(backup_dir).glob('*/'), key=os.path.getctime)
                                for root, dir, files in os.walk(newest_dir ):
                                    for list in files:
                                        list=os.path.join(root,list) #root  und filename gejoint für full path
                                        list1 = "\""+ list +"\""
                                        float_size = os.path.getsize(list)/float(1<<10)
                                        file_size = str(float_size)
                                        file_size1 = "\""+ file_size +"\""
                                        createDate = time.ctime(os.path.getctime(list))
                                        createDate1 = "\""+ createDate +"\""
                                        savequery1 = "INSERT into Backup (filepath, filesize, copydate) values ({}, {}, {});".format(list1, file_size1, createDate1)
                                        cs.execute(savequery1)
                                        mydb.commit()
                                print("Backup abgeschlossen")
                                e = 0
                                d = 1
                            elif uip2 == "N":
                                f = 1
                                while f == 1:
                                    print("Willst du ein Backup von Dokumente machen?")
                                    uip3 = input("Bestätige mit [J]a oder [N]ein ")
                                    if uip3 == "J":
                                        shutil.copytree("/home/vmadmin/Dokumente", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-DK')
                                        backup_dir= "/media/vmadmin/BACKUP/Backup/"
                                        newest_dir = max(pathlib.Path(backup_dir).glob('*/'), key=os.path.getctime)
                                        for root, dir, files in os.walk(newest_dir ):
                                            for list in files:
                                                list=os.path.join(root,list) #root  und filename gejoint für full path
                                                list1 = "\""+ list +"\""
                                                float_size = os.path.getsize(list)/float(1<<10)
                                                file_size = str(float_size)
                                                file_size1 = "\""+ file_size +"\""

                                                createDate = time.ctime(os.path.getctime(list))
                                                createDate1 = "\""+ createDate +"\""
                                                savequery1 = "INSERT into Backup (filepath, filesize, copydate) values ({}, {}, {});".format(list1, file_size1, createDate1)
                                                cs.execute(savequery1)
                                                mydb.commit()
                                        print("Backup abgeschlossen")
                                        f = 0
                                        e = 0
                                        d = 1
                                    elif uip3 == "N":
                                        g = 1
                                        while g == 1:
                                            print("Willst du ein Backup von Downloads machen")
                                            uip4 = input("Bestätige mit [J]a oder [N]ein ")
                                            if uip4 == "J":
                                                shutil.copytree("/home/vmadmin/Downloads", f'/media/vmadmin/BACKUP/Backup/backup-{datetime.now().strftime("%d%m%Y%H%M")}-DL')
                                                backup_dir= "/media/vmadmin/BACKUP/Backup/"
                                                newest_dir = max(pathlib.Path(backup_dir).glob('*/'), key=os.path.getctime)
                                                for root, dir, files in os.walk(newest_dir ):
                                                    for list in files:
                                                        list=os.path.join(root,list) #root  und filename gejoint für full path
                                                        list1 = "\""+ list +"\""
                                                        float_size = os.path.getsize(list)/float(1<<10)
                                                        file_size = str(float_size)
                                                        file_size1 = "\""+ file_size +"\""
                                                        createDate = time.ctime(os.path.getctime(list))
                                                        createDate1 = "\""+ createDate +"\""
                                                        savequery1 = "INSERT into Backup (filepath, filesize, copydate) values ({}, {}, {});".format(list1, file_size1, createDate1)
                                                        cs.execute(savequery1)
                                                        mydb.commit()
                                                print("Backup abgeschlossen")
                                                g = 0
                                                f = 0
                                                e = 0
                                                d = 1
                                            elif uip4 == "N":
                                                print("bye")
                                                g = 0
                                                f = 0
                                                e = 0
                                                d = 0
                    else:
                        print("USB stick nicht richtig eingesteckt oder das Backup Ordner ist nicht vorhanden!")
                        d = 0
                elif uip == "d":
                    print("willst du nach Datum oder Filepfad durchsuchen oder die Anzahl files von bestimmten Backup Ordner anzeigen")
                    uip5 = input("Bestätige mit [D]atum, [F]ilepfad oder [B]ackup Ordner durchsuchen: ")
                    y = 1
                    while y == 1:
                        if uip5 == "D":
                            usrdate = input("Gebe ein Datum ein: ")
                            usrdate1 = "\"%"+ usrdate +"%\""
                            savequery2 = "Select * from Backup where copydate like {}".format(usrdate1)
                            cs.execute(savequery2)
                            mydb.commit()
                            for x in cs:
                                print(x)
                            y = 0
                            d = 1

                        
                        elif uip5 == "F":
                            usrfile_name = input("Gebe ein Filename oder Pfad ein: ")
                            usrfile_name1 = "\"%"+ usrfile_name +"%\""
                            savequery3 = "Select * from Backup where filepath like {}".format(usrfile_name1)
                            cs.execute(savequery3)
                            mydb.commit()
                            for x1 in cs:
                                print(x1)
                            y = 0
                            d = 1
                        
                        elif uip5 == "B":
                            print("Welches der Drei Backup möchtest du Durchsuchen?")
                            uip6 = input("Bestätige mit [A]lles, [D]okumente oder [Do]wnloads: ")    
                            j = 1
                            while j == 1:
                                if uip6 == "A":
                                    if glob.glob("/media/vmadmin/BACKUP/Backup/*-AL"):
                                        for name12 in glob.glob("/media/vmadmin/BACKUP/Backup/*-AL"):
                                            count = 0
                                            for files in os.walk(name12):
                                                count += len(files)
                                            print(name12, "Anzahl Files", count,)
                                            j = 0
                                            y = 0
                                            d = 1
                                    else:
                                        print("Keine Backups von Alles vorhanden!")
                                        j = 0
                                        y = 0
                                        d = 0
                                elif uip6 == "D":
                                    if glob.glob("/media/vmadmin/BACKUP/Backup/*-DK"):
                                        
                                        for name12 in glob.glob("/media/vmadmin/BACKUP/Backup/*-DK"):
                                            count = 0
                                            for files in os.walk(name12):
                                                count += len(files)
                                            print(name12, "Anzahl Files", count,)
>>>>>>> 68f62b41a56c9a4cbd92978d07d5b2429eca666c
                                            j = 0
                                            y = 0
                                            d = 1

<<<<<<< HEAD
                                    elif uip3 == "Do":
                                        if glob.glob("/media/vmadmin/BACKUP/Backup/*-DL"):
                                            for nameDL in glob.glob("/media/vmadmin/BACKUP/Backup/*-DL"):
                                                count = 0
                                                for files in os.walk(nameDL):
                                                    count += len(files)
                                                print(nameDL, "Anzahl Files", count,)
                                                j = 0
                                                y = 0
                                                d = 1
                                        else:
                                            print("Keine Backups von Downloads vorhanden!")
=======
                                elif uip6 == "Do":
                                    if glob.glob("/media/vmadmin/BACKUP/Backup/*-DL"):
                                        for name12 in glob.glob("/media/vmadmin/BACKUP/Backup/*-DL"):
                                            count = 0
                                            for files in os.walk(name12):
                                                count += len(files)
                                            print(name12, "Anzahl Files", count,)
>>>>>>> 68f62b41a56c9a4cbd92978d07d5b2429eca666c
                                            j = 0
                                            y = 0
                                            d = 0
                    elif uip == "E":
                        d = 0
            else:
                showinfo("Opla","Falsche Eingaben, Bitte gebe die richtige Nutzerdaten ein!")
        except:
            showinfo("Opla","Error während der Verbindung zur Datenbank. Schaue, ob der Datenbankpasswort korrekt ist!")
        




class Register():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("575x350")
        self.root.title("Registration")
        self.create_elements()
        self.root.mainloop()
 
    def create_elements(self):
        self.databasepass = Label(self.root, text="Basepassword:", font=('Verdana', 14, 'bold'))
        self.databasepass.place(x=50, y=10)

        self.entry_databasepass= Entry(self.root, font=('Verdana', 14))
        self.entry_databasepass.place(x=300, y=10)
 
        self.username = Label(self.root, text="Username:", font=('Verdana', 14, 'bold'))
        self.username.place(x=50, y=50)
 
        self.entry_username = Entry(self.root, font=('Verdana', 14))
        self.entry_username.place(x=300, y=50)
 
        self.password = Label(self.root, text="Passwort:", font=('Verdana', 14, 'bold'))
        self.password.place(x=50, y=90)
 
        self.entry_password = Entry(self.root, font=('Verdana', 14))
        self.entry_password.place(x=300, y=90)
 
        self.passw = Label(self.root, text="Registrationspasswort:", font=('Verdana', 14, 'bold'))
        self.passw.place(x=50, y=130)
 
        self.entry_passw = Entry(self.root, font=('Verdana', 14))
        self.entry_passw.place(x=300, y=130)
 
        self.register_button = Button(self.root, text="registrieren", height=2, width=10, command=self.register_user)
        self.register_button.place(x=230, y=185)
 
        self.existing_user = Label(self.root, text="Benutzer existiert?", font=('Verdana', 10, 'bold'))
        self.existing_user.place(x=216, y=250)
 
        self.login_button = Button(self.root, text="Login", height=2, width=10, command=self.destroy_register)
        self.login_button.place(x=230, y=270)

    def destroy_register(self):
        self.root.destroy()
        login = Login()
 
    def register_user(self):
        databasepass = self.entry_databasepass.get()
        username = self.entry_username.get()
        userpassword = self.entry_password.get()
        passw = self.entry_passw.get()
        
        if(username == "" or userpassword == "" or passw == "" or databasepass == ""):
            showinfo("Oops!","Die Felder dürfen nicht leer sein!")
            return
<<<<<<< HEAD
        try:
            mydb = mysql.connector.connect(
                                host='localhost',
                                database='Schulprojekt',
                                user='root',
                                password=databasepass)
=======
        
        mydb = mysql.connector.connect(
                            host='localhost',
                            database='Schulprojekt',
							user='root',
							password='sml12345')
 
        mycursor = mydb.cursor()
        passw1 = "\""+ passw +"\""
        sql1 = "select pass from RegistrationPass where pass = {}".format(passw1)
        mycursor.execute(sql1)
        result1 = mycursor.fetchone()
        self.entry_passw.delete(0, END)
        if result1:
            mycursor.execute("select count(*) from user")
            result = mycursor.fetchone()
            old_count = result[0]
>>>>>>> 68f62b41a56c9a4cbd92978d07d5b2429eca666c
    
            mycursor = mydb.cursor()
            passw1 = "\""+ passw +"\""
            sql1 = "select pass from RegistrationPass where pass = {}".format(passw1)
            mycursor.execute(sql1)
            resultRegister = mycursor.fetchone()
            self.entry_passw.delete(0, END)
            if resultRegister:
                mycursor.execute("select count(*) from user")
                result = mycursor.fetchone()
                old_count = result[0]
        
                sql = "INSERT INTO user (user, pass) VALUES (%s, %s)"
                val = (username, userpassword)
                mycursor.execute(sql, val)
                mydb.commit()
                
                mycursor.execute("select count(*) from user")
                result = mycursor.fetchone()
                new_count = result[0]
        
                self.entry_username.delete(0, END)
                self.entry_password.delete(0, END)
                self.entry_databasepass.delete(0, END)
        
                if(old_count + 1 == new_count):
                    showinfo("Geschaft!","Deine Informationen wurden erfolgreich gespeicher!")
                else:
                    showinfo("Fehler","Deine Informationen konnten nicht gespeichert werden!")
            else:
<<<<<<< HEAD
                showinfo("Fehler","Bitte gebe den richtigen Regisrationspasswort ein")   
        except:
            showinfo("Opla","Error während der Verbindung zur Datenbank. Schaue, ob der Datenbankpasswort korrekt ist!")

=======
                showinfo("Fehler","Deine Informationen konnten nicht gespeichert werden!")
        else:
            showinfo("Fehler","Bitte gebe den richtigen Regisrationspasswort ein")   
if __name__ == '__main__':
    login = Login()
>>>>>>> 68f62b41a56c9a4cbd92978d07d5b2429eca666c

