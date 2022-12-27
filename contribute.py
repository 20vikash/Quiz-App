import tkinter
from tkinter import IntVar

import database
import WelcomePage
from colors import *

def page(rootW = None):
    try:
        rootW.destroy()
    except:
        pass
    root4 = tkinter.Tk()
    root4.geometry('600x600+400+100')
    root4.resizable(0, 0)
    root4.title('Contribute')
    
    root4.config(bg=bg)
    
    def reset():
        quesEntry.delete(0, tkinter.END)
        optionsE1.delete(0, tkinter.END)
        optionsE2.delete(0, tkinter.END)
        optionsE3.delete(0, tkinter.END)
        optionsE4.delete(0, tkinter.END)
        number.set(0)
    
    def updateQuiz():
        errL.config(text='')
        
        invalid = False
        options_list = []
        question = quesEntry.get()
        
        if (question.strip(' ')) == '' or (number.get() not in [1, 2, 3, 4]):
            invalid = True
        
        options_list.extend([optionsE1.get(), optionsE2.get(), optionsE3.get(), optionsE4.get()])

        for i in options_list:
            if i.strip(' ') == '':
                invalid = True
                break
        
        if invalid:
            errL.config(text='Please populate the fields with correct values')
            
            reset()
        else:
            options_string = '|'.join(options_list)
            
            database.addQuiz(question, options_string, number.get())
            reset()
    
    def homePage():
        WelcomePage.page(root4)
        
    labelC = tkinter.Label(root4, text='Contribute', bg=bg, font=('Arieal', 18, 'bold'))
    labelC.pack(pady=(45, 35))
    
    quesFrame = tkinter.Frame(root4, bg=bg)
    quesFrame.pack()
    
    qestext = tkinter.Label(quesFrame, text='Enter your question!', 
                            bg=bg, font=('Arieal', 11, 'italic'))
    qestext.grid(row=0, column=0, pady=(0, 20))
    
    quesEntry = tkinter.Entry(quesFrame, width=30)
    quesEntry.grid(row=0, column=1, pady=(0, 20))
    
    optionsText = tkinter.Label(quesFrame, text='Enter the options!', 
                                bg=bg, font=('Arieal', 11, 'italic'))
    optionsText.grid(row=1, column=0)
    
    optionsE1 = tkinter.Entry(quesFrame, width=20)
    optionsE2 = tkinter.Entry(quesFrame, width=20)
    optionsE3 = tkinter.Entry(quesFrame, width=20)
    optionsE4 = tkinter.Entry(quesFrame, width=20)
    
    optionsE1.grid(row=1, column=1, pady=(0, 1))
    optionsE2.grid(row=2, column=1, pady=(0, 3))
    optionsE3.grid(row=3, column=1, pady=(0, 3))
    optionsE4.grid(row=4, column=1, pady=(0, 10))
    
    answerFrame = tkinter.Frame(root4, bg=bg)
    answerFrame.pack(pady=10)
    
    answerText = tkinter.Label(answerFrame, text='Select the answer', 
                               bg=bg, font=('Arieal', 12, 'bold'))
    answerText.grid(row=0, column=0)
    
    number = IntVar()
    
    answer_1 = tkinter.Radiobutton(answerFrame, text='A', value=1, 
                                   variable=number, bg=bg, font=('Arieal', 8, 'italic'))
    answer_2 = tkinter.Radiobutton(answerFrame, text='B', value=2, 
                                   variable=number, bg=bg, font=('Arieal', 8, 'italic'))
    answer_3 = tkinter.Radiobutton(answerFrame, text='C', value=3, 
                                   variable=number, bg=bg, font=('Arieal', 8, 'italic'))
    answer_4 = tkinter.Radiobutton(answerFrame, text='D', value=4, 
                                   variable=number, bg=bg, font=('Arieal', 8, 'italic'))
    
    answer_1.grid(row=1, column=0)
    answer_2.grid(row=2, column=0)
    answer_3.grid(row=3, column=0)
    answer_4.grid(row=4, column=0, pady=(0, 30))
    
    subButton = tkinter.Button(root4, text='Submit', 
                               command=updateQuiz, bg=button, width=8, font=('Arieal', 10, 'bold'))
    subButton.pack()
    
    homeB = tkinter.Button(root4, text='Home', 
                           command=homePage, bg=button, width=8, font=('Arieal', 10, 'bold'))
    homeB.pack(pady=10)
    
    errL = tkinter.Label(root4, text='', bg=bg)
    errL.pack()
