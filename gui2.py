from PIL import ImageTk
from tkinter import *
import os
from tkinter import filedialog
from PIL import Image
import os
from firebase import firebase
cwd = os.getcwd()
#import final
import info
from tkinter.filedialog import askopenfilename 
firebase = firebase.FirebaseApplication('https://skin-disease-12885-default-rtdb.firebaseio.com/', None)
hospital=firebase.get("","hospital")
hospital=list(hospital)
print(hospital)
    

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
    
    
def main(name,city,mail):

    root = Tk()
    frame = Frame(root)
    frame.pack()
    import classify2
    
    
    image = Image.open(cwd+"/wall.jpg")
    photo = ImageTk.PhotoImage(image)
    
    label = Label(root, image=photo)
    label.image = photo  # keep a reference!
    label.pack()
    
    label1 = Label(root, text='CHECK SKIN DISEASE',font=("Arial", 20),fg="blue",)
    label1.pack(padx=10,pady=20)
    
    def callback2():
        root.destroy()
        import start
        start.main()

    
    
    
    def callback():
        
        myFormats = [('JPEG / JFIF', '*.JPG') ]
        file = askopenfilename(filetypes=myFormats)
        skin_class,score = classify2.main(file)
        image = Image.open(file)
        photo = ImageTk.PhotoImage(image)
        output = name+' IS SUFFERING WITH '+skin_class+' DISEASE.'+"with "+score+"% accuracy "
        speak("scan result is "+output)
        speak("showing best skin doctor in "+city)
        label1.configure(text=output,fg="black",font=("Arial", 10))
        label1.text=output
        # label.configure(image=photo)
        # label.image = photo
        if city in hospital:
            hos=firebase.get("","hospital/"+city)
            print(hos)
            info.main(hos,city,mail)
            print("done")
        else:
            speak("Sorry could not find a "+city+" based skin specialist doctor in our database")
            speak("searching a "+city+" based skin specialist on google")
            import webbrowser
            webbrowser.open_new_tab("https://www.google.com/search?q=skin specialist doctor in "+city)
            
        

    
    
    root.title(' Detection Of Melanoma Skin cancer')
    root.geometry('500x600') # Size 200, 200
    root.resizable(width=False, height=False)
    root.configure(bg="cyan")
    
    Button(text='Scan', command=callback,font=("Arial", 10),fg="red",height=1,width=20,bg="yellow").pack(side=TOP, padx=10,pady=20)
    Button(text='Restart', command=callback2,font=("Arial", 10),fg="red",height=1,width=20,bg="yellow").pack(side=TOP, padx=10,pady=20)
    speak("welcome to smart skin disease scan")
    speak("click on Scan button to continue")
    root.mainloop()
    
