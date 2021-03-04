from tkinter import *

window = Tk()

def swap():
    # Get user value from input box and multiply by 1000 to get kilograms
    gram = float(text_value.get()) * 1000

    # Get user value from input box and multiply by 2.20462 to get pounds
    pound = float(text_value.get()) * 2.20462

    # Get user value from input box and multiply by 35.274 to get ounces
    ounce = float(text_value.get()) * 35.274

    grams.delete("1.0", END)  # Deletes the content of the Text box from start to END
    grams.insert(END, gram)  # Fill in the text box with the value of gram variable
    pounds.delete("1.0", END)
    pounds.insert(END, pound)
    ounces.delete("1.0", END)
    ounces.insert(END, ounce)



l1=Label(window,height=1,width=20,text="KG")
l1.grid(row=0,column=0)

text_value = StringVar()
t1=Entry(window, textvariable = text_value)
t1.grid(row=0,column=1)

grams=Text(window,height=1,width=20)
grams.grid(row=1,column=1)

pounds=Text(window,height=1,width=20)
pounds.grid(row=1,column=2)

ounces=Text(window,height=1,width=20)
ounces.grid(row=1,column=3)


b1=Button(window,text="Convert",command=swap)
b1.grid(row=0,column=2)


window.mainloop()