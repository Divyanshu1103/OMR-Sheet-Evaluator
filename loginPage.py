from tkinter import *
# for fonts available in tkinter 
from tkinter import font
# to get mac address of the device
from uuid import getnode
# to execut landingPage.py file
from landingPage import main

any_message = False
old_message = None

# checking user is authenticated or not
def authenticate_user():
    # fetching username entered and password entered
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    print(str(getnode()))
    # if username and password is correct
    if entered_username == str(getnode()) and entered_password == '1234':
        
        # destory login frame , bottom frame and main window
        login_frame.destroy()
        bottom_frame.destroy()
        main_window.destroy()

        # executing landingPage.py file
        main()

    # if username or password is incorrect
    else:
        global old_message,any_message
        if any_message:
            old_message.destroy()
            old_message = Message(main_window,text='Invalid Username or Password!',width=500,font=smallfont,bg='lavender',highlightbackground='deepskyblue',highlightthickness=2)
            old_message.pack(before=login_frame)
        else:
            any_message = True
            old_message = Message(main_window,text='Invalid Username or Password!',width=500,font=smallfont,bg='lavender',highlightbackground='deepskyblue',highlightthickness=2)
            old_message.pack(before=login_frame)

# setup login frame with heading and entry fields
def setup_login_frame():
    print(str(getnode()))
    # heading label
    heading = Label(login_frame,text='Login Page',font=largefont,bg='lavender',fg='deepskyblue')
    heading.grid(columnspan=2,row=0,column=0,pady=20)

    # username label and entry field
    username = Label(login_frame,text='username:',font=smallfont,bg='lavender')
    username.grid(row=1,column=0)
    username_entry = Entry(login_frame,font=smallfont,width=30)
    username_entry.grid(row=1,column=1,pady=10)

    # password label and entry field
    password = Label(login_frame,text='password:',font=smallfont,bg='lavender')
    password.grid(row=2,column=0)
    password_entry = Entry(login_frame,font=smallfont,width=30)
    password_entry.grid(row=2,column=1,pady=10)

    # submit button
    submit = Button(login_frame,text='submit',width=12,bg='deepskyblue',font=smallfont,command=authenticate_user)
    submit.grid(row=3,column=1,pady=10,sticky=E)

    # return username and password entry fields
    return username_entry,password_entry

if __name__ == '__main__':
    # create window
    main_window = Tk()
    main_window.config(bg='lavender')

    # get device screen width and height
    window_width = main_window.winfo_screenwidth()
    window_height = main_window.winfo_screenheight()

    # set main_window to screen fit
    main_window.geometry(str(window_width)+'x'+str(window_height))

    # using two font sizes 
    largefont=font.Font(size=22)
    smallfont=font.Font(size=16)

    # create login frame
    login_frame = Frame(main_window)
    login_frame.config(bg='lavender')
    login_frame.pack(pady=80)

    # setup_login_frame will return username and password entry fields
    username_entry,password_entry = setup_login_frame()

    # create bottom frame
    bottom_frame = Frame(main_window,bg='lavender',highlightbackground='deepskyblue',highlightthickness=2)
    bottom_frame.pack(pady=120)

    # setup bottom frame with developer details
    detail = Label(bottom_frame,text='developed by Divyanshu',bg='lavender',height=6,width=80,font=largefont)
    detail.pack()

    # to display main_window
    main_window.mainloop()