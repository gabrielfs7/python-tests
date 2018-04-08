from tkinter import *

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
# Buttons
#
button_view = Button(window, text="View all", width=12)
button_view.grid(row=3, column=3)

button_search = Button(window, text="Search", width=12)
button_search.grid(row=4, column=3)

button_create = Button(window, text="Create", width=12)
button_create.grid(row=5, column=3)

button_update = Button(window, text="Update", width=12)
button_update.grid(row=6, column=3)

button_delete = Button(window, text="Delete", width=12)
button_delete.grid(row=7, column=3)

button_close = Button(window, text="Close", width=12)
button_close.grid(row=8, column=3)

window.mainloop()