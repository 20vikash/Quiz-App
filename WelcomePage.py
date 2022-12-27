import tkinter

import contribute
import quiz
import about
from colors import *

def page(rootW = None):
    try:
        rootW.destroy()
    except:
        pass
    root3 = tkinter.Tk()

    root3.geometry('600x600+400+100')
    root3.title('HomePage')
    root3.resizable(0, 0)
    
    root3.config(bg=bg)
    
    def aboutPage():
        about.page(root3)
    
    def contribute_():
        contribute.page(root3)
        
    def quiz_():
        quiz.page(root3)
    
    title = tkinter.Label(root3, text='Welcome!', bg=bg, font=('Arieal', 18, 'bold'))
    title.pack(pady=(65, 0))
    
    useB = tkinter.Button(root3, text='Play the Quiz', 
                          command=quiz_, bg='#ca3c0f', height=5, width=30, 
                          font=('Arieal', 12, 'bold'))
    useB.pack(pady=(20, 20))
    
    contributeB = tkinter.Button(root3, text='Contribute', 
                            command=contribute_, bg='#86AD5D', height=5, width=30
                            , font=('Arieal', 12, 'bold'))
    contributeB.pack(pady=(0, 20))
        
    aboutB = tkinter.Button(root3, text='About App', 
                            command=aboutPage, bg='#8FB6C8', height=5, width=30
                            , font=('Arieal', 12, 'bold'))
    aboutB.pack()
