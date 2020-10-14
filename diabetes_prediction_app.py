from sys import winver
from tkinter import Canvas
import joblib
import numpy as np
import tkinter as tk
from tkinter import ttk

#loading ml model 
sav = joblib.load("diabetes_prediction.ml")
#creating tkinter instance
root = tk.Tk() 
root.title("Diabetes checking") 
root.iconbitmap("icon.ico")
canv = tk.Canvas(root,width=250,height=400)
canv.pack()

#creating labels 
pregnancies = tk.Label(root,text='Pregnancies')
canv.create_window(50,20,window=pregnancies)
glucose = tk.Label(root,text='Glucose')
canv.create_window(45,60,window=glucose) 
bp = tk.Label(root,text='Blood pressure')
canv.create_window(45,100,window=bp)
st = tk.Label(root,text='Skin thickness')
canv.create_window(50,140,window=st)
insulin = tk.Label(root,text='Insulin')
canv.create_window(45,180,window=insulin) 
BMI = tk.Label(root,text='BMI')
canv.create_window(45,220,window=BMI)
dpf = tk.Label(root,text='DPF')
canv.create_window(50,260,window=dpf)
age = tk.Label(root,text='Age')
canv.create_window(45,300,window=age) 

#creating input text fields to get data
in_pregnancies = tk.Entry(root)
canv.create_window(150,20,window=in_pregnancies)
in_glucose = tk.Entry(root)
canv.create_window(150,60,window=in_glucose) 
in_bp = tk.Entry(root)
canv.create_window(150,100,window=in_bp)
in_st = tk.Entry(root)
canv.create_window(150,140,window=in_st)
in_insulin = tk.Entry(root)
canv.create_window(150,180,window=in_insulin) 
in_BMI = tk.Entry(root)
canv.create_window(150,220,window=in_BMI)
in_dpf = tk.Entry(root)
canv.create_window(150,260,window=in_dpf)
in_age = tk.Entry(root)
canv.create_window(150,300,window=in_age) 

#creating labels to show output
value1 = tk.Label(root)
canv.create_window(110,380,window=value1)

#submit button function
def cal():
    val = [
        float(in_pregnancies.get()),
        float(in_glucose.get()),
        float(in_bp.get()),
        float(in_st.get()),
        float(in_insulin.get()),
        float(in_BMI.get()),
        float(in_dpf.get()),
        float(in_age.get())
    ]
    pred_val = np.array([val])
    result = sav.predict(pred_val)
    if result == 0:
        value1["text"] = "Be happy you don't have Diabetes"
        value1["fg"] = "green"
    else:
        value1["text"] = "Sorry..! you have Diabetes"
        value1["fg"] = "red"

#reset button function
def clear(): 
    value1["text"] = ""

#creating buttons 
but = tk.Button(text='Submit',command=cal)
canv.create_window(80,340,window=but) 
but1 = tk.Button(text='Reset',command=clear)
canv.create_window(150,340,window=but1)

#apply loop to app so it not close itself
root.mainloop()