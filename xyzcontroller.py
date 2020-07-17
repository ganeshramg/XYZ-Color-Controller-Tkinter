from tkinter import *

root = Tk()                                     #Root window application
root.geometry('600x350')
root.resizable(0,0)
root.title('X Y Z Color Controller')

X = IntVar()                                    # X,Y,Z for RGB and BG string var to change
Y = IntVar()                                    # Right Frame's colour
Z = IntVar()
bg = StringVar()

leftframe = Frame(root,height=350,width=300,bg='#FFFFFF')   # Control Frame
leftframe.pack(side=LEFT)

rightframe = Frame(root,height=350,width=300,bg='#000000')  # Color Frame
rightframe.pack(side=RIGHT)

def control(event):                                         # Control X and Y Sliders
    x = event.x
    y = event.y

    X.set(x*1.275)
    Y.set(y*1.275)

    show(event)

def getHex(var):                                            # Get Hex code in the format
    hex_code = var.split('x')[1]                            # '#RRGGBB'
    if len(hex_code) == 1:
        return '0' + hex_code
    else:
        return hex_code

def show(event):                                            # This method sets BG
    R = getHex(hex(X.get()))
    G = getHex(hex(Y.get()))
    B = getHex(hex(Z.get()))
    bg.set('#' + R + G + B)
    rightframe.config(bg=bg.get())

# Rectangular control area
rect = Canvas(leftframe,height=200,width=200,bg='#000000',cursor='circle')
rect.place(x=25,y=25)
rect.bind('<Button-1>',control)
rect.bind('<B1-Motion>',control)

# X_Slider
x_slider = Scale(leftframe,orient=HORIZONTAL,showvalue=0,length=200,variable=X,from_=0,to_=255)
x_slider.place(x=25,y=260)
x_slider.bind('<Button-1>',show)
x_slider.bind('<B1-Motion>',show)

# Y_Slider
y_slider = Scale(leftframe,orient=VERTICAL,showvalue=0,length=200,variable=Y,from_=0,to_=255)
y_slider.place(x=250,y=25)
y_slider.bind('<Button-1>',show)
y_slider.bind('<B1-Motion>',show)

# Z_Slider
z_slider = Scale(leftframe,orient=HORIZONTAL,showvalue=0,length=200,variable=Z,from_=0,to_=255)
z_slider.place(x=25,y=300)
z_slider.bind('<Button-1>',show)
z_slider.bind('<B1-Motion>',show)

root.mainloop()
