from tkinter import *
import requests

# creating the window
root = Tk()
root.title("Currency Converter")
root.geometry("500x500")
root.config(bg="purple")

value = StringVar()
StringVar = IntVar()


information = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']
print(conversion_rate)


# Creating a label and entries


my_label1 = Label(root, text="Value", )
my_label1.place(x=5, y=10)

my_entry1 = Entry(root, textvariable=value, width=10)
my_entry1.place(x=100, y=10)

my_label2 = Label(root, text="From: USD TO",)
my_label2.place(x=5, y=40)

my_label3 = Label(root, text="results", width=10, font=10)
my_label3.place(x=150, y=300)

# Doing the Conversion of the data with its loop


convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
convert_list.place(x=100, y=70)


def converting():
    num = float(my_entry1.get())
    print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    my_label3['text'] = ans


def clear():
    my_entry1.delete(0, END)


def exit_program():
    root.destroy()

# creating btn


convert_btn = Button(root, command=converting, text="CONVERT", font=10, bg="purple", borderwidth="10", fg="white")
convert_btn.place(x=5, y=300)
clear_btn = Button(root, text="Clear", borderwidth="10", bg="purple", command=clear, fg="white")
clear_btn.place(x=300, y=300)
exit_btn = Button(root, text="Exit", borderwidth="10", bg="purple", command=exit_program, fg="white")
exit_btn.place(x=5, y=370)


root.mainloop()
