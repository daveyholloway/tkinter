########################################################################
#
# Hexagons!
# =========
#
# Modification History
# ====================
#
# When        Who               Why
# =========== ================= ========================================
# 31/05/2018  Dave Hol'         Convert lines to polygon, add fill and
#                               line style.
#
########################################################################


# Import the tkinter library
import tkinter

# Import the maths library
import math

# Create some windows
window01 = tkinter.Tk()

# Set some window attributes
window01.title("Main")
window01.wm_iconbitmap("excalibur.ico")
window01.geometry("400x400")
window01.resizable(width=False, height=False)
#window01.configure(background="#000000")

# Create a canvas
mainCanvas= tkinter.Canvas(window01, width=400, height=400)
mainCanvas.pack()

########################################################################
#
# The Hexagon function
#
########################################################################
def hexagon(pcanvas, px, py, psize, poutline, pfill):
    pcanvas.create_polygon(px - psize/2, py + math.cos(math.radians(30)) * psize,
                           px + psize/2, py + math.cos(math.radians(30)) * psize,
                           px + (psize/2) + math.cos(math.radians(60)) * psize, py,
                           px + psize/2, py - math.cos(math.radians(30)) * psize,
                           px - psize/2, py - math.cos(math.radians(30)) * psize,
                           px - (psize/2) - math.cos(math.radians(60)) * psize, py,
                           px - psize/2, py + math.cos(math.radians(30)) * psize,
                           fill=pfill, outline=poutline, width="2")
    


wSize = 20
wGridx = 100
wGridY = 100

for x in range (0,7):
    for y in range (0,4):
        if x in (0,6):
            hexagon(mainCanvas,
                wGridx + x *(1.5 * wSize),
                wGridY + (math.cos(math.radians(30)) * 2 * wSize * y) + (math.cos(math.radians(30)) * wSize) * (x%2) ,
                wSize,
                "Black",
                "Cyan")
        else:
            hexagon(mainCanvas,
                wGridx + x *(1.5 * wSize),
                wGridY + (math.cos(math.radians(30)) * 2 * wSize * y) + (math.cos(math.radians(30)) * wSize) * (x%2) ,
                wSize,
                "Black",
                "Yellow")            
    
        print(x%2)
        print((math.cos(math.radians(30)) * wSize) * (x%2))


