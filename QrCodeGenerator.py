
from tkinter import *
from tkinter import messagebox
import pyqrcode
import validators


def generateQrCode():
    try:
        url = url_entry.get()
        # checks if the url is empty
        if url == "":
            raise ValueError("Please enter a url")
        #checks if the url is invalid
        elif not validators.url(url):
            raise ValueError("Please enter a valid url")
        else:
            code = pyqrcode.create(str(url))
            code.svg('uca-url.svg', scale=8)
            code.eps('uca-url.eps', scale=2)
            print(code.terminal(quiet_zone=1))
            Label(window, text="QR code generated and saved in a file", font=("Arial", 15), fg="blue", bg="#EDBB99", height = 3).grid(row=5, column=0, columnspan=3)
    except ValueError as e:
        messagebox.showinfo("Error", message=e)
        return


window = Tk()
window.title('QR Code Generator')
window.geometry('400x400')
window.config(background='#EDBB99')

Label(window, text='QR Code Generator', height=2,  font=("Helvetica", 20), fg="blue", bg="#EDBB99").grid(row=0, column=0, columnspan=2)

description_label = Label(window, text='This program generates a QR code from a url.', font=("Arial", 14), bg="#EDBB99")
description_label.grid(row=1, column=0, columnspan=2)

Label(window, text=' The url should be a valid path to a website', font=("Arial", 14), bg="#EDBB99").grid(row=2, column=0, columnspan=2)

prompt_label = Label(window, text='Enter your URL ', font=('Arial', 14), height=2, fg="green", bg="#EDBB99")
prompt_label.grid(row=3, column=0)

url_entry = Entry(window, width=30)
url_entry.grid(row=3, column=1)

button = Button(window, text='Generate QR Code', height=2, bg="white", font=("Helvetica", 10, "bold"),fg="green" ,command=generateQrCode)
button.grid(row=4, column=0, columnspan=2)

window.mainloop()