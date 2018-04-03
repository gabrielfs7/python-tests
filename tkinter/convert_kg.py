from tkinter import *

window = Tk()
window.wm_minsize()

# Add an input field
entry1_text_variable = StringVar()
entry1 = Entry(window, textvariable=entry1_text_variable)
entry1.grid(row=0, column=0)

# Adding labels
label = Label(window, text="Kg")
label.grid(row=0, column=1)

label = Label(window, text="Grams")
label.grid(row=1, column=0)

label = Label(window, text="Pounds")
label.grid(row=1, column=1)

label = Label(window, text="Ounces")
label.grid(row=1, column=2)

# Add a textarea
text_grams = Text(window, height=1, width=20)
text_grams.grid(row=2, column=0)

text_pounds = Text(window, height=1, width=20)
text_pounds.grid(row=2, column=1)

text_ounces = Text(window, height=1, width=20)
text_ounces.grid(row=2, column=2)


def convert_kg():
    kg = float(entry1_text_variable.get())
    grams = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274

    text_grams.delete("1.0", END)
    text_pounds.delete("1.0", END)
    text_ounces.delete("1.0", END)

    text_grams.insert(END, str(grams))
    text_pounds.insert(END, str(pounds))
    text_ounces.insert(END, str(ounces))


btn = Button(window,text='Convert', command=convert_kg)
btn.grid(row=0, column=2)

# Keeps the window opened
window.mainloop()