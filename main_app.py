import pyperclip as pyperclip
import pyshorteners
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Сокращение ссылок")
root.geometry("400x230")
root["bg"] = "#4E4A4A"
Label(root, text="Добро пожаловать в\nсокращетель ссылок!", font='Consolas 11 bold', bg="#4E4A4A", fg="#FFFFFF").pack(
    pady=5)
Label(root, text="Введите ссылку: ", font='Consolas 11 bold', bg="#4E4A4A", fg="#FFFFFF").pack(pady=5)

link = Entry(root, width=40)
link.pack()

Label(root, text='Сокращенная ссылка: ', font='Consolas 11 bold', bg="#4E4A4A", fg="#FFFFFF").pack(pady=5)

res = Entry(root, width=40)
res.pack()


def copytoclipboard():
    url = res.get()
    pyperclip.copy(url)


def short():
    try:
        a = link.get()
        s = pyshorteners.Shortener().tinyurl.short(a)
        res.insert(0, s)
    except:
        messagebox.showerror("Сокращение ссылок", "Неверная ссылка!")


Button(root, text='Сократить ссылку', command=short).pack()
Button(root, text='Скопировать ссылку', command=copytoclipboard).pack(pady=5)
root.mainloop()
