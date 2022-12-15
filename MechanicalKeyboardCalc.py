""" 
This program will show a GUi and you pick whichever keyboard and keyboard parts you want and it will calculate the total. 
12-15-2022

"""

#Imports tkinter for the GUI 
from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image


root = Tk()
root.title("Mechanical Keyboard Calculator") #Title for when the GUI opens up 


#Frame for the whole GUI 
LeftSide = Frame(root, width = 940, height=1080, bd=6, relief="raise")
LeftSide.pack(side=LEFT)

RightSide = Frame(root, width=940, height=1080, bd= 6, relief="raise")
RightSide.pack(side=LEFT)


#create a variable to store the selected value
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()

#Radio buttons connected to images. This is all on the left side. 
class Keyboard(): 
    fullKeyboard = ImageTk.PhotoImage(Image.open("fullKeyboard.jpg"))
    radio_button1 = tk.Radiobutton(LeftSide, image=fullKeyboard, value=180, variable=var1, command = lambda: on_radio_button_select("fullKeyboard"))   
    radio_button1.grid(row=0, column=1) #Instead of .pack() I use .grid to choose where I want my radio buttons. 

    TKLKeyboard = ImageTk.PhotoImage(Image.open("TKLKeyboard.jpg"))
    radio_button2 = tk.Radiobutton(LeftSide, image=TKLKeyboard,value=150, variable=var1, command = lambda: on_radio_button_select("TKLKeyboard.jpg"))
    radio_button2.grid(row=1, column=1)
  
    SFKeyboard = ImageTk.PhotoImage(Image.open("75Keyboard.jpg"))
    radio_button3 = tk.Radiobutton(LeftSide, image=SFKeyboard,value=145,variable=var1, command = lambda: on_radio_button_select("75Keyboard.jpg"))
    radio_button3.grid(row=2, column=1)
  
    SixtyKeyboard = ImageTk.PhotoImage(Image.open("60Keyboard.jpg"))
    radio_button4 = tk.Radiobutton(LeftSide, image=SixtyKeyboard,value=100, variable=var1, command = lambda: on_radio_button_select("75Keyboard.jpg"))
    radio_button4.grid(row=3, column = 1)

#Radio buttons to choose which PCB you want. 
class PCB():

    PCBLabel = Label(RightSide,text="PCB", font=("arial", 20, 'bold')).grid(row=0, column=1)
    
    radio_button5 = tk.Radiobutton(RightSide, text="Hotswap PCB",font=("arial", 16),variable=var2,value=15)
    radio_button5.grid(row=1, column=1)
    
    radio_button6 = tk.Radiobutton(RightSide, text="Solder PCB", font=("arial", 16),variable=var2, value=10)
    radio_button6.grid(row=1, column= 2)


# Different radio buttons for which plate material you want. This is all on the right side. It has different values for the costs. 
class Plate():
    PlateLabel = Label(RightSide, text="Plate Material", font=("arial", 20,"bold")).grid(row=3, column=1)
    
    radio_button7 = tk.Radiobutton(RightSide, text="Aluminum", font=("arial", 16), variable=var3,value=20)
    radio_button7.grid(row=4, column=1)
    
    radio_button8 = tk.Radiobutton(RightSide, text= "Brass", font=("arial", 16),variable=var3, value=25)
    radio_button8.grid(row=4, column=2)
    
    radio_button9 = tk.Radiobutton(RightSide, text="Polycarbonate", font=("arial", 16), variable=var3, value=15)
    radio_button9.grid(row=4, column=3)
    
    
#Radio buttons for the option of having keycaps in your keyboard. This is on the right side. 
class Keycaps():
    KeycapsLabel = Label(RightSide, text="Keycap Option", font=("arial", 20, "bold")).grid(row=5, column=1)
    
    radio_button10 = tk.Radiobutton(RightSide, text="Yes", font=("arial", 16), variable=var4, value=60)
    radio_button10.grid(row=6, column=1)
    
    radio_button11 = tk.Radiobutton(RightSide, text="No", font=("arial", 16),variable=var4, value=0)
    radio_button11.grid(row=6, column=2)
    
    
#Radio buttons for the option of having switches in your keyboard. 
class Switches():
    SwitchesLabel = Label(RightSide, text="Switch Option", font=("arial",20, "bold")).grid(row=7, column=1)
    
    radio_button12 = tk.Radiobutton(RightSide, text="Yes", font=("arial", 16), variable=var5, value=60)
    radio_button12.grid(row=8, column=1)
    
    radio_button13 = tk.Radiobutton(RightSide, text="No", font=("arial", 16), variable=var5, value=0)
    radio_button13.grid(row=8, column=2)
    
 
#Exit button using a messagebox     
def Exit():
    if messagebox.askyesno("Mechanical Keyboard Calculator", "Do you want to exit the program?"):
        root.quit()
        
#This sets all the radiobuttons to empty.      
def clear():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    
#This adds all the selected radio buttons together and has a message box open up 
def total():
    total = var1.get() + var2.get() + var3.get() + var4.get() + var5.get()
    tk.messagebox.showinfo("Total", "The total is: " + str(total))
    

    
    
#Buttons for the GUI to clear, get total, and exit 
clearButton = Button(RightSide, text="Clear", font=("arial",18,'bold'), width=5, command=clear).grid(row=10, column=1)
totalButton = Button(RightSide,text="Total", font=("arial", 18, 'bold'), width=5, command=total).grid(row=10, column=2)  
exitButton = Button(RightSide,text="Exit", font=("arial", 18, 'bold'), width=5, command=Exit).grid(row=10, column=3)




root.mainloop()