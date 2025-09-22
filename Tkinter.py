from tkinter import *
from tkinter import ttk, messagebox
import random as r

def exit():
    root.destroy()

def validate(new_value):
    if new_value == "":
        return True
    
    if not new_value.isdigit():
        messagebox.showwarning("Внимание", "Введите число, а не букву")
        return False
    
    number = int(new_value)
    if 0 <= number <= 100:
        return True
    else:
        messagebox.showwarning("Внимание", "Введите число от 0 до 100")
        return False

def guess():
    user_text = entry.get()
    global c
    c += 1
    if c > 10:
        messagebox.showwarning("Внимание", "Превышен лимит попыток, попробуйте заново")
        return
    if not user_text:
        messagebox.showwarning("Внимание", "Введите число")
        return
    
    number = int(user_text)

    if number == n:
        label1.config(text="Вы угадали!", foreground="#1AFF00", font=("Arial", 14))
        img.config(image=win_image)
    elif number > n:
        label1.config(text=f"Загаданное число меньше {number}", foreground="#FD0000", font=("Arial", 14))
    elif number < n:
        label1.config(text=f"Загаданное число больше {number}", foreground="#FF0000", font=("Arial", 14))

    label_attempts.config(text=f"Попытки: {c}/10")
    entry.focus()

def repeat():
    entry.delete(0, END)
    img.config(image=None)

    global n, c
    n = r.randint(0, 100)
    c = 0

    label_attempts.config(text=f"Попытки: {c}/10")
    label1.config(text="")
    entry.focus()
    
n = r.randint(0, 100)

c = 0

root = Tk()
root.title("Угадайка чисел")
root.geometry("550x350+500+100")    
root.attributes("-fullscreen", True)

style = ttk.Style()

style.configure("Red.TButton", background = "red", foreground = "red")
style.configure("Green.TButton", background = "green", foreground = "green")
style.configure("Yellow.TButton", background = "yellow", foreground = "black")

win_image = PhotoImage(file=r"C:\users\ivana\OneDrive\Desktop\питон\like.png")
root.iconbitmap(r"C:\users\ivana\OneDrive\Desktop\питон\pic.ico")

label = ttk.Label(root, text="Приветсвую в программе по угадыванию чисел", foreground="#000000", font=("Arial", 14))
label.pack(pady=40)

f_valid = (root.register(validate), "%P")

attempts_frame = ttk.Frame()
attempts_frame.pack(padx=10)

entry = ttk.Entry(attempts_frame, validate="key", validatecommand = f_valid)
entry.pack(side=LEFT, padx=10)

label_attempts = ttk.Label(attempts_frame, text=f"Попытки: {c}/10")
label_attempts.pack(side=LEFT, padx=10)

label1 = ttk.Label()
label1.pack(pady=10)

button_frame = ttk.Frame()
button_frame.pack(pady=10)

btn = ttk.Button(button_frame, text="Проверка числа", command=guess, style="Green.TButton")
btn.pack(side=LEFT, padx=10)

btn2 = ttk.Button(button_frame, text="Заново",  command= repeat, style="Yellow.TButton")
btn2.pack(side=LEFT, padx=10)

btn1 = ttk.Button(button_frame, text="Выход", command=exit, style="Red.TButton")
btn1.pack(side=LEFT, padx=10)

img = ttk.Label()
img.pack(pady=30)
 
root.mainloop()