# -*- coding: utf-8 -*-


from tkinter import *

def speak(text1):
    # importing the pyttsx library
    import pyttsx3
    
    # initialisation
    engine = pyttsx3.init()
    newVoiceRate = 140
    engine.setProperty('rate',newVoiceRate)
    # testing
    engine.say(text1) 
    engine.runAndWait()



    
def main(hos,city,mail): 
    
        
    def callback():
        def sendmail(mail,msg):
            
            # Python code to illustrate Sending mail from 
            # your Gmail account 
            import smtplib
              
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
              
            # start TLS for security
            s.starttls()
              
            # Authentication
            s.login("eration6@gmail.com", "Project@123")
              
            # message to be sent
            name=msg["name"]
            add=msg["address"]
            num=msg["number"]
            dr=msg["skin specialist dr"]
            message = "Skin Specialist Doctor Information\n\n[1]Doctor Name         "+str(dr)+"\n[2]Hospital name       "+str(name)+"\n[3]Hospital Address    "+str(add)+"\n[4]hospital number     "+str(num)+"\n\nHope you found this information helpful,Wish you a faster recovery"
            print("message ",message)
            # sending the mail
            s.sendmail("eration6@gmail.com",mail,message)
              
            # terminating the session
            print("sent mail")
            s.quit()
            
        sendmail(mail,hos)
        speak("this same information is sent to your mail id "+mail)
        speak("Wish you quick recovery")
        speak("thank you for using our smart scan system")
        root.destroy()
    class Table:
          
        def __init__(self,root):
              
            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                      
                    self.e = Entry(root, width=50, fg='black',
                                   font=('Arial',12,'bold'))
                      
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
      
    # take the data
    lst = [('Name:',hos['name']),
           ('Address:',hos['address']),
           ('Number:',hos['number']),
           ('Skin specialist dr:',hos['skin specialist dr'])]
       
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
       
    # create root window
    root = Tk()
    root.title("Skin Specialist in "+city)
    

    t = Table(root)

    Button(root,text='Send details on Email', command=callback,font=("Arial", 10),fg="red",height=1,width=20,bg="yellow").grid(row=5, padx=10,pady=20)

    root.mainloop()
    return 1