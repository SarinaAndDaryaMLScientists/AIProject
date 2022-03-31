import tkinter as tk
from tkinter import Canvas

app = tk.Tk()
app.title("Canvas")

canvas = Canvas(app)
canvas.pack()
points = [
    100,100, 100, 200, 200, 100
]
# points = [
#    10, 10, 10, 100, 100, 100, 100, 10, 10, 10
# ]
canvas.create_line(points, smooth='true', splinesteps=1)
canvas.create_line(points)

# canvas.create_line(10, 10, 150, 50)

app.mainloop()