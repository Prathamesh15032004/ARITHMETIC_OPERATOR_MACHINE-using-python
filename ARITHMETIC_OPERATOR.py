#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Multiplication_Table(): 
    # Welcome user 
    print("****Welcome to the Multiplication Table !****")
    
    # Ask user to input a number
    number = int(input("Enter a number to generate multiplication table: "))
    
    # Using For Loop to generate the multiplication table
    for i in range(1, 11):
        answer = number * i
        print(number,"x",i,"=",answer)

def divide_table():
    print("****Welcome to the Divide Table !****")
    # Using For Loop to generate the divide table
    number = int(input("Enter a number to generate divide table: "))
    for i in range(1, 11):
        answer = number / i
        print(number,"/",i,"=",answer)

def addition_table():
    print("****Welcome to the Addition Table !****")
    # Using For Loop to generate the addition table
    number = int(input("Enter a number to generate Addition table: "))
    for i in range(1, 11):
        answer = number + i
        print(number,"+",i,"=",answer)

def subscription_table():
    print("****Welcome to the Subscription Table !****")
    # Using For Loop to generate the subscription table
    number = int(input("Enter a number to generate SUBSCRIPTION table: "))
    for i in range(1, 11):
        answer = number - i
        print(number,"-" ,i,"=",answer)


# In[4]:


#importing library 
import tkinter as tn

# creating window
window=tn.Tk()

# change title
window.title("prathamesh lohakare")

# change background colour
window.title("Change Background Color")
window.configure(bg='lightblue')

# change size
window.geometry('300x300')

# text label
tn.Label(window,text='ARITHMETIC_OPERATOR',fg="darkred",font=('Times New Roman',16)).place(x=20,y=40)


# button 1
tn.Button(window,text='START MULTIPLICATION',fg="Darkblue",width=20,command=Multiplication_Table).place(x=70,y=100)

# Button 2
tn.Button(window,text='START DIVIDE',fg="Darkblue",width=20,command=divide_table).place(x=70,y=150)

# button 3
tn.Button(window,text='START ADDITION',fg="Darkblue",width=20,command=addition_table).place(x=70,y=200)

# button 4
tn.Button(window,text='START subscription',fg="Darkblue",width=20,command=subscription_table).place(x=70,y=250)


# displaying window
window.mainloop()


# In[ ]:




