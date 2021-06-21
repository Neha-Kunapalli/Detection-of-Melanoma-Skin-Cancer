# -*- coding: utf-8 -*-


from tkinter import*




def main():
    from firebase import firebase
    from tkinter import messagebox
    import gui2
    firebase = firebase.FirebaseApplication('https://skin-disease-12885-default-rtdb.firebaseio.com/', None)
    
    hospital=firebase.get("","hospital")
    hospital=list(hospital)
    print(hospital)
    
    
    def register():
        name=entry_1.get()
        mail=entry_2.get()
        mail1=mail.split(".")[0]
        print(mail)
        gender=var.get()
        if gender == 1:
            gender1="male"
        if gender == 2:
            gender1="female"
        age=entry_3.get()
        city=entry_4.get()
        print(name,mail,gender1,age,city)
        firebase.put("",mail1+"/name",name)
        firebase.put("",mail1+"/email",mail)
        firebase.put("",mail1+"/gender",gender1)
        firebase.put("",mail1+"/age",age)
        firebase.put("",mail1+"/city",city)
        root.destroy()
        gui2.main(name,city,mail)
        
        
        
    
    root = Tk()
    root.geometry('500x500')
    root.title("Registration Form")
    
    label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)
    
    
    label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    
    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)
    
    label_2 = Label(root, text="Email",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)
    
    entry_2 = Entry(root)
    entry_2.place(x=240,y=180)
    
    label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
    label_3.place(x=70,y=230)
    
    var = IntVar()
    
    Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
    Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
    
    label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
    label_4.place(x=68,y=280)
    
    
    entry_3 = Entry(root)
    entry_3.place(x=240,y=280)
    
    label_5 = Label(root, text="City:",width=20,font=("bold", 10))
    label_5.place(x=68,y=330)
    
    
    entry_4 = Entry(root)
    entry_4.place(x=240,y=330)
    
    
    Button(root, text='Submit',width=20,bg='brown',fg='white',command=register).place(x=180,y=380)
    # it is use for display the registration form on the window
    root.mainloop()
main()
