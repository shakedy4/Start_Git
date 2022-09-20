import pygame
import pandas as pd
import numpy as pd
import csv
import consts

myList = []


def read_csv(file):
    with open(file, 'r') as game:
        myReader = csv.reader(game)
        # next(myReader)
        mylist = list(myReader)

    for myItem in mylist:
        print(myItem)


# writes to a file
def new_csv(index, data):
    with open('game.csv', 'a') as newFile:
        # create the csv writer
        writer = csv.writer(newFile)
        # write a row to the csv file
        writer.writerow([data])


# checking which number is pressed
def num_press_less(keys_pressed, soldier_rect, field):
    for num_key in range(len(consts.NUMBERS_KEYS)):
        if keys_pressed[consts.NUMBERS_KEYS[num_key]]:
            data = create_data(num_key + 1, soldier_rect, field)
            new_csv(num_key + 1, data)


def create_data(key_num, soldier_rect, field):
    return {key_num: [soldier_rect.x, soldier_rect.y, field]}


def num_press_more(keys_pressed):
    if keys_pressed[pygame.K_1]:
        pass
    elif keys_pressed[pygame.K_2]:
        pass
    elif keys_pressed[pygame.K_3]:
        pass
    elif keys_pressed[pygame.K_4]:
        pass
    elif keys_pressed[pygame.K_5]:
        pass
    elif keys_pressed[pygame.K_6]:
        pass
    elif keys_pressed[pygame.K_7]:
        pass
    elif keys_pressed[pygame.K_8]:
        pass
    elif keys_pressed[pygame.K_9]:
        pass
