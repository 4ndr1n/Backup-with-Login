import mysql.connector
import os
from datetime import datetime
import shutil
import time

now = datetime.now()
date = now.strftime("%d-%m-%Y_%H:%M")
user = os.getlogin()
i = 10

print("Bist du dir sicher das du ein Backup machen möchtest?")

d = 1

arr = []
# os.stat(i).st_ctime
while d == 1:
  uip = input("Bestätige mit [J]a oder [N]ein ")
  if uip == "J":
    d = 0
    os.chdir("/Volumes/Unitled 2")
    if os.getcwd() == "/Volumes/Unitled 2":
      print("woo")
        # Neue Funktion zum Alte versionen zu löschen, wenn zu wenig Speicherplatz vorhanden ist.
    else:
      print("""Kein USB gefunden.
      
      Script wird beendet in 10 sec.""")

      while (i > 0):
        print("Countdown endet in {}".format(i))
        i-=1
        

  elif uip == "N":
    print("Bye")
    d = 0
  else:
    print("Was?")





# shutil.copytree("/Users/Andrin/Desktop", "/Volumes/Untitled 2/copy")

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