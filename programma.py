import math
import random

print ("Hello. Это небольшая программа, созданная в рамках лабораторной работы №1.1")
print ("Давай познакомимся")

name = str(input ("Тебя зовут..? \n"))
print ("Привет,", name, ("! Приятно познакомиться."))

age = int (input("Введи свой возраст: \n"))

if age <= 18:
    print("Отлично, мелюзга, давай дальше.")
elif age >= 18:
    print("Давайте продолжим тест программы")
else:
    print("Ошибка")

print("Проверим хорошо ли ты считаешь.")

a = random.randint(1,100)
b = random.randint(1,100)

print(("Сколько будет"), a,"+", b, ("?"))
example1 = input("Введи ответ: ")

rexample1 = a + b

if example1 == rexample1:
    print("Молодец, верно!")
else:
    print("Ну ты дура")