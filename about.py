import tkinter

import WelcomePage
from colors import *

def page(rootW = None):
    try:
        rootW.destroy()
    except:
        pass
    
    root7 = tkinter.Tk()
    root7.geometry('600x600+400+100')
    root7.resizable(0, 0)
    root7.title('About Page')
    
    root7.config(bg=bg)
    
    def homePage():
        WelcomePage.page(root7)

    header = tkinter.Label(root7, text='About this App', bg=bg, font=('Arieal', 20, 'bold'))
    header.pack(pady=(0, 200))
    
    quizT = tkinter.Label(root7, text='Quiz app where you can contribute', 
                          bg=bg, font=('Arieal', 15, 'italic'))
    quizT.pack()
    
    rulesT = tkinter.Label(root7, text='You get 2 points for contributing and answering', 
                           bg=bg, font=('Arieal', 15, 'italic'))
    rulesT.pack(pady=(0, 50))

    homeB = tkinter.Button(root7, text='Home', command=homePage, bg=button, width=21)
    homeB.pack()
