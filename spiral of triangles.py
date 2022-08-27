# -*- coding: utf-8 -*-
"""

This program can make a spiral with many triangle with different colors

"""
import turtle
pen = turtle.Turtle()
pen.speed(-4)


def spiral_of_triangles(n=3000):
    turtle.bgcolor("black")
    pen.pensize(3)
    colors = ["red","yellow","green","darkblue","blue","purple"]
    for i in range(n):
        pen.color(colors[i%6])
        pen.forward(i)
        pen.left(121)
     

spiral_of_triangles()