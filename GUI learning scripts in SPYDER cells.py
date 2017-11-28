# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:40:02 2017

@author: lu
"""

from tkinter import *

master = Tk()

v = IntVar()

def count_low():
    
    pass
    global ax, fig, canvas, t2, v2, window, i_200, i_400, i

    v2 = volt_hb_low[1:200]
    
    
def count_high():
    
    pass
    global ax, fig, canvas, t2, v2, window, i_200, i_400, i

#Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
#Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)

radio_1 = Radiobutton(master, text = 'Low', command = count_low, variable = v, value = 1)
#radio_1.deselect()
radio_1.grid(row=0, column= 0, sticky = W)
radio_2 = Radiobutton(master, text = 'High', command = count_high, variable = v, value = 2)
#radio_2.deselect()
radio_2.grid(row=0, column= 1, sticky = E)


master.mainloop()
#%%


from tkinter import *

master = Tk()
MODES = [
        ("Monochrome", "1"),
        ("Grayscale", "L"),
        ("True color", "RGB"),
        ("Color separation", "CMYK")]

v = StringVar()
v.set("L") # initialize

for text, mode in MODES:
    b = Radiobutton(master, text=text,
                    variable=v, value=mode)
    b.pack(anchor=W)
    
    
master.mainloop()

#%%

from tkinter import *

root = Tk()

def key(event):
    print ("pressed"), repr(event.char)

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()

#%%


# =============================================================================
# Chapter 1-1
# =============================================================================


import tkinter as tk
win = tk.Tk()
win.title('Python GUI')
win.mainloop()


#class AClass(Object):
#    print('Hello from AClass')
#classInstance = AClass()
#    
#%%
# =============================================================================
# Chapter 1-2
# =============================================================================



import tkinter as tk
win = tk.Tk()
win.title('Python GUI')
win.resizable(0,0)  # 4 Disable resizing the GUI
win.mainloop()


#%%



# =============================================================================
# Chapter 1-3
# =============================================================================



import tkinter as tk
from tkinter import ttk



win = tk.Tk()

ttk.Label(win, text = 'A Label').grid(column = 0, row = 0)




win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI
win.mainloop()


#%%



# =============================================================================
# Chapter 1-4
# =============================================================================



import tkinter as tk
from tkinter import ttk



win = tk.Tk()

aLabel = ttk.Label(win, text = 'A Label')
aLabel.grid(column = 0, row = 0)

def clickMe():
    action.configure(text= '** I have been Clicked!**')
    aLabel.configure(foreground = 'red')
    
action = ttk.Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 1, row = 0)


win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI
win.mainloop()

#%%



# =============================================================================
# Chapter 1-5
# =============================================================================

import tkinter as tk
#from tkinter import ttk
from tkinter import *


win = tk.Tk()

#aLabel = ttk.Label(win, text = 'A Label')
#aLabel.grid(column = 0, row = 0)

def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get())
    print(nameEntered.get())

#    aLabel.configure(foreground = 'red')
    
action = ttk.Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 1, row = 1)
ttk.Label(win, text = 'Enter a name: ').grid(column = 0, row = 0)

#name = tk.StringVar()
#nameEntered = ttk.Entry(win, width=12, textvariable=name)
#
nameEntered = Entry(win, width=12)
nameEntered.grid(column = 0, row=1)



win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI
win.mainloop()

#%%



# =============================================================================
# Chapter 1-5------1   やはり教科書通りでは行かない
# =============================================================================

import tkinter as tk
#from tkinter import ttk
from tkinter import *


win = tk.Tk()

#aLabel = ttk.Label(win, text = 'A Label')
#aLabel.grid(column = 0, row = 0)

def clickMe():
#    global name
    action.configure(text= 'Hello ' + name.get())
    print(name.get())

#    aLabel.configure(foreground = 'red')
    
action = Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 1, row = 1)
Label(win, text = 'Enter a name: ').grid(column = 0, row = 0)

name = StringVar()
nameEntered = Entry(win, width=12, textvariable = name)
# 
#nameEntered = Entry(win, width=12)
nameEntered.grid(column = 0, row=1)



win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI
win.mainloop()


#%%
# =============================================================================
#　Chapter 1-5　補足
# =============================================================================
from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print (e.get())

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
#%%
#----------------------------------

parent=Tk()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")

content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)

parent.mainloop()

#やはりこれもあんまり意味がわからない
#http://effbot.org/tkinterbook/entry.htm
#%%

master = Tk()

e = Entry(master)
e.pack()

e.delete(0, END)
e.insert(0, "a default value")

master.mainloop()

#%%
#------------------------
master = Tk()
# =============================================================================
# You can also bind the entry widget to a StringVar instance, 
# and set or get the entry text via that variable:
# 
# =============================================================================
v = StringVar()
e = Entry(master, textvariable=v)
e.pack()

v.set("a default value")
s = v.get()
print(s)


master.mainloop()

#%%



# =============================================================================
# Chapter 1-6 set_focus() & state = 'disable'
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *


win = tk.Tk()

#aLabel = ttk.Label(win, text = 'A Label')
#aLabel.grid(column = 0, row = 0)

def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

#    aLabel.configure(foreground = 'red')
    
action = ttk.Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 1, row = 1)
ttk.Label(win, text = 'Enter a name: ').grid(column = 0, row = 0)

#name = tk.StringVar()
#nameEntered = ttk.Entry(win, width=12, textvariable=name)
#
nameEntered = Entry(win, width=12)
nameEntered.grid(column = 0, row=1)



win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI

#win.set_focus()
nameEntered.focus()
win.mainloop()

#%%

# =============================================================================
# Chapter 1-7 Combobox numberChosen.get()  state= 'readonly'
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *


win = tk.Tk()

#aLabel = ttk.Label(win, text = 'A Label')
#aLabel.grid(column = 0, row = 0)

def clickMe():
    global name
#    g
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

#    aLabel.configure(foreground = 'red')
    
action = ttk.Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)

#name = tk.StringVar()
#nameEntered = ttk.Entry(win, width=12, textvariable=name)

ttk.Label(win, text = 'Enter a name: ').grid(column = 0, row = 0)
nameEntered = Entry(win, width=12)
nameEntered.grid(column = 0, row=1)



Label(win, text = 'Choose a number:').grid(column = 1, row = 0)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(win, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1)
numberChosen.current(2)




win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI

#win.set_focus()
nameEntered.focus()
win.mainloop()


#%%


# =============================================================================
# Chapter 1-8 Checkbuttons IntVar() select()
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *


win = tk.Tk()

#aLabel = ttk.Label(win, text = 'A Label')
#aLabel.grid(column = 0, row = 0)

def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
#    action.configure(state = 'disable')
#    print(chVarDis)
#    print(chVarUn)
#    print(chVarEn)


#    aLabel.configure(foreground = 'red')
    
action = ttk.Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)

#name = tk.StringVar()
#nameEntered = ttk.Entry(win, width=12, textvariable=name)

ttk.Label(win, text = 'Enter a name: ').grid(column = 0, row = 0)
nameEntered = Entry(win, width=12)
nameEntered.grid(column = 0, row=1)



Label(win, text = 'Choose a number:').grid(column = 1, row = 0)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(win, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1)
numberChosen.current(2)

#def radcall():
##    radVar1.set("1")
##    global radVar1
##    radSel = radVar1.get()
#    if check1['value'] == 1:
#        win.configure(background = COLOR1)
#    elif check2['value'] == 2:
#        win.configure(background = COLOR2)
#    elif check3['value'] == 3:
#        win.configure(background = COLOR3)

#chVarDis = tk.IntVar()
#check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled', command = radcall, onvalue= 1, offvalue= 0)
#check1.select()
#check1.grid(column=0, row = 4, sticky = W)
#
#chVarUn = tk.IntVar()
#check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn, command = radcall, onvalue= 2, offvalue= 0)
#check2.deselect()
#check2.grid(column=1, row = 4, sticky = W)
#
#chVarEn = tk.IntVar()
#check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn, command = radcall, onvalue= 3, offvalue= 0)
#check3.select()
#check3.grid(column=2, row = 4, sticky = W)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column=0, row = 4, sticky = W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn)
check2.deselect()
check2.grid(column=1, row = 4, sticky = W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn)

check3.select()
check3.grid(column=2, row = 4, sticky = W)



win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI

#win.set_focus()
nameEntered.focus()
win.mainloop()



#%%


# =============================================================================
# Chapter 1-8 Checkbuttons IntVar() select()
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *


win = tk.Tk()

#aLabel = ttk.Label(win, text = 'A Label')
#aLabel.grid(column = 0, row = 0)

def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

#    aLabel.configure(foreground = 'red')
    
action = ttk.Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)

#name = tk.StringVar()
#nameEntered = ttk.Entry(win, width=12, textvariable=name)

ttk.Label(win, text = 'Enter a name: ').grid(column = 0, row = 0)
nameEntered = Entry(win, width=12)
nameEntered.grid(column = 0, row=1)



Label(win, text = 'Choose a number:').grid(column = 1, row = 0)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(win, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1)
numberChosen.current(2)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column=0, row = 4, sticky = W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn)
check2.deselect()
check2.grid(column=1, row = 4, sticky = W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn)
check3.select()
check3.grid(column=2, row = 4, sticky = W)

win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI




COLOR1 = 'Blue'
COLOR2 = 'Gold'
COLOR3 = 'Red'

radVar1 = tk.StringVar()

def radcall():
#    radVar1.set("1")
#    global radVar1
    radSel = radVar1.get()
    if radSel == 1:
        win.configure(background = COLOR1)
    elif radSel == 2:
        win.configure(background = COLOR2)
    elif radSel == 3:
        win.configure(background = COLOR3)
    print(radVar1)
    print(radVar1.get())
    print(radSel)
#    print('Hey')
#    print(rad1['value'])
    

#def radcall():
##    radVar1.set("1")
#    global radVar1
#    radSel = radVar1.get()
#    if rad1['value'] == 1:
#        win.configure(background = COLOR1)
#    elif rad1['value'] == 2:
#        win.configure(background = COLOR2)
#    elif rad1['value'] == 3:
#        win.configure(background = COLOR3)
#    print(radVar1)
#    print(radVar1.get())
##    print('Hey')
##    print(rad1['value'])
    


radVar1= tk.IntVar()
#radVar2 = tk.IntVar()
#radVar3 = tk.IntVar()
#radSel = 1

rad1 = tk.Radiobutton(win, text = COLOR1, variable = radVar1, value = 1, command = radcall)
rad1.deselect()
rad1.grid(column=0, row = 5, sticky = W)

rad2 = tk.Radiobutton(win, text = COLOR2, variable = radVar1,  value = 2,command = radcall)
rad2.deselect()
rad2.grid(column=1, row = 5, sticky = W)

rad3 = tk.Radiobutton(win, text = COLOR3, variable = radVar1,  value = 3,command = radcall)
rad3.deselect()
rad3.grid(column=2, row = 5, sticky = W)

#radVar1.set("1")

#radVar1 = tk.IntVar()
#win.set_focus()
#nameEntered.focus()
win.mainloop()

#%%


#Radiobutton 

from tkinter import *
from tkinter import messagebox

master = Tk()

v = IntVar()

#Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
#Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)



# =============================================================================
# 閉じる確認
# =============================================================================

def callback():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        master.destroy()


master.protocol("WM_DELETE_WINDOW", callback)


MODES = [
("Monochrome", "1"),
("Grayscale", "L"),
("True color", "RGB"),
("Color separation", "CMYK"),
]

v = StringVar()
v.set("L") # initialize

for text, mode in MODES:
    b = Radiobutton(master, text=text,
                variable=v, value=mode, indicatoron= 0)
    b.pack(anchor=W)
    
mainloop()


#%%
# =============================================================================
# キーとマウス取得
# =============================================================================

from tkinter import *

root = Tk()

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()



#%%

def callback(*args):
    print ("variable changed!")
    

var = StringVar()
var.trace("w", callback)
var.set("hello")
print(var.get())


#%%

#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title(u"Software Title")
root.geometry("400x300")


# 状態の変更
#def change_state():
#    # チェックされているラジオボタンを取得
#    checked = v.get()
#    print(v.get())
#    if ( checked == 1 ):
#        # radio1がチェックされていたら
#        radio2.configure( state = "disabled" )
#        radio3.configure( state = "disabled" )
#
#    elif ( checked == 2 ):
#        # radio2がチェックされていたら
#        radio1.configure( state = "disabled" )
#        radio3.configure( state = "disabled" )
#
#
#    elif ( checked == 3 ):
#        # radio3がチェックされていたら
#        radio1.configure( state = "disabled" )
#        radio2.configure( state = "disabled" )
#
#    else:
#        print ("error")




# ラジオボタンのグループ
v = IntVar()
v.set(0)


# ラジオボタン
radio1 = Radiobutton(root,text = u"項目1", variable = v, value = 1, command = change_state)
radio1.pack()

radio2 = Radiobutton(root,text = u"項目2", variable = v, value = 2, command = change_state)
radio2.pack()

radio3 = Radiobutton(root,text = u"項目3", variable = v, value = 3, command = change_state)
radio3.pack()


root.mainloop()

#%%


# =============================================================================
# Chapter 1-9 scrolledtext
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext

win = tk.Tk()


def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

    
action = ttk.Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)


ttk.Label(win, text = 'Enter a name: ').grid(column = 0, row = 0)
nameEntered = Entry(win, width=12)
nameEntered.grid(column = 0, row=1)



Label(win, text = 'Choose a number:').grid(column = 1, row = 0)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(win, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1)
numberChosen.current(2)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column=0, row = 4, sticky = W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn)
check2.deselect()
check2.grid(column=1, row = 4, sticky = W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn)
check3.select()
check3.grid(column=2, row = 4, sticky = W)

win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI




COLOR1 = 'Blue'
COLOR2 = 'Gold'
COLOR3 = 'Red'

radVar1 = tk.StringVar()

def radcall():

    radSel = radVar1.get()
    if radSel == 1:
        win.configure(background = COLOR1)
    elif radSel == 2:
        win.configure(background = COLOR2)
    elif radSel == 3:
        win.configure(background = COLOR3)
    print(radVar1)
    print(radVar1.get())
    print(radSel)
#    print('Hey')
#    print(rad1['value'])
    



radVar1= tk.IntVar()

rad1 = tk.Radiobutton(win, text = COLOR1, variable = radVar1, value = 1, command = radcall)
rad1.deselect()
rad1.grid(column=0, row = 5, sticky = W)

rad2 = tk.Radiobutton(win, text = COLOR2, variable = radVar1,  value = 2,command = radcall)
rad2.deselect()
rad2.grid(column=1, row = 5, sticky = W)

rad3 = tk.Radiobutton(win, text = COLOR3, variable = radVar1,  value = 3,command = radcall)
rad3.deselect()
rad3.grid(column=2, row = 5, sticky = W)

#radVar1.set("1")

#radVar1 = tk.IntVar()
#win.set_focus()
#nameEntered.focus()

scrolW = 30
scrolH = 30
scr = scrolledtext.ScrolledText(win, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column = 0, columnspan=3)

win.mainloop()

#%%


# =============================================================================
# Chapter 1-10 refactor the redundant code
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext

win = tk.Tk()


def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

    
action = ttk.Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)


ttk.Label(win, text = 'Enter a name: ').grid(column = 0, row = 0)
nameEntered = Entry(win, width=12)
nameEntered.grid(column = 0, row=1)



Label(win, text = 'Choose a number:').grid(column = 1, row = 0)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(win, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1)
numberChosen.current(2)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column=0, row = 4, sticky = W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn)
check2.deselect()
check2.grid(column=1, row = 4, sticky = W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn)
check3.select()
check3.grid(column=2, row = 4, sticky = W)

win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI



colors = ['Blue', 'Gold', 'Red']

radVar1 = tk.StringVar()


def radcall():

    radSel = radVar1.get()
    if radSel == 0:
        win.configure(background = COLOR1)
    elif radSel == 1:
        win.configure(background = COLOR2)
    elif radSel == 2:
        win.configure(background = COLOR3)
    print(radVar1)
    print(radVar1.get())
    print(radSel)




radVar1= tk.IntVar()
radVar1.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text = colors[col], variable = radVar1, value = col, command = radcall )
    curRad.grid(column = col, row = 5, sticky = tk.W)

#rad1 = tk.Radiobutton(win, text = COLOR1, variable = radVar1, value = 1, command = radcall)
#rad1.deselect()
#rad1.grid(column=0, row = 5, sticky = W)
#
#rad2 = tk.Radiobutton(win, text = COLOR2, variable = radVar1,  value = 2,command = radcall)
#rad2.deselect()
#rad2.grid(column=1, row = 5, sticky = W)
#
#rad3 = tk.Radiobutton(win, text = COLOR3, variable = radVar1,  value = 3,command = radcall)
#rad3.deselect()
#rad3.grid(column=2, row = 5, sticky = W)

#radVar1.set("1")

#radVar1 = tk.IntVar()
#win.set_focus()
#nameEntered.focus()

scrolW = 30
scrolH = 30
scr = scrolledtext.ScrolledText(win, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column = 0, columnspan=3)

win.mainloop()

#%%


# =============================================================================
# Chapter 2-1 Labelframe & use padding to add space around widgets
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext

win = tk.Tk()


def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

    
action = ttk.Button(win, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)


ttk.Label(win, text = 'Enter a name: ').grid(column = 0, row = 0)
nameEntered = Entry(win, width=12)
nameEntered.grid(column = 0, row=1)



Label(win, text = 'Choose a number:').grid(column = 1, row = 0)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(win, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1)
numberChosen.current(2)

#chVarDis = tk.IntVar()
#check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled')
#check1.select()
#check1.grid(column=0, row = 4, sticky = W)
#
#chVarUn = tk.IntVar()
#check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn)
#check2.deselect()
#check2.grid(column=1, row = 4, sticky = W)
#
#chVarEn = tk.IntVar()
#check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn)
#check3.select()
#check3.grid(column=2, row = 4, sticky = W)


chVar = ['chVarDis', 'chVarUn', 'chVarEn']
chText = ['Disabled', 'Unchecked', 'Enabled']
chState = ['disabled', None, None]

for check in range(3):
    checkBu = 'check' + str(check)
    checkBu = tk.Checkbutton(win, text = chText[check], variable = chVar[check], state = chState[check])
#    for eck in checkBu:
    checkBu.select()
#    check0.select()
#    check1.deselect()
#    check2.select()
    checkBu.grid(column = check, row = 4, sticky = tk.W)
    


colors = ['Blue', 'Gold', 'Red']

def radcall():
    radSel = radVar1.get()
    if radSel == 0:win.configure(background = colors[0])
    elif radSel == 1:win.configure(background = colors[1])
    elif radSel == 2:win.configure(background = colors[2])
    print(radVar1)
    print(radVar1.get())
    print(radSel)
    
radVar1= tk.IntVar()
radVar1.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text = colors[col], variable = radVar1, value = col, command = radcall )
    curRad.grid(column = col, row = 6, sticky = tk.W)

#rad1 = tk.Radiobutton(win, text = COLOR1, variable = radVar1, value = 1, command = radcall)
#rad1.deselect()
#rad1.grid(column=0, row = 5, sticky = W)
#
#rad2 = tk.Radiobutton(win, text = COLOR2, variable = radVar1,  value = 2,command = radcall)
#rad2.deselect()
#rad2.grid(column=1, row = 5, sticky = W)
#
#rad3 = tk.Radiobutton(win, text = COLOR3, variable = radVar1,  value = 3,command = radcall)
#rad3.deselect()
#rad3.grid(column=2, row = 5, sticky = W)

#radVar1.set("1")

#radVar1 = tk.IntVar()
#win.set_focus()
#nameEntered.focus()

scrolW = 30
scrolH = 30
scr = scrolledtext.ScrolledText(win, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column = 0, columnspan=3, row = 5)


labelsFrame = ttk.LabelFrame(win, text = 'Labels in a Frame')
labelsFrame.grid(column = 0, row = 7, padx = 20, pady = 40)

ttk.Label(labelsFrame, text ='Label1').grid(column = 0, row= 0)
ttk.Label(labelsFrame, text ='Label2').grid(column = 0, row= 1)
ttk.Label(labelsFrame, text ='Label3').grid(column = 0, row= 2)

nameEntered.focus()

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI

win.mainloop()

#%%


# =============================================================================
# Chapter 2-2 layout with 2 labelFrames in win
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext

win = tk.Tk()
win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI

monty = ttk.LabelFrame(win, text = 'Monty Python')
monty.grid(column = 0, row = 0,padx = 10 , pady =5)




def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

    
action = ttk.Button(monty, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)

name = StringVar()
ttk.Label(monty, text = 'Enter a name: ').grid(column = 0, row = 0, sticky = W)
nameEntered = ttk.Entry(monty, width=12, textvariable = name)
nameEntered.grid(column = 0, row=1, sticky = W)



ttk.Label(monty, text = 'Choose a number:').grid(column = 1, row = 0, sticky = W)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(monty, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1, sticky = W)
numberChosen.current(2)

#chVarDis = tk.IntVar()
#check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled')
#check1.select()
#check1.grid(column=0, row = 4, sticky = W)
#
#chVarUn = tk.IntVar()
#check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn)
#check2.deselect()
#check2.grid(column=1, row = 4, sticky = W)
#
#chVarEn = tk.IntVar()
#check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn)
#check3.select()
#check3.grid(column=2, row = 4, sticky = W)


chVar = ['chVarDis', 'chVarUn', 'chVarEn']
chText = ['Disabled', 'Unchecked', 'Enabled']
chState = ['disabled', None, None]

for check in range(3):
    checkBu = 'check' + str(check)
    checkBu = tk.Checkbutton(monty, text = chText[check], variable = chVar[check], state = chState[check])
#    for eck in checkBu:
    checkBu.select()
#    check0.select()
#    check1.deselect()
#    check2.select()
    checkBu.grid(column = check, row = 4, sticky = tk.W)
    


colors = ['Blue', 'Gold', 'Red']

def radcall():
    radSel = radVar1.get()
    if radSel == 0:win.configure(background = colors[0])
    elif radSel == 1:win.configure(background = colors[1])
    elif radSel == 2:win.configure(background = colors[2])
    print(radVar1)
    print(radVar1.get())
    print(radSel)
    
radVar1= tk.IntVar()
radVar1.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty, text = colors[col], variable = radVar1, value = col, command = radcall )
    curRad.grid(column = col, row = 6, sticky = tk.W)


scrolW = 30
scrolH = 30
scr = scrolledtext.ScrolledText(monty, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column = 0, columnspan=3, row = 5, sticky = 'WE', padx = 20)


labelsFrame = ttk.LabelFrame(win, text = 'Labels in a Frame')
labelsFrame.grid(column = 0, row = 7, padx =5, pady = 5, sticky = W)

ttk.Label(labelsFrame, text ='Label1').grid(column = 0, row= 0)
ttk.Label(labelsFrame, text ='Label2').grid(column = 0, row= 1)
ttk.Label(labelsFrame, text ='Label3').grid(column = 0, row= 2)

nameEntered.focus()

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

win.mainloop()

#%%


# =============================================================================
# Chapter 2-3 Menubars Separator quit
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu



win = tk.Tk()
win.title('Python GUI')
#win.resizable(0,0)  # 4 Disable resizing the GUI

monty = ttk.LabelFrame(win, text = 'Monty Python')
monty.grid(column = 0, row = 0,padx = 10 , pady =5)




def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

    
action = ttk.Button(monty, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)

name = StringVar()
ttk.Label(monty, text = 'Enter a name: ').grid(column = 0, row = 0, sticky = W)
nameEntered = ttk.Entry(monty, width=12, textvariable = name)
nameEntered.grid(column = 0, row=1, sticky = W)



ttk.Label(monty, text = 'Choose a number:').grid(column = 1, row = 0, sticky = W)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(monty, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1, sticky = W)
numberChosen.current(2)

#chVarDis = tk.IntVar()
#check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled')
#check1.select()
#check1.grid(column=0, row = 4, sticky = W)
#
#chVarUn = tk.IntVar()
#check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn)
#check2.deselect()
#check2.grid(column=1, row = 4, sticky = W)
#
#chVarEn = tk.IntVar()
#check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn)
#check3.select()
#check3.grid(column=2, row = 4, sticky = W)


chVar = ['chVarDis', 'chVarUn', 'chVarEn']
chText = ['Disabled', 'Unchecked', 'Enabled']
chState = ['disabled', None, None]

for check in range(3):
    checkBu = 'check' + str(check)
    checkBu = tk.Checkbutton(monty, text = chText[check], variable = chVar[check], state = chState[check])
#    for eck in checkBu:
    checkBu.select()
#    check0.select()
#    check1.deselect()
#    check2.select()
    checkBu.grid(column = check, row = 4, sticky = tk.W)
    


colors = ['Blue', 'Gold', 'Red']

def radcall():
    radSel = radVar1.get()
    if radSel == 0:win.configure(background = colors[0])
    elif radSel == 1:win.configure(background = colors[1])
    elif radSel == 2:win.configure(background = colors[2])
    print(radVar1)
    print(radVar1.get())
    print(radSel)
    
radVar1= tk.IntVar()
radVar1.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty, text = colors[col], variable = radVar1, value = col, command = radcall )
    curRad.grid(column = col, row = 6, sticky = tk.W)


scrolW = 30
scrolH = 30
scr = scrolledtext.ScrolledText(monty, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column = 0, columnspan=3, row = 5, sticky = 'WE', padx = 20)


labelsFrame = ttk.LabelFrame(win, text = 'Labels in a Frame')
labelsFrame.grid(column = 0, row = 7, padx =5, pady = 5, sticky = W)

ttk.Label(labelsFrame, text ='Label1').grid(column = 0, row= 0)
ttk.Label(labelsFrame, text ='Label2').grid(column = 0, row= 1)
ttk.Label(labelsFrame, text ='Label3').grid(column = 0, row= 2)

nameEntered.focus()


for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

menuBar = Menu(win)
win.config(menu = menuBar)

def _quit():
    win.quit()
    win.destroy()
#    exit()

fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'New')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = _quit)
menuBar.add_cascade(label = 'File', menu = fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)



win.mainloop()


#%%

# =============================================================================
#  Chapter 2-3 tab widget & columnspan sticky = 'WE' & grid layout manager
# =============================================================================


import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu

win = tk.Tk()
win.title("Python GUI")

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill="both", padx = 10)


#---------------------------------------
#以上Tabの作成、以下Tab1

#Tab1にMontyを入れる
monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)

#monty.grid(column = 0, row = 0,padx = 10 , pady =5)




def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

    
action = ttk.Button(monty, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)

name = StringVar()
ttk.Label(monty, text = 'Enter a name: ').grid(column = 0, row = 0, sticky = W)
nameEntered = ttk.Entry(monty, width=12, textvariable = name)
nameEntered.grid(column = 0, row=1, sticky = W)

nameEntered.focus()



ttk.Label(monty, text = 'Choose a number:').grid(column = 1, row = 0, sticky = W)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(monty, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1, sticky = W)
numberChosen.current(2)



scrolW = 30
scrolH = 10
scr = scrolledtext.ScrolledText(monty, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column = 0, columnspan=3, row = 5, sticky = 'WE', padx = 20)



#---------------------------------------
#以上Tab1、以下Tab2

monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
monty2.grid(column=0, row=0, padx=8, pady=4)

#chVarDis = tk.IntVar()
#check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled')
#check1.select()
#check1.grid(column=0, row = 4, sticky = W)
#
#chVarUn = tk.IntVar()
#check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn)
#check2.deselect()
#check2.grid(column=1, row = 4, sticky = W)
#
#chVarEn = tk.IntVar()
#check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn)
#check3.select()
#check3.grid(column=2, row = 4, sticky = W)


chVar = ['chVarDis', 'chVarUn', 'chVarEn']
chText = ['Disabled', 'Unchecked', 'Enabled']
chState = ['disabled', None, None]

for check in range(3):
    checkBu = 'check' + str(check)
    checkBu = tk.Checkbutton(monty2, text = chText[check], variable = chVar[check], state = chState[check])
#    for eck in checkBu:
    checkBu.select()
#    check0.select()
#    check1.deselect()
#    check2.select()
    checkBu.grid(column = check, row = 4, sticky = tk.W)
    


colors = ['Blue', 'Gold', 'Red']

def radcall():
    radSel = radVar1.get()
#    if radSel == 0:win.configure(background = colors[0])
#    elif radSel == 1:win.configure(background = colors[1])
#    elif radSel == 2:win.configure(background = colors[2])
    if radSel == 0:monty2.configure(text = colors[0])
    elif radSel == 1:monty2.configure(text = colors[1])
    elif radSel == 2:monty2.configure(text = colors[2])

    print(radVar1)
    print(radVar1.get())
    print(radSel)
    
radVar1= tk.IntVar()
radVar1.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty2, text = colors[col], variable = radVar1, value = col, command = radcall )
    curRad.grid(column = col, row = 6, sticky = tk.W, columnspan = 3)




labelsFrame = ttk.LabelFrame(tab2, text = 'Labels in a Frame')
labelsFrame.grid(column = 0, row = 7, padx =5, pady = 5, sticky = W)

ttk.Label(labelsFrame, text ='Label1').grid(column = 0, row= 0)
ttk.Label(labelsFrame, text ='Label2').grid(column = 0, row= 1)
ttk.Label(labelsFrame, text ='Label3').grid(column = 0, row= 2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)



#---------------------------------------
#以上Tab2、以下Menubar

menuBar = Menu(win)
win.config(menu = menuBar)

def _quit():
    win.quit()
    win.destroy()
#    exit()


fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'New')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = _quit)
menuBar.add_cascade(label = 'File', menu = fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)


win.mainloop()



#%%


# =============================================================================
# Chapter 3-1 # Message box & Warningbox & Errorbox & ask yes no box
# =============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

win = tk.Tk()
win.title("Python GUI")

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill="both", padx = 10)


#---------------------------------------
#以上Tabの作成、以下Tab1

#Tab1にMontyを入れる
monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)

#monty.grid(column = 0, row = 0,padx = 10 , pady =5)




def clickMe():
    global name
    action.configure(text= 'Hello ' + nameEntered.get() + ' ' + numberChosen.get())
    print(nameEntered.get())
    action.configure(state = 'disable')

    
action = ttk.Button(monty, text = 'Click Me!', command = clickMe)
action.grid(column = 2, row = 1)

name = StringVar()
ttk.Label(monty, text = 'Enter a name: ').grid(column = 0, row = 0, sticky = W)
nameEntered = ttk.Entry(monty, width=12, textvariable = name)
nameEntered.grid(column = 0, row=1, sticky = W)

nameEntered.focus()



ttk.Label(monty, text = 'Choose a number:').grid(column = 1, row = 0, sticky = W)
number = tk.StringVar() #ここでnumberをStringと定義したので、1,2,4,42が表示される時に、Stringになる
numberChosen = ttk.Combobox(monty, width = 12, textvariable = number, state= 'readonly')
numberChosen['values' ] = (1,2,4,42,100)
numberChosen.grid(column=1, row = 1, sticky = W)
numberChosen.current(2)



scrolW = 30
scrolH = 10
scr = scrolledtext.ScrolledText(monty, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column = 0, columnspan=3, row = 5, sticky = 'WE', padx = 20)



#---------------------------------------
#以上Tab1、以下Tab2

monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
monty2.grid(column=0, row=0, padx=8, pady=4)

#chVarDis = tk.IntVar()
#check1 = tk.Checkbutton(win, text= 'Disabled', variable = chVarDis, state = 'disabled')
#check1.select()
#check1.grid(column=0, row = 4, sticky = W)
#
#chVarUn = tk.IntVar()
#check2 = tk.Checkbutton(win, text= 'Unchecked', variable = chVarUn)
#check2.deselect()
#check2.grid(column=1, row = 4, sticky = W)
#
#chVarEn = tk.IntVar()
#check3 = tk.Checkbutton(win, text= 'Enabled', variable = chVarEn)
#check3.select()
#check3.grid(column=2, row = 4, sticky = W)


chVar = ['chVarDis', 'chVarUn', 'chVarEn']
chText = ['Disabled', 'Unchecked', 'Enabled']
chState = ['disabled', None, None]

for check in range(3):
    checkBu = 'check' + str(check)
    checkBu = tk.Checkbutton(monty2, text = chText[check], variable = chVar[check], state = chState[check])
#    for eck in checkBu:
    checkBu.select()
#    check0.select()
#    check1.deselect()
#    check2.select()
    checkBu.grid(column = check, row = 4, sticky = tk.W)
    


colors = ['Blue', 'Gold', 'Red']

def radcall():
    radSel = radVar1.get()
#    if radSel == 0:win.configure(background = colors[0])
#    elif radSel == 1:win.configure(background = colors[1])
#    elif radSel == 2:win.configure(background = colors[2])
    if radSel == 0:monty2.configure(text = colors[0])
    elif radSel == 1:monty2.configure(text = colors[1])
    elif radSel == 2:monty2.configure(text = colors[2])

    print(radVar1)
    print(radVar1.get())
    print(radSel)
    
radVar1= tk.IntVar()
radVar1.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty2, text = colors[col], variable = radVar1, value = col, command = radcall )
    curRad.grid(column = col, row = 6, sticky = tk.W, columnspan = 3)




labelsFrame = ttk.LabelFrame(tab2, text = 'Labels in a Frame')
labelsFrame.grid(column = 0, row = 7, padx =5, pady = 5, sticky = W)

ttk.Label(labelsFrame, text ='Label1').grid(column = 0, row= 0)
ttk.Label(labelsFrame, text ='Label2').grid(column = 0, row= 1)
ttk.Label(labelsFrame, text ='Label3').grid(column = 0, row= 2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)



#---------------------------------------
#以上Tab2、以下Menubar

menuBar = Menu(win)
win.config(menu = menuBar)

def _quit():
    win.quit()
    win.destroy()
#    exit()


fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'New')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = _quit)
menuBar.add_cascade(label = 'File', menu = fileMenu)

def _msgBox():
    mBox.showinfo('Python Message Info Box', \
                  'A Python GUI created using ' \
                  'tkinter:\nThe year is 2015.')
    print('yo^^^')
    
def _warBox():
    mBox.showwarning('Python Message Warning Box', 'A Python GUI ' \
    'created using tkinter:\nWarning: There might be a bug in this code.')

def _errBox():
    mBox.showerror('Python Message Error Box', 'A Python GUI created' \
    'using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')

def _ask_yes_no_Box():
    answer = mBox.askyesno("Python Message Dual Choice Box", "Are you" \
    "sure you really wish to do this?")
    print(answer)
    if answer == True:
        _msgBox()
    elif answer == False:
        pass

Boxes = ["About(Message box)", "About(Warning box)", "About(Error box)", "_ask_yes_no_Box"]
Box_commands = [_msgBox, _warBox, _errBox, _ask_yes_no_Box]

helpMenu = Menu(menuBar, tearoff=0)
for x in range(len(Boxes)):
    helpMenu.add_command(label=Boxes[x], command=Box_commands[x])
    
#helpMenu.add_command(label="About(Message box)", command=_msgBox)
#helpMenu.add_command(label="About(Warning box)", command=_warBox)
#helpMenu.add_command(label="About(Error box)", command=_errBox)
menuBar.add_cascade(label="Help", menu=helpMenu)

win.mainloop()


#%%

# =============================================================================
# Chapter 3-2 independent message box
# =============================================================================

from tkinter import messagebox as mBox
from tkinter import Tk

root = Tk()
root.withdraw() #remove the debug window
mBox.showinfo('This is a Title', 'A Python GUI created using ' \
              'tkinter:\nThe year is 2015')
















