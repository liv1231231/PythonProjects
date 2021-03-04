""""
Gui book app
"""

from tkinter import *
from backend import Database

database = Database("books.db")


def get_selected(event):
    global selected_tuple
    index = list1.curselection()
    if index != ():
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])


def delete_selected():
    database.delete(selected_tuple[0])


def update_selected():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def view_all():
    list1.delete(0, END)
    for i in database.view():
        list1.insert(END, i)


def search_entry():
    list1.delete(0, END)
    for i in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, i)


def add_entry():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


window = Tk()

window.wm_title("Liv's BOOK STORE")

l1 = Label(window, text="Title")
l1.grid(column=0, row=0)

l2 = Label(window, text="Year")
l2.grid(column=0, row=1)

l3 = Label(window, text="Author")
l3.grid(column=2, row=0)

l4 = Label(window, text="ISBN")
l4.grid(column=2, row=1)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(column=1, row=0)

year_text = StringVar()
e2 = Entry(window, textvariable=year_text)
e2.grid(column=1, row=1)

author_text = StringVar()
e3 = Entry(window, textvariable=author_text)
e3.grid(column=3, row=0)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(column=3, row=1)

list1 = Listbox(window, height=6, width=35)
list1.grid(column=0, row=2, columnspan=2, rowspan=6)

sb1 = Scrollbar(window)
sb1.grid(column=2, row=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected)

b1 = Button(window, text="View All", width=12, command=view_all)
b1.grid(column=3, row=2)

b2 = Button(window, text="Search entry", width=12, command=search_entry)
b2.grid(column=3, row=3)

b3 = Button(window, text="Add entry", width=12, command=add_entry)
b3.grid(column=3, row=4)

b4 = Button(window, text="Update", width=12, command=update_selected)
b4.grid(column=3, row=5)

b5 = Button(window, text="Delete", width=12, command=delete_selected)
b5.grid(column=3, row=6)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(column=3, row=7)

window.mainloop()
