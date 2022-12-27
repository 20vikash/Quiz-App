import tkinter
from tkinter import IntVar

import database
import leaderboard
import WelcomePage
from colors import *

print(database.qidL, 'Hi2')

def page(rootW = None):
    try:
        rootW.destroy()
    except:
        pass
    root5 = tkinter.Tk()

    root5.geometry('600x600+400+100')
    root5.title('Quiz')
    root5.resizable(0, 0)
    
    root5.config(bg=bg)
    
    def next():
        try:
            errL.config(text='')
            if number.get() != 0:
                if database.first:
                    nonlocal initial_data
                    print('Hi')
                    if initial_data[2] == number.get():
                        if not database.corrupted:
                            database.score += 2
                        else:
                            database.corrupted = False
                        database.fState = False
                        database.first = False
                        database.correctAns = True
                    else:
                        database.correctAns = False
                        database.corrupted = True
                        errL.config(text='Wrong answer!! Try again.')
                else:
                    if lans[database.state] == number.get():
                        if not database.corrupted:
                            database.score += 2
                        else:
                            database.corrupted = False
                        database.correctAns = True
                        database.state += 1
                    else:
                        database.correctAns = False
                        database.corrupted = True
                        errL.config(text='Wrong answer!! Try again.')
                
                print(database.score)

                if database.correctAns:
                    data = database.fetchData()
                    
                    number.set(0)
                    questionL.config(text=data[0])
                    
                    option1.config(text=data[1].split('|')[0])
                    option2.config(text=data[1].split('|')[1])
                    option3.config(text=data[1].split('|')[2])
                    option4.config(text=data[1].split('|')[3])
                    
                    userL.config(text='By - {}'.format(data[3]))
            else:
                errL.config(text='Please choose an option!!')
        except:
            database.updateScore()
            database.updateAnsName()
            leaderboard.page(root5)
    
    def submit():
        nextButton.config(state=tkinter.DISABLED)
        if database.submitB and not database.fState:
            database.state += 1
            database.submitB = False
        if number.get() != 0:
            print(database.state)
            if lans[database.state - 1] == number.get() and not database.corrupted:
                database.score += 2
                database.correctAns = True
            elif lans[database.state - 1] == number.get() and database.corrupted:
                database.correctAns = True
            else:
                database.correctAns = False
                database.corrupted = True
                errL.config(text='Wrong answer!! Try again.')
        if number.get() != 0:
            if database.correctAns:
                database.updateScore()
                database.updateAnsName()
                leaderboard.page(root5)
        else:
            errL.config(text='Please choose an option!')

    try:
        database.answers()
        lans = database.answersL
        
        print(lans, 'Hi')
        
        database.Qdata()
        initial_data = database.fetchData()
        
        header = tkinter.Label(root5, text='Play!!', bg=bg, font=('Arieal', 18, 'bold'))
        header.pack(pady=(50, 50))
        
        frame = tkinter.Frame(root5, bg=bg)
        frame.pack()
        
        questionL = tkinter.Label(frame, text=initial_data[0], 
                                  bg=bg, font=('Arieal', 12, 'italic'))
        questionL.grid(row=0, column=0)
        
        number = IntVar()
        
        option1 = tkinter.Radiobutton(frame, 
                                    text=initial_data[1].split('|')[0], variable=number, 
                                    value=1, bg=bg)
        option2 = tkinter.Radiobutton(frame, 
                                    text=initial_data[1].split('|')[1], variable=number, 
                                    value=2, bg=bg)
        option3 = tkinter.Radiobutton(frame, 
                                    text=initial_data[1].split('|')[2], variable=number, 
                                    value=3, bg=bg)
        option4 = tkinter.Radiobutton(frame, 
                                    text=initial_data[1].split('|')[3], variable=number, 
                                    value=4, bg=bg)

        option1.grid(row=1, column=0)
        option2.grid(row=2, column=0)
        option3.grid(row=3, column=0)
        option4.grid(row=4, column=0, pady=(0, 15))
        
        nextButton = tkinter.Button(root5, text='Next', 
                                    command=next, bg=button, font=('Arieal', 10, 'bold'))
        nextButton.pack(pady=(0, 9))
        
        submitB = tkinter.Button(root5, text='Submit', 
                                 command=submit, bg=button, font=('Arieal', 10, 'bold'))
        submitB.pack(pady=15)
        
        userL = tkinter.Label(root5, text='By - {}'.format(initial_data[3]), 
                              bg=bg, font=('Arieal', 10, 'italic'))
        userL.pack(pady=10)
        
        errL = tkinter.Label(root5, text='', bg=bg)
        errL.pack(pady=10)
    except:
        def homePage():
            database.reset()
            WelcomePage.page(root5)
        
        pointL = tkinter.Label(root5, text='Contribute to earn points!!', 
                               bg=bg, font=('Arieal', 16, 'italic'))
        pointL.pack(pady=(50, 40))
        
        homeB = tkinter.Button(root5, text='Home', width=19, command=homePage)
        homeB.pack()
