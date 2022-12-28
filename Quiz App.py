import tkinter

import database
import WelcomePage
from colors import *

def login(rootW = None):
    try:
        rootW.destroy()
    except:
        pass
    root = tkinter.Tk()

    root.geometry('600x600+400+100')
    root.title('Authenticate')
    root.resizable(0, 0)
    
    root.config(bg=bg)
    
    def welpage(email, passwd):
        if database.authenticate(email.get(), passwd.get()):
            try:
                root.destroy()
            except:
                pass
            
            WelcomePage.page()
        else:
            print('Log in failed')
    
    def signUp():
        try:
            root.destroy()
        except:
            pass
        
        root2 = tkinter.Tk()
        root2.geometry('600x600+400+100')
        root2.title('Sign up')
        root2.resizable(0, 0)
        
        root2.config(bg='#f3a861')
        
        def updateDatabase(user, mail, passwd, errL):
            try:
                errL.config(text='')
                for i in range(len(mail.get()) - 1, -1, -1):
                    if mail.get()[i] == '@':
                        indexVal = i
                        break
                if (mail.get()[indexVal: ] == '@gmail.com') and (passwd.get().strip(' ') != '') and (user.get().strip(' ') != ''):
                    if not database.insertValues(user.get(), mail.get(), passwd.get()):
                        errL.config(text='The Gmail acc or the username has already been registered!!')
                    else:
                        login(root2)

                else:
                    errL.config(text='Either of the entered fields are invalid!!')
                    user.delete(0, 'end')
                    mail.delete(0, 'end')
                    passwd.delete(0, 'end')
            except:
                database.updateScore()
        
        title_frame = tkinter.Frame(root2, bg=bg)
        title_frame.pack()

        title = tkinter.Label(title_frame, text='Sign Up!', font=('Arieal', 20, 'bold'), bg=bg)
        title.pack(pady=(55, 20))
        
        signUpFrame = tkinter.Frame(root2, bg=bg)
        signUpFrame.pack(anchor='w', padx=(200, 0), pady=(75, 0))
        
        gmailL = tkinter.Label(signUpFrame, text='Enter your Gmail ID', bg=bg
                               , font=('Arieal', 11, 'italic'))
        gmailE = tkinter.Entry(signUpFrame, width=30)
        
        passL = tkinter.Label(signUpFrame, text='Enter your password', bg=bg
                              , font=('Arieal', 11, 'italic'))
        passE = tkinter.Entry(signUpFrame, width=30, show='*')
        
        usernameL = tkinter.Label(signUpFrame, text='Enter your username', bg=bg
                                  , font=('Arieal', 11, 'italic'))
        usernameE = tkinter.Entry(signUpFrame, width=30)
        
        usernameL.grid(row=0, column=0, sticky='w')
        usernameE.grid(row=1, column=0, padx=20)
        
        gmailL.grid(row=2, column=0, sticky='w')
        gmailE.grid(row=3, column=0, padx=20)
        
        passL.grid(row=4, column=0, sticky='w')
        passE.grid(row=5, column=0, padx=20)
        
        error_label = tkinter.Label(root2, text='', bg=bg)
        error_label.pack()
        
        submit_button = tkinter.Button(root2, text='Submit', 
                                       command=lambda: updateDatabase(usernameE,
                                                        gmailE, passE, error_label), bg=button
                                       , width=10, font=('Arieal', 10, 'bold'))
        submit_button.pack()
        
        
    title_frame = tkinter.Frame(root, bg=bg)
    title_frame.pack()

    title = tkinter.Label(title_frame, text='Quiz App', font=('Arieal', 20, 'bold'), bg=bg)
    title.pack(pady=(45, 75))

    login_frame = tkinter.Frame(root, width=600, bg=bg)
    login_frame.pack(anchor='w', padx=(70, 0))

    login_text = tkinter.Label(login_frame, text='Login to continue.', bg=bg, font=('Arieal', 15, 'bold'))
    login_text.pack(padx=10, pady=15)

    logD = tkinter.Frame(root, bg=bg)
    logD.pack()

    user_text = tkinter.Label(logD, text='Enter your username', bg=bg, font=('Arieal', 13, 'italic'))
    pass_text = tkinter.Label(logD, text='Enter your password', bg=bg, font=('Arieal', 13, 'italic'))

    user_entry = tkinter.Entry(logD, width=30)
    pass_entry = tkinter.Entry(logD, width=30, show='*')

    user_text.grid(row=0, column=0)
    user_entry.grid(row=0, column=1, pady=10)

    pass_text.grid(row=1, column=0)
    pass_entry.grid(row=1, column=1)

    signFrame = tkinter.Frame(root, bg=bg)
    signFrame.pack()
    
    loginButton = tkinter.Button(logD, text='Log in', command=lambda: welpage(user_entry, 
                                                                        pass_entry), bg=button,
                                 width=10, font=('Arieal', 10, 'bold'))
    loginButton.grid(row=2, column=0, pady=20)

    textS = tkinter.Label(signFrame, text='Don\'t have an account ? Sign up', bg=bg, font=('Arieal', 10, 'bold'))
    textS.grid(row=0, column=0, padx=(0, 10))

    signb = tkinter.Button(signFrame, text='Sign Up', command=signUp, bg=button
                           , width=8, font=('Arieal', 8, 'bold'))
    signb.grid(row=0, column=1)

    root.mainloop()


if __name__ == '__main__':
    login()
