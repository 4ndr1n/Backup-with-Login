import mysql.connector
import os
from datetime import datetime
import shutil

now = datetime.now()
date = now.strftime("%d-%m-%Y_%H:%M")
user = os.getlogin()

uinput = input("Bist du dir sicher das du ein Backup machen möchtest?")

d = 1

arr = []

while d == 1:
  uip = input("Bestätige mit [J]a oder [N]ein ")
  if uip == "J":
    if "/Volumes/Unitled 2":
      d = 0
      for i in "/Volumes/Unitled 2":
        arr.append(os.stat(i).st_ctime)
    else:
      print("""Kein USB gefunden.
      
      Script wird beendet in 10 sec.""")

      while (i > 0):
        
  elif uip == "N":
    print("Bye")
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