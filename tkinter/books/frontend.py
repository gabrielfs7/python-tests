from tkinter import *
import backend

window = Tk(screenName="Book Store")

#
# Labels
#
id_label = Label(window, text="ID")
id_label.grid(row=0, column=0)

title_label = Label(window, text="Title")
title_label.grid(row=1, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=1, column=2)

year_label = Label(window, text="Year")
year_label.grid(row=2, column=0)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=2, column=2)

#
# Inputs
#
id_input = StringVar()
id_entry = Entry(window, textvariable=id_input)
id_entry.grid(row=0, column=0, columnspan=5)

title_input = StringVar()
title_entry = Entry(window, textvariable=title_input)
title_entry.grid(row=1, column=1)

author_input = StringVar()
author_entry = Entry(window, textvariable=author_input)
author_entry.grid(row=1, column=3)

year_input = StringVar()
year_entry = Entry(window, textvariable=year_input)
year_entry.grid(row=2, column=1)

isbn_input = StringVar()
isbn_entry = Entry(window, textvariable=isbn_input)
isbn_entry.grid(row=2, column=3)

#
# List and scrollbar
#
book_list = Listbox(window, height=9, width=35)
book_list.grid(row=3, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=3, column=2, rowspan=6)

scrollbar.configure(command=book_list.yview)
book_list.configure(yscrollcommand=scrollbar.set)

#
# Button commands
#


def clear_entries():
    id_entry.delete(0, END)
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    year_entry.delete(0, END)
    isbn_entry.delete(0, END)


def get_selected_row(event):
    book_list_index = book_list.curselection()[0]

    book_id = book_list.get(book_list_index)[0]
    book_title = book_list.get(book_list_index)[1]
    book_author = book_list.get(book_list_index)[2]
    book_year = book_list.get(book_list_index)[3]
    book_isbn = book_list.get(book_list_index)[4]

    clear_entries()

    id_entry.insert(END, book_id)
    author_entry.insert(END, book_author)
    title_entry.insert(END, book_title)
    year_entry.insert(END, book_year)
    isbn_entry.insert(END, book_isbn)

    return book_id


def view_all_command():
    book_list.delete(0, END)

    for row in backend.select():
        book_list.insert(END, row)


def search_command():
    book_list.delete(0, END)

    results = backend.select(
        title=title_entry.get(),
        author=author_entry.get(),
        year=year_entry.get(),
        isbn=isbn_entry.get()
    )

    for row in results:
        book_list.insert(END, row)


def create_command():
    backend.insert(
        id=isbn_entry.get(),
        title=title_entry.get(),
        author=author_entry.get(),
        year=year_entry.get(),
        isbn=isbn_entry.get()
    )

    clear_entries()
    view_all_command()


def update_command():
    backend.update(
        id=id_entry.get(),
        title=title_entry.get(),
        author=author_entry.get(),
        year=year_entry.get(),
        isbn=isbn_entry.get()
    )

    view_all_command()


def delete_command():
    backend.delete(id=id_entry.get())

    view_all_command()


def close_command():
    clear_entries()
    view_all_command()

#
# Bind events
#


book_list.bind('<<ListboxSelect>>', get_selected_row)


#
# Buttons
#
button_view = Button(window, text="View all", width=12, command=view_all_command)
button_view.grid(row=3, column=3)

button_search = Button(window, text="Search", width=12, command=search_command)
button_search.grid(row=4, column=3)

button_create = Button(window, text="Create", width=12, command=create_command)
button_create.grid(row=5, column=3)

button_update = Button(window, text="Update", width=12, command=update_command)
button_update.grid(row=6, column=3)

button_delete = Button(window, text="Delete", width=12, command=delete_command)
button_delete.grid(row=7, column=3)

button_close = Button(window, text="Close", width=12, command=close_command)
button_close.grid(row=8, column=3)


window.mainloop()