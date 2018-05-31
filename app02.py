# Import the tkinter library
import tkinter

# Import the maths library
import math

# Create some windows
window01 = tkinter.Tk()

# Set some window attributes
window01.title("Main")
window01.wm_iconbitmap("excalibur.ico")
window01.geometry("1000x800")
window01.resizable(width=False, height=False)
#window01.configure(background="#000000")

# Create a canvas
mainCanvas= tkinter.Canvas(window01, width=800, height=600)
mainCanvas.pack()

def hexagon(pcanvas, px, py, psize):
    pcanvas.create_line(px - psize/2, py + math.cos(math.radians(30)) * psize, px + psize/2, py + math.cos(math.radians(30)) * psize)
    pcanvas.create_line(px + psize/2, py + math.cos(math.radians(30)) * psize, px + (psize/2) + math.cos(math.radians(60)) * psize, py)
    pcanvas.create_line(px + (psize/2) + math.cos(math.radians(60)) * psize, py,px + psize/2, py - math.cos(math.radians(30)) * psize)
    pcanvas.create_line(px + psize/2, py - math.cos(math.radians(30)) * psize,px - psize/2, py - math.cos(math.radians(30)) * psize)
    pcanvas.create_line(px - psize/2, py - math.cos(math.radians(30)) * psize, px - (psize/2) - math.cos(math.radians(60)) * psize, py)
    pcanvas.create_line(px - (psize/2) - math.cos(math.radians(60)) * psize, py, px - psize/2, py + math.cos(math.radians(30)) * psize)
    


wSize = 50
wGridx = 100
wGridY = 100

for x in range (0,5):
    for y in range (0,4):
        hexagon(mainCanvas, wGridx + x *(1.5 * wSize), wGridY + (math.cos(math.radians(30)) * 2 * wSize * y) + (math.cos(math.radians(30)) * wSize) * (x%2) , wSize)
    
        print(x%2)
        print((math.cos(math.radians(30)) * wSize) * (x%2))


