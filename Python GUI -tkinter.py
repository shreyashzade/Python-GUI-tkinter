#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Creating button in a window or container
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()


# In[ ]:


#Canvas: Used to draw pictures and other complex layout like graphics, text and widgets.
from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()


# In[5]:


#CheckButton: Used to select any number of options by displaying a number of options to a user as toggle buttons. 
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='Yes', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='No', variable=var2).grid(row=1, sticky=W)
mainloop()


# In[6]:


#Entry:Used to input the single line text entry from the user.. For multi-line text input, Text widget is used. 
from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()


# In[7]:


#Frame: It acts as a container to hold the widgets. It is used for grouping and organizing the widgets.
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text = 'Red', fg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)
root.mainloop()


# In[9]:


#Label: It refers to the display box where you can put any text or image which can be updated any time as per the code.
from tkinter import *
root = Tk()
w = Label(root, text='ShreyashZade')
w.pack()
root.mainloop()


# In[10]:


#Listbox: It offers a list to the user from which the user can accept any number of options.
from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()


# In[15]:


#Menu: It is used to create all kinds of menus used by the application.
from tkinter import *
	
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()


# In[2]:


#Message: It refers to the multi-line and non-editable text. It works same as that of Label.
from tkinter import *
main = Tk()
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack( )
main.mainloop( )


# In[3]:


#RadioButton: It is used to offer multi-choice option to the user. It offers several options to the user and the user has to choose one option. 
from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
mainloop()


# In[ ]:




