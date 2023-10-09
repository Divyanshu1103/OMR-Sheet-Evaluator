from tkinter import *
from tkinter import filedialog
import os
from tkinter import font
from cvfile import get_bubbles
from PIL import Image,ImageTk
from csvUpload import *

main_window = None
largefont = None
smallfont = None

main_frame = None
first_frame = None
second_frame = None
third_frame = None

master_key_bubbles = None
master_key_name = None
master_key_path = None

any_message = False
old_message = None

def deleteImage():
    for i in second_frame.winfo_children():
        i.destroy()

def submit_function(file_directory_path,master_file_path,test_name_entry,subject_name_entry,class_name_entry):
    global any_message,old_message

    if len(file_directory_path.get()) == 0 or len(master_file_path.get()) == 0:
        if any_message:
            old_message.destroy()
            old_message = Message(main_frame,text='please provide directory path and master file path',width=600,bg='lavender',highlightbackground='deepskyblue',highlightthickness=2)
            old_message.pack()
        else:
            any_message = True
            old_message = Message(main_frame,text='please provide directory path and master file path',width=600,bg='lavender',highlightbackground='deepskyblue',highlightthickness=2)
            old_message.pack()
    elif len(test_name_entry.get()) == 0 or len(subject_name_entry.get()) == 0 or len(class_name_entry.get()) == 0:
        if any_message:
            old_message.destroy()
            old_message = Message(main_frame,text='please provide test name, subject name and class name',width=600,bg='lavender',highlightbackground='deepskyblue',highlightthickness=2)
            old_message.pack()
        else:
            any_message = True
            old_message = Message(main_frame,text='please provide test name, subject name and class name',width=600,bg='lavender',highlightbackground='deepskyblue',highlightthickness=2)
            old_message.pack()
    else:
        set_csv_file_name(test_name_entry,subject_name_entry,class_name_entry)
        create_csv()
        global master_key_bubbles

        marked = get_bubbles(master_key_path)
        master_key_bubbles = marked
        add_to_csv(master_key_name,marked,100)

        for base_directory,directories,img_files in os.walk(file_directory_path.get()):
            for file in img_files:
                deleteImage()
                image_path=base_directory+"/"+file
                frame2(image_path,file)
                marked = get_bubbles(image_path)
                total = get_total(marked,master_key_bubbles)
                add_to_csv(file,marked,total)
        if any_message:
            old_message.destroy()
        Message(main_frame,text='Marks have been successfully uploaded',width=500).pack()

def choose_master_file(master_file_path):
    global master_key_name,master_key_path

    filetype = (('image file','*.jpg'),('img','*.jpeg'))
    openimage = filedialog.askopenfilename(title='open omr sheet',initialdir='/',filetypes=filetype)
    master_file_path.delete(0,len(master_file_path.get()))
    master_file_path.insert(0,openimage)
    master_key_path = openimage
    master_key_name = openimage.split('/')[-1]
    frame2(openimage,master_key_name)

def choose_directory(file_directory_path):
    path = filedialog.askdirectory()
    file_directory_path.delete(0,len(file_directory_path.get()))
    file_directory_path.insert(0,path)

def frame3():
    detail = Label(third_frame,text='developed by Divyanshu',bg='lavender',height=6,width=80,font=largefont)
    detail.grid(row=0,column=0)

def frame2(image_path,name):
    img = ImageTk.PhotoImage(Image.open(image_path).resize((350,400),Image.ANTIALIAS))
    image_box = Label(second_frame,image=img)
    image_box.image = img
    image_box.pack()
    image_name = Label(second_frame,text=name,font=smallfont,bg='lavender')
    image_name.pack()

def frame1():
    file_directory_label = Label(first_frame,text='add directory: ',bg='lavender',font=smallfont)
    file_directory_label.grid(row=0,column=0)

    file_directory_path = Entry(first_frame,width=60,font=smallfont)
    file_directory_path.grid(row=0,column=1,ipady=2,pady=20)
    file_directory_browse_button = Button(first_frame,text='Browse',width=10,bg='hotpink',font=smallfont,command=lambda:choose_directory(file_directory_path))
    file_directory_browse_button.grid(row=0,column=2,padx=10)

    master_file_label = Label(first_frame,text='add master file: ',bg='lavender',font=smallfont)
    master_file_label.grid(row=1,column=0)
    master_file_path = Entry(first_frame,width=60,font=smallfont)
    master_file_path.grid(row=1,column=1,ipady=2,pady=20)
    master_file_browse_button = Button(first_frame,text='Browse',width=10,bg='deepskyblue',font=smallfont,command=lambda:choose_master_file(master_file_path))
    master_file_browse_button.grid(row=1,column=2)

    test_name_label = Label(first_frame,text='name of test: ',bg='lavender',font=smallfont)
    test_name_label.grid(row=2,column=0)
    test_name_entry = Entry(first_frame,width=20,font=smallfont)
    test_name_entry.grid(row=2,column=1,ipady=2,pady=20,sticky=W)

    subject_name_label = Label(first_frame,text='subject: ',bg='lavender',font=smallfont)
    subject_name_label.grid(row=3,column=0)
    subject_name_entry = Entry(first_frame,width=20,font=smallfont)
    subject_name_entry.grid(row=3,column=1,ipady=2,pady=20,sticky=W)

    class_name_label = Label(first_frame,text='class name: ',bg='lavender',font=smallfont)
    class_name_label.grid(row=4,column=0)
    class_name_entry = Entry(first_frame,width=20,font=smallfont)
    class_name_entry.grid(row=4,column=1,ipady=2,pady=20,sticky=W)

    submit_button = Button(first_frame,text='Submit',width=10,bg='mediumseagreen',font=smallfont,command=lambda:submit_function(file_directory_path,master_file_path,test_name_entry,subject_name_entry,class_name_entry))
    submit_button.grid(row=5,column=2)

def start_display():
    global main_frame,first_frame,second_frame,third_frame

    main_frame = Frame(main_window,bg='lavender')
    main_frame.grid(row=0,columnspan=2,column=0)

    first_frame = Frame(main_window,bg='lavender')
    first_frame.grid(row=1,column=0,pady=40)

    second_frame = Frame(main_window,bg='lavender',highlightbackground='deepskyblue',highlightthickness=2)
    second_frame.grid(row=1,column=1,pady=40)
    frame1()

    third_frame = Frame(main_window,bg='lavender',highlightbackground='deepskyblue',highlightthickness=2)
    third_frame.grid(row=2,column=0,columnspan=2,pady=30,padx=100)
    frame3()

def main():
    global main_window,largefont,smallfont

    main_window = Tk()
    main_window.config(bg='lavender')
    window_width = main_window.winfo_screenwidth()
    window_height = main_window.winfo_screenheight()
    main_window.geometry(str(window_width)+'x'+str(window_height))
    largefont = font.Font(size=20)
    smallfont = font.Font(size=16)

    start_display()

    main_window.mainloop()