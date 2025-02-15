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
example1 = int(input("Введи ответ: "))

try:
    rexample1 = a + b

    if example1 == rexample1:
        print("Молодец, верно!")
    else:
        print("Ну ты дура")

    print("Теперь вычитание.")

    a2 = random.randint(1,100)
    b2 = random.randint(1,100)

except ValueError:
    print("Точно число ввел?")


print(("Сколько будет"), a2,"+", b2, ("?"))
example2 = int(input("Введи ответ: "))

try:
    rexample2 = a2 + b2

    if example2 == rexample2:
        print("Молодец, верно!")
    else:
        print("Ну ты дура")
except ValueError:
    print("Пожалуйста, введи число.")