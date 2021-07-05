import random, time, re, csv, math, turtle
import numpy as np, pandas as pd, datetime, os
import seaborn as sns, scipy as sci, matplotlib.pyplot as plt
import matplotlib.transforms as mt, matplotlib.pylab as pl
from matplotlib.transforms import offset_copy 
from matplotlib.font_manager import FontProperties

win_length = 500
win_height = 500
turtles = input("How many racers would you like? (input must be of int type)")
while turtles is None or type(int(turtles)) != int:
      turtles = input("How many racers would you like? (input must be of int type)")
turtle.screensize(win_length, win_height)

class racer(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        shapeType = input("Enter Turtle Shape Type Here: ")
        shapeType= shapeType.lower()
        while shapeType is None or type(shapeType) != str:
           shapeType = input("Enter Turtle Shape Type Here: ")
           shapeType= shapeType.lower()
        if shapeType.strip().lower() not in ["arrow","circle", "square", "triangle", "classic"]:
           shapeType = "turtle"
        print(f"ShapeType is {shapeType}\n")
        self.turt.shape(shapeType) 
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1, 20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)

def setupFile(name, colors):
    file = open(name, 'w+')
    for color in colors:
        file.write('{}: 0\n'.format(color))
    file.close()

def startGame():
    global win_length, win_height, turtles
    tList = []
    turtle.clearscreen()
    turtle.hideturtle()
    n = input("How many colors do you want to set to the color map? (input must be of int type)")
    while n is None or type(int(n)) != int:
          n = input("How many colors do you want to set to the color map? (input must be of int type)")
    n = int (n) 
    colors = colors = pl.cm.jet(np.linspace(0,1,n))
    start = 20 - (win_length/2)
    for t in range(0, turtles, 1):
        newPosX = start + t*(win_length)//turtles
        tList.append(racer(colors[t],(newPosX, -230)))
        tList[t].turt.showturtle()
    run = True
    while run:
        for t in tList:
            t.move()

        maxColor = []
        maxDist = 0
        for t in tList:
            if t.pos[1] > 230 and t.pos[1] > maxDist:
                maxDist = t.pos[1]
                maxColor = []
                maxColor.append(t.color)
            elif t.pos[1] > 230 and t.pos[1] == maxDist:
                maxDist = t.pos[1]
                maxColor.append(t.color)
                  
        if len(maxColor) > 0:
            run = False
            print(f'The winner is: {winCol for winCol in maxColor}\n')

    oldScore = []
    file = open('scores.txt', 'r')
    for line in file:
        l = line.split() 
        color,score = l
        oldScore.append([color,score])
    file.close()

    file = open('scores.txt', 'w+')
    for entry in oldScore:
        for winCol in maxColor:
            if entry[0] == winCol:
                entry[1] = int(entry[1]) + 1
        file.write("{} {}\n".format(str(entry[0]), str(entry[1])) )
    file.close()
