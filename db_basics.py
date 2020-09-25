import mysql.connector
import requests


mydb = mysql.connector.connect(
  host="localhost",
  database = "easy_db",
  user="root",
  password="Arena11.0!"
)

sql_select_Query = "SELECT * from cars "

cursor = mydb.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

#receive = requests.get('https://pokeapi.co/api/v2/generation/generation-ii')
receive = requests.get('https://official-joke-api.appspot.com/random_ten')

print(type(records))
data = receive.json()
print(type(data))

#for x in data:
#  print(data[x])
#abc

print(data[2]["punchline"])
#print(records["name"])


for x in records:
 print(x)










