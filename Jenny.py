from tkinter import*
import pyttsx3
import os
from datetime import datetime
from threading import Thread
from PIL import Image, ImageTk


icon="resource/robot.ico"

#intilizing the gui Window.
Root=Tk()
Root.title("J E N N Y  A S S I S T A N T")
Root.resizable(0,0)
Root.geometry("600x400")
Root.iconbitmap(icon)
engine = pyttsx3.init('sapi5')
try:
    apptone="F"
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
except:
    apptone="M"
    Root.title("J A R V I S   A S S I S T A N T")


def Speak(text):
    engine.say(text)
    engine.runAndWait()
#Global values
global name,gender,password


#Adding gui widgets

#->Adding Main frame for the application
MainFrame=Frame(Root,background="red")
MainFrame.place(x=0,y=0,height=400,width=600)

#->Adding screen to display text
Screen=Text(MainFrame,bg="white",fg="black",width=73,height=20)
Screen.place(x=5,y=5)
#->Adding searchbar
SearchBar=Entry(MainFrame,textvariable=StringVar())
SearchBar.place(x=110,y=350,height=40,width=378)

#->Functions



#->Adding search button 
VoiceSearchButton=Button(MainFrame,text="Voice search" )
VoiceSearchButton.place(x=5,y=350,height=41,width=100)
#->Adding search button 
SearchButton=Button(MainFrame,text="SEARCH")
SearchButton.place(x=494,y=350,height=41,width=100)

#->Functions
#Login function
def Login():
    pass
#Check user Function
def LoginStatus():
    if(os.path.isfile("resource/User_details.pickle")):
        print("failed!")
    else:
        # imagepng=Image.open("resource\login-avatar.png")
        # image = image.resize(10, 20)
        subWindow=Toplevel()
        subWindow.title("U S E R   L O G I N")
        subWindow.geometry("500x250")
        subWindow.resizable(0,0)
        subWindow.config(background="#1fdba9")
        Frame(subWindow,height=190,width=160,relief="raised").place(x=5,y=15)
        Label(subWindow,text="Name: ",font=("Arial",13),relief="flat").place(x=170,y=25,width=90,height=30)
        Entrybox=Entry(subWindow,width=20,font=("Arial",13),relief="flat")
        Entrybox.place(x=262,y=25,width=233,height=30)
        Label(subWindow,text="Password: ",font=("Arial",13),relief="flat").place(x=170,y=65,width=90,height=30)
        Entrybox=Entry(subWindow,width=20,font=("Arial",13),relief="flat")
        Entrybox.place(x=262,y=65,width=233,height=30)
        # Create a StringVar to store the selected gender
        gender_variable = StringVar(subWindow)
        gender_variable.set("Select gender")  # Set the default value
        # Create the dropdown menu
        gender_options = ["Male", "Female"]
        gender_menu = OptionMenu(subWindow, gender_variable, *gender_options)
        gender_menu.place(x=182,y=115)
        submitButton=Button(subWindow,text="Submit",font=("Arial",13),relief="groove",background="light green",activebackground="orange")
        submitButton.place(x=310,y=115,width=143,height=30)
    

#Adding greeting function

def greeeting():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!")
    elif hour>=12 and hour<18:
        Speak("Good Afternoon!")   

    else:
        Speak("Good Evening!")  

 
    
# greeeting()
#Main functions call
# Thread(greeeting).start()
LoginStatus()
Root.mainloop()