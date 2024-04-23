from tkinter import*

subWindow=Tk()




# Assuming you have already created the subWindow and UI elements...

entrybox1 = Entry(subWindow, width=20, font=("Arial", 13), relief="flat")
entrybox1.place(x=262, y=25, width=233, height=30)

entrybox2 = Entry(subWindow, width=20, font=("Arial", 13), relief="flat")
entrybox2.place(x=262, y=65, width=233, height=30)

gender_variable = StringVar(subWindow)
gender_variable.set("Select gender")  # Set the default value

gender_options = ["Male", "Female"]
gender_menu = OptionMenu(subWindow, gender_variable, *gender_options)
gender_menu.place(x=182, y=115)

submitButton = Button(subWindow, text="Submit", font=("Arial", 13),
                      relief="groove", background="light green", activebackground="orange",
                      command=lambda: handle_submit(entrybox1, entrybox2, gender_variable))
submitButton.place(x=310, y=115, width=143, height=30)

# Run the main loop
subWindow.mainloop()
