import mysql.connector

BotPython = mysql.connector.connect(
    host="localhost",
    user="gabrielolis",
    password="123",
    database="BotPython"
)

finger = BotPython.cursor()

insert = """INSERT INTO clients (name, phoneNumber,
street, cep) VALUE (%s, %s, %s, %s)"""
val = ("Carlinhos", "+5511912345678", "Ponte que Partiu, 666", "66666-666")


finger.execute(insert, val)
BotPython.commit()


print(finger.rowcount, "usuário inserido.")
