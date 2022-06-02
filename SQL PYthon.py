import mysql.connector
import os
from datetime import datetime
import shutil
import time

now = datetime.now()
date = now.strftime("%d-%m-%Y_%H:%M")
user = "Andrin"
i = 10

print("Bist du dir sicher das du ein Backup machen möchtest?")

d = 1

arr = []
# os.stat(i).st_ctime
while d == 1:
  uip = input("Bestätige mit [J]a oder [N]ein ")
  if uip == "J":
    d = 0

    try:
      os.chdir("/Volumes/Untitled 2")
    except:
      print("""Error: Kein USB gefunden.
        
        Script wird beendet in 10 sec.""")
        
    if os.getcwd() == "/Volumes/Untitled 2":
      try:
        os.chdir("/Volumes/Untitled 2/backup")
      except:
        print("Error: Backup wurde nicht gefunden")

      if os.getcwd() == "/Volumes/Untitled 2/backup":
        # Neue Funktion zum Alte versionen zu löschen, wenn zu wenig Speicherplatz vorhanden ist.

        quip = input ("Willst du ein Backup von allen Ordner machen? Bestätige mit Ja oder Nein: ")

        if quip == "Ja":
          os.mkdir("/Volumes/Untitled 2/backup/{}-AL".format(time))

          shutil.copytree("/Users/{}/Desktop", "/Volumes/Untitled 2/copy".format(user))

          shutil.copytree("/Users/{}/Pictures".format(user), "/Volumes/Untitled 2/backup/{}".format(date))
          
          shutil.copytree("/Users/{}/Downloads".format(user), "/Volumes/Untitled 2/backup/{}".format(date))

          shutil.copytree("/Users/{}/Music".format(user), "/Volumes/Untitled 2/backup/{}".format(date))

          shutil.copytree("/Users/{}/Documents".format(user), "/Volumes/Untitled 2/backup/{}".format(date))

          print("Backup abgeschlossen")

        elif quip == "Nein":
          dip = input("Willst du ein Backup von Dokumente machen? Bestätige mit Ja oder Nein: ")

        if dip == "Ja":
          shutil.copytree("/Users/{}/Documents".format(user),  "/Volumes/Untitled 2/backup/{}-DK".format(date))

          print("Backup abgeschlossen")

        elif dip == "Nein":
          dlip = input("Willst du ein Backup von Downloads machen? Bestätige mit Ja oder Nein: ")

        if dlip == "Ja":
          shutil.copytree("/Users/{}}/Downloads".format(user), "/Volumes/Untitled 2/backup/{}-DL".format(date))

          print("Backup abgeschlossen")
      else:
        for i in range(10):
          print("Countdown ends in {}".format(10-i))
          time.sleep(1)
          print("Script wird beendet.")


    else:
      while (i > 0):
        print("Countdown endet in {}".format(i))
        i-=1
        time.sleep(1)
      
  elif uip == "N":
    print("Bye")
    d = 0
  else:
    print("Was?")

"""
mydb = mysql.connector.connect(
  user="root",
  password="asdfasdf",
  host="127.0.0.1",
  database="Schulprojekt"
) 

mc = mydb.cursor()

mc.execute("USE Schulprojekt;")

print("Geb din name aa")
x = input()

x = "\"" + x + "\""

input = "INSERT INTO dis VALUES ({});"

mc.execute(input.format(x))

mydb.commit()

mc.execute("SELECT * FROM dis;")

for x in mc:
  print(x)
"""