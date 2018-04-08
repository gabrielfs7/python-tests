from tkinter import *
from backend import Database
from datetime import datetime


class Commands:
    """Class to execute Book store commands"""
    def __init__(self, database, book_list, id_entry, title_entry, author_entry, year_entry, isbn_entry):
        self.__database = database
        self.__id_entry = id_entry
        self.__title_entry = title_entry
        self.__author_entry = author_entry
        self.__year_entry = year_entry
        self.__isbn_entry = isbn_entry
        self.__book_list = book_list

        self.__id_entry.configure(state="normal")
        self.__id_entry.delete(0, END)
        self.__id_entry.configure(state="readonly")
        self.__title_entry.delete(0, END)
        self.__author_entry.delete(0, END)
        self.__year_entry.delete(0, END)
        self.__isbn_entry.delete(0, END)

    def __clear_entries(self):
        self.__id_entry.configure(state="normal")
        self.__id_entry.delete(0, END)
        self.__id_entry.configure(state="readonly")
        self.__title_entry.delete(0, END)
        self.__author_entry.delete(0, END)
        self.__year_entry.delete(0, END)
        self.__isbn_entry.delete(0, END)

    def get_selected_row(self, event):
        current_selection = self.__book_list.curselection()

        if len(current_selection) == 0:
            return

        book_list_index = self.__book_list.curselection()[0]

        book_id = self.__book_list.get(book_list_index)[0]
        book_title = self.__book_list.get(book_list_index)[1]
        book_author = self.__book_list.get(book_list_index)[2]
        book_year = self.__book_list.get(book_list_index)[3]
        book_isbn = self.__book_list.get(book_list_index)[4]

        self.__clear_entries()

        self.__id_entry.configure(state="normal")
        self.__id_entry.insert(END, book_id)
        self.__id_entry.configure(state="readonly")
        self.__author_entry.insert(END, book_author)
        self.__title_entry.insert(END, book_title)
        self.__year_entry.insert(END, book_year)
        self.__isbn_entry.insert(END, book_isbn)

    def view_all_command(self):
        self.__book_list.delete(0, END)

        for row in self.__database.select():
            self.__book_list.insert(END, row)

    def search_command(self):
        self.__book_list.delete(0, END)

        results = self.__database.select(
            title=self.__title_entry.get(),
            author=self.__author_entry.get(),
            year=self.__year_entry.get(),
            isbn=self.__isbn_entry.get()
        )

        for row in results:
            self.__book_list.insert(END, row)

    def create_command(self):
        self.__database.insert(
            title=self.__title_entry.get(),
            author=self.__author_entry.get(),
            year=self.__year_entry.get(),
            isbn=self.__isbn_entry.get()
        )

        self.__clear_entries()
        self.view_all_command()

    def update_command(self):
        self.__database.update(
            id=self.__id_entry.get(),
            title=self.__title_entry.get(),
            author=self.__author_entry.get(),
            year=self.__year_entry.get(),
            isbn=self.__isbn_entry.get()
        )

        self.view_all_command()

    def delete_command(self):
        self.__database.delete(id=self.__id_entry.get())
        self.__clear_entries()

        self.view_all_command()

    def close_command(self):
        self.__clear_entries()
        self.view_all_command()


class Display:
    """Class to display Book Store elements"""
    def __init__(self):
        self.__window = Tk()
        self.__window.wm_title("Book Store")

        self.__book_list = Listbox(self.__window, height=9, width=35)
        self.__scrollbar = Scrollbar(self.__window)
        self.__book_list.grid(row=3, column=0, rowspan=6, columnspan=2)
        self.__scrollbar.grid(row=3, column=2, rowspan=6)

        self.__book_list.configure(yscrollcommand=self.__scrollbar.set)
        self.__scrollbar.configure(command=self.__book_list.yview)

    def add_label(self, text, row, column):
        label = Label(self.__window, text=text)
        label.grid(row=row, column=column)

    def render(self):
        self.__window.mainloop()

    def add_entry(self, row, column, textvariable=None, state="normal"):
        entry = Entry(self.__window, state=state, textvariable=textvariable)
        entry.grid(row=row, column=column)

        return entry

    def add_button(self, text, width, row, column, command):
        button_view = Button(self.__window, text=text, width=width, command=command)
        button_view.grid(row=row, column=column)

        return button_view

    def book_list(self):
        return self.__book_list


display = Display()
display.add_label("ID", 0, 0)
display.add_label("Title", 1, 0)
display.add_label("Author", 1, 2)
display.add_label("Year", 2, 0)
display.add_label("ISBN", 2, 2)

#
# Inputs
#
title_input = StringVar()
author_input = StringVar()
year_input = StringVar()
isbn_input = StringVar()

id_entry = display.add_entry(0, 1, None, "readonly")
title_entry = display.add_entry(1, 1, title_input)
author_entry = display.add_entry(1, 3, author_input)
year_entry = display.add_entry(2, 1, year_input)
isbn_entry = display.add_entry(2, 3, isbn_input)

#
# Bind events
#
commands = Commands(Database(), display.book_list(), id_entry, title_entry, author_entry, year_entry, isbn_entry)
commands.view_all_command()

display.book_list().bind('<<ListboxSelect>>', commands.get_selected_row)
button_view = display.add_button("View all", 12, 3, 3, commands.view_all_command)
button_search = display.add_button("Search", 12, 4, 3, commands.search_command)
button_create = display.add_button("Create", 12, 5, 3, commands.create_command)
button_update = display.add_button("Update", 12, 6, 3, commands.update_command)
button_delete = display.add_button("Delete", 12, 7, 3, commands.delete_command)
button_close = display.add_button("Close", 12, 8, 3, commands.close_command)

display.render()