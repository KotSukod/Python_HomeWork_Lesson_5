#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

import random

def turn(candy):
    x = int(input("Конфеты: "))
    if candy < 28:
        while  x > candy:
            print("Количество конфет должно быть от 1 до {}".format(candy))
            x = int(input("Конфеты: "))
        return int(x)
    else:
        while x == '' or int(x) > 28 or int(x) <= 0:
            print("Количество конфет должно быть от 1 до 28")
            x = int(input("Конфеты: "))
        return int(x) 

def chance_turn(x):
    if x == 2:
        print ("Ходит игорок {}".format(player_1))
        return  1
    else:    
        print ("Ходит игорок {}".format(player_2))
        return 2 

candy = int(2021)

player_1 = input("Введите имя первого игрока: ")
player_2 = input("Введите имя второго игрока: ")

fist_turn = random.randint(1, 3)
if fist_turn == 1:
    play_turn = 2
else:
    play_turn = 1

while candy != 0:
    play_turn = chance_turn(play_turn)
    print("Осталось конфет: {}".format(candy)) 
    candy = candy - turn(candy)
    
    
if play_turn == 1:
    print("Победил игрок {}".format(player_1))
else:
    print("Победил игрок {}".format(player_2))        

