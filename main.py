import badger2040
import jpegdec
from time import sleep
from random import randint
import COORDINATES

badger = badger2040.Badger2040()
jpeg = jpegdec.JPEG(badger.display)
badger.set_update_speed(2)
COORDINATES = COORDINATES.COORDINATES_AND_SIZE

def cls():
    badger.set_pen(15)
    badger.clear() 

#Menu
number_of_dice = 1
def menu_title():
    badger.set_pen(0)
    badger.set_update_speed(2)
    badger.set_font("bitmap8")
    badger.text("Dice Roller", 48, 10, badger2040.WIDTH, 4)
    badger.text("How many die you want to roll?", 15, 50, badger2040.WIDTH, 2)

def number_of_dice_text(number_of_dice):
    badger.set_pen(0)
    badger.set_update_speed(2)
    badger.text(str(number_of_dice), 130, 80, badger2040.WIDTH, 4)
    
def draw_menu():
    cls()
    number_of_dice_text(number_of_dice)
    menu_title()
    badger.set_update_speed(1)
    badger.update()

#run
#---------------------------------------------
def roller(number_of_dice):
    for i in range(number_of_dice):
        jpeg.open_file(f"dice{randint(1,6)}.jpg")
        coods = COORDINATES[number_of_dice][i]
        jpeg.decode(coods[0], coods[1], eval(f"jpegdec.{coods[2]}"))
    badger.update()

def roll_dice(number_of_dice):
    cls()
    
    # very cool animation
    badger.set_update_speed(3)
    for i in range(5):
        roller(number_of_dice)
        sleep(0.1)
        
    #actual roll
    badger.set_update_speed(2)
    cls()
    roller(number_of_dice) 

#---------------------------------------------
#Inital menu draw
draw_menu()
menu = True

#loop
while True:
    while menu == True:
        while not badger.pressed(badger2040.BUTTON_B):
            if badger.pressed(badger2040.BUTTON_DOWN):
                number_of_dice -= 1
                if number_of_dice < 1:
                    number_of_dice = 1
                cls()
                number_of_dice_text(number_of_dice)
                menu_title()
                badger.update()
            
            if badger.pressed(badger2040.BUTTON_UP):
                number_of_dice += 1
                if number_of_dice > 10:
                    number_of_dice = 10
                cls()
                number_of_dice_text(number_of_dice)
                menu_title()
                badger.update()
        menu = False

    if badger.pressed(badger2040.BUTTON_B):
        cls()
        badger.set_update_speed(2)
        badger.update()
        roll_dice(number_of_dice)
        badger.update()
    #\(@^0^@)/
    if badger.pressed(badger2040.BUTTON_A):
        menu = True
        draw_menu()
