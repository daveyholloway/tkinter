# Import the tkinter library
import tkinter

# Create some windows
window01 = tkinter.Tk()
window02 = tkinter.Tk()

# Set some window attributes
window01.title("Main")
window01.wm_iconbitmap("excalibur.ico")
window01.geometry("1000x800")
window01.resizable(width=False, height=False)
#window01.configure(background="#000000")

window02.title("Control")
window02.wm_iconbitmap("excalibur.ico")
window02.geometry("200x400")
window02.resizable(width=False, height=False)

def closeApplication():
    exit(0)

mainCanvas= tkinter.Canvas(window01, width=800, height=600)
mainCanvas.pack()

mainCanvas.create_rectangle(50, 20, 150, 80, fill="#476042")
mainCanvas.create_rectangle(65, 35, 135, 65, fill="yellow")
mainCanvas.create_line(0, 0, 50, 20, fill="#476042", width=3)
mainCanvas.create_line(0, 100, 50, 80, fill="#476042", width=3)
mainCanvas.create_line(150,20, 200, 0, fill="#476042", width=3)
mainCanvas.create_line(150, 80, 200, 100, fill="#476042", width=3)


#exitButton = tkinter.Button(window02, text="Exit", command=closeApplication)
exitButton = tkinter.Button(window02, text="Exit", command=closeApplication)
exitButton.pack()



