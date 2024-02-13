#Mason Thomas
#Assignment A3/A4
#GUI Dev

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


#Global Holders
picPrime = None
picVeggie = None
imageFile = None

#Create Form
frmBurgers = Tk()
frmBurgers.title("Burger Specials")
frmBurgers.geometry("800x590")


#Create Frame
picPrime = ttk.Frame(frmBurgers, width=260, height=260)
picPrime.place(relx=.3, rely=.3, anchor=CENTER)
picPrime.configure(borderwidth="2")
picPrime.configure(relief="groove")
picVeggie = ttk.Frame(frmBurgers, width=260, height=260)
picVeggie.place(relx=.7, rely=.3, anchor=CENTER)
picVeggie.configure(borderwidth="2")
picVeggie.configure(relief="groove")

#Instructions
lblInstructions = Label(text = "Choose a burger and then click the Select Meal button")
lblInstructions.place(relx=.5,rely=.75,anchor=CENTER)
#Button Actions
def btnPrime(*args):
    global imageFile
    if imageFile == "beef.png":
        imageFile = "blank.png"
    else:
        imageFile = "beef.png"
    newImagePrime()
    btnSelectMeal = ttk.Button(text = "Select Meal", command=btnSelect)
    btnSelectMeal.place(relx=.5, rely=.7, anchor=CENTER)
        
def btnVeggie(*args):
    global imageFile
    if imageFile == "veggies.png":
        imageFile = "blank.png"
    else:
        imageFile = "veggies.png"
    newImageVeggie()
    btnSelectMeal = ttk.Button(text = "Select Meal", command=btnSelect)
    btnSelectMeal.place(relx=.5, rely=.7, anchor=CENTER)

def btnSelect():
    lblConfirmation = Label(text = "Enjoy your burger special")
    lblConfirmation.place(relx=.5,rely=.8,anchor=CENTER)
    btnExit = ttk.Button(text = "Exit", command = exitBtn)
    btnExit.place(relx=.5,rely=.85,anchor=CENTER)
    
def newImagePrime():
    frame = picPrime
    img = Image.open(imageFile)
    photo = ImageTk.PhotoImage(img.resize((260,260)))
    lblImage = ttk.Label(frame, image = photo)
    lblImage.image = photo
    lblImage.place(relx=.5,rely=.5,anchor=CENTER)

def newImageVeggie():
    frame = picVeggie
    img = Image.open(imageFile)
    photo = ImageTk.PhotoImage(img.resize((260,260)))
    lblImage = ttk.Label(frame, image = photo)
    lblImage.image = photo
    lblImage.place(relx=.5,rely=.5,anchor=CENTER)

def exitBtn():
    quit()
    
    
#Create button
btnPrime = ttk.Button(text = "Prime Beef", command=btnPrime)
btnPrime.place(relx=.3, rely=.7, anchor=CENTER)
btnVeggie = ttk.Button(text = "Veggie", command=btnVeggie)
btnVeggie.place(relx=.7, rely=.7, anchor=CENTER)
