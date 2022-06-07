import mysql.connector
import os
from datetime import datetime
import shutil
import time

# Creates the connection to the SQLdatabase
mydb = mysql.connector.connect(
  user="root",
  password="asdfasdf",
  host="127.0.0.1",
  database="Schulprojekt"
) 

# Vars
now = datetime.now()
date = now.strftime("%d-%m-%Y_%H:%M")
user = "Andrin"
e = 1



# Alias for the cursor for efficiency
mc = mydb.cursor()

mc.execute("USE Schulprojekt;")


# Methods
# returns all the filenames in a specified path
def scantree(path):
    for i in path:
        if i.is_dir(follow_symlinks=False):
            yield from os.scandir(i.path)
        else:
            yield i

# Copy all specified directories and inserts then into the database
def copyAll():
  shutil.copytree("/Users/{}/Desktop", "/Volumes/Untitled 2/copy".format(user))

  shutil.copytree("/Users/{}/Pictures".format(user), "/Volumes/Untitled 2/backup/{}".format(date))

  shutil.copytree("/Users/{}/Downloads".format(user), "/Volumes/Untitled 2/backup/{}".format(date))

  shutil.copytree("/Users/{}/Music".format(user), "/Volumes/Untitled 2/backup/{}".format(date))

  shutil.copytree("/Users/{}/Documents".format(user), "/Volumes/Untitled 2/backup/{}".format(date))

  print("Backup abgeschlossen")

# copies the directory Downloads and enters the copied files into the DB
def copyDownloads():
  shutil.copytree("/Users/{}/Downloads".format(user), "/Volumes/Untitled 2/backup/{}-DL".format(date))

  for i in scantree("/Users/Andrin/Downloads"):
    input = "INSERT INTO Eintraege (Zeit,Dateiname) VALUES ({});"

  mc.execute(input.format(date,i))
  mydb.commit()


  print("Backup abgeschlossen")

# copies the directory Documents and enters the copied files into the DB
def copyDocuments():
  shutil.copytree("/Users/{}/Documents".format(user),  "/Volumes/Untitled 2/backup/{}-DK".format(date))

  print("Backup abgeschlossen")

# Counts to ten
def whileCounter():
  i = 10
  while (i > 0):
          print("Countdown endet in {}".format(i))
          i-=1
          time.sleep(1)

# Counts to ten but differently
def forCounter():
  for i in range(10):
            print("Countdown ends in {}".format(10-i))
            time.sleep(1)
            print("Script wird beendet.")

def checkUSB():
  try:
    os.chdir("/Volumes/Untitled 2")
  except:
    print("""Error: Kein USB gefunden.
      
      Script wird beendet in 10 sec.""")
      

# manages the backup process
def backup():
  d = 1
  print("Bist du dir sicher, dass du ein Backup machen möchtest?")
  arr = []
  # os.stat(i).st_ctime
  while d == 1:
    uip = input("Bestätige mit [J]a oder [N]ein ")
    if uip == "J":
      d = 0
      
      checkUSB()

      if os.getcwd() == "/Volumes/Untitled 2":
        try:
          os.chdir("/Volumes/Untitled 2/backup")
        except:
          print("Error: Backup wurde nicht gefunden")

        if os.getcwd() == "/Volumes/Untitled 2/backup":
          # Neue Funktion zum Alte versionen zu löschen, wenn zu wenig Speicherplatz vorhanden ist.

          quip = input ("Willst du ein Backup von allen Ordner machen? Bestätige mit Ja oder Nein: ")

          if quip == "Ja":
            copyAll()

          elif quip == "Nein":
            dip = input("Willst du ein Backup von Dokumente machen? Bestätige mit Ja oder Nein: ")

          if dip == "Ja":
            copyDocuments()
          elif dip == "Nein":
            dlip = input("Willst du ein Backup von Downloads machen? Bestätige mit Ja oder Nein: ")

          if dlip == "Ja":
            copyDownloads()
        else:
          forCounter()
      else:
        whileCounter()
        
    elif uip == "N":
      print("Bye")
      d = 0
    else:
      print("Was?")

#flaskdjfds

  input = "INSERT INTO Eintraege (Zeit,Dateiname) VALUES ({});"

  mc.execute(input.format())

  mydb.commit()

  mc.execute("SELECT * FROM dis;")

  for x in mc:
    print(x)


while e == 1:
  wuip = input("Willst du ein [b]ackup machen oder sie [d]urchsuchen?")
  if wuip == "b":
    d = 0
    backup()
  elif wuip == "d":
    d = 0

import os, sys, time
from venv import create

folder = "/media/vmadmin/BACKUP/Backup"
listOfFiles = ""

for root, dirs, files in os.walk(folder):
    for list in files:
        list=os.path.join(root,list) # joining root and the file name for full path
        file_size = os.path.getsize(list)/float(1<<10)
        createDate = time.ctime(os.path.getctime(list))
        listOfFiles = "{} Grösse: {} KB, Backup date:{}".format(list, file_size,createDate)
        print(listOfFiles)