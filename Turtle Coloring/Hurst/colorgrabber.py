import colorgram
import os

rgb_colors = []
colors = colorgram.extract(r"C:\Users\okkah\Python\Grind\Turtle Coloring\Hurst\image.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)