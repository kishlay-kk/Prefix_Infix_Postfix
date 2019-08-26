#!/usr/bin/env python
# coding: utf-8

# In[45]:


from tkinter import *
root=Tk()
root.geometry("600x300")
root.configure(bg="#2F2FA2")
import prefix_infix_postfix


# In[46]:


eq=""
exp1=""

def convert():
    global eq
    global exp1
    buttonpushed()
    t1= var1.get()
    t2= var2.get()
    if(t1=="infix" and t2=="postfix"):
        eq=prefix_infix_postfix.infix_to_postfix(exp1)
        v2.set(eq)
    elif(t1=="postfix" and t2=="infix"):
        eq=prefix_infix_postfix.postfix_to_infix(exp1)
        v2.set(eq)
    elif(t1=="prefix" and t2=="infix"):
        eq=prefix_infix_postfix.prefix_to_infix(exp1)
        v2.set(eq)
    elif(t1=="infix" and t2=="prefix"):
        eq=prefix_infix_postfix.infix_to_prefix(exp1)
        v2.set(eq)
    else:
        print("ERROR")
    
def buttonpushed():
    global txtb
    global exp1
    exp1= txtb.get()


# In[47]:




var1= StringVar(root)
var1.set("infix")
option1 = OptionMenu(root,var1,"prefix","infix","postfix")
option1.grid(row=0,column=0,padx=5,pady=5)
#option1.pack()
txtb = Entry(root,bg="pink",fg="#161BEE",font=("Comic Sans MS",15),width=40)
txtb.grid(row=0,column=1,padx=5,pady=5)
#txtb.pack()

var2= StringVar(root)
var2.set("None")
option2 = OptionMenu(root,var2,"prefix","infix","postfix")
option2.grid(row=1,column=0,padx=5,pady=5)
#option2.pack()
v2=StringVar()
label2 = Label(root,textvariable=v2,width="40",bg="pink",fg="BLACK",padx=1,pady=1,font=("Comic Sans MS",15)).grid(row=1,column=1,padx=5,pady=5)
#label2.pack()
b = Button(root,text="CONVERT",relief=GROOVE,command=convert).place(x=50,y=90)


# In[48]:


root.mainloop()


# In[ ]:




