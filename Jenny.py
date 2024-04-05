from tkinter import*


#intilizing the gui Window.
Root=Tk()
Root.title("J E N N Y  A S S I S T A N T")
Root.resizable(0,0)
Root.geometry("600x400")
# Root.iconbitmap(NONE) #Add the icon 

#Adding gui widgets

#->Adding Main frame for the application
MainFrame=Frame(Root,background="red")
MainFrame.place(x=0,y=0,height=400,width=600)

#->Adding screen to display text
Screen=Text(MainFrame,bg="white",fg="black",width=73,height=20)
Screen.place(x=5,y=5)







#Main functions call
Root.mainloop()