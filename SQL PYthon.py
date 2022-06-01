import mysql.connector
import os
from datetime import datetime
import shutil

now = datetime.now()
date = now.strftime("%H:%M")




shutil.copytree("/Users/Andrin/Desktop", "/Volumes/Untitled 2/copy")

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