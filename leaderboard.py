import tkinter

import database
import WelcomePage
from colors import *

def page(rootW = None):
    try:
        rootW.destroy()
    except:
        pass
    root6 = tkinter.Tk()

    root6.geometry('600x600+400+100')
    root6.title('log in')
    root6.resizable(0, 0)
    root6.title('LeaderBoard')
    
    root6.config(bg=bg)
    
    def homePage():
        database.reset()
        WelcomePage.page(root6)
    
    leaderT = tkinter.Label(root6, text='LeaderBoard', bg=bg, font=('Arieal', 20, 'bold'))
    leaderT.pack(pady=(40, 25))
    
    data = database.leaderBoard()
    myScore = database.yourScore()[0]
    
    for i in data:
        dataL = tkinter.Label(root6, text='{}           {}'.format(i[0], i[1]), 
                              bg=bg, font=('Arieal', 13, 'italic'))
        dataL.pack()
    
    homeB = tkinter.Button(root6, text='Home', command=homePage, bg=button, width=19)
    homeB.pack(pady=(15, 10))
    
    yourScoreL = tkinter.Label(root6, bg=bg,
                        text='Your place: {}'.format(myScore[0]), font=('Arieal', 13, 'italic'))
    yourScoreL.pack()
